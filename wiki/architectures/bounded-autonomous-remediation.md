---
type: architecture
title: Bounded Autonomous Remediation
description: Reference architecture governing iterative, autonomous problem resolution
  within predefined task boundaries, activity units, and convergence budgets.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/49
tags:
- architecture
- remediation
- workflows
- runtime
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T10:51:37.206517+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-pr-49
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/49
  author: mzagar
  last_modified: '2026-10-09T11:27:17+00:00'
---

# Overview
The Bounded Autonomous Remediation reference architecture defines a controlled execution environment where an autonomous agent diagnoses and resolves operational failures within strictly bounded task parameters. It couples iterative exploration with deterministic budgets and safety checkpoints to prevent runaway execution or out-of-scope operational impact.

# Architecture / Specification
The architecture explicitly differentiates between business-level problem bounds and internal execution units to maintain operational clarity[^evt-wg-workflows-and-process-integration-pr-49]:

- **Business Task**: The bounded business problem or operational incident admitted to and handled by a remediation run (such as resolving a specific deployment alert or failed node)[^evt-wg-workflows-and-process-integration-pr-49]. The business task sets the boundary conditions, blast radius, and target recovery objectives.
- **Activity**: The granular workflow subunit executed within the context of a business task (such as running a health check command, inspecting logs, or applying a configuration patch)[^evt-wg-workflows-and-process-integration-pr-49].
- **Convergence Controls**: The run operates under a [bounded convergence loop](../patterns/bounded-convergence-loop.md), ensuring that repeated activity iterations terminate deterministically against strict iteration count and resource budgets.
- **Gate Separation**: Enforces transition gates such as a [deterministic acceptance gate](../patterns/deterministic-acceptance-gate.md) or [human approval gate](../patterns/human-approval-gate.md) before promoting remediation changes to production systems.

# References
- [Workflow Architecture Principles](../guidelines/workflow-architecture-principles.md)
- [Single-Agent Human Approval](../architectures/single-agent-human-approval.md)
- [Proposal-Execution Split](../patterns/proposal-execution-split.md)

[^evt-wg-workflows-and-process-integration-pr-49]: https://github.com/aaif/wg-workflows-and-process-integration/pull/49
