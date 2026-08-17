# ADR-005: Curator Harness as a Delta Over the Horizon Long-Horizon Harness

## Status
**Proposed** — the dependency is real and the delta is specified, but the harness has not been built
or measured against a real corpus.

## Context
Curating a knowledge graph across dozens of documents breaks naive agent architectures:

1. **Context drift** — taxonomy rules fall out of attention as the window fills with diffs.
2. **Token bloat** — re-sending whole files every turn is expensive and slow.
3. **No compaction** — long sessions accumulate dead tool output.

These are solved problems. Google's **Horizon** long-horizon-harness recipe landed in
[`google/adk-samples`](https://github.com/google/adk-samples) in August 2026 and already implements
tiered prompt assembly, context compaction, and the guardrail plugin chain.

The previous revision of this ADR re-described Horizon's architecture as though it were original to
this project — three-tier assembly, `HorizonSummarizer`, the guardrails — and in doing so created a
maintenance liability: a paraphrase of an upstream design that will drift from it silently. It also
claimed the harness is *"fully decoupled from any single vendor SDK,"* which is simply not true. This
project hard-depends on `google-adk` (2.x) and `google-genai`.

**This ADR is therefore rewritten as a delta.** It records what we take from Horizon, what we change,
and why — and nothing else.

## Decision
We **depend on** the Horizon long-horizon-harness recipe and implement `aaif_wiki/curator/` as a thin
specialization of it.

```
        ┌───────────────────────────────────────────────────────────┐
        │  UPSTREAM: google/adk-samples long-horizon-harness         │
        │  (tiered prompt assembly · compaction · guardrail chain    │
        │   · iteration budget · no-progress halt)                   │
        │  — vendored at a pinned revision; NOT re-described here    │
        └───────────────────────────┬───────────────────────────────┘
                                    │ specialized by
                                    ▼
        ┌───────────────────────────────────────────────────────────┐
        │  aaif_wiki/curator/  — the delta, and only the delta       │
        │  D1 tier content (OKF profile, AAIF graph, event batch)    │
        │  D2 structured mutation output (no free-form file writes)  │
        │  D3 untrusted-input fencing for inline events              │
        │  D4 compaction threshold tied to the ADR-004 invariant     │
        │  D5 model pin + resolved-id provenance capture             │
        └───────────────────────────────────────────────────────────┘
```

### Dependency handling
Horizon is a **recipe**, not a versioned package. We vendor it under `third_party/horizon/` at a
pinned upstream revision recorded in `config.yaml:curator.horizon_revision`, with an `UPSTREAM.md`
recording the source commit and the local patch set. Upgrades are a deliberate, diffable act. We do
not fork-and-forget, and we do not paraphrase.

### The delta

**D1 · What goes in each prompt tier.** Horizon defines the tiering mechanism; we define the
content.
| Tier | Contents (ours) | Cache behaviour |
| :--- | :--- | :--- |
| Stable | The OKF v0.2 **profile** this project emits (ADR-001): required/recommended field rules, frontmatter validation laws, relative-link rule, heading conventions | Static prefix, high cache hit rate |
| Cached | Current graph index — working groups, active topics, taxonomy terms, canonical charter summaries | Invalidated per run, not per turn |
| Volatile | The current event batch (pointer summaries, rehydrated bodies, fenced inline text) and the immediate curation objective | Per turn |

The Stable tier states the OKF **profile**, not "what OKF requires." OKF v0.2 requires only `type`;
everything else this project mandates is a local profile and the prompt says so, so that generated
content is never justified by a rule the spec does not contain.

**D2 · The curator emits structured mutations, not files.** Horizon's default tool surface is
general-purpose. Ours is not: the curator returns a validated `ConceptMutation` (concept id, field
set, body sections, `sources[]` entries, `status`) and a deterministic applier writes the markdown.
The agent never holds a free-form file-write tool. This is a security property (ADR-007) and a
testability property (ADR-008's golden set diffs mutations, which are stable, rather than prose,
which is not).

**D3 · Inline event bodies are fenced.** PR bodies, issue comments, and discussion posts (ADR-003
§1) are attacker-controllable. They enter the Volatile tier inside an explicit delimiter with a
label identifying source, author, and lifecycle, and the Stable tier states that fenced content is
data to describe, never instructions to follow. Full treatment in ADR-007.

**D4 · Compaction threshold is bound by config invariant.** `curator.compaction_threshold` must be
strictly less than `curator.iteration_budget` or the compactor never fires. Asserted at config load
(ADR-004 §3).

**D5 · Model pin and resolved-id provenance.** `curator.model` pins `gemini-3.7-flash` (released
2026-08-13; ~$0.75/1M input, ~$3.75/1M output at introductory pricing). The Flash line moves on a
roughly three-week cadence (3.5 → 3.6 → 3.7), so the pin is a decision with a review date, not a
fossil — revisit quarterly. The **resolved** model id returned by the API is recorded in each
concept's `generated.by`, so provenance reflects what actually ran rather than what was requested.

### On vendor neutrality — the honest claim
The pipeline is **not** vendor-neutral. It depends on `google-adk`, `google-genai`, and a Gemini
endpoint, and swapping the model provider would be real work. That is a fine choice for a personal
project and we are not going to pretend otherwise.

The neutrality claim that *is* true is about **output portability**: the artifact is plain Markdown
with YAML frontmatter in a git repository, readable with `cat`, renderable by GitHub, Obsidian, or
any static site generator, and consumable by any OKF reader (ADR-007). Nothing about the artifact
requires Google software to read. That is the property that matters for donating the corpus to AAIF
(ADR-010), and it is the one we will defend.

`config.yaml:curator.fallback_model` exists so the routing path is exercised by at least two entries
rather than being an untested claim, but it is a resilience mechanism, not evidence of portability.

## Consequences

### Positive
* **Upstream improvements arrive as a diff.** Horizon fixes and features land by bumping a pinned
  revision instead of being reinvented locally.
* **This ADR is short and stays true.** It documents only decisions this project actually owns;
  it cannot drift from an upstream design it no longer restates.
* **Structured mutations are the enabling constraint** for both the untrusted-input defence
  (ADR-007) and the golden-set regression suite (ADR-008).
* **Honest claims survive review.** "Portable output, non-portable pipeline" is defensible; "fully
  decoupled from any vendor SDK" was not.

### Negative / Trade-offs
* **Vendored dependency maintenance.** A pinned copy of an upstream *recipe* needs a human to decide
  when and how to re-sync; there is no dependency resolver doing it.
* **Real lock-in to google-adk / google-genai.** Accepted deliberately. Migration cost is
  non-trivial and we are choosing to owe it.
* **Model pin ages fast.** A ~3-week Flash cadence means the pin is stale within a quarter. Replay
  provenance requires the pin; freshness requires moving it. Quarterly review is the compromise.
* **Structured mutations reduce agent flexibility.** Anything the mutation schema cannot express,
  the curator cannot do — schema changes become a gating step for new capabilities. This is the
  intended trade.
* **Unmeasured.** Cache hit rates, compaction effectiveness, and per-concept token cost are all
  projections. Status stays Proposed until a real run produces numbers.
