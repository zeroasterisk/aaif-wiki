# ADR-003: Immutable Event Sourcing & Ingestion Pipeline

## Status
**Accepted**

## Context
When processing documentation changes over time across 15 repositories, a naive pipeline simply overwrites Markdown files with the latest state. This presents several critical problems:
1. **Lost Provenance**: You cannot tell *when* or *why* a particular section in a concept document was updated.
2. **Irreversible Context Clobbering**: If a flawed agent prompt corrupts a concept page during an update, the historical context is destroyed unless manually salvaged from Git history.
3. **No Non-Destructive Replay**: If the OKF schema or system prompt is improved, there is no clean way to re-synthesize the knowledge graph from raw historical inputs without re-querying external APIs.

## Decision
We implement an **Immutable Event Sourcing architecture** where raw source events are stored permanently in an event log (`raw/events/`), and the OKF Wiki (`wiki/`) acts as a **stateful projection** over that event stream.

```
Incoming Events (Git Commits, PR Diffs, Meeting Notes)
                         │
                         ▼
       ┌───────────────────────────────────┐
       │   Immutable Event Store (raw/)    │
       │   raw/events/YYYY/MM/DD/*.json    │
       └─────────────────┬─────────────────┘
                         │
                         ▼  (Processed by ADK Curator)
       ┌───────────────────────────────────┐
       │  Stateful Projection (wiki/)      │
       │  • Concept Pages (.md)            │
       │  • Cumulative Changelog (log.md)  │
       │  • Knowledge Graph (graph.json)   │
       └───────────────────────────────────┘
```

### Technical Schema: `RawEvent`
Every ingested event is serialized as an immutable JSON record:
```json
{
  "event_id": "evt_20260817_spaa_pr11",
  "source_type": "github_pr",
  "repository": "aaif/wg-security-and-privacy",
  "reference_id": "PR#11",
  "title": "Attested Isolated Runtime design pattern",
  "timestamp": "2026-08-17T21:00:00Z",
  "author": "intel-lead",
  "diff_summary": "Added architectural specification for hardware-isolated enclaves",
  "files_changed": [
    {
      "path": "deliverables/design-patterns/attested-isolated-runtime.md",
      "status": "added",
      "content_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "raw_text": "..."
    }
  ]
}
```

### Ingestion Lifecycle Modes
1. **Bootstrap Mode (`--mode=bootstrap`)**:
   - Clones all repositories at `HEAD`.
   - Generates initial `RawEvent` records for baseline charters, RFCs, and documents.
   - Projects the foundational `wiki/` directory from scratch.
2. **Incremental Delta Mode (`--mode=incremental`)**:
   - Compares commit SHAs against `raw/.state.json`.
   - Extracts only new commits and PR changes since the last run.
   - Appends new `RawEvent` objects to the store and updates affected concept pages.
3. **Replay Mode (`--mode=replay`)**:
   - Wipes `wiki/`.
   - Replays all recorded events in chronological order through the ADK curator agent to rebuild the knowledge graph deterministically.

## Consequences

### Positive
* **Deterministic Replayability**: Any modification to agent prompts, taxonomy rules, or OKF schemas can be tested across the entire history in minutes.
* **Offline Development**: Developers can replay historical events from disk without needing network or GitHub API access.
* **Granular Provenance**: Every concept document links back to the exact `event_id` in its `sources` frontmatter.

### Negative / Trade-offs
* **Storage Footprint**: Raw events take disk space (mitigated by text compression and Git tracking).
