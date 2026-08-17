"""Derived SQLite index over the event store.

This database is **not** a source of truth. It is a disposable, rebuildable read
model: delete it and ``aaif-wiki index rebuild`` reconstructs it from
``raw/events/`` in one pass. It is gitignored for exactly that reason.

It exists because the event store is a directory of JSON files, which is the right
*storage* choice (diffable, inspectable, no daemon) and the wrong *query* choice
once there are thousands of events and the curator wants "give me every open PR in
wg-security-and-privacy touching design-patterns since March".
"""

from __future__ import annotations

import sqlite3
from collections.abc import Iterable
from pathlib import Path

from ..models import Lifecycle, RawEvent, SourceType

SCHEMA = """
CREATE TABLE IF NOT EXISTS events (
    event_id     TEXT PRIMARY KEY,
    source_type  TEXT NOT NULL,
    lifecycle    TEXT NOT NULL,
    repository   TEXT NOT NULL,
    reference_id TEXT NOT NULL,
    title        TEXT NOT NULL,
    timestamp    TEXT NOT NULL,
    author       TEXT,
    url          TEXT,
    summary      TEXT,
    has_inline   INTEGER NOT NULL DEFAULT 0
);
CREATE INDEX IF NOT EXISTS idx_events_repo      ON events(repository);
CREATE INDEX IF NOT EXISTS idx_events_lifecycle ON events(lifecycle);
CREATE INDEX IF NOT EXISTS idx_events_ts        ON events(timestamp);

CREATE TABLE IF NOT EXISTS pointers (
    event_id   TEXT NOT NULL,
    repo       TEXT NOT NULL,
    commit_sha TEXT NOT NULL,
    path       TEXT NOT NULL,
    blob_sha   TEXT NOT NULL,
    status     TEXT NOT NULL,
    PRIMARY KEY (event_id, path, blob_sha)
);
CREATE INDEX IF NOT EXISTS idx_pointers_path ON pointers(path);
CREATE INDEX IF NOT EXISTS idx_pointers_repo ON pointers(repo);
"""


class EventIndex:
    def __init__(self, db_path: Path):
        self.db_path = db_path
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(str(db_path))
        self.conn.row_factory = sqlite3.Row
        self.conn.executescript(SCHEMA)
        self.conn.commit()

    def close(self) -> None:
        self.conn.close()

    def __enter__(self) -> EventIndex:
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()

    # -- write ----------------------------------------------------------
    def upsert(self, event: RawEvent) -> None:
        self.conn.execute(
            """INSERT INTO events
               (event_id, source_type, lifecycle, repository, reference_id,
                title, timestamp, author, url, summary, has_inline)
               VALUES (?,?,?,?,?,?,?,?,?,?,?)
               ON CONFLICT(event_id) DO UPDATE SET
                 lifecycle=excluded.lifecycle,
                 title=excluded.title,
                 summary=excluded.summary""",
            (
                event.event_id,
                event.source_type.value,
                event.lifecycle.value,
                event.repository,
                event.reference_id,
                event.title,
                event.timestamp.isoformat(),
                event.author,
                event.url,
                event.summary,
                1 if event.inline_text else 0,
            ),
        )
        for ptr in event.pointers:
            self.conn.execute(
                """INSERT OR REPLACE INTO pointers
                   (event_id, repo, commit_sha, path, blob_sha, status)
                   VALUES (?,?,?,?,?,?)""",
                (event.event_id, ptr.repo, ptr.commit_sha, ptr.path, ptr.blob_sha, ptr.status),
            )

    def rebuild(self, events: Iterable[RawEvent]) -> int:
        self.conn.execute("DELETE FROM events")
        self.conn.execute("DELETE FROM pointers")
        count = 0
        for event in events:
            self.upsert(event)
            count += 1
        self.conn.commit()
        return count

    def commit(self) -> None:
        self.conn.commit()

    # -- read -----------------------------------------------------------
    def query(
        self,
        repository: str | None = None,
        lifecycle: Lifecycle | None = None,
        source_type: SourceType | None = None,
        since: str | None = None,
        limit: int = 200,
    ) -> list[sqlite3.Row]:
        clauses, params = [], []
        if repository:
            clauses.append("repository = ?")
            params.append(repository)
        if lifecycle:
            clauses.append("lifecycle = ?")
            params.append(lifecycle.value)
        if source_type:
            clauses.append("source_type = ?")
            params.append(source_type.value)
        if since:
            clauses.append("timestamp >= ?")
            params.append(since)
        where = f"WHERE {' AND '.join(clauses)}" if clauses else ""
        params.append(limit)
        return list(
            self.conn.execute(
                f"SELECT * FROM events {where} ORDER BY timestamp DESC LIMIT ?", params
            )
        )

    def repos(self) -> list[str]:
        return [r[0] for r in self.conn.execute("SELECT DISTINCT repository FROM events ORDER BY 1")]

    def count(self) -> int:
        return self.conn.execute("SELECT COUNT(*) FROM events").fetchone()[0]
