"""Reproducible Jev on/off rendering ablation for GitHub Actions."""

from __future__ import annotations

import copy
import hashlib
import json
import os
import shutil
import tarfile
import time
from pathlib import Path
from typing import Any

from .config import Config
from .curator import Curator
from .jev import assess_mutations
from .models import BudgetState, ConceptStatus, Mutation, RawEvent
from .okf import load_bundle, write_concept
from .store import EventStore
from .validate import validate_bundle, validate_mutation

# Inline events require no mutable upstream checkout, so both arms consume exact bytes.
DEFAULT_EVENT_IDS = [
    "evt-wg-security-and-privacy-pr-19",
    "evt-wg-security-and-privacy-pr-9",
    "evt-wg-security-and-privacy-pr-10",
    "evt-wg-security-and-privacy-pr-11",
    "evt-wg-security-and-privacy-pr-8",
]


def _tree_hash(root: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        digest.update(str(path.relative_to(root)).encode())
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def _apply(bundle: Path, mutations: list[Mutation]) -> dict[str, Any]:
    issues = []
    applied = 0
    for mutation in mutations:
        problems = validate_mutation(mutation)
        if problems:
            issues.extend(p.model_dump(mode="json") for p in problems)
            continue
        if mutation.action == "deprecate":
            concept = load_bundle(bundle).get(mutation.slug)
            if concept:
                concept.status = ConceptStatus.DEPRECATED
                write_concept(bundle, concept)
                applied += 1
        elif mutation.concept:
            mutation.concept.slug = mutation.slug
            write_concept(bundle, mutation.concept)
            applied += 1
    return {"applied": applied, "mutation_issues": issues}


def _snapshot(
    cfg: Config,
    base_bundle: Path,
    destination: Path,
    mutations: list[Mutation],
    known_event_ids: set[str],
) -> dict[str, Any]:
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(base_bundle, destination)
    result = _apply(destination, mutations)
    validation = validate_bundle(
        destination,
        known_event_ids=known_event_ids,
        link_allowlist=cfg.trust.link_allowlist,
        forbidden_patterns=cfg.trust.forbidden_patterns,
    )
    result.update(
        {
            "tree_hash": _tree_hash(destination),
            "files": len(list(destination.rglob("*.md"))),
            "validation_ok": validation.ok,
            "validation_issues": [i.model_dump(mode="json") for i in validation.issues],
        }
    )
    return result


def run_ablation(
    cfg: Config,
    output_dir: Path,
    runs: int = 5,
    event_ids: list[str] | None = None,
) -> dict[str, Any]:
    if not 1 <= runs <= 5:
        raise ValueError("runs must be between 1 and 5")
    output_dir.mkdir(parents=True, exist_ok=True)
    store = EventStore(cfg.events_dir)
    ids = event_ids or DEFAULT_EVENT_IDS
    events = [store.get(event_id) for event_id in ids]
    missing = [event_id for event_id, event in zip(ids, events, strict=True) if event is None]
    if missing:
        raise ValueError(f"missing fixed events: {missing}")
    fixed_events: list[RawEvent] = [event for event in events if event is not None]
    if any(event.pointers for event in fixed_events):
        raise ValueError("ablation inputs must be inline events for snapshot reproducibility")

    existing = load_bundle(cfg.bundle_dir)
    known = {event.event_id for event in store.iter_events()}
    jev_available = bool(os.environ.get("JEV_API_KEY"))
    records: list[dict[str, Any]] = []

    for run in range(1, runs + 1):
        curator = Curator(cfg.curator, cfg.budget, BudgetState())
        started = time.monotonic()
        curated = curator.curate(fixed_events, existing)
        curator_ms = round((time.monotonic() - started) * 1000)

        # Both arms start with byte-equivalent deep copies of the exact same
        # curator output. The only independent variable is Jev enrichment.
        disabled = copy.deepcopy(curated.mutations)
        enabled = copy.deepcopy(curated.mutations)
        jev_stats: dict[str, Any] = {"enabled": False, "skipped": not jev_available}
        jev_ms = 0
        if jev_available:
            jev_cfg = cfg.jev.model_copy(update={"enabled": True})
            previous = os.environ.get("JEV_ENABLED")
            os.environ["JEV_ENABLED"] = "true"
            jev_started = time.monotonic()
            enabled, jev_stats = assess_mutations(enabled, fixed_events, existing, jev_cfg)
            jev_ms = round((time.monotonic() - jev_started) * 1000)
            if previous is None:
                os.environ.pop("JEV_ENABLED", None)
            else:
                os.environ["JEV_ENABLED"] = previous

        run_dir = output_dir / f"run-{run}"
        off_dir = run_dir / "jev-off" / "wiki"
        on_dir = run_dir / "jev-on" / "wiki"
        off = _snapshot(cfg, cfg.bundle_dir, off_dir, disabled, known)
        on = _snapshot(cfg, cfg.bundle_dir, on_dir, enabled, known)
        on["jev"] = jev_stats
        on["jev_latency_ms"] = jev_ms
        record = {
            "run": run,
            "fixed_event_ids": ids,
            "curator": {
                "model": curated.model,
                "tokens_in": curated.tokens_in,
                "tokens_out": curated.tokens_out,
                "estimated_usd": curated.usd,
                "latency_ms": curator_ms,
                "mutations": len(curated.mutations),
            },
            "jev_off": off,
            "jev_on": on,
            "rendered_bytes_identical": off["tree_hash"] == on["tree_hash"],
            "mutation_metadata": [
                {
                    "slug": mutation.slug,
                    "action": mutation.action,
                    "jev": mutation.jev.model_dump(mode="json") if mutation.jev else None,
                }
                for mutation in enabled
            ],
        }
        records.append(record)
        (run_dir / "result.json").write_text(json.dumps(record, indent=2))

    summary = {
        "runs_requested": runs,
        "runs_completed": len(records),
        "jev_enabled_arm_executed": jev_available,
        "fixed_event_ids": ids,
        "all_rendered_bytes_identical": all(r["rendered_bytes_identical"] for r in records),
        "all_off_valid": all(r["jev_off"]["validation_ok"] for r in records),
        "all_on_valid": all(r["jev_on"]["validation_ok"] for r in records),
        "curator_tokens_in": sum(r["curator"]["tokens_in"] for r in records),
        "curator_tokens_out": sum(r["curator"]["tokens_out"] for r in records),
        "curator_estimated_usd": sum(r["curator"]["estimated_usd"] for r in records),
        "curator_latency_ms": sum(r["curator"]["latency_ms"] for r in records),
        "jev_input_tokens": sum(
            m["jev"].get("input_tokens", 0)
            for r in records
            for m in r["mutation_metadata"]
            if m["jev"]
        ),
        "jev_output_tokens": sum(
            m["jev"].get("output_tokens", 0)
            for r in records
            for m in r["mutation_metadata"]
            if m["jev"]
        ),
        "jev_latency_ms": sum(r["jev_on"]["jev_latency_ms"] for r in records),
        "note": "TypeSafe does not publish a verified token price; Jev dollar cost is not estimated.",
        "records": records,
    }
    (output_dir / "summary.json").write_text(json.dumps(summary, indent=2))
    with tarfile.open(output_dir / "rendered-outputs.tar.gz", "w:gz") as archive:
        for path in sorted(output_dir.glob("run-*/jev-*/wiki")):
            archive.add(path, arcname=str(path.relative_to(output_dir)))
    return summary
