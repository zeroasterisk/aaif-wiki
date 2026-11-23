---
type: pattern
title: Bounded Convergence Loop
description: Iterative workflow pattern safely executing agent attempts within strict
  budget, scope, and deterministic acceptance gates.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/bounded-convergence-loop.md
tags:
- workflows
- patterns
- remediation
- iteration
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T09:53:05.393482+00:00'
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
The Bounded Convergence Loop is a workflow orchestration pattern that enables an agent to iterate on a bounded task until an external deterministic acceptance condition is met, or until declared resource limits terminate execution[^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0]. It addresses tasks that cannot reliably be resolved in a single step—such as lint errors, type corrections, dependency upgrades, or documentation fixes—without granting the probabilistic model open-ended authority or self-certification privileges[^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0].

This pattern is primarily utilized in [Bounded Autonomous Remediation](../architectures/bounded-autonomous-remediation.md) and relies on close composition with the [Deterministic Acceptance Gate](deterministic-acceptance-gate.md), [Proposal/Execution Split](proposal-execution-split.md), and [Durable Wait](durable-wait.md)[^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0].

# Architecture / Specification
The workflow engine orchestrates candidate generation while strictly isolating the evaluation and effect boundaries[^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0]:
1. **Task Admission:** An explicitly bounded task with pre-declared scope and capabilities is admitted.
2. **Agent Attempt:** The agent attempts work using only granted tools and constrained context.
3. **Deterministic Evaluation:** A deterministic acceptance gate independently tests candidate output against explicit criteria and scope boundaries.
4. **Retry Arbitration:** If the gate rejects the candidate, the workflow verifies configured retry budgets (iteration counts, wall-clock time, or cost caps). If budgets remain, another attempt is permitted; otherwise, the loop halts, fails, or escalates.
5. **Controlled Effect:** Once accepted, execution exits to apply the change through controlled mechanisms.

## Invariants
Implementations must enforce seven core invariants[^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0]:
- Scope, allowed capabilities, and acceptance criteria must be fixed before loop initiation.
- Agents cannot declare convergence; deterministic verification must evaluate every attempt.
- Every retry is bound by declared budgets (mandatory iteration limit, plus time or cost limits).
- Attempt counts, gate evaluation payloads, and terminal reasons must be logged in an audit trail.
- A gate failure can only lead to bounded retries, escalation, abstention, or recorded failure.
- Passing changes that violate declared task scope must not proceed to protected effects.
- Restarts must resume from persisted state without resetting iteration counters or budgets.

# Lifecycle History
Introduced and merged into `wg-workflows-and-process-integration` as part of the bounded autonomous remediation reference architecture pull request[^evt-wg-workflows-and-process-integration-pr-26].

[^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/bounded-convergence-loop.md
[^evt-wg-workflows-and-process-integration-pr-26]: https://github.com/aaif/wg-workflows-and-process-integration/pull/26
