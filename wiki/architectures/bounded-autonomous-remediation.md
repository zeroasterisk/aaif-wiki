---
type: architecture
title: Bounded Autonomous Remediation
description: Reference architecture governing iterative, autonomous problem resolution
  within predefined task boundaries, budget constraints, and deterministic acceptance
  gates.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/43
tags:
- architecture
- reference-architecture
- remediation
- deterministic-gate
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:14:40.565482+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-pr-43
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/43
  author: narko4u
  last_modified: '2026-10-02T15:00:07+00:00'
---

# Overview

The Bounded Autonomous Remediation reference architecture defines an operational model for autonomous incident remediation and bug resolution operating within explicit step and cost budgets.[^evt-wg-workflows-and-process-integration-pr-43] The architecture allows agents to iteratively hypothesize, patch, and test candidate solutions, terminating when objective criteria are satisfied or when boundary constraints force escalation.

# Architecture / Specification

The architecture relies on [Deterministic acceptance gate](../patterns/deterministic-acceptance-gate.md) checks to validate proposed fixes before applying them to target systems.[^evt-wg-workflows-and-process-integration-pr-43]

### Minimum Evidence Requirements
Gate evaluation strength scales with two primary properties of the permitted remediation effect:[^evt-wg-workflows-and-process-integration-pr-43]
- **Blast radius**: The scope of systems, users, or data impacted if the proposed remediation introduces regressions.
- **Reversal cost**: The complexity, downtime, or operational cost necessary to roll back or undo the applied modification.

### Acceptance Invariants
Regardless of gate strength, three baseline properties hold for every generated acceptance record:[^evt-wg-workflows-and-process-integration-pr-43]
1. **Determinism of the verdict**: The pass/fail outcome is produced through reproducible, deterministic validation checks rather than subjective or non-deterministic model self-evaluations.
2. **Binding of verdict to candidate**: The verdict record explicitly binds to the exact patch or candidate artifact evaluated.
3. **Preservation as execution evidence**: The evaluation record and associated diagnostic outputs are preserved within the execution trace for post-incident auditability.

[^evt-wg-workflows-and-process-integration-pr-43]: https://github.com/aaif/wg-workflows-and-process-integration/pull/43
