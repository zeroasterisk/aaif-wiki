"""Event store, derived cursor, and curator response handling."""

from __future__ import annotations

import json
from datetime import UTC, datetime, timedelta

from aaif_wiki.config import BudgetCfg, CuratorCfg
from aaif_wiki.curator.agent import Curator
from aaif_wiki.models import (
    BudgetState,
    FilePointer,
    Lifecycle,
    RawEvent,
    SourceType,
)
from aaif_wiki.store import EventIndex, EventStore

NOW = datetime(2026, 8, 17, 12, 0, tzinfo=UTC)


def _event(eid: str, *, repo="aaif/wg-security-and-privacy", sha="abc123", when=None, **kw) -> RawEvent:
    base = dict(
        event_id=eid,
        source_type=SourceType.REPO_FILE,
        lifecycle=Lifecycle.MERGED,
        repository=repo,
        reference_id=f"docs/{eid}.md",
        title=eid,
        timestamp=when or NOW,
        pointers=[
            FilePointer(repo=repo.split("/")[-1], commit_sha=sha, path=f"docs/{eid}.md", blob_sha="b" + eid)
        ],
    )
    base.update(kw)
    return RawEvent(**base)


def test_store_is_append_only(tmp_path):
    store = EventStore(tmp_path)
    assert store.append(_event("e1")) is not None
    assert store.append(_event("e1")) is None, "duplicate ids must not overwrite"
    assert store.count() == 1


def test_store_roundtrip_and_lookup(tmp_path):
    store = EventStore(tmp_path)
    store.append(_event("e1"))
    fetched = store.get("e1")
    assert fetched is not None
    assert fetched.pointers[0].blob_sha == "be1"
    assert store.get("nope") is None


def test_cursor_is_derived_from_newest_event(tmp_path):
    """No mutable .state.json: the cursor falls out of the store itself."""
    store = EventStore(tmp_path)
    store.append(_event("old", sha="old_sha", when=NOW - timedelta(days=5)))
    store.append(_event("new", sha="new_sha", when=NOW))
    assert store.cursor()["wg-security-and-privacy"] == "new_sha"


def test_inline_events_carry_no_pointers(tmp_path):
    """PR bodies are inline because git cannot reproduce them."""
    store = EventStore(tmp_path)
    pr = RawEvent(
        event_id="evt-pr-11",
        source_type=SourceType.PULL_REQUEST,
        lifecycle=Lifecycle.OPEN,
        repository="aaif/wg-security-and-privacy",
        reference_id="PR#11",
        title="Add attested runtime",
        timestamp=NOW,
        inline_text="proposal body",
    )
    store.append(pr)
    got = store.get("evt-pr-11")
    assert got.inline_text == "proposal body"
    assert not got.is_pointer_backed


def test_index_rebuilds_from_store(tmp_path):
    store = EventStore(tmp_path / "events")
    store.append(_event("e1"))
    store.append(_event("e2", when=NOW + timedelta(hours=1)))

    with EventIndex(tmp_path / "index.db") as index:
        assert index.rebuild(store.iter_events()) == 2
        assert index.count() == 2
        assert index.query(lifecycle=Lifecycle.MERGED)[0]["event_id"] in {"e1", "e2"}


# --------------------------------------------------------------------------
# curator response handling (no network)
# --------------------------------------------------------------------------


def _curator() -> Curator:
    return Curator(CuratorCfg(), BudgetCfg(), BudgetState())


def test_curator_forces_draft_for_unmerged_sources():
    """The model is told to mark unsettled sources draft; we do not trust it to."""
    curator = _curator()
    curator._model_used = "gemini-3.7-flash"
    open_pr = RawEvent(
        event_id="evt-pr-1",
        source_type=SourceType.PULL_REQUEST,
        lifecycle=Lifecycle.OPEN,
        repository="aaif/wg-x",
        reference_id="PR#1",
        title="draft proposal",
        timestamp=NOW,
        inline_text="body",
    )
    payload = json.dumps(
        {
            "mutations": [
                {
                    "action": "create",
                    "slug": "taxonomy/thing",
                    "rationale": "because",
                    "source_event_ids": ["evt-pr-1"],
                    # The model claims stability; the source is an open PR.
                    "concept": {
                        "type": "Glossary Term",
                        "title": "Thing",
                        "description": "A thing.",
                        "status": "stable",
                        "body": "# Overview\n\nA thing.\n",
                    },
                }
            ]
        }
    )
    mutations = curator._parse(payload, [open_pr])
    assert len(mutations) == 1
    assert mutations[0].concept.status.value == "draft"


def test_curator_allows_stable_when_all_sources_merged():
    curator = _curator()
    curator._model_used = "gemini-3.7-flash"
    payload = json.dumps(
        {
            "mutations": [
                {
                    "action": "create",
                    "slug": "taxonomy/thing",
                    "rationale": "r",
                    "source_event_ids": ["e1"],
                    "concept": {
                        "type": "Glossary Term",
                        "title": "Thing",
                        "description": "A thing.",
                        "status": "stable",
                        "body": "# Overview\n\nx\n",
                    },
                }
            ]
        }
    )
    mutations = curator._parse(payload, [_event("e1")])
    assert mutations[0].concept.status.value == "stable"


def test_curator_never_emits_verified_entries():
    """Only a human review may add `verified` (ADR-009)."""
    curator = _curator()
    payload = json.dumps(
        {
            "mutations": [
                {
                    "action": "create",
                    "slug": "a/b",
                    "rationale": "r",
                    "source_event_ids": ["e1"],
                    "concept": {"type": "T", "title": "t", "description": "d", "body": "# Overview\n\nx"},
                }
            ]
        }
    )
    assert curator._parse(payload, [_event("e1")])[0].concept.verified == []


def test_curator_discards_malformed_response():
    assert _curator()._parse("this is not json", [_event("e1")]) == []


def test_curator_skips_mutations_with_bad_actions():
    payload = json.dumps({"mutations": [{"action": "rm -rf", "slug": "a", "source_event_ids": []}]})
    assert _curator()._parse(payload, [_event("e1")]) == []


def test_budget_breach_is_detected():
    state = BudgetState(usd_spent=30.0)
    assert state.would_breach(BudgetCfg(max_usd_per_run=25.0)) is not None
    assert BudgetState(usd_spent=1.0).would_breach(BudgetCfg(max_usd_per_run=25.0)) is None
