from __future__ import annotations

import asyncio
import json
from datetime import UTC, datetime

import pytest

from aaif_wiki.config import Config
from aaif_wiki.models import (
    BudgetState,
    Concept,
    ConceptStatus,
    CurateResult,
    JevAssessment,
    Lifecycle,
    Mutation,
    RawEvent,
    ResolutionEvidence,
    SourceType,
)
from aaif_wiki.okf import load_bundle
from aaif_wiki.orchestration.local import BudgetExceeded
from aaif_wiki.pipeline import apply_mutations
from aaif_wiki.resolution import (
    DeterministicContextLayer,
    VertexResolutionLayer,
    resolve_exception,
    resolve_mutations,
    write_exceptions,
)


def event(event_id="e1", lifecycle=Lifecycle.OPEN):
    return RawEvent(
        event_id=event_id,
        source_type=SourceType.ISSUE,
        lifecycle=lifecycle,
        repository="aaif/x",
        reference_id="1",
        title="x",
        timestamp=datetime.now(UTC),
    )


def test_duplicate_is_queued_but_mutation_survives():
    mutation = Mutation(action="create", slug="taxonomy/x", source_event_ids=["e1"])
    result, exceptions = resolve_mutations([mutation], [event()], [DeterministicContextLayer({"taxonomy/x"})], 0.65)
    assert result == [mutation]
    assert exceptions == [mutation]
    assert "duplicate-create" in mutation.exception_reasons


def test_stable_from_open_source_is_evidence_not_blocker():
    mutation = Mutation(action="update", slug="taxonomy/x", source_event_ids=["e1"], concept=Concept(type="Term", title="x", description="x", status=ConceptStatus.STABLE))
    result, exceptions = resolve_mutations([mutation], [event()], [DeterministicContextLayer(set())], 0.65)
    assert result[0] is mutation
    assert "stable-from-unsettled-source" in exceptions[0].exception_reasons


def test_multi_event_batch_filters_sources_per_mutation():
    # e1 is merged; e2 is open
    e1 = event(event_id="e1", lifecycle=Lifecycle.MERGED)
    e2 = event(event_id="e2", lifecycle=Lifecycle.OPEN)

    # m1 only cites e1 (merged) -> should NOT be flagged as stable-from-unsettled-source
    m1 = Mutation(action="create", slug="taxonomy/clean", source_event_ids=["e1"], concept=Concept(type="Term", title="Clean", description="c", status=ConceptStatus.STABLE))
    # m2 cites e2 (open) -> SHOULD be flagged
    m2 = Mutation(action="create", slug="taxonomy/unsettled", source_event_ids=["e2"], concept=Concept(type="Term", title="Unsettled", description="u", status=ConceptStatus.STABLE))

    layer = DeterministicContextLayer(set())
    result, exceptions = resolve_mutations([m1, m2], [e1, e2], [layer], 0.65)

    assert "stable-from-unsettled-source" not in m1.exception_reasons
    assert "stable-from-unsettled-source" in m2.exception_reasons
    assert m1 not in exceptions
    assert m2 in exceptions


def test_deterministic_flags_are_sticky_and_cannot_be_cleared_by_model_layer():
    class ModelResolver:
        name = "resolver"
        def resolve(self, mutation, events):
            return ResolutionEvidence(
                layer=self.name,
                outcome="resolved",
                confidence=0.95,
                rationale="Model attempts to resolve duplicate create",
                flags=[],
            )

    mutation = Mutation(action="create", slug="taxonomy/x", source_event_ids=["e1"])
    det_layer = DeterministicContextLayer({"taxonomy/x"})
    result, exceptions = resolve_mutations([mutation], [event()], [det_layer, ModelResolver()], 0.65)

    assert result[0] is mutation
    # Deterministic flag 'duplicate-create' CANNOT be cleared by a model outcome
    assert "duplicate-create" in mutation.exception_reasons
    assert mutation in exceptions


def test_downstream_resolution_clears_prior_model_flags():
    class FlaggingModelLayer:
        name = "model-1"
        def resolve(self, mutation, events):
            return ResolutionEvidence(
                layer=self.name,
                outcome="flagged",
                confidence=0.5,
                rationale="Uncertain semantic connection",
                flags=["semantic-ambiguity"],
            )

    class ResolvingModelLayer:
        name = "model-2"
        def resolve(self, mutation, events):
            return ResolutionEvidence(
                layer=self.name,
                outcome="resolved",
                confidence=0.9,
                rationale="Resolved semantic connection",
                flags=[],
            )

    mutation = Mutation(action="create", slug="taxonomy/y", source_event_ids=["e1"])
    result, exceptions = resolve_mutations([mutation], [event()], [FlaggingModelLayer(), ResolvingModelLayer()], 0.65)

    assert result[0] is mutation
    assert exceptions == []
    assert mutation.exception_reasons == []


