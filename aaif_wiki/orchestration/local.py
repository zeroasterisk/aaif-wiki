"""In-process orchestrator with durable checkpointing.

This is the default backend. It is honest about what it is: a single process with
a checkpoint file, not a distributed durable execution engine.

What it gives you:
* Retries with true full jitter, per the activity's declared policy.
* Non-retryable error classes fail fast instead of burning the retry budget.
* A checkpoint file, so a crash or Ctrl-C resumes at the next incomplete activity
  rather than redoing completed work.
* Combined with the append-only event store, a re-run skips already-ingested
  events, so most of the "don't lose work" value lands without a daemon.

What it does NOT give you, and why Temporal remains one config line away:
* No durability if the machine dies mid-activity (only completed activities are
  checkpointed).
* No distributed workers, no external visibility UI, no cross-process coordination.
* No guarantee against duplicate side effects if a process is killed between
  performing an effect and writing the checkpoint.

If flakiness ever exceeds what this handles, set ``orchestrator.backend: temporal``.
Activity code does not change.
"""

from __future__ import annotations

import asyncio
import json
import logging
import time
from pathlib import Path

from pydantic import BaseModel

from .base import REGISTRY, ActivityRegistry, Orchestrator, RetryPolicy

log = logging.getLogger("aaif_wiki.orchestration")


class BudgetExceeded(RuntimeError):
    """Non-retryable: a ceiling was hit and retrying cannot help."""


class Checkpoint:
    """Records completed activities so a resumed run can skip them."""

    def __init__(self, path: Path):
        self.path = path
        self.data: dict[str, dict] = {}
        if path.exists():
            try:
                self.data = json.loads(path.read_text())
            except json.JSONDecodeError:
                self.data = {}

    def key(self, run_id: str, activity: str, payload_digest: str) -> str:
        return f"{run_id}:{activity}:{payload_digest}"

    def get(self, key: str) -> dict | None:
        return self.data.get(key)

    def put(self, key: str, value: dict) -> None:
        self.data[key] = value
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text(json.dumps(self.data, indent=2, default=str))
        tmp.replace(self.path)

    def clear(self) -> None:
        self.data = {}
        if self.path.exists():
            self.path.unlink()


def _digest(payload: BaseModel) -> str:
    import hashlib

    return hashlib.sha256(payload.model_dump_json().encode()).hexdigest()[:16]


class LocalOrchestrator(Orchestrator):
    def __init__(
        self,
        registry: ActivityRegistry | None = None,
        checkpoint_path: Path | None = None,
        run_id: str = "default",
        retry_override: RetryPolicy | None = None,
        resume: bool = True,
    ):
        self.registry = registry or REGISTRY
        self.checkpoint = Checkpoint(checkpoint_path) if checkpoint_path else None
        self.run_id = run_id
        self.retry_override = retry_override
        self.resume = resume

    @property
    def backend(self) -> str:
        return "local"

    async def execute(self, name: str, payload: BaseModel) -> BaseModel:
        act = self.registry.get(name)
        policy = self.retry_override or act.retry

        ck_key = None
        if self.checkpoint and self.resume:
            ck_key = self.checkpoint.key(self.run_id, name, _digest(payload))
            cached = self.checkpoint.get(ck_key)
            if cached is not None:
                log.info("skip %s (checkpointed)", name)
                return act.output_type.model_validate(cached)

        last_error: Exception | None = None
        for attempt in range(policy.maximum_attempts):
            try:
                started = time.monotonic()
                result = await act.fn(payload)
                log.info("ok %s in %.2fs", name, time.monotonic() - started)
                if ck_key and self.checkpoint:
                    self.checkpoint.put(ck_key, json.loads(result.model_dump_json()))
                return result
            except Exception as exc:  # noqa: BLE001 - policy decides what is fatal
                last_error = exc
                if type(exc).__name__ in policy.non_retryable_errors:
                    log.error("fatal %s: %s (non-retryable)", name, exc)
                    raise
                if attempt == policy.maximum_attempts - 1:
                    break
                delay = policy.backoff_for(attempt)
                log.warning(
                    "retry %s attempt %d/%d after %.1fs: %s",
                    name, attempt + 1, policy.maximum_attempts, delay, exc,
                )
                await asyncio.sleep(delay)

        raise RuntimeError(f"activity {name!r} failed after {policy.maximum_attempts} attempts") from last_error

    async def close(self) -> None:
        return None
