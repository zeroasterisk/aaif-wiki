# ADR-003: Immutable Event Sourcing, Ingest Scope & Rehydration

## Status
**Accepted** — supersedes the first revision (which stored all content inline, claimed deterministic
replay, ingested merged content only, hardcoded the repo list, and kept mutable cursor state in
`raw/.state.json`).

## Context
The wiki is a projection over what AAIF actually produced. Getting that projection right requires
answering four questions the first revision answered badly:

1. **What do we store?** Inlining every file's raw text duplicates content git already stores
   perfectly, and bloats the repository for no provenance benefit.
2. **What do we ingest?** Merged files only is not enough. The project owner's framing:
   *"We need to know what landed but also what is work in progress, and we cannot rely on all WGs
   working the same way."* Some working groups land specs; some argue them out in an issue thread
   for two months first. A merged-only ingest sees the second group as inactive.
3. **How do we track position?** A mutable `raw/.state.json` is a second source of truth that can
   silently disagree with the event store, and is exactly the file that gets clobbered by a crash.
4. **What does replay actually guarantee?** The first revision claimed "deterministic replay." That
   is false: replay runs through an LLM.

## Decision

### 1. Storage split by reproducibility
The event store (`raw/events/YYYY/MM/DD/*.json`) is append-only and git-tracked. **What goes into an
event depends on whether git can reproduce it.**

```
             Can git reproduce this content byte-for-byte, forever?
                                    │
              ┌─────────────────────┴─────────────────────┐
             YES                                          NO
   (files in AAIF repositories)      (PR bodies, review comments, issue
              │                       threads, discussion posts — editable
              │                       and deletable by their authors)
              ▼                                           ▼
   ┌────────────────────────────┐          ┌────────────────────────────┐
   │ POINTER event              │          │ INLINE event               │
   │  repo, commit_sha,         │          │  full text captured at     │
   │  path, blob_sha            │          │  fetch time + author +     │
   │  + derived summary         │          │  fetched_at + edit marker  │
   └────────────┬───────────────┘          └────────────────────────────┘
                │ rehydrate on demand
                ▼
   ┌────────────────────────────────────────────┐
   │ raw/cache/  — shallow git mirrors          │
   │ gitignored, rebuildable, no API cost       │
   └────────────────────────────────────────────┘
```

**Pointer event** (`source_type: repo_file`):
```json
{
  "event_id": "evt-2026-08-17-spaa-a1b2c3d",
  "source_type": "repo_file",
  "lifecycle": "merged",
  "repo": "aaif/wg-security-and-privacy",
  "commit_sha": "a1b2c3d4e5f60718293a4b5c6d7e8f9012345678",
  "path": "deliverables/design-patterns/attested-isolated-runtime.md",
  "blob_sha": "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391",
  "committed_at": "2026-08-17T21:00:00Z",
  "author": "intel-lead",
  "summary": "Adds architectural specification for hardware-isolated enclaves."
}
```
The `blob_sha` is the git object id, so the exact bytes are addressable forever without storing them
twice. `summary` is a derived convenience field; it is never authoritative.

**Inline event** (`source_type: github_pr | github_issue | github_discussion | github_comment`)
stores `body_text` verbatim, plus `author`, `fetched_at`, and `upstream_edited_at` when GitHub
reports one. Rationale: an author can edit or delete a PR description tomorrow. If we only kept a
pointer, the provenance chain for any concept derived from it would break. These are the *only*
events that carry raw third-party prose — and per ADR-007 they are the untrusted-input surface.

### 2. Rehydration
`raw/cache/<org>/<repo>` holds a **shallow git mirror** per repository, gitignored and rebuildable.
`rehydrate(event) -> str` runs `git cat-file blob <blob_sha>`, fetching the object if the shallow
clone lacks it. Consequences worth stating plainly: rehydration requires network access on a cold
cache, and if upstream force-pushes away a commit, rehydration fails loudly with the missing
`commit_sha` rather than silently substituting current content.

