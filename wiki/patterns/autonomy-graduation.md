---
type: pattern
title: Autonomy Graduation
description: Operational progression model transitioning agent oversight from strict
  approval gates to exception-based escalation and full autonomy as reliability matures.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/42
tags:
- workflows
- patterns
- lifecycle
- governance
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

Autonomy Graduation is an operational lifecycle pattern that systematically reduces human oversight over an agentic workflow as the system demonstrates empirical reliability and meets acceptance thresholds [^evt-wg-workflows-and-process-integration-pr-42]. The progression typically transitions through defined oversight stages: mandatory approval gates, exception-only escalations, and unassisted autonomous execution.

# Architecture / Specification

The graduation model establishes a structured trajectory for AI agent autonomy within enterprise workflows [^evt-wg-workflows-and-process-integration-pr-42]:

1. **Approval Gate Phase**: Every candidate output requires human review and authorization prior to execution via a [Human Approval Gate](human-approval-gate.md) [^evt-wg-workflows-and-process-integration-pr-42].
2. **Exception Escalation Phase**: The agent executes autonomously within bounded parameters, escalating only when confidence scores fall below defined thresholds or unexpected state transitions occur [^evt-wg-workflows-and-process-integration-pr-42].
3. **Autonomous Execution Phase**: Fully autonomous execution bounded by deterministic policy checks and telemetry logging.

### Boundary Constraints
- **Exclusion of Hard Constraints**: Workflows governed by external legal, regulatory, or organizational mandates cannot graduate out of human oversight; these must remain fixed as a [Hard Constraint Gate](hard-constraint-gate.md) [^evt-wg-workflows-and-process-integration-pr-42].

# References

- [Hard Constraint Human-in-the-Loop Gate](hard-constraint-gate.md)
- [Human Approval Gate](human-approval-gate.md)
- [Bounded Autonomous Remediation](../architectures/bounded-autonomous-remediation.md)

[^evt-wg-workflows-and-process-integration-pr-42]: https://github.com/aaif/wg-workflows-and-process-integration/pull/42
