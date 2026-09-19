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
    mutation = Mutation(action="update", slug="taxonomy/x", concept=Concept(type="Term", title="x", description="x", status=ConceptStatus.STABLE))
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
