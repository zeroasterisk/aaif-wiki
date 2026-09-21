---
type: pattern
title: Bounded Convergence Loop
description: Workflow design pattern safely iterating agent tasks within explicit
  budget and scope constraints until verified by a deterministic gate or terminating
  in a defined non-success state.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/patterns/bounded-convergence-loop.md
tags:
- pattern
- workflow
- iteration
- safety
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T10:03:22.515811+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/patterns/bounded-convergence-loop.md
  author: Mario Zagar
  last_modified: '2026-08-28T22:42:47-04:00'
- id: evt-wg-workflows-and-process-integration-pr-26
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/26
  author: mzagar
  last_modified: '2026-08-29T02:42:47+00:00'
---

# Overview
The Bounded Convergence Loop pattern governs iterative, agent-assisted problem solving by enforcing explicit scope limits, strict execution budgets, and independent gate evaluation on each cycle [^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0]. Bounded tasks—such as automated code linting, type correction, or patch remediation—often require multiple diagnostic and editing attempts. This pattern enables multi-step refinement while preventing open-ended iteration, runaway financial costs, and unauthorized autonomous drift [^evt-wg-workflows-and-process-integration-pr-26].

# Architecture / Specification
The workflow admits a single bounded task and restricts the agent's tool access and operational scope [^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0]. Each iteration follows a structured sequence:
1. The agent attempts permitted modifications within its restricted sandbox.
2. An external [Deterministic Acceptance Gate](deterministic-acceptance-gate.md) evaluates the resulting candidate against pre-declared acceptance criteria and scope boundaries.
3. If the gate accepts the candidate, the workflow transitions to controlled downstream execution or a [Proposal/Execution Split](proposal-execution-split.md).
4. If the gate rejects the candidate or verification fails, the workflow evaluates configured retry criteria against remaining iteration, time, and cost budgets.
5. If budgets are exhausted or non-retryable errors occur, execution terminates safely in escalation, abstention, or recorded failure [^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0].

### Invariants
To prevent runaway loops and state inconsistency, implementations must enforce the following invariants [^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0]:
- Scope, tool allowances, and acceptance criteria must be fixed before the loop begins.
- The agent cannot declare convergence or self-certify completion.
- Every retry consumes explicit, non-resettable budget limits (at minimum an iteration count limit and a time or cost threshold).
- Workflow engines must record attempt numbers, gate outcomes, and retry rationales in durable state.
- After an engine interruption or restart, the loop must resume from recorded state without resetting attempt counters or budget limits.

[^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0]: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/patterns/bounded-convergence-loop.md
[^evt-wg-workflows-and-process-integration-pr-26]: https://github.com/aaif/wg-workflows-and-process-integration/pull/26
