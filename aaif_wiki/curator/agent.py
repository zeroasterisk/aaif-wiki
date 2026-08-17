"""The curator: events in, schema-validated mutations out.

Two design points worth stating explicitly.

**The curator never touches the filesystem.** It returns :class:`Mutation` objects
which are validated before anything is applied. That is the inbound half of the
trust boundary (ADR-007): ingested third-party text cannot become a file write,
because the only channel out of the model is a typed structure.

**Budget is enforced here, not hoped for.** Every call updates the running spend
and a breach raises ``BudgetExceeded``, which the retry policy classifies as
non-retryable -- retrying a ceiling breach cannot help.
"""

from __future__ import annotations

import json
import logging
from datetime import UTC, datetime

from ..config import CuratorCfg
from ..models import (
    Actor,
    BudgetState,
    Concept,
    ConceptSource,
    ConceptStatus,
    CurateResult,
    Mutation,
    RawEvent,
)
from ..orchestration.local import BudgetExceeded
from .prompts import PromptAssembler, lifecycle_forces_draft

log = logging.getLogger("aaif_wiki.curator")

MUTATION_SCHEMA = {
    "type": "object",
    "properties": {
        "mutations": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "action": {"type": "string", "enum": ["create", "update", "deprecate"]},
                    "slug": {"type": "string"},
                    "rationale": {"type": "string"},
                    "source_event_ids": {"type": "array", "items": {"type": "string"}},
                    "concept": {
                        "type": "object",
                        "properties": {
                            "type": {"type": "string"},
                            "title": {"type": "string"},
                            "description": {"type": "string"},
                            "tags": {"type": "array", "items": {"type": "string"}},
                            "status": {
                                "type": "string",
                                "enum": ["draft", "stable", "deprecated"],
                            },
                            "body": {"type": "string"},
                        },
                        "required": ["type", "title", "description", "body"],
                    },
                },
                "required": ["action", "slug", "rationale", "source_event_ids"],
            },
        }
    },
    "required": ["mutations"],
}


class Curator:
    def __init__(self, cfg: CuratorCfg, budget_limits, budget: BudgetState | None = None):
        self.cfg = cfg
        self.limits = budget_limits
        self.budget = budget or BudgetState()
        self.prompts = PromptAssembler(cfg.iteration_budget, cfg.compaction_threshold)
        self._client = None
        self._model_used = cfg.model

    # -- model access ---------------------------------------------------
    def _get_client(self):
        if self._client is None:
            from ..vertex_compat import prepare_environment

            prepare_environment()
            from google import genai

            project = self.cfg.vertex.resolved_project()
            if not project:
                raise RuntimeError(
                    "no Vertex project: set curator.vertex.project in config.yaml "
                    "or GOOGLE_CLOUD_PROJECT"
                )
            self._client = genai.Client(
                vertexai=True, project=project, location=self.cfg.vertex.location
            )
        return self._client

    def _generate(self, system: str, user: str) -> tuple[str, int, int]:
        from google.genai import types

        client = self._get_client()
        config = types.GenerateContentConfig(
            system_instruction=system,
            temperature=self.cfg.temperature,
            response_mime_type="application/json",
            response_schema=MUTATION_SCHEMA,
        )

        last_exc: Exception | None = None
        for model in (self.cfg.model, self.cfg.fallback_model):
            if not model:
                continue
            try:
                resp = client.models.generate_content(
                    model=model, contents=user, config=config
                )
                self._model_used = model
                usage = getattr(resp, "usage_metadata", None)
                tin = getattr(usage, "prompt_token_count", 0) or 0
                tout = getattr(usage, "candidates_token_count", 0) or 0
                return (resp.text or "", tin, tout)
            except Exception as exc:  # noqa: BLE001 - try the fallback model
                log.warning("model %s failed (%s); trying fallback", model, exc)
                last_exc = exc
        raise RuntimeError(f"all models failed; last error: {last_exc}") from last_exc

    def _charge(self, tin: int, tout: int) -> None:
        usd = (tin / 1e6) * self.cfg.usd_per_1m_input + (tout / 1e6) * self.cfg.usd_per_1m_output
        self.budget.tokens_used += tin + tout
        self.budget.usd_spent += usd
        breach = self.budget.would_breach(self.limits)
        if breach:
            raise BudgetExceeded(breach)

    # -- main entry point ------------------------------------------------
    def curate(
        self,
        events: list[RawEvent],
        existing: dict[str, Concept],
        objective: str = "Curate these events into OKF concepts.",
        rehydrate=None,
    ) -> CurateResult:
        if not events:
            return CurateResult(model=self.cfg.model)

        system = self.prompts.stable()
        user = "\n".join(
            [
                self.prompts.cached(existing),
                self.prompts.volatile(events, rehydrate=rehydrate),
                self.prompts.task(objective),
            ]
        )

        text, tin, tout = self._generate(system, user)
        self._charge(tin, tout)

        mutations = self._parse(text, events)
        self.budget.concepts_written += len(mutations)

        return CurateResult(
            mutations=mutations,
            tokens_in=tin,
            tokens_out=tout,
            usd=(tin / 1e6) * self.cfg.usd_per_1m_input
            + (tout / 1e6) * self.cfg.usd_per_1m_output,
            model=self._model_used,
        )

    # -- response handling ------------------------------------------------
    def _parse(self, text: str, events: list[RawEvent]) -> list[Mutation]:
        try:
            payload = json.loads(text)
        except json.JSONDecodeError:
            log.error("curator returned non-JSON; discarding batch")
            return []

        by_id = {e.event_id: e for e in events}
        now = datetime.now(UTC)
        actor = Actor(by=f"agent:aaif-wiki-curator/{self._model_used}", at=now)

        out: list[Mutation] = []
        for raw in payload.get("mutations", []) or []:
            if not isinstance(raw, dict):
                continue
            slug = (raw.get("slug") or "").strip().strip("/")
            action = raw.get("action")
            if not slug or action not in {"create", "update", "deprecate"}:
                continue

            source_ids = [s for s in (raw.get("source_event_ids") or []) if s in by_id]
            contributing = [by_id[s] for s in source_ids] or events

            concept = None
            if action != "deprecate":
                cdata = raw.get("concept") or {}
                if not cdata.get("title"):
                    continue

                # Server-side enforcement. The model is told to mark unsettled
                # sources as draft; we do not rely on it having complied.
                declared = cdata.get("status", "draft")
                status = ConceptStatus.DRAFT
                if declared == "stable" and not lifecycle_forces_draft(contributing):
                    status = ConceptStatus.STABLE
                elif declared == "deprecated":
                    status = ConceptStatus.DEPRECATED

                concept = Concept(
                    type=str(cdata.get("type", "Concept")),
                    title=str(cdata["title"]),
                    description=str(cdata.get("description", ""))[:300],
                    resource=contributing[0].url if contributing else None,
                    tags=[str(t) for t in (cdata.get("tags") or [])][:8],
                    generated=actor,
                    verified=[],  # only a human review adds this (ADR-009)
                    status=status,
                    sources=[
                        ConceptSource(
                            id=e.event_id,
                            resource=e.url or f"{e.repository}:{e.reference_id}",
                            author=e.author,
                            last_modified=e.timestamp,
                        )
                        for e in contributing
                    ],
                    slug=slug,
                    body=str(cdata.get("body", "")),
                )

            out.append(
                Mutation(
                    action=action,
                    slug=slug,
                    concept=concept,
                    rationale=str(raw.get("rationale", ""))[:500],
                    source_event_ids=source_ids,
                )
            )
        return out
