---
type: pattern
title: Bounded Convergence Loop
description: Workflow pattern safely iterating agent execution within strict time,
  cost, and iteration limits until a deterministic gate passes or defined termination
  is reached.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/bounded-convergence-loop.md
tags:
- workflows
- patterns
- convergence-loop
- iteration
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:36:52.018344+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/bounded-convergence-loop.md
  author: Mario Zagar
  last_modified: '2026-08-28T22:42:47-04:00'
- id: evt-wg-workflows-and-process-integration-pr-26
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/26
  author: mzagar
  last_modified: '2026-08-29T02:42:47+00:00'
---

# Overview
The Bounded Convergence Loop pattern governs iterative agent-assisted problem solving by constraining retries within explicit scope, time, cost, and iteration limits until an independent deterministic gate evaluates the candidate result as acceptable [^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0]. This prevents runaway execution, budget exhaustion, or self-certified success during autonomous tasks [^evt-wg-workflows-and-process-integration-pr-26].

# Architecture / Specification
The loop admits a bounded task with predetermined scope and allowed tools, executes an agent attempt, and routes the output to a deterministic gate [^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0].

Key invariants include [^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0]:
- Explicit task scope, tool capabilities, and acceptance criteria are fixed before iteration begins.
- The agent is prohibited from self-certifying convergence.
- Every retry consumes from a declared budget including iteration limits and time or cost caps.
- All attempts, gate outcomes, and terminal transitions (success, escalation, abstention, or failure) are durably recorded in workflow state.
- Workflow restarts resume from recorded state without resetting attempt budgets.

# References
- [Deterministic Acceptance Gate](deterministic-acceptance-gate.md)
- [Proposal/Execution Split](proposal-execution-split.md)
- [Durable Wait](durable-wait.md)
- [Bounded Autonomous Remediation](../reference-architectures/bounded-autonomous-remediation.md)

[^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/bounded-convergence-loop.md
[^evt-wg-workflows-and-process-integration-pr-26]: https://github.com/aaif/wg-workflows-and-process-integration/pull/26
