"""External (non-AAIF) sources: config, connector coordinates, curator provenance (ADR-013)."""

from __future__ import annotations

import json
import subprocess
from datetime import UTC, datetime

from aaif_wiki.config import BudgetCfg, CuratorCfg, ExternalSourceCfg, GitHubCfg, load_config
from aaif_wiki.connectors.github import GitHubConnector, is_external
from aaif_wiki.curator.agent import Curator
from aaif_wiki.curator.prompts import PromptAssembler, external_steward
from aaif_wiki.models import BudgetState, ConceptSource, Lifecycle, RawEvent, SourceType

NOW = datetime(2026, 10, 18, tzinfo=UTC)

EXT = ExternalSourceCfg(
    repo="example-org/agent-pay",
    steward="FIDO Alliance",
    topics=["payments"],
    include_paths=["README.md", "docs"],
    file_limit=10,
)


def _cfg(**kw) -> GitHubCfg:
    return GitHubCfg(discover_repos=False, repositories=["wg-agentic-commerce"], external=[EXT], **kw)


def test_project_config_loads_external_sources():
    cfg = load_config()
    ext = cfg.sources.github.external
    assert ext, "config.yaml should declare external sources"
    assert all("/" in e.repo and e.steward for e in ext)
    assert all("aaif" not in e.steward.lower() for e in ext), "external stewards are never AAIF"
    assert cfg.sources.github.external_for("google-agentic-commerce/AP2").steward == "FIDO Alliance"


def test_discovery_appends_external_after_aaif(tmp_path):
    conn = GitHubConnector(_cfg(), tmp_path)
    assert conn.discover_repos() == ["wg-agentic-commerce", "example-org/agent-pay"]
    assert is_external("example-org/agent-pay") and not is_external("wg-agentic-commerce")


def test_coordinates_keep_aaif_unchanged(tmp_path):
    conn = GitHubConnector(_cfg(), tmp_path)
    assert conn._full_name("wg-agentic-commerce") == "aaif/wg-agentic-commerce"
    assert conn._event_prefix("wg-agentic-commerce") == "wg-agentic-commerce"
    assert conn._full_name("example-org/agent-pay") == "example-org/agent-pay"
    # event ids are filenames; no slash allowed
    assert "/" not in conn._event_prefix("example-org/agent-pay")


def _git(repo, *args):
    subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True)


def test_scan_files_filters_paths_and_labels_provenance(tmp_path, monkeypatch):
    conn = GitHubConnector(_cfg(), tmp_path)
    repo = conn.repo_cache / "example-org" / "agent-pay"
    (repo / "docs").mkdir(parents=True)
    (repo / "legal").mkdir()
    (repo / "README.md").write_text("# Agent Pay\n")
    (repo / "docs" / "spec.md").write_text("# Spec\n")
    (repo / "legal" / "CLA.md").write_text("# CLA\n")
    _git(repo, "init", "-q")
    _git(repo, "-c", "user.name=t", "-c", "user.email=t@example.com", "add", ".")
    _git(repo, "-c", "user.name=t", "-c", "user.email=t@example.com", "commit", "-qm", "init")
    monkeypatch.setattr(conn, "sync_repo", lambda r: repo)

    events = conn.scan_files("example-org/agent-pay")
    paths = sorted(e.reference_id for e in events)
    assert paths == ["README.md", "docs/spec.md"], "include_paths must exclude legal/CLA.md"
    for e in events:
        assert e.repository == "example-org/agent-pay"
        assert e.url.startswith("https://github.com/example-org/agent-pay/blob/")
        assert e.event_id.startswith("evt-ext-example-org-agent-pay-")
        assert "external" in e.labels and "steward:FIDO Alliance" in e.labels
        assert external_steward(e) == "FIDO Alliance"


def test_external_prs_and_issues_off_by_default(tmp_path, monkeypatch):
    conn = GitHubConnector(_cfg(), tmp_path)
    monkeypatch.setattr(conn, "_get", lambda *a, **k: (_ for _ in ()).throw(AssertionError("no API call")))
    assert conn.scan_pull_requests("example-org/agent-pay") == []
    assert conn.scan_issues("example-org/agent-pay") == []


def _event(labels):
    return RawEvent(
        event_id="evt-ext-x-file-1",
        source_type=SourceType.REPO_FILE,
        lifecycle=Lifecycle.MERGED,
        repository="example-org/agent-pay",
        reference_id="README.md",
        title="README.md",
        timestamp=NOW,
        url="https://github.com/example-org/agent-pay/blob/abc/README.md",
        inline_text="Agent Pay is a payments protocol.",
        labels=labels,
    )


def test_prompt_marks_external_steward():
    text = PromptAssembler().volatile([_event(["external", "steward:FIDO Alliance"])])
    assert "steward: FIDO Alliance (EXTERNAL -- not AAIF" in text
    plain = PromptAssembler().volatile([_event([])])
    assert "steward:" not in plain
    assert "NEVER describe them as AAIF work" in PromptAssembler().stable()


