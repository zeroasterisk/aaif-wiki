"""Best-effort semantic resolution and durable last-resort exceptions.

Resolution never blocks application. Layers enrich a mutation with evidence and
may refine advisory fields. Anything still uncertain is written to the durable
exceptions store for later batch review while the original mutation continues to
mechanical validation and application.
"""

from __future__ import annotations

import json
from collections.abc import Callable
from datetime import UTC, datetime
from pathlib import Path
from typing import Protocol

from .config import Config
from .models import BudgetState, Mutation, RawEvent, ResolutionEvidence
from .orchestration.local import BudgetExceeded


class ResolutionLayer(Protocol):
    name: str

    def resolve(self, mutation: Mutation, events: list[RawEvent]) -> ResolutionEvidence: ...


class DeterministicContextLayer:
    """Cheap first layer: lifecycle and duplicate-target facts."""

    name = "deterministic-context"

    def __init__(self, existing_slugs: set[str]):
        self.existing_slugs = existing_slugs

    def resolve(self, mutation: Mutation, events: list[RawEvent]) -> ResolutionEvidence:
        events = [event for event in events if event.event_id in mutation.source_event_ids]
        facts: list[str] = []
        flags: list[str] = []
        if mutation.action == "create" and mutation.slug in self.existing_slugs:
            flags.append("duplicate-create")
            facts.append(f"target `{mutation.slug}` already exists")
        unsettled = [e.event_id for e in events if e.lifecycle.value != "merged"]
        if unsettled:
            facts.append(f"{len(unsettled)} source event(s) are not merged")
            if mutation.concept and mutation.concept.status.value == "stable":
                flags.append("stable-from-unsettled-source")
        return ResolutionEvidence(
            layer=self.name,
            outcome="flagged" if flags else "clear",
            confidence=1.0,
            rationale="; ".join(facts) or "no deterministic conflict found",
            flags=flags,
        )


class VertexResolutionLayer:
    """Model-backed resolver using the application's existing Vertex path."""

    def __init__(self, name: str, model: str, cfg, budget_limits, budget: BudgetState):
        self.name = name
        self.model = model
        self.cfg = cfg
        self.budget_limits = budget_limits
        self.budget = budget
        self._client = None

    def _get_client(self):
        if self._client is None:
            from .vertex_compat import prepare_environment

            prepare_environment()
            from google import genai

            project = self.cfg.vertex.resolved_project()
            if not project:
                raise RuntimeError("no Vertex project configured")
            self._client = genai.Client(
                vertexai=True,
                project=project,
                location=self.cfg.vertex.location,
            )
        return self._client

    def resolve(self, mutation: Mutation, events: list[RawEvent]) -> ResolutionEvidence:
        from google.genai import types

        events = [event for event in events if event.event_id in mutation.source_event_ids]
        payload = {
            "proposal": mutation.model_dump(mode="json", exclude={"resolution_evidence"}),
            "sources": [e.model_dump(mode="json") for e in events],
            "instruction": (
                "Resolve semantic conflicts best-effort. Return whether the proposal is clear, "
                "flagged, or resolved; confidence 0..1; concise rationale; and machine-readable flags."
            ),
        }
        schema = {
            "type": "object",
            "properties": {
                "outcome": {"type": "string", "enum": ["clear", "flagged", "resolved"]},
                "confidence": {"type": "number"},
                "rationale": {"type": "string"},
                "flags": {"type": "array", "items": {"type": "string"}},
            },
            "required": ["outcome", "confidence", "rationale", "flags"],
        }
        response = self._get_client().models.generate_content(
            model=self.model,
            contents=json.dumps(payload, default=str),
            config=types.GenerateContentConfig(
                temperature=0.0,
                response_mime_type="application/json",
                response_schema=schema,
            ),
        )
        data = json.loads(response.text or "{}")
        usage = getattr(response, "usage_metadata", None)
        tokens_in = int(getattr(usage, "prompt_token_count", 0) or 0)
        tokens_out = int(getattr(usage, "candidates_token_count", 0) or 0)
        estimated_usd = (
            (tokens_in / 1e6) * self.cfg.usd_per_1m_input
            + (tokens_out / 1e6) * self.cfg.usd_per_1m_output
        )
        self.budget.tokens_used += tokens_in + tokens_out
        self.budget.usd_spent += estimated_usd
        breach = self.budget.would_breach(self.budget_limits)
        if breach:
            raise BudgetExceeded(breach)
        return ResolutionEvidence(
            layer=self.name,
            outcome=data["outcome"],
            confidence=max(0.0, min(1.0, float(data["confidence"]))),
            rationale=str(data["rationale"])[:1000],
            flags=[str(flag) for flag in data.get("flags", [])][:20],
            tokens_in=tokens_in,
            tokens_out=tokens_out,
            estimated_usd=estimated_usd,
        )


