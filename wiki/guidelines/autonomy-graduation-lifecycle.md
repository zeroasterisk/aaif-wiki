---
type: guideline
title: Autonomy Graduation Lifecycle
description: Operational progression guideline for evolving agent oversight from synchronous
  approval gates to exception escalation and unprompted execution.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/42
tags:
- guideline
- autonomy
- hitl
- lifecycle
- operations
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:14:13.366090+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-pr-42
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/42
  author: askulkarni2
  last_modified: '2026-09-24T01:00:06+00:00'
---

# Overview

The Autonomy Graduation Lifecycle documents the staged progression of operational oversight as an agentic system demonstrates empirical reliability in production environments [^evt-wg-workflows-and-process-integration-pr-42].

# Architecture / Specification

### Graduation Stages

The typical progression moves across three discrete stages:

1. **Approval Gate**: Synchronous human review and authorization required for every candidate action or state transition [^evt-wg-workflows-and-process-integration-pr-42].
2. **Exception Escalation**: Autonomous execution proceeds by default within bounded operational parameters, escalating to human operators only when uncertainty boundaries or safety guards are triggered [^evt-wg-workflows-and-process-integration-pr-42].
3. **Full Autonomous Execution (None)**: Autonomous execution within defined environmental boundaries without routine human intervention [^evt-wg-workflows-and-process-integration-pr-42].

### Non-Graduating Invariants

Structural requirements designated under [Hard Constraint Human Oversight](../patterns/hard-constraint-human-oversight.md) are strictly excluded from the graduation lifecycle and must remain intact regardless of reliability metrics [^evt-wg-workflows-and-process-integration-pr-42].

# References

- [Hard Constraint Human Oversight](../patterns/hard-constraint-human-oversight.md)
- [Human Approval Gate](../patterns/human-approval-gate.md)
- [Workflow Architecture Principles](../guidelines/workflow-architecture-principles.md)

[^evt-wg-workflows-and-process-integration-pr-42]: https://github.com/aaif/wg-workflows-and-process-integration/pull/42
