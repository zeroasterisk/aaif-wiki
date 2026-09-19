"""Optional Jev assessment for proposed mutations.

This module is deliberately outside the deterministic validation path. When the
feature is disabled, missing credentials, or the service is unavailable, the
caller gets the original mutations back unchanged.
"""

from __future__ import annotations

import json
import logging
import time
import urllib.error
import urllib.request
from collections.abc import Iterable
from typing import Any

from .config import JevCfg
from .models import Concept, JevAssessment, Mutation, RawEvent

log = logging.getLogger("aaif_wiki.jev")


class JevError(RuntimeError):
    pass


def _answer_confidence(answer: dict[str, Any]) -> float:
    if "confidence" in answer:
        return float(answer["confidence"])
    if "noul" in answer:
        value = float(answer["noul"])
        return max(value, 1.0 - value)
    return 0.0


def _candidate_targets(mutation: Mutation, existing: dict[str, Concept], limit: int = 8) -> dict[str, str]:
    """Return compact choice keys mapped to real slugs.

    Jev choice criteria are kept small. Candidates are deterministic lexical
    neighbours, so enabling Jev does not add another retrieval dependency.
    """
    words = set(mutation.slug.replace("/", " ").replace("-", " ").split())
    ranked = sorted(
        existing,
        key=lambda slug: (
            -len(words & set(slug.replace("/", " ").replace("-", " ").split())),
            slug,
        ),
    )
    slugs = [mutation.slug]
    slugs.extend(slug for slug in ranked if slug != mutation.slug)
    unique = list(dict.fromkeys(slugs))[:limit]
    return {f"node_{i}": slug for i, slug in enumerate(unique)}


class JevClient:
    def __init__(self, cfg: JevCfg):
        self.cfg = cfg

    def _post(self, payload: dict[str, Any]) -> dict[str, Any]:
        key = self.cfg.api_key()
        if not key:
            raise JevError("JEV_API_KEY is not set")
        request = urllib.request.Request(
            self.cfg.endpoint,
            data=json.dumps(payload).encode(),
            headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
            method="POST",
        )
        last: Exception | None = None
        for attempt in range(self.cfg.maximum_attempts):
            try:
                with urllib.request.urlopen(request, timeout=self.cfg.timeout_seconds) as response:
                    return json.loads(response.read().decode())
            except urllib.error.HTTPError as exc:
                last = exc
                if exc.code not in {429, 529}:
                    break
            except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
                last = exc
            if attempt + 1 < self.cfg.maximum_attempts:
                time.sleep(self.cfg.retry_backoff_seconds * (2**attempt))
        raise JevError(f"Jev request failed: {last}") from last

    def assess(
        self,
        mutation: Mutation,
        events: Iterable[RawEvent],
        existing: dict[str, Concept],
    ) -> JevAssessment:
        targets = _candidate_targets(mutation, existing)
        target_criteria = {key: f"The best target is `{slug}`." for key, slug in targets.items()}
        target_criteria["new_node"] = "This should create a distinct new knowledge node."

        source_by_id = {event.event_id: event for event in events}
        sources = [source_by_id[eid] for eid in mutation.source_event_ids if eid in source_by_id]
        state = {
            "proposal": mutation.model_dump(mode="json", exclude={"jev"}),
            "candidate_targets": targets,
            "sources": [
                {
                    "event_id": event.event_id,
                    "source_type": event.source_type.value,
                    "lifecycle": event.lifecycle.value,
                    "repository": event.repository,
                    "title": event.title,
                    "summary": event.summary,
                    "url": event.url,
                }
                for event in sources
            ],
        }
        payload = {
            "state": state,
            "model": self.cfg.model,
            "questions": {
                "mutation_kind": {
                    "type": "choice",
                    "instructions": "Classify the semantic effect of this proposed knowledge mutation.",
                    "criteria": {
                        "new_concept": "Creates a genuinely new concept.",
                        "update": "Changes or extends an existing concept.",
                        "relation": "Primarily adds or changes a relation between concepts.",
                        "conflict": "Conflicts with existing knowledge or the supplied sources.",
                        "no_op": "Adds no meaningful information or duplicates existing knowledge.",
                    },
                },
                "target_node": {
                    "type": "choice",
                    "instructions": "Choose the best target node for this proposal.",
                    "criteria": target_criteria,
                },
                "provenance": {
                    "type": "score",
                    "instructions": "Score how well the proposal is supported by the supplied provenance.",
                    "criteria": [
                        "Unsupported or contradicted",
                        "Partially supported or unsettled",
                        "Directly supported by authoritative source material",
                    ],
                },
                "review_priority": {
                    "type": "score",
                    "instructions": "How urgently and carefully should a human review this proposal?",
                    "criteria": ["Routine", "Normal", "High", "Critical"],
                },
            },
        }
        started = time.monotonic()
        response = self._post(payload)
        latency_ms = int((time.monotonic() - started) * 1000)
        answers = response.get("answers") or {}
        kind = answers.get("mutation_kind") or {}
        target = answers.get("target_node") or {}
        provenance = answers.get("provenance") or {}
        priority = answers.get("review_priority") or {}
        confidences = [_answer_confidence(value) for value in (kind, target, provenance, priority)]
        confidence = min(confidences) if confidences else 0.0
        target_choice = target.get("choice", "new_node")
        target_node = targets.get(target_choice, mutation.slug)
        decision = "pass" if confidence >= self.cfg.confidence_threshold else "abstain"
        return JevAssessment(
            decision=decision,
            mutation_kind=str(kind.get("choice", "no_op")),
            target_node=target_node,
            provenance_score=max(0.0, min(1.0, float(provenance.get("score", 0.0)) / 2.0)),
            review_priority=max(0.0, min(1.0, float(priority.get("score", 0.0)) / 3.0)),
            confidence=confidence,
            model=str(response.get("model") or self.cfg.model),
            latency_ms=latency_ms,
        )


def assess_mutations(
    mutations: list[Mutation],
    events: list[RawEvent],
    existing: dict[str, Concept],
    cfg: JevCfg,
) -> tuple[list[Mutation], dict[str, Any]]:
    """Attach advisory assessments without making Jev a pipeline dependency."""
    if not cfg.is_enabled():
        return mutations, {"enabled": False, "attempted": 0, "failures": 0, "abstained": 0}
    if not cfg.api_key():
        log.warning("Jev enabled but JEV_API_KEY is missing; continuing without assessments")
        return mutations, {"enabled": True, "attempted": 0, "failures": 1, "abstained": 0}

    client = JevClient(cfg)
    failures = 0
    abstained = 0
    for mutation in mutations:
        try:
            mutation.jev = client.assess(mutation, events, existing)
            abstained += mutation.jev.decision == "abstain"
        except Exception as exc:  # noqa: BLE001 - optional means fail open to deterministic flow
            failures += 1
            log.warning("optional Jev assessment failed for %s: %s", mutation.slug, exc)
    assessed = sum(m.jev is not None for m in mutations)
    latency = sum(m.jev.latency_ms for m in mutations if m.jev)
    return mutations, {
        "enabled": True,
        "attempted": len(mutations),
        "assessed": assessed,
        "failures": failures,
        "abstained": abstained,
        "average_latency_ms": round(latency / assessed) if assessed else 0,
    }
