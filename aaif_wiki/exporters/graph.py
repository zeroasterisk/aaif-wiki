"""Compile the bundle into a node/edge graph.

Note the output location: ``dist/``, not ``wiki/``. The original design wrote
``graph.json`` into the bundle itself, which put a regenerable build artifact
inside the canonical source of truth -- a guaranteed merge conflict on concurrent
runs, and a file every OKF consumer has to know to skip.

Edge typing is namespaced under ``x_aaif_`` because OKF has no typed-relationship
field; typed edges remain an upstream proposal, not spec.
"""

from __future__ import annotations

import json
from pathlib import Path

from ..okf import extract_links, load_bundle
from .base import BaseExporter, ExportResult


class GraphExporter(BaseExporter):
    name = "graph"

    def export(self) -> ExportResult:
        concepts = load_bundle(self.cfg.bundle_dir)
        if not concepts:
            return ExportResult(ok=True, message="bundle is empty; nothing to compile")

        blocked = self.guard(list(concepts.values()))
        if blocked:
            return ExportResult(ok=False, blocked=blocked, message="leak guard blocked export")

        nodes = []
        for slug, c in sorted(concepts.items()):
            nodes.append(
                {
                    "id": slug,
                    "title": c.title,
                    "type": c.type,
                    "description": c.description,
                    "status": c.status.value,
                    "trust_tier": c.trust_tier,
                    "tags": c.tags,
                    "resource": c.resource,
                    "source_count": len(c.sources),
                }
            )

        edges = []
        known = set(concepts)
        for slug, c in sorted(concepts.items()):
            for target in extract_links(c.body):
                if not target.endswith(".md"):
                    continue
                import posixpath

                base = posixpath.dirname(slug)
                resolved = posixpath.normpath(posixpath.join(base, target))[:-3]
                if resolved in known:
                    edges.append({"source": slug, "target": resolved, "x_aaif_rel": "references"})

        payload = {
            "okf_version": "0.2",
            "generator": "aaif-wiki",
            "nodes": nodes,
            "edges": edges,
            "stats": {
                "nodes": len(nodes),
                "edges": len(edges),
                "by_status": _tally(nodes, "status"),
                "by_trust_tier": _tally(nodes, "trust_tier"),
            },
        }

        out_dir: Path = self.cfg.dist_dir
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / "graph.json"
        path.write_text(json.dumps(payload, indent=2))
        return ExportResult(ok=True, artifacts=[path], message=f"{len(nodes)} nodes, {len(edges)} edges")


def _tally(nodes: list[dict], key: str) -> dict[str, int]:
    out: dict[str, int] = {}
    for n in nodes:
        out[n[key]] = out.get(n[key], 0) + 1
    return out