def test_jev_is_strictly_advisory_and_does_not_withhold_mutations():
    # Low confidence or conflict in Jev does NOT add to exception_reasons
    low_jev = JevAssessment(
        decision="abstain",
        mutation_kind="conflict",
        target_node="taxonomy/x",
        provenance_score=0.2,
        review_priority=0.8,
        confidence=0.4,
    )
    mutation = Mutation(action="create", slug="taxonomy/x", source_event_ids=["e1"], jev=low_jev)
    result, exceptions = resolve_mutations([mutation], [event(lifecycle=Lifecycle.MERGED)], [DeterministicContextLayer(set())], 0.65)

    assert exceptions == []
    assert mutation.exception_reasons == []
    assert mutation.jev == low_jev


def test_budget_exceeded_precheck_halts_resolution():
    cfg = Config()
    budget = BudgetState(tokens_used=19_999_999)
    layer = VertexResolutionLayer("vertex-fast", "gemini-flash", cfg.curator, cfg.budget, budget)

    # would_breach will trip if tokens exceed max_tokens_per_run
    layer.budget.tokens_used = cfg.budget.max_tokens_per_run + 100
    mutation = Mutation(action="create", slug="taxonomy/x", source_event_ids=["e1"])

    with pytest.raises(BudgetExceeded):
        layer.resolve(mutation, [event()])


def test_apply_mutations_withholds_conflicted_mutations(tmp_path, monkeypatch):
    cfg = Config(root=tmp_path)
    cfg.project.bundle_root = "wiki"
    (tmp_path / "wiki").mkdir(parents=True)
    monkeypatch.setattr("aaif_wiki.pipeline.get_config", lambda: cfg)

    clean_mut = Mutation(
        action="create",
        slug="taxonomy/clean",
        source_event_ids=["e1"],
        concept=Concept(type="Term", title="Clean", description="desc", body="# Clean"),
        exception_reasons=[],
    )
    conflicted_mut = Mutation(
        action="create",
        slug="taxonomy/conflicted",
        source_event_ids=["e2"],
        concept=Concept(type="Term", title="Conflicted", description="desc", body="# Conflicted"),
        exception_reasons=["duplicate-create"],
    )

    curate_result = CurateResult(mutations=[clean_mut, conflicted_mut])
    validate_result = asyncio.run(apply_mutations(curate_result))

    bundle = load_bundle(tmp_path / "wiki")
    assert "taxonomy/clean" in bundle
    assert "taxonomy/conflicted" not in bundle
    assert validate_result.checked == 1


def test_layer_failure_queues_and_continues():
    class Broken:
        name = "vertex-deep"
        def resolve(self, mutation, events):
            raise RuntimeError("unavailable")
    mutation = Mutation(action="update", slug="taxonomy/x")
    result, exceptions = resolve_mutations([mutation], [], [Broken()], 0.65)
    assert result[0] is mutation
    assert exceptions[0].resolution_evidence[0].outcome == "error"


def test_human_resolution_becomes_training_signal(tmp_path):
    cfg = Config(root=tmp_path)
    mutation = Mutation(
        action="create",
        slug="taxonomy/x",
        concept=Concept(type="Term", title="X", description="x", body="# X"),
        exception_reasons=["duplicate-create"],
    )
    path = write_exceptions(cfg, "run-1", [mutation])[0]
    resolve_exception(path, "update existing node", "human:zeroasterisk")
    record = json.loads(path.read_text())
    assert record["status"] == "resolved"
    assert record["proposed_concept"]["title"] == "X"
    assert record["training_signal"]["label"] == "update existing node"


def test_unrelated_open_event_does_not_flag_stable_mutation():
    cited = event(event_id="e1", lifecycle=Lifecycle.MERGED)
    unrelated = RawEvent(
        event_id="e2",
        source_type=SourceType.ISSUE,
        lifecycle=Lifecycle.OPEN,
        repository="aaif/x",
        reference_id="2",
        title="unrelated",
        timestamp=datetime.now(UTC),
    )
    mutation = Mutation(
        action="update",
        slug="taxonomy/x",
        source_event_ids=["e1"],
        concept=Concept(
            type="Term", title="x", description="x", status=ConceptStatus.STABLE
        ),
    )
    _, exceptions = resolve_mutations(
        [mutation], [cited, unrelated], [DeterministicContextLayer(set())], 0.65
    )
    assert not exceptions
