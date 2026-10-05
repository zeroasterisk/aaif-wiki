---
type: pattern
title: Human Approval Gate
description: Workflow architecture pattern requiring an authorized, uniquely identified
  human to explicitly approve an agent-generated proposal before execution.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/42
tags:
- hitl
- approval
- workflow-pattern
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:46:04.724106+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-pr-42
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/42
  author: askulkarni2
  last_modified: '2026-09-24T01:00:06+00:00'
---

# Overview
The Human Approval Gate is a workflow pattern requiring an authorized, uniquely identified human to explicitly inspect, validate, and approve an agent-generated proposal before any side-effecting action is committed to production state.[^evt-wg-workflows-and-process-integration-pr-42] It serves as a capability-verification and risk-mitigation checkpoint during early deployment stages.[^evt-wg-workflows-and-process-integration-pr-42]

# Architecture / Specification
A Human Approval Gate intercepts proposals produced by probabilistic agent runs and pauses execution via [Durable Wait](./durable-wait.md) until a valid approval token is recorded.[^evt-wg-workflows-and-process-integration-pr-42]

### Distinction from Hard Constraints
Within the AAIF workflow taxonomy, Human Approval Gates represent confidence-driven checkpoints established because an agent system is not yet fully trusted to operate autonomously.[^evt-wg-workflows-and-process-integration-pr-42] As empirical reliability metrics meet target thresholds, approval gates may transition through [Autonomy Graduation](./autonomy-graduation.md) into exception-based escalation.[^evt-wg-workflows-and-process-integration-pr-42]

In contrast, requirements rooted in statutory mandates, legal certifications, or enterprise policy are modeled as [Hard Constraint Gate](./hard-constraint-gate.md) patterns, which are non-negotiable and cannot be relaxed through autonomy graduation.[^evt-wg-workflows-and-process-integration-pr-42]

# Lifecycle History
Updated to reflect the Workflows and Process Integration Working Group classification schema distinguishing transitional approval gates from permanent hard constraints.[^evt-wg-workflows-and-process-integration-pr-42]

[^evt-wg-workflows-and-process-integration-pr-42]: https://github.com/aaif/wg-workflows-and-process-integration/pull/42