### 3. `raw/index.db` is derived, never authoritative
A SQLite database at `raw/index.db` indexes events for fast queries ("all events touching
`wg-observability` since sha X", "all open PRs mentioning attestation"). It is:
- **derived** — built by a full scan of `raw/events/`;
- **rebuildable** — `aaif-wiki reindex` recreates it from scratch;
- **gitignored** — it is a cache, and a binary merge conflict waiting to happen otherwise.

The JSON files on disk are the source of truth. Any query result that disagrees with the JSON is an
index bug, and the fix is always "rebuild the index," never "patch the row."

### 4. The cursor is derived; `raw/.state.json` is eliminated
Incremental position is computed, not stored:

```
cursor(repo) = max(committed_at, commit_sha) over all repo_file events for that repo
open_item_cursor(repo) = max(upstream_updated_at) over all inline events for that repo
```

There is no mutable state file. This removes an entire class of "the cursor says we're at X but the
store only has events through W" bugs, and it means the store can be truncated or extended by hand
and the next run does the right thing automatically.

### 5. Ingest scope: merged **and** in-flight
Four source classes, every event carrying an explicit `lifecycle` marker:

| Source | `source_type` | `lifecycle` | Storage |
| :--- | :--- | :--- | :--- |
| Repository files at a commit | `repo_file` | `merged` | pointer |
| Open pull requests (body, changed-file list, review comments) | `github_pr` | `open` or `draft` | inline (+ pointers for the changed files at head sha) |
| Active issues (body + comment thread) | `github_issue` | `open` | inline |
| Discussions | `github_discussion` | `open` | inline |

**Hard rule:** a concept whose `sources[]` contains **any** non-`merged` event MUST carry OKF v0.2
`status: draft`. It is promoted to `stable` only when the underlying work merges *and* a human
approves the page (ADR-009). Draft provenance is not a soft signal to be averaged away — it is a
frontmatter fact, and ADR-008's validators enforce it.

### 6. Repo discovery, not a hardcoded list
The repository set is **discovered** from the GitHub org API (`GET /orgs/aaif/repos`) and filtered
through `config.yaml:ingest.exclude_repos`. AAIF is actively adding repositories; a hardcoded list of
15 is wrong the moment a new working group spins up. Discovery results are recorded as an event so a
replay knows which repos existed at the time.

### 7. GitHub API budget (a real constraint, documented)
- **Unauthenticated REST is 60 requests/hour.** That is not enough for even one bootstrap run.
- **File content therefore comes via `git clone`/`fetch`, which has no REST rate limit.** This is the
  primary reason for the shallow-mirror design in §2 — it is a rate-limit strategy as much as a
  storage strategy.
- **The REST API is reserved for what git cannot give us**: PR metadata, issue threads, discussions
  (GraphQL for discussions), and org repo listing. Responses are cached in `raw/cache/api/` keyed by
  URL + ETag, and conditional requests (`If-None-Match`) do not count against the limit when they
  return 304.
- **A `GITHUB_TOKEN` raises the limit to 5,000 requests/hour** and is strongly recommended; the
  pipeline warns loudly at startup when running unauthenticated and reduces concurrency to 1.

### 8. Replay is re-derivable, not deterministic
Replaying the event store through the curator does **not** reproduce byte-identical output. The
curator is an LLM; temperature, model revision, and provider-side changes all move the text. What
replay guarantees is that the **inputs** are fixed and recorded, so any output difference is
attributable to a prompt, schema, or model change rather than to lost source data.

Replay is therefore **non-destructive by default**:
```
aaif-wiki replay                 # renders to wiki.shadow/, prints a diff, touches nothing
aaif-wiki replay --promote       # only after the diff has been reviewed
```
`--promote` still goes through the ADR-009 Pull Request gate. There is no flag that wipes `wiki/`
in place.

### 9. Tombstones for upstream deletions
When an upstream file, PR, issue, or discussion disappears (deleted, or a repo goes private), we
append a **tombstone event** rather than removing anything:

```json
{
  "event_id": "evt-2026-09-02-tomb-spaa-pr11",
  "source_type": "tombstone",
  "lifecycle": "merged",
  "targets": ["evt-2026-08-17-spaa-pr11"],
  "reason": "upstream_deleted",
  "observed_at": "2026-09-02T10:14:00Z"
}
```
A tombstone projects the affected concept to OKF `status: deprecated` and adds a note to the body
explaining what went away and when. **The page is not deleted.** Deleting it would break every
inbound relative link in the bundle and every external link someone bookmarked — deprecation
preserves the graph while telling the truth about the source.

### 10. Ingestion modes
1. **`--mode=bootstrap`** — discover repos, shallow-clone, emit pointer events for every matching
   document at `HEAD`, then sweep open PRs/issues/discussions. Subject to the bootstrap budget
   ceiling in ADR-004.
2. **`--mode=incremental`** — compute cursors per §4, emit events for commits since the cursor and
   for in-flight items updated since the cursor. The default scheduled mode.
3. **`--mode=replay`** — §8. Shadow render + diff.

## Consequences

### Positive
* **The repository stays small and reviewable.** Pointer events are a few hundred bytes; the
  content lives where it already lived. A `git diff` of an ingest run is readable by a human.
* **Provenance survives upstream mutation.** The one category of content that *can* vanish is the
  one category we copy.
* **One source of truth.** No cursor file, no authoritative database — a directory of JSON files
  that any tool, including `grep`, can read.
* **In-flight visibility.** The wiki can say "Working Group X is actively debating Y in PR #42"
  instead of "no activity," which is the actual question a reader has.
* **Cheap resumption.** Because events are durable and cursors are derived, aborting a run
  mid-flight (ADR-004's budget ceilings) is safe and the next run picks up exactly where it stopped.

### Negative / Trade-offs
* **Rehydration needs the mirror.** Cold-cache replay is not offline. A force-push upstream can make
  a specific historical blob unrehydratable; we fail loudly rather than substitute.
* **Two event shapes, two code paths.** Pointer and inline events need different validation,
  different summarization, and different handling in the untrusted-input fence (ADR-007).
* **Draft noise.** Ingesting open PRs and issues means the wiki carries speculative material.
  Mitigated by mandatory `status: draft` and by the fact that draft pages are visibly marked, but a
  casual reader can still mistake a proposal for a standard.
* **API surface for in-flight content is rate-limited and paginated.** Even at 5,000 req/hr, a full
  sweep of issue comments across a growing org is the slowest part of the run.
* **Replay does not prove correctness.** It proves the inputs were preserved. Catching regressions
  in the *output* requires the golden-set and validators in ADR-008.
