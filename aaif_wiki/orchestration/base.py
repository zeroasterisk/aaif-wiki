"""The orchestration contract.

The whole point of this module is that swapping to Temporal must not require
rewriting pipeline logic. That is only achievable if activities obey rules that
Temporal already imposes, whether or not Temporal is running:

1. An activity is ``async def (PydanticInput) -> PydanticOutput``. One argument in,
   one value out, both JSON-serializable.
2. No closures over mutable state, no reliance on process-local globals, no passing
   open handles. Anything an activity needs, it receives or reconstructs.
3. Activities are idempotent. Retries and resumption re-run them; that must be safe.
4. Retry policy is declared *with* the activity, not applied at the call site, so
   both backends see the same policy.

If those hold, ``LocalOrchestrator`` and ``TemporalOrchestrator`` are genuinely
interchangeable. If they stop holding, the swap silently breaks -- so
:func:`ActivityRegistry.check_contract` asserts what it can at registration time.
"""

from __future__ import annotations

import inspect
from collections.abc import Awaitable, Callable
from dataclasses import dataclass, field
from typing import Any, Protocol, TypeVar, get_type_hints

from pydantic import BaseModel

In = TypeVar("In", bound=BaseModel)
Out = TypeVar("Out", bound=BaseModel)


@dataclass(frozen=True)
class RetryPolicy:
    initial_interval_seconds: float = 2.0
    backoff_coefficient: float = 2.0
    maximum_interval_seconds: float = 60.0
    maximum_attempts: int = 5
    non_retryable_errors: tuple[str, ...] = (
        "InvalidAuthError",
        "InvalidSchemaError",
        "BudgetExceeded",
    )

    def backoff_for(self, attempt: int) -> float:
        """True full jitter: uniform(0, capped_exponential).

        Not a +/-20% band. Only sampling the whole interval meaningfully
        decorrelates a thundering herd, which is the entire purpose of jitter.
        """
        import random

        capped = min(
            self.maximum_interval_seconds,
            self.initial_interval_seconds * (self.backoff_coefficient**attempt),
        )
        return random.uniform(0, capped)


@dataclass
class Activity:
    name: str
    fn: Callable[[Any], Awaitable[Any]]
    input_type: type[BaseModel]
    output_type: type[BaseModel]
    retry: RetryPolicy = field(default_factory=RetryPolicy)


class ActivityRegistry:
    """Holds every activity. Both backends consume this same registry."""

    def __init__(self) -> None:
        self._activities: dict[str, Activity] = {}

    def register(self, act: Activity) -> None:
        self.check_contract(act)
        self._activities[act.name] = act

    def get(self, name: str) -> Activity:
        if name not in self._activities:
            raise KeyError(f"activity not registered: {name}")
        return self._activities[name]

    def names(self) -> list[str]:
        return sorted(self._activities)

    def __contains__(self, name: object) -> bool:
        return name in self._activities

    @staticmethod
    def check_contract(act: Activity) -> None:
        """Fail loudly at registration if an activity could not run under Temporal."""
        if not inspect.iscoroutinefunction(act.fn):
            raise TypeError(f"activity {act.name!r} must be async def")
        sig = inspect.signature(act.fn)
        params = [p for p in sig.parameters.values() if p.name != "self"]
        if len(params) != 1:
            raise TypeError(
                f"activity {act.name!r} must take exactly one argument "
                f"(got {len(params)}); Temporal activities are single-payload"
            )
        if not (isinstance(act.input_type, type) and issubclass(act.input_type, BaseModel)):
            raise TypeError(f"activity {act.name!r} input must be a pydantic BaseModel")
        if not (isinstance(act.output_type, type) and issubclass(act.output_type, BaseModel)):
            raise TypeError(f"activity {act.name!r} output must be a pydantic BaseModel")


REGISTRY = ActivityRegistry()


def activity(
    name: str, *, retry: RetryPolicy | None = None, registry: ActivityRegistry | None = None
):
    """Declare an activity and its retry policy together."""

    def decorator(fn: Callable[[In], Awaitable[Out]]):
        hints = get_type_hints(fn)
        params = [p for p in inspect.signature(fn).parameters if p != "self"]
        if not params:
            raise TypeError(f"activity {name!r} needs one input parameter")
        input_type = hints.get(params[0])
        output_type = hints.get("return")
        if input_type is None or output_type is None:
            raise TypeError(
                f"activity {name!r} must annotate its input and return types "
                f"(they define the serialization boundary)"
            )
        act = Activity(
            name=name,
            fn=fn,
            input_type=input_type,
            output_type=output_type,
            retry=retry or RetryPolicy(),
        )
        (registry or REGISTRY).register(act)
        fn.__activity__ = act  # type: ignore[attr-defined]
        return fn

    return decorator


class Orchestrator(Protocol):
    """What the pipeline is allowed to assume about its runtime."""

    async def execute(self, name: str, payload: BaseModel) -> BaseModel:
        """Run one activity to completion, applying its declared retry policy."""
        ...

    async def close(self) -> None:
        ...

    @property
    def backend(self) -> str:
        ...
