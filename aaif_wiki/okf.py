"""Open Knowledge Format v0.2 reading, writing and conformance.

Deliberately dependency-light and bundle-agnostic: nothing in this module knows
about AAIF. That is what lets the MCP server (exporters/mcp_server.py) serve any
OKF bundle, not just this one.

Spec notes that are easy to get wrong and are therefore encoded here:

* ``type`` is the ONLY field OKF requires. ``title``/``description``/``resource``/
  ``tags`` are RECOMMENDED. This project mandates more than the spec does; that is
  a *profile*, and :func:`validate_concept` reports profile violations separately
  from spec violations.
* v0.1 ``timestamp`` is superseded by ``generated.at``; a v0.1 document is still
  valid and we fall back rather than reject.
* The body ``# Citations`` list is superseded by frontmatter ``sources``; per-claim
  attribution uses markdown footnotes keyed to the source id (``[^src-id]``).
* ``status`` absent means ``stable``.
* Trust tiers are DERIVED from ``verified``, never stored. The spec deliberately
  refuses to persist a computed credibility score.
* OKF has NO typed-relationship field. Edge typing is a producer extension and is
  namespaced under ``x_aaif_`` so a downstream consumer cannot mistake it for spec.
"""

from __future__ import annotations

import re
from datetime import date, datetime
from pathlib import Path
from typing import Any

import yaml

from .models import Actor, Concept, ConceptSource, ConceptStatus

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", re.DOTALL)
LINK_RE = re.compile(r"(?<!\!)\[([^\]]*)\]\(([^)]+)\)")
FOOTNOTE_DEF_RE = re.compile(r"^\[\^([^\]]+)\]:", re.MULTILINE)
FOOTNOTE_REF_RE = re.compile(r"\[\^([^\]]+)\]")

# Namespace for anything that is not in the OKF spec.
EXTENSION_PREFIX = "x_aaif_"

SPEC_REQUIRED = {"type"}
PROFILE_REQUIRED = {"type", "title", "description", "generated", "status"}


# --------------------------------------------------------------------------
# serialization
# --------------------------------------------------------------------------


def _iso(value: Any) -> Any:
    if isinstance(value, datetime):
        return value.isoformat()
    if isinstance(value, date):
        return value.isoformat()
    return value


def _actor_to_dict(actor: Actor) -> dict:
    return {"by": actor.by, "at": _iso(actor.at)}


def concept_to_frontmatter(concept: Concept) -> dict:
    """Build the YAML frontmatter mapping for a concept, in spec field order."""
    fm: dict[str, Any] = {"type": concept.type, "title": concept.title}
    if concept.description:
        fm["description"] = concept.description
    if concept.resource:
        fm["resource"] = concept.resource
    if concept.tags:
        fm["tags"] = list(concept.tags)

    # v0.2 trust / lifecycle
    fm["status"] = concept.status.value
    if concept.generated:
        fm["generated"] = _actor_to_dict(concept.generated)
    if concept.verified:
        fm["verified"] = [_actor_to_dict(a) for a in concept.verified]
    if concept.stale_after:
        fm["stale_after"] = _iso(concept.stale_after)
    if concept.sources:
        out = []
        for s in concept.sources:
            entry: dict[str, Any] = {"id": s.id, "resource": s.resource}
            if s.author:
                entry["author"] = s.author
            if s.last_modified:
                entry["last_modified"] = _iso(s.last_modified)
            if s.usage_count is not None:
                entry["usage_count"] = s.usage_count
            out.append(entry)
        fm["sources"] = out
    return fm


def render_concept(concept: Concept) -> str:
    """Render a concept to an OKF v0.2 markdown document."""
    fm = concept_to_frontmatter(concept)
    head = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True).strip()
    body = concept.body.strip()

    # Footnote definitions for any source referenced in the body but not yet defined.
    defined = set(FOOTNOTE_DEF_RE.findall(body))
    referenced = set(FOOTNOTE_REF_RE.findall(body)) - defined
    if referenced:
        by_id = {s.id: s for s in concept.sources}
        lines = []
        for ref in sorted(referenced):
            src = by_id.get(ref)
            if src:
                lines.append(f"[^{ref}]: {src.resource}")
        if lines:
            body = f"{body}\n\n" + "\n".join(lines)

    return f"---\n{head}\n---\n\n{body}\n"


def _parse_actor(raw: Any) -> Actor | None:
    if not isinstance(raw, dict):
        return None
    by, at = raw.get("by"), raw.get("at")
    if not by or not at:
        return None
    if isinstance(at, str):
        at = datetime.fromisoformat(at.replace("Z", "+00:00"))
    elif isinstance(at, date) and not isinstance(at, datetime):
        at = datetime.combine(at, datetime.min.time())
    return Actor(by=str(by), at=at)


