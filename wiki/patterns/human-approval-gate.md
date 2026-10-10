---
type: pattern
title: Human Approval Gate
description: Workflow pattern requiring an authorized human to explicitly approve
  an immutable proposal before a boundary action is executed.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/42
tags:
- patterns
- workflows
- governance
- hitl
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:10:15.206888+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-pr-42
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/42
  author: askulkarni2
  last_modified: '2026-09-24T01:00:06+00:00'
---

# Overview

The Human Approval Gate pattern pauses execution at an authorization boundary until an authorized human operator evaluates an immutable proposal and issues an attributable approval or rejection [^evt-wg-workflows-and-process-integration-pr-42]. This gate separates transient confidence-building checkpoints from permanent statutory requirements.

# Architecture / Specification

The pattern operates in conjunction with the [Proposal-Execution Split](proposal-execution-split.md) to ensure an agent cannot execute side-effecting operations without external review.

### Operational Distinctions and Lifecycle
- **Confidence-Driven Gates**: Deployed when an agentic system is nascent or unproven. These gates are eligible for relaxation over time under the [Autonomy Graduation](autonomy-graduation.md) lifecycle [^evt-wg-workflows-and-process-integration-pr-42].
- **Structural and Regulatory Boundaries**: Checkpoints mandated by law or institutional governance (such as physician sign-offs or legal filings) are distinct from confidence gates and must be modeled as a permanent [Hard Constraint Gate](hard-constraint-gate.md) [^evt-wg-workflows-and-process-integration-pr-42].

# References

- [Hard Constraint Human-in-the-Loop Gate](hard-constraint-gate.md)
- [Autonomy Graduation](autonomy-graduation.md)
- [Proposal-Execution Split](proposal-execution-split.md)
- [Deterministic Acceptance Gate](deterministic-acceptance-gate.md)

[^evt-wg-workflows-and-process-integration-pr-42]: https://github.com/aaif/wg-workflows-and-process-integration/pull/42
