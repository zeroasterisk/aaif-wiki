"""Deterministic validators (ADR-008).

Everything here runs without an LLM, without network, and in well under a second.
That is the point: these are the checks that can gate CI and block a merge, and
they catch the majority of real failure modes (broken links, dangling provenance,
schema drift, leaked paths) for effectively zero cost.

The distinction between *spec* violations and *profile* violations is deliberate.
OKF requires only ``type``; this bundle requires more. Conflating the two would
misreport a local policy choice as a standards violation.
"""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import urlparse

from ..models import Concept, Mutation, ValidateResult, ValidationIssue
from ..okf import PROFILE_REQUIRED, SPEC_REQUIRED, extract_links, is_root_absolute, load_bundle

SLUG_RE = re.compile(r"^[a-z0-9]+(?:[-/][a-z0-9]+)*$")
URL_RE = re.compile(r"https?://[^\s<>()\[\]\"']+")


def _issue(severity: str, check: str, path: str, message: str) -> ValidationIssue:
    return ValidationIssue(severity=severity, check=check, path=path, message=message)


# --------------------------------------------------------------------------
# concept-level
# --------------------------------------------------------------------------


def validate_concept(
    concept: Concept,
    *,
    known_slugs: set[str] | None = None,
    known_event_ids: set[str] | None = None,
    link_allowlist: list[str] | None = None,
    forbidden_patterns: list[str] | None = None,
) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    path = concept.relative_path()

    # -- OKF spec conformance
    for field in SPEC_REQUIRED:
        if not getattr(concept, field, None):
            issues.append(_issue("error", "okf-spec", path, f"missing required OKF field: {field}"))

    # -- aaif-wiki profile
    for field in PROFILE_REQUIRED - SPEC_REQUIRED:
        if not getattr(concept, field, None):
            issues.append(
                _issue("error", "okf-profile", path, f"missing profile-required field: {field}")
            )

    if concept.slug and not SLUG_RE.match(concept.slug):
        issues.append(_issue("error", "slug", path, f"slug is not kebab/path-safe: {concept.slug!r}"))

    if concept.description and len(concept.description) > 300:
        issues.append(_issue("warning", "l0-length", path, "description exceeds 300 chars (L0 should be one line)"))

    if concept.description and "\n" in concept.description:
        issues.append(_issue("error", "l0-shape", path, "description must be a single line"))

    # -- provenance integrity
    if not concept.generated:
        issues.append(_issue("error", "provenance", path, "no `generated` actor recorded"))
    if not concept.sources:
        issues.append(_issue("warning", "provenance", path, "concept cites no sources"))
    if known_event_ids is not None:
        for src in concept.sources:
            if src.id not in known_event_ids:
                issues.append(
                    _issue("error", "provenance", path, f"sources[] id not in event store: {src.id}")
                )

    # -- trust tier coherence (ADR-009)
    if concept.status.value == "stable" and concept.trust_tier == "unverified":
        issues.append(
            _issue(
                "error",
                "trust",
                path,
                "status=stable but no `verified` entry; only human review may promote to stable",
            )
        )

    # -- body structure (ADR-006 authoring discipline)
    if concept.body and not re.search(r"^#\s+Overview", concept.body, re.MULTILINE):
        issues.append(_issue("warning", "structure", path, "body has no `# Overview` heading"))
    if re.search(r"^#\s+Citations", concept.body, re.MULTILINE):
        issues.append(
            _issue("warning", "okf-v2", path, "`# Citations` is superseded by frontmatter `sources`")
        )

    # -- links
    for target in extract_links(concept.body):
        if is_root_absolute(target):
            issues.append(
                _issue("error", "link-style", path, f"root-absolute link breaks on Pages/Obsidian: {target}")
            )
            continue
        if known_slugs is not None:
            resolved = _resolve(concept.slug, target)
            if resolved is not None and resolved not in known_slugs:
                issues.append(_issue("error", "link-target", path, f"link does not resolve: {target}"))

    # -- outbound link allowlist (ADR-007)
    if link_allowlist is not None:
        for url in URL_RE.findall(concept.body):
            host = (urlparse(url).hostname or "").lower()
            if host and not any(host == a or host.endswith("." + a) for a in link_allowlist):
                issues.append(
                    _issue("error", "link-allowlist", path, f"external host not allowlisted: {host}")
                )

    # -- leak guard (ADR-007)
    for pattern in forbidden_patterns or []:
        if re.search(pattern, concept.body) or re.search(pattern, concept.description):
            issues.append(_issue("error", "leak-guard", path, f"matched forbidden pattern: {pattern}"))

    return issues


def _resolve(from_slug: str, target: str) -> str | None:
    """Resolve a relative markdown link to a bundle slug."""
    if not target.endswith(".md"):
        return None
    base = Path(from_slug).parent
    try:
        return (base / target).resolve().relative_to(Path.cwd().resolve()).with_suffix("").as_posix()
    except (ValueError, OSError):
        import posixpath

        joined = posixpath.normpath(posixpath.join(str(base), target))
        return joined[:-3] if joined.endswith(".md") else joined


# --------------------------------------------------------------------------
# bundle-level
# --------------------------------------------------------------------------


def validate_bundle(
    bundle_dir: Path,
    *,
    known_event_ids: set[str] | None = None,
    link_allowlist: list[str] | None = None,
    forbidden_patterns: list[str] | None = None,
) -> ValidateResult:
    concepts = load_bundle(bundle_dir)
    known_slugs = set(concepts)
    issues: list[ValidationIssue] = []

    for concept in concepts.values():
        issues.extend(
            validate_concept(
                concept,
                known_slugs=known_slugs,
                known_event_ids=known_event_ids,
                link_allowlist=link_allowlist,
                forbidden_patterns=forbidden_patterns,
            )
        )

    # bundle root must declare the OKF version (spec §11)
    index = bundle_dir / "index.md"
    if not index.exists():
        issues.append(_issue("error", "bundle", "index.md", "bundle root index.md is missing"))
    elif "okf_version" not in index.read_text():
        issues.append(
            _issue("error", "bundle", "index.md", "bundle root must declare okf_version: \"0.2\"")
        )

    # orphan detection: reachable from index or linked by another concept
    linked: set[str] = set()
    for concept in concepts.values():
        for target in extract_links(concept.body):
            resolved = _resolve(concept.slug, target)
            if resolved:
                linked.add(resolved)
    if index.exists():
        for target in extract_links(index.read_text()):
            resolved = _resolve("", target)
            if resolved:
                linked.add(resolved)
    for slug in known_slugs - linked:
        issues.append(_issue("warning", "orphan", f"{slug}.md", "concept is not linked from anywhere"))

    return ValidateResult(issues=issues, checked=len(concepts))


def validate_mutation(mutation: Mutation) -> list[ValidationIssue]:
    """Gate a mutation before it is allowed to touch the filesystem."""
    issues: list[ValidationIssue] = []
    slug = mutation.slug
    if not SLUG_RE.match(slug):
        issues.append(_issue("error", "slug", slug, f"unsafe slug: {slug!r}"))
    if ".." in slug or slug.startswith("/"):
        issues.append(_issue("error", "path-escape", slug, "slug attempts to escape the bundle"))
    if mutation.action != "deprecate" and mutation.concept is None:
        issues.append(_issue("error", "mutation", slug, f"action={mutation.action} requires a concept"))
    return issues
