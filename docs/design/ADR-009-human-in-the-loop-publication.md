# ADR-009: Human-in-the-Loop Publication via Pull Request

## Status
**Accepted**

## Context
Nothing in ADR-001 through ADR-008 stops the curator from writing directly to `main`. The 2026-08
architecture review flagged this as an S1 finding, and it is the single most consequential gap in the
original design:

1. **Machine claims become published facts with no gate.** A concept synthesized from an open PR
   lands in the canonical bundle and is indistinguishable, to a reader arriving from a search engine,
   from a curated statement about a ratified AAIF standard.
2. **The untrusted-input defences in ADR-007 are bounded, not absolute.** Prompt fencing reduces the
   frequency of injected content surviving into output; it does not eliminate it. The structural
   control (schema-validated mutations) bounds the blast radius. Neither is a substitute for
   somebody looking at the diff before it is public.
3. **OKF v0.2 has the vocabulary for this and we were not using it.** `status: draft|stable|deprecated`
   and `verified: [{by, at}]` exist precisely so consumers can tell machine output from
   human-confirmed output. Trust tiers in OKF are **derived by the consumer** from `verified` —
   absent means unverified, machine actors only means machine-confirmed, a `human:<id>` actor means
   human-reviewed. The spec deliberately stores no computed credibility score. Writing everything
   straight to `main` with no `verified` entry throws that signal away.
4. **The review itself is valuable and was being discarded.** When a human fixes a machine-generated
   concept, that edit is a labelled correction — exactly the data needed to improve the prompts and
   build an eval set. Committing straight to `main` destroys it.

## Decision
**The curator never writes to `main`.** Every run's output reaches the canonical bundle through a
Pull Request, and OKF status/verification fields carry the trust state honestly.

```
  run completes (or aborts at a budget ceiling — ADR-004 §5)
        │
        ▼
  branch: wiki/run-<run_id>            ── never main, no exceptions
        │
        ▼
  commit the wiki delta + the run summary event
        │
        ▼
  open a Pull Request
    ├─ body: concepts added/changed/deprecated, budget consumed,
    │        validator results, blocked links (ADR-007 §3),
    │        detected injection attempts, PARTIAL flag if aborted
    └─ CI: Layer 1 validators + export guards  ── BLOCKING (ADR-008)
        │
        ├──────────────── publication.auto_merge: true ────────────────┐
        │                 merge on green CI                            │
        │                 → status stays `draft`, no `verified` entry  │
        │                                                              ▼
        └──────────────── publication.auto_merge: false ──────► human reviews
                                                                       │
                                                          ┌────────────┴────────────┐
                                                     approve                     edit + approve
                                                          │                         │
                                                          └────────────┬────────────┘
                                                                       ▼
                                              merge → verified: [{by: "human:<id>", at: <iso>}]
                                                       status: draft → stable
                                                       review record written
```

### 1. Branch and PR, always
- Branch name `wiki/run-<run_id>`; one PR per run.
- The PR body is generated, structured, and complete: concepts added / changed / deprecated with
  links, budget consumed against the ceiling, Layer 1 validator results, every link blocked by the
  allowlist with its host, every detected injection attempt, and a `PARTIAL` banner when the run hit
  a budget ceiling (ADR-004 §5).
- Branch protection on `main` enforces this at the platform level. The curator's credential does not
  have push access to `main`; this is not a policy the curator is trusted to follow.

### 2. Auto-merge is a config choice, and it changes the trust claim — not the gate
```yaml
publication:
  auto_merge: false            # default
  require_human_for_stable: true   # not configurable; stated for clarity
```
| Mode | CI must pass | Merges without a human | Resulting `status` | `verified` |
| :--- | :--- | :--- | :--- | :--- |
| `auto_merge: true` | Yes | Yes | `draft` | absent |
| `auto_merge: false` | Yes | No | `stable` on approval | `[{by: "human:<id>", at: <iso>}]` |

Auto-merge changes **who pushes the button**, never **what the content claims about itself**. An
auto-merged concept is in the bundle and readable, and it is honestly labelled `draft` with no
`verified` entry, so any OKF consumer deriving trust tiers sees "unverified." There is no path by
which the machine produces a `stable`, human-verified page.

This is enforced structurally, not by convention: `verified` is **not a field in the
`ConceptMutation` schema** (ADR-007 §1.3). The curator physically cannot emit it. The only writer is
the merge-time review applier, which reads the GitHub review event and stamps the actor id and
timestamp. Validator V6 (ADR-008) fails the build if a `verified` entry ever appears on a path that
did not go through that applier.

