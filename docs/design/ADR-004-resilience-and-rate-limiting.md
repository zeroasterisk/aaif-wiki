# ADR-004: Resilience, Rate Limiting & Failure Mitigation

## Status
**Accepted**

## Context
Autonomous agent workflows that interact with multiple third-party systems encounter frequent operational transient failures:
1. **HTTP 429 / `RESOURCE_EXHAUSTED`**: LLM API quota and rate limits.
2. **GitHub API Secondary Rate Limits**: Fast concurrent Git/PR queries trigger abuse detection.
3. **Infinite Generation Loops**: Agent hallucinating repeated tool calls without converging on a mutation.
4. **Context Window Token Blowup**: Huge source files or bloated tool outputs exceeding context limits.

Without strict architectural guardrails, an automated background job can consume excessive API tokens, stall indefinitely, or leave corrupted partial outputs.

## Decision
We enforce a **multi-layered resilience architecture** combining Temporal retry policies, ADK guardrail plugins, and token-aware backoff algorithms.

### 1. Temporal Retry Policy with Exponential Jitter
Every external activity (GitHub fetch, LLM curation, Gist publication) is governed by an explicit Temporal Retry Policy:
```python
RETRY_POLICY = RetryPolicy(
    initial_interval=timedelta(seconds=2),
    backoff_coefficient=2.0,
    maximum_interval=timedelta(seconds=60),
    maximum_attempts=6,
    non_retryable_error_types=["InvalidAuthError", "InvalidSchemaError"]
)
```

### 2. Intelligent HTTP 429 & Rate Limit Handler
When an LLM or GitHub API returns HTTP 429 or `RESOURCE_EXHAUSTED`:
1. The activity extracts the `Retry-After` header if present.
2. If absent, it computes exponential backoff with full jitter:
   $$t_{\text{sleep}} = \min(t_{\text{max}}, t_{\text{initial}} \times 2^{\text{attempt}}) \times \text{uniform}(0.8, 1.2)$$
3. The activity raises an application exception, causing Temporal to pause the activity without consuming process CPU or blocking other tasks.

### 3. Horizon-Style ADK Guardrails Chain
We integrate three defensive plugins directly into the ADK Agent loop:
- **`RepeatedFailureGuard`**: If an individual tool call fails 3 consecutive times with the same error signature, the agent is forced to halt the sub-task and log an error event instead of looping.
- **`IterationBudgetPlugin`**: Hard limits the number of reasoning turns (e.g. max 15 turns per concept curation batch).
- **`NoProgressHalt`**: Tracks state diffs; if 3 consecutive turns produce zero changes to the working concept draft, the agent terminates early.

### 4. Payload Pruning & Truncation
Before passing Git diffs to the LLM:
- Lockfiles (`package-lock.json`, `uv.lock`), compiled binaries, and minified bundles are automatically stripped.
- Diffs larger than 50 KB are summarized via structured AST metadata (file paths, symbols modified, export signatures) rather than raw text.

## Consequences

### Positive
* **Self-Healing Execution**: Transient network spikes and quota limits resolve automatically without human intervention.
* **Cost & Token Protection**: Hard iteration budgets prevent runaway token usage.
* **Deterministic Circuit Breaking**: Permanent errors (e.g. invalid auth tokens) fail immediately instead of wasting retry attempts.

### Negative / Trade-offs
* **Execution Latency**: In the event of heavy rate-limiting, pipeline execution will intentionally slow down to respect upstream quotas.
