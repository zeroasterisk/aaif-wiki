---
type: pattern
title: Bounded Convergence Loop
description: Architectural pattern safely iterating an agent-driven task within explicit
  budget limits until a deterministic acceptance condition passes or an escalation
  path triggers.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/workstreams/reference-architectures/patterns/bounded-convergence-loop.md
tags:
- pattern
- workflow
- remediation
- governance
- acceptance-gate
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:43:19.607440+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-dc0b08806fbd-14b411d8
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/workstreams/reference-architectures/patterns/bounded-convergence-loop.md
  author: Mario Zagar
  last_modified: '2026-11-05T08:39:35-08:00'
---

# Overview
The Bounded Convergence Loop pattern governs iterative agent-assisted execution for bounded business tasks that cannot reliably be completed in a single pass.[^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-14b411d8] Rather than granting an open-ended goal or allowing models to self-certify completion, the workflow admits an explicitly scoped task, exposes strictly bounded tools, and subjects every candidate result to evaluation by an independent deterministic gate.[^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-14b411d8]

This pattern serves as a core primitive in [Bounded Autonomous Remediation](../architectures/bounded-autonomous-remediation.md) and cooperates with [Deterministic Acceptance Gate](deterministic-acceptance-gate.md), [Proposal/Execution Split](proposal-execution-split.md), and [Durable Wait](durable-wait.md).[^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-14b411d8]

# Architecture / Specification

## Operational Lifecycle
1. **Task Admission:** A bounded business task enters the workflow with declared constraints, required tools, and an explicit acceptance test before execution begins.[^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-14b411d8]
2. **Bounded Execution:** The agent attempts the permitted remediation or authoring work within its sandboxed environment.[^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-14b411d8]
3. **Deterministic Evaluation:** A deterministic gate assesses the candidate artifact. If the check passes and stays within scope, execution exits to controlled effect stages.[^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-14b411d8]
4. **Budgeted Retry Evaluation:** If the gate rejects the candidate, the workflow evaluates configured retry criteria including iteration counts, elapsed time, and cost budgets. If criteria permit, a retry is dispatched; otherwise, the workflow halts or escalates to human review.[^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-14b411d8]

## Mandatory Invariants
Any conforming implementation must enforce the following invariants:[^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-14b411d8]
- The agent cannot declare its own convergence; an independent deterministic gate evaluates every attempt.[^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-14b411d8]
- Every loop operates under an explicit budget containing an iteration limit and at least one of a time or cost boundary.[^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-14b411d8]
- Attempt counters, gate outputs, and transition reasons must be durably recorded in audit state.[^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-14b411d8]
- Following a process restart, the loop resumes from persisted state rather than resetting consumed attempt counters or budgets.[^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-14b411d8]
- An output that passes technical verification but violates declared task scope is blocked from executing protected effects.[^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-14b411d8]

# References
- Workflows and Process Integration WG: Reference Architectures repository.[^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-14b411d8]

[^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-14b411d8]: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/workstreams/reference-architectures/patterns/bounded-convergence-loop.md
