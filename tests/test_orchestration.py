"""Orchestration contract tests.

The value of the abstraction is that swapping to Temporal is a config change.
That claim is only true while activities stay Temporal-compatible, so these tests
assert the contract rather than trusting a comment.
"""

from __future__ import annotations

import pytest
from pydantic import BaseModel

from aaif_wiki.orchestration.base import Activity, ActivityRegistry, RetryPolicy, activity
from aaif_wiki.orchestration.local import BudgetExceeded, Checkpoint, LocalOrchestrator


class Inp(BaseModel):
    value: int = 0


class Outp(BaseModel):
    doubled: int = 0


def test_full_jitter_samples_whole_interval():
    """Full jitter is uniform(0, capped) -- not a narrow band around the target."""
    policy = RetryPolicy(initial_interval_seconds=2.0, maximum_interval_seconds=60.0)
    samples = [policy.backoff_for(3) for _ in range(400)]
    cap = min(60.0, 2.0 * 2**3)
    assert all(0 <= s <= cap for s in samples)
    assert min(samples) < cap * 0.25, "should sometimes sample near zero"
    assert max(samples) > cap * 0.75, "should sometimes sample near the cap"


def test_backoff_respects_maximum_interval():
    policy = RetryPolicy(initial_interval_seconds=2.0, maximum_interval_seconds=10.0)
    assert all(policy.backoff_for(20) <= 10.0 for _ in range(50))


def test_registry_rejects_sync_activities():
    reg = ActivityRegistry()
    with pytest.raises(TypeError, match="async def"):
        reg.register(Activity(name="x", fn=lambda p: p, input_type=Inp, output_type=Outp))


def test_registry_rejects_multi_argument_activities():
    reg = ActivityRegistry()

    async def two_args(a: Inp, b: Inp) -> Outp:
        return Outp()

    with pytest.raises(TypeError, match="exactly one argument"):
        reg.register(Activity(name="x", fn=two_args, input_type=Inp, output_type=Outp))


def test_registry_rejects_non_pydantic_payloads():
    reg = ActivityRegistry()

    async def bad(a: Inp) -> dict:
        return {}

    with pytest.raises(TypeError, match="pydantic BaseModel"):
        reg.register(Activity(name="x", fn=bad, input_type=Inp, output_type=dict))


def test_decorator_requires_annotations():
    reg = ActivityRegistry()
    with pytest.raises(TypeError, match="annotate"):

        @activity("unannotated", registry=reg)
        async def unannotated(payload):
            return Outp()


async def test_local_orchestrator_executes_and_retries():
    reg = ActivityRegistry()
    attempts = {"n": 0}

    @activity("flaky", retry=RetryPolicy(initial_interval_seconds=0.001, maximum_attempts=4), registry=reg)
    async def flaky(payload: Inp) -> Outp:
        attempts["n"] += 1
        if attempts["n"] < 3:
            raise RuntimeError("transient")
        return Outp(doubled=payload.value * 2)

    orch = LocalOrchestrator(registry=reg)
    result = await orch.execute("flaky", Inp(value=21))
    assert result.doubled == 42
    assert attempts["n"] == 3


async def test_non_retryable_errors_fail_fast():
    reg = ActivityRegistry()
    attempts = {"n": 0}

    @activity("broke", retry=RetryPolicy(initial_interval_seconds=0.001, maximum_attempts=5), registry=reg)
    async def broke(payload: Inp) -> Outp:
        attempts["n"] += 1
        raise BudgetExceeded("ceiling hit")

    orch = LocalOrchestrator(registry=reg)
    with pytest.raises(BudgetExceeded):
        await orch.execute("broke", Inp())
    assert attempts["n"] == 1, "a budget breach must not consume the retry budget"


async def test_checkpoint_skips_completed_work(tmp_path):
    reg = ActivityRegistry()
    calls = {"n": 0}

    @activity("counted", registry=reg)
    async def counted(payload: Inp) -> Outp:
        calls["n"] += 1
        return Outp(doubled=payload.value * 2)

    ck = tmp_path / "ck.json"
    first = LocalOrchestrator(registry=reg, checkpoint_path=ck, run_id="r1")
    assert (await first.execute("counted", Inp(value=5))).doubled == 10
    assert calls["n"] == 1

    # A resumed run with the same payload must not re-execute.
    second = LocalOrchestrator(registry=reg, checkpoint_path=ck, run_id="r1")
    assert (await second.execute("counted", Inp(value=5))).doubled == 10
    assert calls["n"] == 1, "checkpointed activity should be skipped on resume"

    # A different payload is different work.
    assert (await second.execute("counted", Inp(value=6))).doubled == 12
    assert calls["n"] == 2


def test_checkpoint_survives_corrupt_file(tmp_path):
    path = tmp_path / "ck.json"
    path.write_text("{not json")
    assert Checkpoint(path).data == {}


def test_pipeline_activities_satisfy_the_temporal_contract():
    """Every real activity must be registerable under the strict contract."""
    from aaif_wiki import pipeline  # noqa: F401
    from aaif_wiki.orchestration.base import REGISTRY

    assert set(REGISTRY.names()) == {
        "scan_sources",
        "curate_concepts",
        "apply_mutations",
        "validate_bundle",
    }
    for name in REGISTRY.names():
        ActivityRegistry.check_contract(REGISTRY.get(name))
