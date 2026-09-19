from __future__ import annotations

import json
from datetime import UTC, datetime

from aaif_wiki.config import Config
from aaif_wiki.models import Concept, ConceptStatus, Lifecycle, Mutation, RawEvent, SourceType
from aaif_wiki.resolution import (
    DeterministicContextLayer,
    resolve_exception,
    resolve_mutations,
    write_exceptions,
)


def event(lifecycle=Lifecycle.OPEN):
    return RawEvent(event_id="e1", source_type=SourceType.ISSUE, lifecycle=lifecycle, repository="aaif/x", reference_id="1", title="x", timestamp=datetime.now(UTC))


def test_duplicate_is_queued_but_mutation_survives():
    mutation = Mutation(action="create", slug="taxonomy/x")
    result, exceptions = resolve_mutations([mutation], [event()], [DeterministicContextLayer({"taxonomy/x"})], 0.65)
    assert result == [mutation]
    assert exceptions == [mutation]
    assert "duplicate-create" in mutation.exception_reasons


def test_stable_from_open_source_is_evidence_not_blocker():
    mutation = Mutation(action="update", slug="taxonomy/x", source_event_ids=["e1"], concept=Concept(type="Term", title="x", description="x", status=ConceptStatus.STABLE))
    result, exceptions = resolve_mutations([mutation], [event()], [DeterministicContextLayer(set())], 0.65)
    assert result[0] is mutation
    assert "stable-from-unsettled-source" in exceptions[0].exception_reasons


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
    mutation = Mutation(action="create", slug="taxonomy/x", exception_reasons=["duplicate-create"])
    path = write_exceptions(cfg, "run-1", [mutation])[0]
    resolve_exception(path, "update existing node", "human:zeroasterisk")
    record = json.loads(path.read_text())
    assert record["status"] == "resolved"
    assert record["training_signal"]["label"] == "update existing node"


def test_unrelated_open_event_does_not_flag_stable_mutation():
    cited = event(Lifecycle.MERGED)
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


def test_downstream_resolution_clears_prior_flags():
    from aaif_wiki.models import ResolutionEvidence

    class Resolved:
        name = "custom-resolver"

        def resolve(self, mutation, events):
            return ResolutionEvidence(
                layer=self.name,
                outcome="resolved",
                confidence=0.9,
                rationale="duplicate merged into the existing target",
                flags=[],
            )

    mutation = Mutation(action="create", slug="taxonomy/x")
    _, exceptions = resolve_mutations(
        [mutation],
        [],
        [DeterministicContextLayer({"taxonomy/x"}), Resolved()],
        0.65,
    )
    assert not exceptions
