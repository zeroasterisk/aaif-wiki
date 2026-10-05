---
type: pattern
title: Autonomy Graduation
description: Lifecycle pattern governing the progressive relaxation of human oversight
  from active approval gates to exception escalation as empirical reliability is demonstrated.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/42
tags:
- lifecycle
- hitl
- autonomy
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
Autonomy Graduation is a workflow deployment pattern that models the progressive evolution of human oversight over an agentic system as empirical performance, verification data, and operational trust accumulate.[^evt-wg-workflows-and-process-integration-pr-42] The graduation progression transitions operational checkpoints through defined oversight tiers while holding structural regulatory constraints static.[^evt-wg-workflows-and-process-integration-pr-42]

# Architecture / Specification
Autonomy Graduation models the operational maturity of agent tasks across three canonical phases:[^evt-wg-workflows-and-process-integration-pr-42]
1. **Approval Gate**: Every agent execution or proposal requires explicit human sign-off prior to state mutation (see [Human Approval Gate](./human-approval-gate.md)).[^evt-wg-workflows-and-process-integration-pr-42]
2. **Exception Escalation**: The agent executes autonomously within bounded parameters, pausing and alerting an operator only when uncertainty metrics, invariant violations, or policy exceptions occur.[^evt-wg-workflows-and-process-integration-pr-42]
3. **Autonomous Execution (None)**: Routine execution proceeds without real-time human intervention, relying on downstream asynchronous audit trails and deterministic bounds.[^evt-wg-workflows-and-process-integration-pr-42]

### Invariants
- **Exclusion of Hard Constraints**: Structural, regulatory, or statutory requirements (such as clinical signatures or fiduciary thresholds) are classified under [Hard Constraint Gate](./hard-constraint-gate.md) and are permanently barred from graduating to exception-only or autonomous tiers.[^evt-wg-workflows-and-process-integration-pr-42]
- **Evidence-Based Progression**: Transitioning between graduation tiers requires empirical validation against predefined accuracy, deterministic checks, and safety metrics.[^evt-wg-workflows-and-process-integration-pr-42]

# Lifecycle History
Introduced in the Workflows and Process Integration Working Group classification schema to formalize enterprise deployment lifecycles and disambiguate graduated trust from fixed compliance gates.[^evt-wg-workflows-and-process-integration-pr-42]

[^evt-wg-workflows-and-process-integration-pr-42]: https://github.com/aaif/wg-workflows-and-process-integration/pull/42
