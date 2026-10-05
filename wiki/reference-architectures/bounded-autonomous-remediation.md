---
type: architecture
title: Bounded Autonomous Remediation Reference Architecture
description: Job-oriented reference architecture orchestrating autonomous agent iteration
  over fenced problems under strict convergence limits, blast radius controls, and
  deterministic gates.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/43
tags:
- reference-architecture
- workflows
- remediation
- deterministic-gate
- bounded-loop
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T06:01:04.234755+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-pr-43
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/43
  author: narko4u
  last_modified: '2026-10-02T15:00:07+00:00'
---

# Overview

The Bounded Autonomous Remediation reference architecture defines a job-oriented workflow orchestrating autonomous AI agent iteration over strictly fenced problems under hard convergence limits, deterministic gates, and verifiable evidence preservation.[^evt-wg-workflows-and-process-integration-pr-43] It operationalizes patterns such as [Bounded Convergence Loop](../patterns/bounded-convergence-loop.md) and [Deterministic Acceptance Gate](../patterns/deterministic-acceptance-gate.md) to ensure bounded execution without unbounded autonomy.

# Architecture / Specification

The remediation lifecycle isolates candidate generation from deterministic execution and evaluation:

1. **Problem Fencing and Scope Enforcement**: Execution is bounded to pre-declared scopes and parameter envelopes.
2. **Deterministic Evaluation and Minimum Evidence**: Gate strength scales in proportion to the permitted effect's blast radius and reversal cost.[^evt-wg-workflows-and-process-integration-pr-43]
3. **Acceptance Record Guarantees**: Independent of gate strength, every acceptance record must satisfy three invariant properties:[^evt-wg-workflows-and-process-integration-pr-43]
   - **Determinism of the verdict**: The evaluation logic and rules produce repeatable, unambiguous pass/fail results.
   - **Binding of verdict to candidate**: The acceptance verdict cryptographically or identifiably binds to the exact candidate state evaluated.
   - **Preservation as execution evidence**: The record is durably preserved in audit logs and execution traces as unalterable evidence.

# Lifecycle History

- PR #43 in `wg-workflows-and-process-integration` added minimum evidence criteria scaled to blast radius and reversal cost, while defining universal acceptance record invariants.[^evt-wg-workflows-and-process-integration-pr-43]

[^evt-wg-workflows-and-process-integration-pr-43]: https://github.com/aaif/wg-workflows-and-process-integration/pull/43
