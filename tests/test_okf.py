"""OKF v0.2 conformance tests.

These encode the spec details that are easiest to get wrong, so a regression
shows up as a red test rather than as a subtly non-conformant bundle.
"""

from __future__ import annotations

from datetime import UTC, datetime

from aaif_wiki.models import Actor, Concept, ConceptSource, ConceptStatus
from aaif_wiki.okf import (
    extract_links,
    is_root_absolute,
    l0_abstract,
    l1_overview,
    parse_concept,
    render_concept,
)

NOW = datetime(2026, 8, 17, 12, 0, tzinfo=UTC)


def _concept(**kw) -> Concept:
    base = dict(
        type="Working Group",
        title="Security and Privacy",
        description="AAIF working group covering agent security and privacy.",
        slug="working-groups/security-and-privacy",
        body="# Overview\n\nThe WG covers security.\n",
        generated=Actor(by="agent:test/gemini-3.7-flash", at=NOW),
    )
    base.update(kw)
    return Concept(**base)


def test_roundtrip_preserves_v2_fields():
    original = _concept(
        status=ConceptStatus.STABLE,
        verified=[Actor(by="human:zeroasterisk", at=NOW)],
        sources=[ConceptSource(id="evt-1", resource="https://github.com/aaif/x", author="alice")],
        tags=["security"],
    )
    parsed = parse_concept(render_concept(original), slug=original.slug)

    assert parsed.type == "Working Group"
    assert parsed.status is ConceptStatus.STABLE
    assert parsed.sources[0].id == "evt-1"
    assert parsed.sources[0].author == "alice"
    assert parsed.verified[0].by == "human:zeroasterisk"
    assert parsed.generated.by == "agent:test/gemini-3.7-flash"


def test_absent_status_means_stable():
    """Spec: absent `status` means stable, not draft."""
    doc = "---\ntype: Metric\ntitle: X\n---\n\n# Overview\n\nbody\n"
    assert parse_concept(doc).status is ConceptStatus.STABLE


def test_v01_timestamp_falls_back_to_generated_at():
    """v0.1 `timestamp` is superseded by `generated.at` but must still load."""
    doc = "---\ntype: Metric\ntitle: X\ntimestamp: '2026-05-28T22:53:05+00:00'\n---\n\n# Overview\n\nb\n"
    parsed = parse_concept(doc)
    assert parsed.generated is not None
    assert parsed.generated.at.year == 2026


def test_trust_tier_is_derived_not_stored():
    assert _concept().trust_tier == "unverified"
    assert _concept(verified=[Actor(by="agent:x", at=NOW)]).trust_tier == "machine-confirmed"
    assert _concept(verified=[Actor(by="human:alan", at=NOW)]).trust_tier == "human-reviewed"

    # Derived value must never be persisted into frontmatter.
    assert "trust_tier" not in render_concept(_concept(verified=[Actor(by="human:a", at=NOW)]))


def test_footnote_definitions_are_emitted_for_cited_sources():
    c = _concept(
        body="# Overview\n\nAttested runtime matters.[^evt-9]\n",
        sources=[ConceptSource(id="evt-9", resource="https://github.com/aaif/wg/pull/11")],
    )
    rendered = render_concept(c)
    assert "[^evt-9]: https://github.com/aaif/wg/pull/11" in rendered


def test_root_absolute_links_are_detected():
    assert is_root_absolute("/architectures/x.md")
    assert not is_root_absolute("../architectures/x.md")


def test_extract_links_ignores_external_and_images():
    body = "[a](../x.md) [b](https://example.com) ![img](y.png) [c](#anchor)"
    # Images, external URLs and bare anchors are all excluded; only real
    # intra-bundle link targets become graph edges.
    assert extract_links(body) == ["../x.md"]


def test_tiered_context_extraction():
    c = _concept(body="# Overview\n\nFirst para here.\n\nSecond.\n\n## Details\n\nmore\n")
    assert l0_abstract(c) == c.description
    overview = l1_overview(c)
    assert "# Overview" in overview
    assert "## Details" in overview
    assert "First para here." in overview
