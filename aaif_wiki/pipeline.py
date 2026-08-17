"""Activity definitions and the run sequence.

Each activity obeys the contract in ``orchestration/base.py``: one pydantic in,
one pydantic out, idempotent, retry policy declared alongside. That is what makes
``orchestrator.backend: temporal`` a config change rather than a rewrite.

The sequence itself is deliberately plain. Ordering lives here, in normal Python,
so both backends produce identical orderings and so the pipeline is readable
without knowing anything about durable execution.
"""

from __future__ import annotations

import logging
from datetime import UTC, datetime
from pathlib import Path

from .config import Config, get_config
from .curator import Curator
from .models import (
    BudgetState,
    ConceptStatus,
    CurateRequest,
    CurateResult,
    Mutation,
    RunMode,
    ScanRequest,
    ScanResult,
    ValidateResult,
)
from .okf import load_bundle, write_concept
from .orchestration.base import REGISTRY, RetryPolicy, activity
from .store import EventIndex, EventStore
from .validate import validate_bundle, validate_mutation

log = logging.getLogger("aaif_wiki.pipeline")

NETWORK_RETRY = RetryPolicy(
    initial_interval_seconds=2.0,
    backoff_coefficient=2.0,
    maximum_interval_seconds=60.0,
    maximum_attempts=5,
)
LLM_RETRY = RetryPolicy(
    initial_interval_seconds=4.0,
    backoff_coefficient=2.0,
    maximum_interval_seconds=120.0,
    maximum_attempts=4,
)
LOCAL_RETRY = RetryPolicy(maximum_attempts=2)


# --------------------------------------------------------------------------
# activities
# --------------------------------------------------------------------------


@activity("scan_sources", retry=NETWORK_RETRY)
async def scan_sources(req: ScanRequest) -> ScanResult:
    """Ingest from GitHub into the append-only event store."""
    from .connectors import GitHubConnector

    cfg = get_config()
    conn = GitHubConnector(cfg.sources.github, cfg.cache_dir)
    store = EventStore(cfg.events_dir)

    repos = req.repos or conn.discover_repos()
    result = ScanResult(repos_scanned=[])

    file_limit = 200 if req.mode is RunMode.BOOTSTRAP else 60
    for repo in repos:
        try:
            events = conn.scan_repo(repo, file_limit=file_limit)
        except Exception as exc:  # noqa: BLE001 - one bad repo must not kill the run
            log.warning("repo %s failed: %s", repo, exc)
            result.skipped[repo] = str(exc)
            continue

        # Idempotent: the store refuses duplicates, so re-runs are cheap.
        new = [e for e in events if not store.exists(e.event_id)]
        store.append_many(new)
        result.events.extend(new)
        result.repos_scanned.append(repo)
        if req.max_events and len(result.events) >= req.max_events:
            result.events = result.events[: req.max_events]
            break

    with EventIndex(cfg.index_db_path) as index:
        for event in result.events:
            index.upsert(event)
        index.commit()

    return result


@activity("curate_concepts", retry=LLM_RETRY)
async def curate_concepts(req: CurateRequest) -> CurateResult:
    """Turn events into schema-validated mutations. No filesystem writes here."""
    from .connectors import GitHubConnector

    cfg = get_config()
    store = EventStore(cfg.events_dir)
    conn = GitHubConnector(cfg.sources.github, cfg.cache_dir)

    events = [e for e in (store.get(eid) for eid in req.event_ids) if e]
    if not events:
        return CurateResult(model=cfg.curator.model)

    def rehydrate(event):
        for ptr in event.pointers:
            text = conn.read_pointer(ptr)
            if text:
                return text
        return event.inline_text

    existing = load_bundle(cfg.bundle_dir)
    curator = Curator(cfg.curator, cfg.budget, BudgetState())
    return curator.curate(events, existing, rehydrate=rehydrate)