def parse_concept(text: str, slug: str = "") -> Concept:
    """Parse an OKF document. Tolerant by design: v0.1 docs must still load."""
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError("document has no YAML frontmatter block")
    fm = yaml.safe_load(match.group(1)) or {}
    body = match.group(2)

    if not isinstance(fm, dict):
        raise ValueError("frontmatter is not a mapping")

    generated = _parse_actor(fm.get("generated"))
    # v0.1 fallback: `timestamp` is superseded by `generated.at` but still valid.
    if generated is None and fm.get("timestamp"):
        ts = fm["timestamp"]
        if isinstance(ts, str):
            ts = datetime.fromisoformat(ts.replace("Z", "+00:00"))
        elif isinstance(ts, date) and not isinstance(ts, datetime):
            ts = datetime.combine(ts, datetime.min.time())
        generated = Actor(by="unknown", at=ts)

    verified = [a for a in (_parse_actor(v) for v in fm.get("verified") or []) if a]

    sources = []
    for raw in fm.get("sources") or []:
        if not isinstance(raw, dict) or "id" not in raw:
            continue
        lm = raw.get("last_modified")
        if isinstance(lm, str):
            lm = datetime.fromisoformat(lm.replace("Z", "+00:00"))
        elif isinstance(lm, date) and not isinstance(lm, datetime):
            lm = datetime.combine(lm, datetime.min.time())
        sources.append(
            ConceptSource(
                id=str(raw["id"]),
                resource=str(raw.get("resource", "")),
                author=raw.get("author"),
                last_modified=lm,
                usage_count=raw.get("usage_count"),
            )
        )

    status_raw = fm.get("status")
    try:
        # Spec: absent means stable.
        status = ConceptStatus(status_raw) if status_raw else ConceptStatus.STABLE
    except ValueError:
        status = ConceptStatus.STABLE

    stale_after = fm.get("stale_after")
    if isinstance(stale_after, str):
        stale_after = date.fromisoformat(stale_after)
    elif isinstance(stale_after, datetime):
        stale_after = stale_after.date()

    return Concept(
        type=str(fm.get("type", "Concept")),
        title=str(fm.get("title", slug or "Untitled")),
        description=str(fm.get("description", "")),
        resource=fm.get("resource"),
        tags=list(fm.get("tags") or []),
        generated=generated,
        verified=verified,
        status=status,
        stale_after=stale_after,
        sources=sources,
        slug=slug,
        body=body,
    )


# --------------------------------------------------------------------------
# bundle IO
# --------------------------------------------------------------------------


def load_bundle(bundle_dir: Path) -> dict[str, Concept]:
    """Load every concept in a bundle, keyed by slug (path relative to root, no .md)."""
    concepts: dict[str, Concept] = {}
    if not bundle_dir.exists():
        return concepts
    for path in sorted(bundle_dir.rglob("*.md")):
        slug = path.relative_to(bundle_dir).with_suffix("").as_posix()
        if slug in {"index", "log"}:
            continue
        try:
            concepts[slug] = parse_concept(path.read_text(), slug=slug)
        except (ValueError, yaml.YAMLError):
            continue
    return concepts


def write_concept(bundle_dir: Path, concept: Concept) -> Path:
    path = bundle_dir / concept.relative_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_concept(concept))
    return path


def extract_links(body: str) -> list[str]:
    """Return markdown link targets, excluding images, anchors and external URLs."""
    out = []
    for _text, target in LINK_RE.findall(body):
        target = target.strip()
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        out.append(target.split("#")[0])
    return [t for t in out if t]


def is_root_absolute(target: str) -> bool:
    """Root-absolute links break on GitHub Pages sub-paths and in Obsidian."""
    return target.startswith("/")


# --------------------------------------------------------------------------
# tiered context (ADR-006 authoring discipline)
# --------------------------------------------------------------------------


def l0_abstract(concept: Concept) -> str:
    """~1 sentence. Used for relevance checks before committing to a read."""
    return concept.description.strip()


def l1_overview(concept: Concept) -> str:
    """Headings plus the first paragraph of ``# Overview``."""
    headings = [
        line.strip()
        for line in concept.body.splitlines()
        if line.strip().startswith(("#", "##", "###"))
    ]
    first_para = ""
    in_overview = False
    buf: list[str] = []
    for line in concept.body.splitlines():
        if line.strip().lower().startswith("# overview"):
            in_overview = True
            continue
        if in_overview:
            if line.strip().startswith("#"):
                break
            if not line.strip() and buf:
                break
            if line.strip():
                buf.append(line.strip())
    first_para = " ".join(buf)
    return "\n".join([*headings, "", first_para]).strip()