class CallableLayer:
    """Adapter for optional model-backed resolvers (Vertex, future providers)."""

    def __init__(self, name: str, fn: Callable[[Mutation, list[RawEvent]], ResolutionEvidence]):
        self.name = name
        self.fn = fn

    def resolve(self, mutation: Mutation, events: list[RawEvent]) -> ResolutionEvidence:
        return self.fn(mutation, events)


def resolve_mutations(
    mutations: list[Mutation],
    events: list[RawEvent],
    layers: list[ResolutionLayer],
    confidence_threshold: float,
) -> tuple[list[Mutation], list[Mutation]]:
    """Run every available layer. Return mutations and unresolved exceptions.

    A layer failure is itself evidence, not a pipeline failure. The original
    mutation always survives for deterministic validation and best-effort apply.
    """
    exceptions: list[Mutation] = []
    for mutation in mutations:
        mutation.resolution_evidence = []
        for layer in layers:
            prior = mutation.resolution_evidence[-1] if mutation.resolution_evidence else None
            is_model_layer = isinstance(layer, VertexResolutionLayer)
            jev_needs_resolution = bool(
                mutation.jev
                and (
                    mutation.jev.mutation_kind == "conflict"
                    or mutation.jev.confidence < confidence_threshold
                )
            )
            if is_model_layer:
                if not prior or (prior.outcome == "clear" and not jev_needs_resolution):
                    continue
                if layer.name == "vertex-deep" and prior.outcome == "resolved" and prior.confidence >= confidence_threshold:
                    continue
            try:
                evidence = layer.resolve(mutation, events)
            except Exception as exc:  # noqa: BLE001 - autonomy requires fail-open enrichment
                evidence = ResolutionEvidence(
                    layer=layer.name,
                    outcome="error",
                    confidence=0.0,
                    rationale=str(exc)[:500],
                    flags=["resolver-error"],
                )
            mutation.resolution_evidence.append(evidence)

        flags: set[str] = set()
        for evidence in mutation.resolution_evidence:
            if evidence.outcome == "resolved":
                flags.clear()
            elif evidence.outcome in {"flagged", "error"}:
                flags.update(evidence.flags)
        low_confidence = bool(mutation.jev and mutation.jev.confidence < confidence_threshold)
        model_conflict = bool(mutation.jev and mutation.jev.mutation_kind == "conflict")
        resolver_error = any(e.outcome == "error" for e in mutation.resolution_evidence)
        mutation.exception_reasons = sorted(flags)
        if low_confidence:
            mutation.exception_reasons.append("low-jev-confidence")
        if model_conflict:
            mutation.exception_reasons.append("jev-conflict")
        if resolver_error:
            mutation.exception_reasons.append("resolver-error")
        mutation.exception_reasons = sorted(set(mutation.exception_reasons))
        if mutation.exception_reasons:
            exceptions.append(mutation)
    return mutations, exceptions


def write_exceptions(cfg: Config, run_id: str, mutations: list[Mutation]) -> list[Path]:
    """Append immutable exception records. Existing records are never overwritten."""
    if not mutations:
        return []
    now = datetime.now(UTC)
    day = cfg.exceptions_dir / now.strftime("%Y/%m/%d")
    day.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for i, mutation in enumerate(mutations):
        path = day / f"{run_id}-{i:04d}.json"
        suffix = 1
        while path.exists():
            path = day / f"{run_id}-{i:04d}-{suffix}.json"
            suffix += 1
        record = {
            "run_id": run_id,
            "queued_at": now.isoformat(),
            "status": "open",
            "slug": mutation.slug,
            "action": mutation.action,
            "reasons": mutation.exception_reasons,
            "source_event_ids": mutation.source_event_ids,
            "jev_assessment": mutation.jev.model_dump(mode="json") if mutation.jev else None,
            "resolution_evidence": [e.model_dump(mode="json") for e in mutation.resolution_evidence],
            "human_resolution": None,
            "training_signal": None,
        }
        path.write_text(json.dumps(record, indent=2))
        written.append(path)
    return written


def resolve_exception(path: Path, resolution: str, actor: str) -> None:
    """Capture a human correction as durable refinement/training signal."""
    record = json.loads(path.read_text())
    now = datetime.now(UTC).isoformat()
    record["status"] = "resolved"
    record["human_resolution"] = {"actor": actor, "at": now, "resolution": resolution}
    record["training_signal"] = {
        "input": {
            "slug": record["slug"],
            "action": record["action"],
            "sources": record["source_event_ids"],
            "model_evidence": record["resolution_evidence"],
        },
        "label": resolution,
    }
    path.write_text(json.dumps(record, indent=2))