@activity("apply_mutations", retry=LOCAL_RETRY)
async def apply_mutations(result: CurateResult) -> ValidateResult:
    """Validate every mutation, then write the surviving ones to the bundle."""
    cfg = get_config()
    issues = []
    applied = 0

    for mutation in result.mutations:
        problems = validate_mutation(mutation)
        if problems:
            issues.extend(problems)
            continue
        if mutation.action == "deprecate":
            existing = load_bundle(cfg.bundle_dir).get(mutation.slug)
            if existing:
                existing.status = ConceptStatus.DEPRECATED
                write_concept(cfg.bundle_dir, existing)
                applied += 1
            continue
        if mutation.concept:
            mutation.concept.slug = mutation.slug
            write_concept(cfg.bundle_dir, mutation.concept)
            applied += 1

    log.info("applied %d/%d mutations", applied, len(result.mutations))
    return ValidateResult(issues=issues, checked=applied)


@activity("validate_bundle", retry=LOCAL_RETRY)
async def validate_bundle_activity(_: CurateRequest) -> ValidateResult:
    """Deterministic, LLM-free gate."""
    cfg = get_config()
    store = EventStore(cfg.events_dir)
    known = {e.event_id for e in store.iter_events()}
    return validate_bundle(
        cfg.bundle_dir,
        known_event_ids=known,
        link_allowlist=cfg.trust.link_allowlist,
        forbidden_patterns=cfg.trust.forbidden_patterns,
    )


# --------------------------------------------------------------------------
# run sequence
# --------------------------------------------------------------------------


def uncurated_event_ids(cfg: Config, limit: int = 0) -> list[str]:
    """Events in the store that no concept yet cites.

    Derived, not tracked. A concept records its inputs in ``sources[]``, so the
    set of un-projected events falls out of a diff -- there is no "curated" flag
    to keep in sync and no second source of truth to corrupt. Same reasoning as
    the store-derived cursor.

    This matters because ingestion is idempotent: a re-run legitimately finds
    zero *new* events while un-curated events are still waiting in the store.
    Curating only what the current scan returned would silently skip them.
    """
    store = EventStore(cfg.events_dir)
    projected: set[str] = set()
    for concept in load_bundle(cfg.bundle_dir).values():
        projected.update(s.id for s in concept.sources)

    pending = [e.event_id for e in store.all_events() if e.event_id not in projected]
    return pending[:limit] if limit else pending


def reindex_bundle(cfg: Config) -> Path:
    """Regenerate the bundle root index so every concept is reachable.

    An OKF bundle is a graph, and a concept nothing links to is invisible to any
    consumer that traverses from the root. Rather than asking the model to
    maintain the index (which it would drift on), we derive it deterministically
    from what is on disk.
    """
    concepts = load_bundle(cfg.bundle_dir)
    by_section: dict[str, list] = {}
    for slug, concept in sorted(concepts.items()):
        section = slug.split("/")[0] if "/" in slug else "other"
        by_section.setdefault(section, []).append((slug, concept))

    lines = [
        "---",
        'okf_version: "0.2"',
        "type: Index",
        "title: AAIF Knowledge Wiki",
        "description: Machine-curated OKF v0.2 knowledge bundle covering the Agentic AI Foundation.",
        "status: draft",
        "---",
        "",
        "# Overview",
        "",
        "An Open Knowledge Format (OKF) v0.2 bundle covering the working groups, reference",
        "architectures and taxonomy of the Agentic AI Foundation (AAIF).",
        "",
        "> **Unofficial.** Generated by [`aaif-wiki`](https://github.com/zeroasterisk/aaif-wiki),",
        "> a personal open-source project. Not endorsed by or affiliated with the Agentic AI",
        "> Foundation or the Linux Foundation. All content is derived from public sources;",
        "> follow each concept's `resource` link for canonical material.",
        "",
        "# Sections",
        "",
    ]
    if not concepts:
        lines.append("_No concepts curated yet._")
    for section, entries in sorted(by_section.items()):
        lines.append(f"## {section}")
        lines.append("")
        for slug, concept in entries:
            rel = f"{slug}.md"
            badge = "" if concept.trust_tier == "human-reviewed" else f" _({concept.status.value}, {concept.trust_tier})_"
            lines.append(f"- [{concept.title}]({rel}) — {concept.description}{badge}")
        lines.append("")

    lines += ["# References", "", "- [AAIF on GitHub](https://github.com/aaif)", ""]

    path = cfg.bundle_dir / "index.md"
    path.write_text("\n".join(lines))
    return path


