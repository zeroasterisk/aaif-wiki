---
type: pattern
title: Bounded Convergence Loop
description: Workflow design pattern constraining iterative agent attempts with declared
  iteration, time, cost, and scope budgets evaluated by a deterministic gate.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/bounded-convergence-loop.md
tags:
- pattern
- workflows
- loop
- remediation
- iteration
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:03:10.474790+00:00'
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
The bounded convergence loop pattern safely iterates an agent-assisted task until a deterministic acceptance condition passes, or halts in a defined non-success state such as escalation or failure[^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0]. It enables iterative diagnosis, modification, and re-checking without granting an open-ended objective, infinite retries, or self-certification authority[^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0].

# Architecture / Specification
The workflow admits an explicitly bounded task, provides tool access scoped strictly to the task, and evaluates candidate attempts via an independent deterministic gate[^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0].

Key invariants include:
- The task scope, capabilities, and target acceptance condition are declared before loop execution begins[^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0].
- The agent cannot declare its own convergence; an independent gate evaluates every candidate output[^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0].
- Every retry must operate against a declared budget, minimally enforcing an iteration limit and either a time or cost boundary[^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0].
- The workflow persists attempt counters, gate outcomes, and transition rationales, resuming safely from recorded state upon restart rather than resetting budgets[^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0].
- Candidate outputs that pass functional checks but violate scope rules cannot proceed to protected effects[^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0].

# References
- Composed in [Bounded Autonomous Remediation](../reference-architectures/bounded-autonomous-remediation.md)[^evt-wg-workflows-and-process-integration-pr-26].
- Related to [Deterministic Acceptance Gate](deterministic-acceptance-gate.md), [Proposal/Execution Split](proposal-execution-split.md), and [Durable Wait](durable-wait.md)[^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0].

[^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/bounded-convergence-loop.md
[^evt-wg-workflows-and-process-integration-pr-26]: https://github.com/aaif/wg-workflows-and-process-integration/pull/26
