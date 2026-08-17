# ADR-004: Resilience, Rate Limiting & Hard Budget Ceilings

## Status
**Proposed** — the mechanisms are specified but none of the numbers have been validated by a real
end-to-end run. The ceilings below are estimates chosen to fail safe, not measurements. This ADR
moves to Accepted after the first bootstrap run reports actual token and dollar consumption.

## Context
An autonomous pipeline that talks to git, the GitHub REST API, and an LLM endpoint hits transient
failures constantly:

1. **HTTP 429 / `RESOURCE_EXHAUSTED`** — LLM quota and rate limits.
2. **GitHub secondary rate limits** — concurrent queries trip abuse detection even under the
   primary quota (see ADR-003 §7 for the primary-quota strategy).
3. **Non-converging agent loops** — repeated tool calls that never produce a mutation.
4. **Oversized payloads** — a 400 KB spec diff dropped into a prompt.
5. **Unbounded spend** — the failure mode nobody notices until the bill arrives. Per-batch iteration
   budgets bound one batch; nothing bounds the *number* of batches.

Item 5 is the one that motivates the status change. The previous revision treated cost as a
side-effect of iteration limits. It is not: an incremental run that discovers 400 changed documents
will happily spend all night inside its per-batch limits.

## Decision
Four layers, all configuration-driven, plus one hard outer boundary.

### 1. Retry policy — configured once, referenced everywhere
Per-activity retry policies live in the ADR-002 activity registry and read their attempt counts from
`config.yaml:temporal.retry_policy`. **The ADR does not restate literal values**; the previous
revision hardcoded `maximum_attempts=6` in prose while config said something else, and the two drifted
(review finding F14).

```python
# aaif_wiki/activities/registry.py
RETRY = RetryPolicy(
    initial_interval=timedelta(seconds=CFG.temporal.retry_policy.initial_interval_seconds),
    backoff_coefficient=CFG.temporal.retry_policy.backoff_coefficient,
    maximum_interval=timedelta(seconds=CFG.temporal.retry_policy.maximum_interval_seconds),
    maximum_attempts=CFG.temporal.retry_policy.maximum_attempts,   # config is the only source
    non_retryable_error_types=["InvalidAuthError", "InvalidSchemaError", "BudgetExceededError"],
)
```
`BudgetExceededError` is non-retryable by construction — retrying a budget breach is the exact
opposite of what should happen.

The same policy object is consumed by `LocalOrchestrator` directly and mapped onto
`temporal.common.RetryPolicy` by `TemporalOrchestrator` (ADR-002 §3).

### 2. Backoff: true full jitter
On 429 / `RESOURCE_EXHAUSTED`:
1. Honour a `Retry-After` header verbatim if present.
2. Otherwise sleep for **full jitter**:

   `t_sleep = uniform(0, min(t_max, t_init * 2^attempt))`

   Note the shape: the random draw spans the *entire* interval from zero to the capped exponential
   bound. The previous revision wrote `min(t_max, t_init * 2^n) * uniform(0.8, 1.2)`, which is a
   ±20% band around a deterministic value — that is "equal jitter" at best and does not decorrelate
   concurrent retriers, which is the whole reason to jitter (review finding F15).
3. Raise a retryable application error so the orchestrator, not a blocking `sleep` inside the
   activity, owns the wait.

### 3. Agent guardrails (inside the curation activity)
- **`RepeatedFailureGuard`** — three consecutive failures with the same error signature halt the
  sub-task and emit an error event rather than looping.
- **`IterationBudgetPlugin`** — hard cap on reasoning turns per concept batch,
  `config.yaml:curator.iteration_budget`.
- **`NoProgressHalt`** — three consecutive turns with zero diff to the working draft terminate the
  batch early.
- **Invariant:** `curator.compaction_threshold < curator.iteration_budget`. If the compaction
  threshold is greater than or equal to the iteration budget, the compactor can never fire — the run
  hits its turn cap first and context compaction (ADR-005) is dead code. This is asserted at config
  load time and fails startup, not silently at turn 40.

### 4. Payload reduction for prose
This corpus is **prose**, not source code — `config.yaml:ingest.doc_extensions` admits only `.md`,
`.markdown`, `.yaml`, `.yml`. Truncation is therefore **structural summarization**, not syntactic
extraction:

