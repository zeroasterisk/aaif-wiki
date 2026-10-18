"""External (non-AAIF) sources: config, connector coordinates, curator provenance (ADR-013)."""

from __future__ import annotations

import json
import subprocess
from datetime import UTC, datetime

from aaif_wiki.config import BudgetCfg, CuratorCfg, ExternalSourceCfg, GitHubCfg, load_config
from aaif_wiki.connectors.github import GitHubConnector, is_external
from aaif_wiki.curator.agent import Curator
from aaif_wiki.curator.prompts import PromptAssembler, external_steward
from aaif_wiki.models import BudgetState, Lifecycle, RawEvent, SourceType

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
        assert e.event_id.startswith("evt-ext-example-org-agent-pay-file-")
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
