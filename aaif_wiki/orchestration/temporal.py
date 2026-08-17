"""Temporal backend (optional extra).

This module is the proof that the abstraction in ``base.py`` is real rather than
aspirational: it maps the *same* activity registry onto Temporal without touching
a single activity implementation.

Enable with::

    uv sync --extra temporal
    temporal server start-dev            # in another terminal
    # config.yaml -> orchestrator.backend: temporal
    uv run aaif-wiki worker              # run the worker
    uv run aaif-wiki ingest --mode=incremental

Why you might: Temporal gives durable execution across process and machine death,
automatic replay of workflow state, a visibility UI, and distributed workers --
none of which the local backend attempts.
"""

from __future__ import annotations

from datetime import timedelta
from typing import Any

from pydantic import BaseModel

from .base import REGISTRY, ActivityRegistry, Orchestrator

try:  # pragma: no cover - exercised only with the optional extra installed
    from temporalio import activity as temporal_activity
    from temporalio import workflow
    from temporalio.client import Client
    from temporalio.common import RetryPolicy as TemporalRetryPolicy
    from temporalio.worker import Worker

    TEMPORAL_AVAILABLE = True
except ImportError:  # pragma: no cover
    TEMPORAL_AVAILABLE = False
    Client = Any  # type: ignore[misc,assignment]
    Worker = Any  # type: ignore[misc,assignment]


def _shim(act) -> Any:
    """Wrap a registered activity as a Temporal activity.

    Payloads cross the boundary as plain dicts, which is why the contract in
    ``base.py`` insists on pydantic in and pydantic out.
    """

    @temporal_activity.defn(name=act.name)
    async def run(payload: dict) -> dict:
        typed = act.input_type.model_validate(payload)
        result = await act.fn(typed)
        return result.model_dump(mode="json")

    return run


def build_activities(registry: ActivityRegistry | None = None) -> list[Any]:
    registry = registry or REGISTRY
    return [_shim(registry.get(name)) for name in registry.names()]


if TEMPORAL_AVAILABLE:  # pragma: no cover

    @workflow.defn(name="AAIFWikiActivityWorkflow")
    class AAIFWikiActivityWorkflow:
        """Single-activity workflow.

        The pipeline sequences activities on the client side so that the local and
        Temporal backends produce identical orderings. A future revision can lift
        the whole sequence into a workflow body for full replay durability; that is
        a strict upgrade and does not change activity code.
        """

        @workflow.run
        async def run(self, name: str, payload: dict, retry: dict) -> dict:
            return await workflow.execute_activity(
                name,
                payload,
                start_to_close_timeout=timedelta(minutes=15),
                retry_policy=TemporalRetryPolicy(
                    initial_interval=timedelta(seconds=retry["initial_interval_seconds"]),
                    backoff_coefficient=retry["backoff_coefficient"],
                    maximum_interval=timedelta(seconds=retry["maximum_interval_seconds"]),
                    maximum_attempts=retry["maximum_attempts"],
                    non_retryable_error_types=list(retry["non_retryable_errors"]),
                ),
            )


class TemporalOrchestrator(Orchestrator):
    def __init__(
        self,
        host: str = "localhost:7233",
        namespace: str = "default",
        task_queue: str = "aaif-wiki-queue",
        registry: ActivityRegistry | None = None,
        **_ignored,
    ):
        if not TEMPORAL_AVAILABLE:
            raise RuntimeError("temporalio is not installed: uv sync --extra temporal")
        self.host = host
        self.namespace = namespace
        self.task_queue = task_queue
        self.registry = registry or REGISTRY
        self._client: Any = None

    @property
    def backend(self) -> str:
        return "temporal"

    async def _get_client(self) -> Any:
        if self._client is None:
            self._client = await Client.connect(self.host, namespace=self.namespace)
        return self._client

    async def execute(self, name: str, payload: BaseModel) -> BaseModel:
        act = self.registry.get(name)
        client = await self._get_client()
        import uuid

        result = await client.execute_workflow(
            "AAIFWikiActivityWorkflow",
            args=[
                name,
                payload.model_dump(mode="json"),
                {
                    "initial_interval_seconds": act.retry.initial_interval_seconds,
                    "backoff_coefficient": act.retry.backoff_coefficient,
                    "maximum_interval_seconds": act.retry.maximum_interval_seconds,
                    "maximum_attempts": act.retry.maximum_attempts,
                    "non_retryable_errors": list(act.retry.non_retryable_errors),
                },
            ],
            id=f"aaif-wiki-{name}-{uuid.uuid4().hex[:8]}",
            task_queue=self.task_queue,
        )
        return act.output_type.model_validate(result)

    async def close(self) -> None:
        self._client = None


async def run_worker(
    host: str = "localhost:7233",
    namespace: str = "default",
    task_queue: str = "aaif-wiki-queue",
    registry: ActivityRegistry | None = None,
) -> None:  # pragma: no cover
    if not TEMPORAL_AVAILABLE:
        raise RuntimeError("temporalio is not installed: uv sync --extra temporal")
    client = await Client.connect(host, namespace=namespace)
    worker = Worker(
        client,
        task_queue=task_queue,
        workflows=[AAIFWikiActivityWorkflow],
        activities=build_activities(registry),
    )
    await worker.run()
