from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path

from aaif_wiki.ablation import run_ablation
from aaif_wiki.config import Config
from aaif_wiki.jev import JevClient
from aaif_wiki.models import Concept, CurateResult, Lifecycle, Mutation, RawEvent, SourceType
from aaif_wiki.okf import write_concept
from aaif_wiki.store import EventStore


def test_ablation_uses_same_curator_output_for_both_arms(tmp_path, monkeypatch):
    cfg = Config(root=tmp_path)
    cfg.project.bundle_root = "wiki"
    cfg.project.event_store = "events"
    cfg.jev.enabled = False
    write_concept(tmp_path / "wiki", Concept(type="Term", title="Existing", description="x", slug="taxonomy/existing"))
    event = RawEvent(event_id="e1", source_type=SourceType.ISSUE, lifecycle=Lifecycle.OPEN, repository="aaif/x", reference_id="1", title="x", timestamp=datetime.now(UTC), inline_text="proposal")
    EventStore(tmp_path / "events").append(event)
    mutation = Mutation(action="create", slug="taxonomy/new", source_event_ids=["e1"], concept=Concept(type="Term", title="New", description="new", body="# New"))
    monkeypatch.setattr("aaif_wiki.ablation.Curator.curate", lambda *args, **kwargs: CurateResult(mutations=[mutation], model="test", tokens_in=10, tokens_out=2, usd=0.1))
    monkeypatch.delenv("JEV_API_KEY", raising=False)
    summary = run_ablation(cfg, tmp_path / "out", runs=2, event_ids=["e1"])
    assert summary["runs_completed"] == 2
    assert summary["all_rendered_bytes_identical"]
    assert not summary["jev_enabled_arm_executed"]
    assert (tmp_path / "out" / "rendered-outputs.tar.gz").exists()
    assert json.loads((tmp_path / "out" / "summary.json").read_text())["curator_tokens_in"] == 20


def test_ablation_with_jev_enabled_proves_byte_identical(tmp_path, monkeypatch):
    cfg = Config(root=tmp_path)
    cfg.project.bundle_root = "wiki"
    cfg.project.event_store = "events"
    cfg.jev.enabled = True
    write_concept(tmp_path / "wiki", Concept(type="Term", title="Existing", description="x", slug="taxonomy/existing"))
    event = RawEvent(event_id="e1", source_type=SourceType.ISSUE, lifecycle=Lifecycle.OPEN, repository="aaif/x", reference_id="1", title="x", timestamp=datetime.now(UTC), inline_text="proposal")
    EventStore(tmp_path / "events").append(event)
    mutation = Mutation(action="create", slug="taxonomy/new", source_event_ids=["e1"], concept=Concept(type="Term", title="New", description="new", body="# New"))
    monkeypatch.setattr("aaif_wiki.ablation.Curator.curate", lambda *args, **kwargs: CurateResult(mutations=[mutation], model="test", tokens_in=10, tokens_out=2, usd=0.1))
    monkeypatch.setenv("JEV_API_KEY", "mock-key")
    monkeypatch.setattr(
        JevClient,
        "_post",
        lambda self, payload: {
            "model": "jev-latest",
            "answers": {
                "mutation_kind": {"type": "choice", "choice": "new_concept", "confidence": 0.95},
                "target_node": {"type": "choice", "choice": "new_node", "confidence": 0.95},
                "provenance": {"type": "score", "score": 2.0, "confidence": 0.9},
                "review_priority": {"type": "score", "score": 1.0, "confidence": 0.9},
            },
            "usage": {"input_tokens": 50, "output_tokens": 20},
        },
    )
    summary = run_ablation(cfg, tmp_path / "out", runs=2, event_ids=["e1"])
    assert summary["runs_completed"] == 2
    assert summary["jev_enabled_arm_executed"] is True
    assert summary["all_rendered_bytes_identical"] is True
    assert summary["jev_input_tokens"] == 100
    assert summary["jev_output_tokens"] == 40


def test_ablation_workflow_is_manual_and_uploads_evidence():
    workflow = Path(".github/workflows/jev-ablation.yml").read_text()
    assert "workflow_dispatch:" in workflow
    assert "GCP_VERTEX_SERVICE_ACCOUNT_JSON" in workflow
    assert "JEV_API_KEY" in workflow
    assert "actions/upload-artifact@v4" in workflow
    assert "ablate-jev" in workflow