def test_curator_tags_concepts_from_external_sources():
    curator = Curator(CuratorCfg(), BudgetCfg(), BudgetState())
    event = _event(["external", "steward:FIDO Alliance"])
    payload = {
        "mutations": [
            {
                "action": "create",
                "slug": "standards/agent-pay",
                "rationale": "r",
                "source_event_ids": [event.event_id],
                "concept": {
                    "type": "Standard",
                    "title": "Agent Pay",
                    "description": "d",
                    "tags": ["payments"],
                    "body": "# Overview\nAgent Pay is stewarded by the FIDO Alliance.",
                },
            }
        ]
    }
    [m] = curator._parse(json.dumps(payload), [event])
    assert m.concept.tags[0] == "external" and "payments" in m.concept.tags


def _concept(ids: list[str]):
    from aaif_wiki.models import Concept, ConceptSource

    return Concept(
        type="Standard", title="t", description="d", body="# Overview\n\nx",
        sources=[ConceptSource(id=i, resource="https://github.com/x") for i in ids],
    )


def _src(eid):
    """Realistic resource URL: provenance is read from the GitHub owner, not the id."""
    if eid.startswith("evt-ext-"):
        return ConceptSource(id=eid, resource="https://github.com/coinbase/x402/blob/a/README.md")
    return ConceptSource(id=eid, resource="https://github.com/aaif/wg-agentic-commerce/blob/a/README.md")


def _page(ids, slug=None, tags=()):
    c = _concept([])
    c.sources = [_src(i) for i in ids]
    c.tags = list(tags)
    if slug:
        c.slug = slug
    return c


def _apply(tmp_path, monkeypatch, mutations):
    import asyncio

    from aaif_wiki import pipeline
    from aaif_wiki.models import CurateResult

    class _Sources:
        github = GitHubCfg()

    class _Cfg:
        bundle_dir = tmp_path
        sources = _Sources()

    monkeypatch.setattr(pipeline, "get_config", lambda: _Cfg())
    return asyncio.run(pipeline.apply_mutations(CurateResult(mutations=mutations)))


def _mut(slug, ids, tags=()):
    from aaif_wiki.models import Mutation

    return Mutation(action="update", slug=slug, rationale="r", source_event_ids=ids,
                    concept=_page(ids, tags=tags))


def test_single_class_rewrite_may_not_flip_page_provenance(tmp_path, monkeypatch):
    """Regression (live run + review #2): updates replace sources wholesale, so a
    single-class rewrite flipped provenance in BOTH directions."""
    from aaif_wiki.okf import load_bundle, write_concept

    write_concept(tmp_path, _page(["evt-wg-agentic-commerce-pr-1"], "working-groups/agentic-commerce"))
    write_concept(tmp_path, _page(["evt-ext-x402-file-1"], "standards/x402", ["external"]))

    res = _apply(tmp_path, monkeypatch, [
        _mut("working-groups/agentic-commerce", ["evt-ext-map-file-9"]),   # refused: AAIF -> external
        _mut("standards/x402", ["evt-wg-agentic-commerce-file-2"]),        # refused: drops steward source
        _mut("working-groups/agentic-commerce", ["evt-ext-a-file-1", "evt-wg-agentic-commerce-file-2"]),
        _mut("standards/x402", ["evt-ext-x402-file-2"]),                   # same class: ok
        _mut("standards/new-thing", ["evt-ext-x402-file-3"]),              # new page: ok
    ])
    assert res.checked == 3
    assert [i.check for i in res.issues] == ["provenance-overwrite"] * 2
    b = load_bundle(tmp_path)
    assert "external" in b["standards/x402"].tags
    assert [s.id for s in b["working-groups/agentic-commerce"].sources] == [
        "evt-ext-a-file-1", "evt-wg-agentic-commerce-file-2"]
    assert "external" in b["working-groups/agentic-commerce"].tags  # mixed page is tagged


def test_external_tag_is_recomputed_from_sources_on_apply(tmp_path, monkeypatch):
    """Model output can't add or strip the tag: apply normalises it from sources."""
    from aaif_wiki.okf import load_bundle

    _apply(tmp_path, monkeypatch, [
        _mut("standards/fake-external", ["evt-wg-agentic-commerce-file-1"], tags=["external", "x"]),
        _mut("standards/hidden-external", ["evt-ext-x402-file-1"], tags=["x"]),
    ])
    b = load_bundle(tmp_path)
    assert b["standards/fake-external"].tags == ["x"]
    assert b["standards/hidden-external"].tags == ["external", "x"]


def test_provenance_reads_github_owner_not_id_prefix():
    from aaif_wiki import provenance

    aaif_named_ext = ConceptSource(id="evt-ext-tools-file-1",
                                   resource="https://github.com/aaif/ext-tools/blob/a/README.md")
    assert not provenance.source_is_external(aaif_named_ext)
    assert provenance.source_is_external(
        ConceptSource(id="evt-wg-x-file-1", resource="https://github.com/coinbase/x402/blob/a/x.md"))
    assert provenance.source_is_external(
        ConceptSource(id="evt-wg-x", resource="https://github.com/aaif-impostor/x/blob/a/x.md"))


