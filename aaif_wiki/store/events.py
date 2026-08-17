"""Append-only event store (ADR-003).

Two properties matter and are enforced here rather than by convention:

1. **Append-only.** :meth:`EventStore.append` refuses to overwrite an existing
   event id. Corrections arrive as new events, never as edits.
2. **No separate cursor file.** The incremental cursor is DERIVED from the store
   (the newest ingested commit per repo). The original design had a mutable
   ``raw/.state.json``, which is a single point of corruption inside an otherwise
   immutable design, conflicts on concurrent runs, and makes incremental mode
   irreproducible across machines. Deriving it costs one scan and removes the file.
"""

from __future__ import annotations

import json
from collections.abc import Iterator
from pathlib import Path

from ..models import RawEvent


class EventStore:
    def __init__(self, root: Path):
        self.root = root
        self.root.mkdir(parents=True, exist_ok=True)

    # -- layout ---------------------------------------------------------
    def path_for(self, event: RawEvent) -> Path:
        ts = event.timestamp
        return self.root / f"{ts.year:04d}" / f"{ts.month:02d}" / f"{ts.day:02d}" / f"{event.event_id}.json"

    def exists(self, event_id: str) -> bool:
        return any(self.root.rglob(f"{event_id}.json"))

    # -- write ----------------------------------------------------------
    def append(self, event: RawEvent) -> Path | None:
        """Write an event. Returns None if it was already present (idempotent)."""
        path = self.path_for(event)
        if path.exists():
            return None
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(event.model_dump_json(indent=2))
        return path

    def append_many(self, events: list[RawEvent]) -> int:
        return sum(1 for e in events if self.append(e) is not None)

    # -- read -----------------------------------------------------------
    def iter_events(self) -> Iterator[RawEvent]:
        for path in sorted(self.root.rglob("*.json")):
            try:
                yield RawEvent.model_validate_json(path.read_text())
            except (ValueError, OSError):
                continue

    def all_events(self) -> list[RawEvent]:
        return sorted(self.iter_events(), key=lambda e: e.timestamp)

    def get(self, event_id: str) -> RawEvent | None:
        for path in self.root.rglob(f"{event_id}.json"):
            try:
                return RawEvent.model_validate_json(path.read_text())
            except ValueError:
                return None
        return None

    def count(self) -> int:
        return sum(1 for _ in self.root.rglob("*.json"))

    # -- derived cursor -------------------------------------------------
    def cursor(self) -> dict[str, str]:
        """Newest ingested commit sha per repo, derived from the store itself.

        This replaces the mutable ``raw/.state.json`` from the original design.
        """
        newest: dict[str, tuple[str, str]] = {}
        for event in self.iter_events():
            stamp = event.timestamp.isoformat()
            for ptr in event.pointers:
                prev = newest.get(ptr.repo)
                if prev is None or stamp > prev[0]:
                    newest[ptr.repo] = (stamp, ptr.commit_sha)
        return {repo: sha for repo, (_, sha) in newest.items()}

    def seen_reference_ids(self, repo: str) -> set[str]:
        return {e.reference_id for e in self.iter_events() if e.repository == repo}

    def stats(self) -> dict:
        by_type: dict[str, int] = {}
        by_lifecycle: dict[str, int] = {}
        repos: set[str] = set()
        total = 0
        for event in self.iter_events():
            total += 1
            by_type[event.source_type.value] = by_type.get(event.source_type.value, 0) + 1
            by_lifecycle[event.lifecycle.value] = by_lifecycle.get(event.lifecycle.value, 0) + 1
            repos.add(event.repository)
        return {
            "total": total,
            "by_source_type": by_type,
            "by_lifecycle": by_lifecycle,
            "repositories": sorted(repos),
        }


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
