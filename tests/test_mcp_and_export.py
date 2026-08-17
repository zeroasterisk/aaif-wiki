"""Generic OKF MCP service and exporters.

The MCP service is deliberately bundle-agnostic, so these tests build a synthetic
bundle in a tmpdir rather than depending on the AAIF content. If a test here ever
needs to know about AAIF, the abstraction has leaked.
"""

from __future__ import annotations

from datetime import UTC, datetime

import pytest

from aaif_wiki.config import Config, ProjectCfg
from aaif_wiki.exporters.gist import GistExporter
from aaif_wiki.exporters.graph import GraphExporter
from aaif_wiki.exporters.mcp_server import OKFBundleService
from aaif_wiki.models import Actor, Concept, ConceptSource, ConceptStatus
from aaif_wiki.okf import write_concept

NOW = datetime(2026, 8, 17, tzinfo=UTC)


@pytest.fixture
def bundle(tmp_path):
    root = tmp_path / "wiki"
    root.mkdir()
    write_concept(
        root,
        Concept(
            type="Working Group",
            title="Security and Privacy",
            description="Threat models and privacy patterns for agentic systems.",
            slug="working-groups/security",
            tags=["security"],
            generated=Actor(by="agent:test/gemini-3.7-flash", at=NOW),
            sources=[ConceptSource(id="evt-1", resource="https://github.com/aaif/x")],
            body=(
                "# Overview\n\nThe WG covers threat modeling.\n\n"
                "## Scope\n\nSee [taxonomy](../taxonomy/attested-runtime.md).\n"
            ),
        ),
    )
    write_concept(
        root,
        Concept(
            type="Glossary Term",
            title="Attested Runtime",
            description="Hardware-isolated execution with remote attestation.",
            slug="taxonomy/attested-runtime",
            generated=Actor(by="agent:test/gemini-3.7-flash", at=NOW),
            status=ConceptStatus.STABLE,
            verified=[Actor(by="human:alan", at=NOW)],
            sources=[ConceptSource(id="evt-2", resource="https://github.com/aaif/y")],
            body="# Overview\n\nAn attested runtime proves its own integrity.\n",
        ),
    )
    (root / "index.md").write_text(
        '---\nokf_version: "0.2"\ntype: Index\ntitle: T\ndescription: d\nstatus: draft\n---\n\n'
        "# Overview\n\nx\n\n- [a](working-groups/security.md)\n- [b](taxonomy/attested-runtime.md)\n"
    )
    return root


def _cfg(tmp_path, bundle_dir) -> Config:
    cfg = Config(project=ProjectCfg(bundle_root=bundle_dir.name, dist_dir="dist"))
    cfg.root = tmp_path
    return cfg


# --------------------------------------------------------------------------
# MCP service
# --------------------------------------------------------------------------


def test_list_and_filter(bundle):
    svc = OKFBundleService(bundle)
    assert len(svc.list_concepts()) == 2
    assert len(svc.list_concepts(type_filter="Glossary Term")) == 1
    assert len(svc.list_concepts(status="stable")) == 1


def test_search_ranks_title_matches_higher(bundle):
    results = OKFBundleService(bundle).search("attested runtime")
    assert results[0]["slug"] == "taxonomy/attested-runtime"


def test_search_empty_query_returns_nothing(bundle):
    assert OKFBundleService(bundle).search("   ") == []


def test_tiered_reads_get_progressively_larger(bundle):
    svc = OKFBundleService(bundle)
    slug = "working-groups/security"
    l0, l1, l2 = svc.abstract(slug), svc.overview(slug), svc.read(slug)
    assert len(l0) < len(l2)
    assert "## Scope" in l1, "L1 should expose the heading tree"
    assert "threat modeling" in l2.lower()


def test_missing_slug_is_reported_not_raised(bundle):
    assert "not found" in OKFBundleService(bundle).abstract("nope/nope")


def test_provenance_exposes_derived_trust_tier(bundle):
    svc = OKFBundleService(bundle)
    assert svc.provenance("taxonomy/attested-runtime")["trust_tier"] == "human-reviewed"
    assert svc.provenance("working-groups/security")["trust_tier"] == "unverified"


def test_stats(bundle):
    stats = OKFBundleService(bundle).stats()
    assert stats["total"] == 2
    assert stats["by_trust_tier"]["human-reviewed"] == 1


# --------------------------------------------------------------------------
# exporters
# --------------------------------------------------------------------------


def test_graph_export_resolves_edges(tmp_path, bundle):
    result = GraphExporter(_cfg(tmp_path, bundle)).export()
    assert result.ok
    import json

    graph = json.loads(result.artifacts[0].read_text())
    assert graph["okf_version"] == "0.2"
    assert graph["stats"]["nodes"] == 2
    assert graph["edges"][0]["target"] == "taxonomy/attested-runtime"


def test_graph_export_writes_outside_the_bundle(tmp_path, bundle):
    """Build artifacts must not pollute the canonical OKF bundle."""
    result = GraphExporter(_cfg(tmp_path, bundle)).export()
    assert bundle not in result.artifacts[0].parents


def test_leak_guard_blocks_export(tmp_path, bundle):
    write_concept(
        bundle,
        Concept(
            type="Note", title="Leaky", description="d", slug="leaky",
            generated=Actor(by="agent:t", at=NOW),
            body="# Overview\n\nBuilt from /google/src/thing.\n",
        ),
    )
    result = GraphExporter(_cfg(tmp_path, bundle)).export()
    assert not result.ok
    assert result.blocked


def test_digest_publishes_only_human_reviewed(tmp_path, bundle):
    """Draft/unverified content must never reach a public digest (ADR-009)."""
    result = GistExporter(_cfg(tmp_path, bundle)).export()
    assert result.ok
    text = result.artifacts[0].read_text()
    assert "Attested Runtime" in text, "human-reviewed concept should publish"
    assert "Security and Privacy" not in text, "unverified concept must be withheld"
    assert "Unofficial" in text, "disclaimer is mandatory (ADR-010)"
