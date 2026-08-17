"""A generic OKF MCP server.

Deliberately **bundle-agnostic**: point it at any OKF v0.2 bundle directory and it
serves that bundle. Nothing here knows about AAIF. That is what makes it
independently useful -- and independently donatable to the OKF ecosystem, rather
than being a private convenience for this one repository.

The tiered reads (``okf_abstract`` / ``okf_overview`` / ``okf_read``) implement the
L0/L1/L2 discipline from ADR-006 directly over markdown, with no vector store and
no external dependency. An agent can triage on L0, plan on L1, and only pay for
full documents it has decided it needs.

Run::

    uv sync --extra mcp
    uv run aaif-wiki mcp --bundle wiki
"""

from __future__ import annotations

import json
from pathlib import Path

from ..okf import l0_abstract, l1_overview, load_bundle


class OKFBundleService:
    """Transport-independent core, so it is testable without an MCP client."""

    def __init__(self, bundle_dir: Path):
        self.bundle_dir = bundle_dir

    def _load(self) -> dict:
        return load_bundle(self.bundle_dir)

    # -- tools ----------------------------------------------------------
    def list_concepts(self, type_filter: str | None = None, status: str | None = None) -> list[dict]:
        out = []
        for slug, c in sorted(self._load().items()):
            if type_filter and c.type.lower() != type_filter.lower():
                continue
            if status and c.status.value != status:
                continue
            out.append(
                {
                    "slug": slug,
                    "title": c.title,
                    "type": c.type,
                    "status": c.status.value,
                    "trust_tier": c.trust_tier,
                    "description": c.description,
                }
            )
        return out

    def search(self, query: str, limit: int = 10) -> list[dict]:
        """Substring scoring. No embeddings, no index, no service to run."""
        q = query.lower().strip()
        if not q:
            return []
        terms = q.split()
        scored = []
        for slug, c in self._load().items():
            haystack = f"{c.title}\n{c.description}\n{' '.join(c.tags)}\n{c.body}".lower()
            score = sum(haystack.count(t) for t in terms)
            if c.title.lower().find(q) >= 0:
                score += 25
            if c.description.lower().find(q) >= 0:
                score += 10
            if score:
                scored.append((score, slug, c))
        scored.sort(key=lambda x: -x[0])
        return [
            {
                "slug": slug,
                "title": c.title,
                "score": score,
                "status": c.status.value,
                "trust_tier": c.trust_tier,
                "description": c.description,
            }
            for score, slug, c in scored[:limit]
        ]

    def abstract(self, slug: str) -> str:
        c = self._load().get(slug)
        return l0_abstract(c) if c else f"not found: {slug}"

    def overview(self, slug: str) -> str:
        c = self._load().get(slug)
        return l1_overview(c) if c else f"not found: {slug}"

    def read(self, slug: str) -> str:
        c = self._load().get(slug)
        if not c:
            return f"not found: {slug}"
        return c.body

    def provenance(self, slug: str) -> dict:
        c = self._load().get(slug)
        if not c:
            return {"error": f"not found: {slug}"}
        return {
            "slug": slug,
            "status": c.status.value,
            "trust_tier": c.trust_tier,
            "generated": {"by": c.generated.by, "at": c.generated.at.isoformat()} if c.generated else None,
            "verified": [{"by": a.by, "at": a.at.isoformat()} for a in c.verified],
            "sources": [{"id": s.id, "resource": s.resource, "author": s.author} for s in c.sources],
        }

    def stats(self) -> dict:
        concepts = self._load()
        by_status: dict[str, int] = {}
        by_tier: dict[str, int] = {}
        for c in concepts.values():
            by_status[c.status.value] = by_status.get(c.status.value, 0) + 1
            by_tier[c.trust_tier] = by_tier.get(c.trust_tier, 0) + 1
        return {"total": len(concepts), "by_status": by_status, "by_trust_tier": by_tier}


def _server_class():
    """Locate the decorator-style server class across MCP SDK versions.

    The SDK renamed this: older releases expose ``mcp.server.fastmcp.FastMCP``,
    newer ones ``mcp.server.mcpserver.MCPServer``. Both present the same
    ``.tool()`` / ``.run()`` surface, so we bind whichever is available rather
    than pinning a narrow version range.
    """
    try:
        from mcp.server.mcpserver import MCPServer

        return MCPServer
    except ImportError:
        pass
    try:
        from mcp.server.fastmcp import FastMCP

        return FastMCP
    except ImportError as exc:
        raise ImportError(
            "no compatible MCP server class found; install the extra: uv sync --extra mcp"
        ) from exc


def build_server(bundle_dir: Path):  # pragma: no cover - requires the mcp extra
    svc = OKFBundleService(bundle_dir)
    mcp = _server_class()("okf-bundle")

    @mcp.tool()
    def okf_list(type_filter: str = "", status: str = "") -> str:
        """List concepts in the bundle, optionally filtered by type or status."""
        return json.dumps(svc.list_concepts(type_filter or None, status or None), indent=2)

    @mcp.tool()
    def okf_search(query: str, limit: int = 10) -> str:
        """Search concepts by keyword. Returns ranked slugs with L0 descriptions."""
        return json.dumps(svc.search(query, limit), indent=2)

    @mcp.tool()
    def okf_abstract(slug: str) -> str:
        """L0: one-line summary. Cheapest way to check relevance."""
        return svc.abstract(slug)

    @mcp.tool()
    def okf_overview(slug: str) -> str:
        """L1: heading outline plus the opening of the overview. For planning."""
        return svc.overview(slug)

    @mcp.tool()
    def okf_read(slug: str) -> str:
        """L2: the full concept document. Load only once you know you need it."""
        return svc.read(slug)

    @mcp.tool()
    def okf_provenance(slug: str) -> str:
        """Trust signals: status, derived trust tier, generating actor, sources."""
        return json.dumps(svc.provenance(slug), indent=2)

    @mcp.tool()
    def okf_stats() -> str:
        """Bundle-level counts by status and trust tier."""
        return json.dumps(svc.stats(), indent=2)

    return mcp