- Non-document paths never enter a diff; the extension filter runs first.
- Diffs over `curator.max_diff_bytes` (default 50 KB) are reduced to a **heading tree** — H1/H2/H3
  with per-section change counts — plus the frontmatter delta.
- Sections whose bodies are unchanged are passed as frontmatter-only stubs.
- YAML files are reduced to a key-path diff rather than a line diff.

> Earlier revisions specified AST metadata ("symbols modified, export signatures") and lockfile
> stripping. Those were inherited from code-documentation designs (e.g. OpenWiki, which is
> codebase-first) and are meaningless against working-group charters and RFCs (review finding F16).

### 5. Hard per-run ceilings
Three independent ceilings, checked by the workflow **before dispatching each batch** and again
after each LLM response resolves its actual usage:

| Ceiling | Config key | Incremental default | Bootstrap default | Absolute max |
| :--- | :--- | :--- | :--- | :--- |
| Spend | `budget.max_usd_per_run` | **$25** | **$150** | **$200** |
| Tokens | `budget.max_tokens_per_run` | derived from spend at the pinned model's rate | derived | — |
| Concepts | `budget.max_concepts_per_run` | bounded per profile | bounded per profile | — |

- **$200 is an absolute ceiling.** Config validation rejects any value above it at load time; there
  is no override flag. If a run genuinely needs more, it needs to be split into more runs, and the
  event store makes that free.
- Token ceilings are derived from the spend ceiling using the pinned model's published rate
  (`gemini-3.7-flash`, ~$0.75 / 1M input and ~$3.75 / 1M output at introductory pricing) so that the
  two ceilings cannot silently disagree. Rates live in config alongside the model pin and are
  reviewed whenever the pin is.
- Cost accounting uses the **actual** `usage_metadata` returned by the API where available, with a
  pre-flight token estimate used only to decide whether a batch is admissible.

**On breach: abort with a partial-progress commit.**
```
budget check fails
      │
      ├─► stop dispatching new batches
      ├─► let in-flight batches finish (they are already paid for)
      ├─► flush completed concepts to the wiki delta
      ├─► write a run summary event: {ceiling_hit, spent, remaining_work}
      └─► exit non-zero, open/annotate the PR as PARTIAL (ADR-009)
```
Aborting is cheap precisely because ADR-003 makes resumption cheap: the events are already durable,
the cursor is derived, and the ADR-002 checkpoint records which activities completed. The next run
resumes rather than restarts. A partial wiki delta behind a Pull Request is a strictly better
outcome than either a silent overspend or a lost night's work.

## Consequences

### Positive
* **Spend has a hard, non-overridable ceiling.** The worst case for a runaway run is $200, not
  "however long it took someone to notice."
* **Partial progress is a first-class outcome**, not an error state — which is only true because
  ingestion is event-sourced and the publication path is a reviewable PR.
* **Config is the single source of truth for retry and budget numbers.** Prose in this ADR cannot
  drift from behaviour because it no longer restates the numbers it does not own.
* **Backoff actually decorrelates.** Full jitter spreads concurrent retriers across the whole
  window instead of clustering them in a ±20% band.
* **The compaction invariant is caught at startup**, so the context-management design in ADR-005 is
  guaranteed to be reachable.

### Negative / Trade-offs
* **The numbers are unvalidated.** This is why the ADR is Proposed. The bootstrap default of $150
  is a guess; it may be 3x too high or half of what a full org sweep needs.
* **Deliberate slowness.** Under heavy rate limiting, full jitter plus honoured `Retry-After`
  headers make runs take substantially longer. That is the intended behaviour.
* **Budget aborts fragment a logical unit of work.** A bootstrap that stops at 60% leaves a wiki
  that is visibly incomplete until the next run. The PR must be labelled `PARTIAL` so a reviewer
  does not read absence as a claim.
* **Cost estimation is approximate before the call.** Pre-flight estimates can under-count, so the
  effective ceiling is "last admitted batch" rather than a precise dollar figure. We accept
  overshoot bounded by one batch.
* **Structural summarization loses detail.** A heading tree tells the curator *where* a 400 KB spec
  changed, not *what* it says. Large documents will occasionally need a targeted re-read, which
  costs an extra turn.
