"""Swappable orchestration (ADR-002).

``local`` is the default. ``temporal`` is a config change, not a rewrite -- which
is only true because activities are Temporal-compatible *by construction*. See
:mod:`aaif_wiki.orchestration.base` for the rules that keeps them that way.
"""

from .base import Activity, ActivityRegistry, Orchestrator, RetryPolicy, activity
from .local import LocalOrchestrator

__all__ = [
    "Activity",
    "ActivityRegistry",
    "Orchestrator",
    "RetryPolicy",
    "activity",
    "LocalOrchestrator",
    "get_orchestrator",
]


def get_orchestrator(backend: str, **kwargs) -> Orchestrator:
    """Resolve a backend by name. Temporal is imported lazily so it stays optional."""
    if backend == "local":
        return LocalOrchestrator(**kwargs)
    if backend == "temporal":
        try:
            from .temporal import TemporalOrchestrator
        except ImportError as exc:  # pragma: no cover - depends on optional extra
            raise RuntimeError(
                "backend 'temporal' requires the optional extra: uv sync --extra temporal"
            ) from exc
        return TemporalOrchestrator(**kwargs)
    raise ValueError(f"unknown orchestrator backend: {backend!r}")