### 3. Status lifecycle
| Transition | Trigger |
| :--- | :--- |
| → `draft` | Concept generated. Always. Also mandatory and permanent-until-merge for any concept sourced from a non-`merged` event (ADR-003 §5) — human approval alone does not promote a concept whose underlying work is still an open PR. |
| `draft` → `stable` | Human approves the PR **and** every source event is `lifecycle: merged`. |
| `stable` → `draft` | A new run materially changes the concept. Re-review required; the prior `verified` entry is retained with its original timestamp, so the record shows what was approved and when. |
| any → `deprecated` | Tombstone event (ADR-003 §9). The page is not deleted; inbound links keep working. |

`verified` is a **list**. Re-approval appends rather than replaces, so the page carries its full
review history and a consumer can see whether a human has looked at it once, or repeatedly, or not
since 2026.

### 4. The review record is a training and eval dataset
This is a first-class purpose of the gate, not a byproduct. Every merged publication PR produces a
structured record at `raw/reviews/<run_id>.json`:

```json
{
  "run_id": "run-2026-08-17-1432",
  "pr": "https://github.com/zeroasterisk/aaif-wiki/pull/128",
  "reviewer": "human:zeroasterisk",
  "reviewed_at": "2026-08-17T22:41:00Z",
  "prompt_revision": "curator/v7",
  "model_resolved": "<resolved model id as returned by the API>",
  "outcome": "approved_with_edits",
  "concepts": [
    {
      "concept_id": "architectures/attested-isolated-runtime",
      "source_events": ["evt-2026-08-17-spaa-a1b2c3d"],
      "machine_output_sha": "…",
      "human_output_sha": "…",
      "edit_kind": ["factual_correction", "link_fix"],
      "diff": "unified diff, machine → human"
    }
  ]
}
```

Each entry with `machine_output_sha != human_output_sha` is a **labelled correction pair**:
`(input events, machine output, human-corrected output)`, with the prompt revision and resolved model
id that produced the machine side. That triple is what makes it usable as eval data rather than
anecdote.

`edit_kind` is a small closed vocabulary — `factual_correction`, `link_fix`, `scope_change`,
`tone`, `schema_fix`, `hallucination_removal` — chosen at review time from a checklist in the PR
template. Closed because free-text labels are unaggregatable, and the point of the vocabulary is to
answer "what does this pipeline get wrong most often?" Rejections are recorded too, with a reason;
a rejected concept is at least as informative as an approved one.

Harvesting into golden cases and validators is a deliberate, human-triaged step (ADR-008), not an
automatic training loop. Review records are committed to the repository alongside the events, so the
dataset is versioned, diffable, and — like the bundle itself — donatable (ADR-010).

## Consequences

### Positive
* **No unreviewed machine claim can present itself as verified.** Enforced by branch protection and
  by `verified` being absent from the mutation schema, not by the curator behaving well.
* **OKF's trust vocabulary is used as designed.** Consumers derive tiers from `verified` and get an
  accurate answer, which is the difference between the corpus being citable and being a curiosity.
* **The gate is the same review surface humans already use.** GitHub PRs mean diffs, comments,
  suggested edits, CI status, and history — no bespoke review UI to build or maintain.
* **Budget aborts have somewhere safe to land.** A partial run becomes a `PARTIAL`-labelled PR
  rather than a half-written `main`.
* **Review effort compounds.** Every correction is captured as structured, labelled data with the
  prompt and model that produced the error, so it can improve the next run instead of evaporating.
* **Publication is auditable end to end.** Event id → concept → PR → reviewer → `verified` entry.

### Negative / Trade-offs
* **A human becomes the bottleneck for `stable`.** With one maintainer, a large bootstrap run
  produces a review queue that will not clear quickly. Realistically much of the corpus sits at
  `draft` for a long time, and the index must make that visible rather than hide it.
* **Review fatigue degrades the gate.** A 200-concept PR gets rubber-stamped. Runs need to be sized
  for reviewability — which is an argument for smaller, more frequent incremental runs, and a real
  constraint on the budget defaults in ADR-004.
* **`edit_kind` labelling adds friction** to every review, and its quality depends entirely on the
  reviewer bothering. Low-quality labels make the eval corpus less useful without making it
  obviously broken.
* **Review records grow the repository** and contain full diffs of every corrected concept.
* **PR-per-run does not compose with concurrent runs.** Two overlapping runs produce conflicting
  branches. Runs are serialized by a lock; this is a real limitation of the single-operator design.
* **Auto-merge mode is a genuine risk surface.** It means unreviewed (if honestly-labelled) content
  is publicly readable. We accept it because CI is blocking, the content is `draft` and unverified,
  and the alternative — nothing published until a human has time — makes the project useless as a
  living wiki.
