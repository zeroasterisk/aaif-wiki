"""Optional Jev mutation assessment: config, parsing, fallback, and abstention."""

from __future__ import annotations

from datetime import UTC, datetime

from aaif_wiki.config import JevCfg
from aaif_wiki.jev import JevClient, assess_mutations
from aaif_wiki.models import Concept, Lifecycle, Mutation, RawEvent, SourceType


def _mutation() -> Mutation:
    return Mutation(action="create", slug="taxonomy/agents", source_event_ids=["e1"])


def _event() -> RawEvent:
    return RawEvent(
        event_id="e1",
        source_type=SourceType.ISSUE,
        lifecycle=Lifecycle.OPEN,
        repository="aaif/ws-taxonomy-landscape",
        reference_id="1",
        title="Agent definition",
        timestamp=datetime(2026, 9, 1, tzinfo=UTC),
        url="https://github.com/aaif/ws-taxonomy-landscape/issues/1",
    )


def test_disabled_is_exact_passthrough(monkeypatch):
    monkeypatch.delenv("JEV_ENABLED", raising=False)
    mutation = _mutation()
    result, stats = assess_mutations([mutation], [_event()], {}, JevCfg(enabled=False))
    assert result == [mutation]
    assert result[0].jev is None
    assert stats == {"enabled": False, "attempted": 0, "failures": 0, "abstained": 0}


def test_environment_can_enable(monkeypatch):
    monkeypatch.setenv("JEV_ENABLED", "true")
    assert JevCfg(enabled=False).is_enabled()
    monkeypatch.setenv("JEV_ENABLED", "0")
    assert not JevCfg(enabled=True).is_enabled()


def test_missing_key_falls_back(monkeypatch):
    monkeypatch.setenv("JEV_ENABLED", "1")
    monkeypatch.delenv("JEV_API_KEY", raising=False)
    result, stats = assess_mutations([_mutation()], [_event()], {}, JevCfg())
    assert result[0].jev is None
    assert stats["failures"] == 1


def test_low_confidence_abstains(monkeypatch):
    monkeypatch.setenv("JEV_API_KEY", "test-only")
    client = JevClient(JevCfg(confidence_threshold=0.65))
    monkeypatch.setattr(
        client,
        "_post",
        lambda payload: {
            "model": "jev-latest",
            "answers": {
                "mutation_kind": {"type": "choice", "choice": "new_concept", "confidence": 0.9},
                "target_node": {"type": "choice", "choice": "new_node", "confidence": 0.6},
                "provenance": {"type": "score", "score": 1.5, "confidence": 0.8},
                "review_priority": {"type": "score", "score": 2.0, "confidence": 0.7},
            },
            "usage": {"input_tokens": 1, "output_tokens": 1},
        },
    )
    assessment = client.assess(_mutation(), [_event()], {})
    assert assessment.decision == "abstain"
    assert assessment.target_node == "taxonomy/agents"
    assert assessment.provenance_score == 0.75
    assert assessment.review_priority == 2 / 3


def test_service_error_does_not_block_deterministic_path(monkeypatch):
    monkeypatch.setenv("JEV_ENABLED", "1")
    monkeypatch.setenv("JEV_API_KEY", "test-only")
    monkeypatch.setattr(JevClient, "assess", lambda *args: (_ for _ in ()).throw(RuntimeError("down")))
    mutation = _mutation()
    result, stats = assess_mutations([mutation], [_event()], {}, JevCfg())
    assert result[0].jev is None
    assert stats["failures"] == 1


def test_existing_target_is_resolved_from_choice(monkeypatch):
    monkeypatch.setenv("JEV_API_KEY", "test-only")
    client = JevClient(JevCfg())
    monkeypatch.setattr(
        client,
        "_post",
        lambda payload: {
            "model": "jev-latest",
            "answers": {
                "mutation_kind": {"type": "choice", "choice": "update", "confidence": 0.9},
                "target_node": {"type": "choice", "choice": "node_1", "confidence": 0.9},
                "provenance": {"type": "score", "score": 2, "confidence": 0.9},
                "review_priority": {"type": "score", "score": 1, "confidence": 0.9},
            },
        },
    )
    existing = {"taxonomy/agent-system": Concept(type="Term", title="Agent system", description="x")}
    assessment = client.assess(_mutation(), [_event()], existing)
    assert assessment.decision == "pass"
    assert assessment.target_node == "taxonomy/agent-system"


def test_eval_harness_uses_committed_labels(tmp_path):
    import json

    from aaif_wiki.eval_jev import evaluate_review_records

    (tmp_path / "run.json").write_text(
        json.dumps(
            {
                "review_status": "accepted",
                "mutations": [
                    {
                        "jev_assessment": {
                            "decision": "pass",
                            "mutation_kind": "update",
                            "confidence": 0.8,
                        },
                        "human_label": {"mutation_kind": "update"},
                    }
                ],
            }
        )
    )
    report = evaluate_review_records(tmp_path)
    assert report["assessed"] == 1
    assert report["agreement"] == 1.0
