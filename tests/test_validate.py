"""Validator tests -- the LLM-free CI gate.

These are the checks that block a merge, so their failure modes matter more than
most. Each test pins one rule that a real bug would otherwise slip past.
"""

from __future__ import annotations

from datetime import UTC, datetime

from aaif_wiki.models import Actor, Concept, ConceptSource, ConceptStatus, Mutation
from aaif_wiki.validate import validate_concept, validate_mutation

NOW = datetime(2026, 8, 17, tzinfo=UTC)
AGENT = Actor(by="agent:aaif-wiki-curator/gemini-3.7-flash", at=NOW)


def _c(**kw) -> Concept:
    base = dict(
        type="Working Group",
        title="Security",
        description="A working group.",
        slug="working-groups/security",
        body="# Overview\n\nBody text.\n",
        generated=AGENT,
        sources=[ConceptSource(id="evt-1", resource="https://github.com/aaif/x")],
    )
    base.update(kw)
    return Concept(**base)


def _checks(issues) -> set[str]:
    return {i.check for i in issues}


def test_clean_concept_has_no_errors():
    issues = validate_concept(_c(), known_event_ids={"evt-1"})
    assert [i for i in issues if i.severity == "error"] == []


def test_stable_without_human_review_is_an_error():
    """Only human review may promote a concept to stable (ADR-009)."""
    issues = validate_concept(_c(status=ConceptStatus.STABLE), known_event_ids={"evt-1"})
    assert "trust" in _checks(issues)


def test_stable_with_human_verification_is_allowed():
    c = _c(status=ConceptStatus.STABLE, verified=[Actor(by="human:alan", at=NOW)])
    issues = validate_concept(c, known_event_ids={"evt-1"})
    assert "trust" not in _checks(issues)


def test_dangling_source_id_is_an_error():
    issues = validate_concept(_c(), known_event_ids={"some-other-event"})
    assert "provenance" in _checks(issues)


def test_root_absolute_link_is_an_error():
    c = _c(body="# Overview\n\nSee [x](/taxonomy/x.md).\n")
    assert "link-style" in _checks(validate_concept(c, known_event_ids={"evt-1"}))


def test_non_allowlisted_host_is_blocked():
    c = _c(body="# Overview\n\nSee [x](https://evil.example.com/steal).\n")
    issues = validate_concept(c, known_event_ids={"evt-1"}, link_allowlist=["github.com", "aaif.io"])
    assert "link-allowlist" in _checks(issues)


def test_allowlisted_host_passes():
    c = _c(body="# Overview\n\nSee [x](https://github.com/aaif/foundation).\n")
    issues = validate_concept(c, known_event_ids={"evt-1"}, link_allowlist=["github.com"])
    assert "link-allowlist" not in _checks(issues)


def test_leak_guard_catches_internal_paths():
    c = _c(body="# Overview\n\nBuilt at /google/bin/thing.\n")
    issues = validate_concept(
        c, known_event_ids={"evt-1"}, forbidden_patterns=[r"/google/(bin|src)/"]
    )
    assert "leak-guard" in _checks(issues)


def test_multiline_description_is_an_error():
    """L0 must be a single line; it is what an agent reads before loading."""
    assert "l0-shape" in _checks(validate_concept(_c(description="a\nb"), known_event_ids={"evt-1"}))


def test_v01_citations_heading_is_flagged():
    c = _c(body="# Overview\n\nx\n\n# Citations\n\n- a\n")
    assert "okf-v2" in _checks(validate_concept(c, known_event_ids={"evt-1"}))


def test_unresolvable_internal_link_is_an_error():
    c = _c(body="# Overview\n\nSee [y](../taxonomy/missing.md).\n")
    issues = validate_concept(c, known_slugs={"working-groups/security"}, known_event_ids={"evt-1"})
    assert "link-target" in _checks(issues)


def test_mutation_path_escape_is_rejected():
    m = Mutation(action="create", slug="../../etc/passwd", concept=_c())
    checks = {i.check for i in validate_mutation(m)}
    assert "slug" in checks or "path-escape" in checks


def test_mutation_without_concept_is_rejected():
    assert "mutation" in {i.check for i in validate_mutation(Mutation(action="create", slug="a/b"))}


def test_deprecate_needs_no_concept():
    assert validate_mutation(Mutation(action="deprecate", slug="a/b")) == []