def test_validator_flags_external_tag_mismatch():
    from aaif_wiki.validate.checks import validate_concept

    def checks(c):
        return [i.check for i in validate_concept(c)]

    assert "external-tag" in checks(_page(["evt-ext-x402-file-1"], "standards/x402"))
    assert "external-tag" in checks(_page(["evt-wg-agentic-commerce-file-1"], "standards/f", ["external"]))
    assert "external-tag" not in checks(_page(["evt-ext-x402-file-1"], "standards/ok", ["external"]))


# -- review findings on 9273e95 (deleg_45d6a19c) ---------------------------------

def _ev(eid, repo, labels):
    return RawEvent(event_id=eid, source_type=SourceType.REPO_FILE, lifecycle=Lifecycle.MERGED,
                    repository=repo, reference_id="README.md", title="README.md", timestamp=NOW,
                    url=f"https://github.com/{repo}/blob/a/README.md", inline_text="x", labels=labels)


def _payload(slug, ids):
    import json

    return json.dumps({"mutations": [{"action": "update", "slug": slug, "rationale": "r",
        "source_event_ids": ids,
        "concept": {"type": "Concept", "title": "T", "tags": [], "body": "# Overview\nx"}}]})


def test_mixed_batch_without_valid_source_ids_is_dropped_not_misattributed():
    from aaif_wiki.config import BudgetCfg, CuratorCfg
    from aaif_wiki.curator.agent import Curator
    from aaif_wiki.models import BudgetState

    cur = Curator(CuratorCfg(), BudgetCfg(), BudgetState())
    aaif = _ev("evt-wg-agentic-commerce-file-1", "aaif/wg-agentic-commerce", [])
    ext = _ev("evt-ext-coinbase-x402-file-1", "coinbase/x402", ["external", "steward:x402 Foundation"])
    assert cur._parse(_payload("working-groups/agentic-commerce", ["evt-bogus"]), [aaif, ext]) == []
    [m] = cur._parse(_payload("working-groups/agentic-commerce", []), [aaif])  # single-class fallback
    assert "external" not in m.concept.tags


def test_unlisted_or_miscased_external_repo(tmp_path, monkeypatch):
    import pytest

    from aaif_wiki.connectors.github import UnlistedRepo

    conn = GitHubConnector(GitHubCfg(discover_repos=False, external=[
        ExternalSourceCfg(repo="coinbase/x402", steward="x402 Foundation")]), tmp_path)
    assert conn.resolve("Coinbase/X402") == "coinbase/x402"
    assert conn.resolve("aaif/wg-x") == "wg-x"  # no ext- duplicate of AAIF repos
    assert conn.resolve("wg-x") == "wg-x"
    with pytest.raises(UnlistedRepo):
        conn.resolve("evil/repo")
    calls = []
    monkeypatch.setattr(conn, "scan_files", lambda r, limit: calls.append(r) or [])
    monkeypatch.setattr(conn, "_get", lambda *a, **k: [])
    conn.scan_repo("Coinbase/X402")
    assert calls == ["coinbase/x402"]


def test_token_never_sent_to_external_api(tmp_path, monkeypatch):
    import httpx

    monkeypatch.setenv("AAIF_SOURCES_TOKEN", "secret")
    conn = GitHubConnector(GitHubCfg(discover_repos=False, external=[
        ExternalSourceCfg(repo="coinbase/x402", steward="x402 Foundation",
                          include_prs=True, include_issues=True)]), tmp_path)
    seen = []

    def fake_get(url, headers, timeout):
        seen.append((url, headers.get("Authorization")))
        return httpx.Response(200, json=[], request=httpx.Request("GET", url))

    monkeypatch.setattr(httpx, "get", fake_get)
    conn.scan_pull_requests("coinbase/x402")
    conn.scan_issues("coinbase/x402")
    conn.scan_pull_requests("wg-agentic-commerce")
    assert [a for u, a in seen if "coinbase" in u] == [None, None]
    assert [a for u, a in seen if "/aaif/" in u] == ["Bearer secret"]


def test_file_limit_keeps_include_paths_in_priority_order():
    ext = ExternalSourceCfg(repo="a/b", steward="S", include_paths=["README.md", "specs", "docs"])
    paths = ["README.md", "docs/examples/a.md", "docs/guides/b.md", "specs/z.md",
             "specs/v2/y.md", "specs/schema.yaml", "CLA.md"]
    lines = [f"100644 blob {i:040x}\t{p}" for i, p in enumerate(paths)]
    picked = [p for _sha, p in GitHubConnector._select_external(lines, ext)]
    assert picked == ["README.md", "specs/z.md", "specs/v2/y.md",
                      "docs/examples/a.md", "docs/guides/b.md"]


def test_external_event_prefix_is_collision_free(tmp_path):
    conn = GitHubConnector(GitHubCfg(discover_repos=False), tmp_path)
    assert conn._event_prefix("a-b/c") != conn._event_prefix("a/b-c")
    assert conn._event_prefix("Coinbase/X402") == conn._event_prefix("coinbase/x402")