def ensure_bundle_root(cfg: Config) -> None:
    """The bundle root must declare okf_version (spec §11)."""
    cfg.bundle_dir.mkdir(parents=True, exist_ok=True)
    index = cfg.bundle_dir / "index.md"
    if index.exists():
        return
    index.write_text(
        """---
okf_version: "0.2"
type: Index
title: AAIF Knowledge Wiki
description: Machine-curated knowledge bundle covering the Agentic AI Foundation.
status: draft
---

# Overview

An Open Knowledge Format (OKF) v0.2 bundle covering the working groups, reference
architectures and taxonomy of the Agentic AI Foundation (AAIF).

> **Unofficial.** Generated by [`aaif-wiki`](https://github.com/zeroasterisk/aaif-wiki),
> a personal open-source project. Not endorsed by or affiliated with the Agentic AI
> Foundation or the Linux Foundation. All content is derived from public sources.

# Sections

- `working-groups/` — one concept per working group and workstream
- `architectures/` — reference architectures and RFC concepts
- `taxonomy/` — terms and definitions

# References

- [AAIF on GitHub](https://github.com/aaif)
"""
    )


async def run_pipeline(
    orchestrator,
    mode: RunMode = RunMode.INCREMENTAL,
    repos: list[str] | None = None,
    max_events: int = 0,
    batch_size: int = 6,
    curate: bool = True,
) -> dict:
    """Scan, curate in batches, apply, validate."""
    cfg = get_config()
    ensure_bundle_root(cfg)

    scan: ScanResult = await orchestrator.execute(
        "scan_sources",
        ScanRequest(mode=mode, repos=repos or [], max_events=max_events),
    )

    # Curate everything not yet projected, not just what this scan happened to
    # find. Ingestion is idempotent, so a re-run legitimately returns zero new
    # events while un-curated events are still sitting in the store.
    pending = uncurated_event_ids(cfg, limit=max_events)

    summary = {
        "mode": mode.value,
        "repos_scanned": scan.repos_scanned,
        "skipped": scan.skipped,
        "new_events": len(scan.events),
        "pending_curation": len(pending),
        "mutations": 0,
        "tokens": 0,
        "usd": 0.0,
        "model": "",
        "applied": 0,
        "issues": [],
    }
    if not curate or not pending:
        return summary

    all_mutations: list[Mutation] = []
    for i in range(0, len(pending), batch_size):
        batch_ids = pending[i : i + batch_size]
        try:
            result: CurateResult = await orchestrator.execute(
                "curate_concepts", CurateRequest(event_ids=batch_ids)
            )
        except Exception as exc:  # noqa: BLE001
            if type(exc).__name__ == "BudgetExceeded" or "BudgetExceeded" in str(exc):
                log.warning("budget ceiling reached; stopping with partial progress")
                summary["halted"] = str(exc)
                break
            raise

        summary["tokens"] += result.tokens_in + result.tokens_out
        summary["usd"] += result.usd
        summary["model"] = result.model or summary["model"]
        if result.mutations:
            all_mutations.extend(result.mutations)
            applied = await orchestrator.execute("apply_mutations", result)
            summary["applied"] += applied.checked

    summary["mutations"] = len(all_mutations)
    summary["_mutations"] = all_mutations

    # Regenerate the root index before validating, so newly written concepts are
    # reachable and do not trip the orphan check.
    reindex_bundle(cfg)

    validation: ValidateResult = await orchestrator.execute(
        "validate_bundle", CurateRequest(event_ids=[])
    )
    summary["issues"] = [
        {"severity": i.severity, "check": i.check, "path": i.path, "message": i.message}
        for i in validation.issues
    ]
    summary["validation_ok"] = validation.ok
    summary["generated_at"] = datetime.now(UTC).isoformat()
    return summary


def registered_activities() -> list[str]:
    return REGISTRY.names()
