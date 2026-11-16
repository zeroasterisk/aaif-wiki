---
type: taxonomy
title: Workflow Primitives
description: Structural vocabulary and modular execution primitives standardizing
  agent task boundaries, execution steps, budgets, and handoff contracts.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/29
tags:
- workflows
- primitives
- taxonomy
- orchestration
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:26:49.093110+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-pr-29
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/29
  author: praneeth2k3
  last_modified: '2026-10-06T15:45:22+00:00'
- id: evt-wg-workflows-and-process-integration-pr-54
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/54
  author: praneeth2k3
  last_modified: '2026-10-06T03:09:10+00:00'
---

# Overview
Workflow primitives provide a foundational, composable vocabulary and structural execution building blocks defined by the Workflows and Process Integration Working Group [^evt-wg-workflows-and-process-integration-pr-29]. The catalog standardizes common operational units—such as triggers, agent steps, execution budgets, and handoffs—enabling consistent cross-architecture composition across single-agent and multi-agent reference systems [^evt-wg-workflows-and-process-integration-pr-29].

# Architecture / Specification
The primitive framework organizes workflow execution across modular categories and boundary contracts [^evt-wg-workflows-and-process-integration-pr-29]:

- **Primitive Catalog (P1–P19)**: Identifies shared runtime building blocks including `Trigger`, `AgentStep`, `Budget`, and `Handoff` [^evt-wg-workflows-and-process-integration-pr-29]. A subset (P1–P12) specifically defines the core control loop for single-agent systems incorporating human approval checkpoints [^evt-wg-workflows-and-process-integration-pr-54].
- **Boundary Contracts**: Defines strict invariant contracts across primitive transitions, specifically mandating schema satisfaction for the `AgentStep` boundary and `Handoff` interfaces [^evt-wg-workflows-and-process-integration-pr-29].
- **Multi-Agent Topologies (T1–T6)**: Standardizes execution network topologies that route inter-agent communication, coordinating with patterns like [parallel-fan-out-and-join](../patterns/parallel-fan-out-and-join.md) and [branch-isolation](../patterns/branch-isolation.md) [^evt-wg-workflows-and-process-integration-pr-29].

# Lifecycle History
Originally drafted as part of the foundational taxonomy for the Workflows and Process Integration WG, the primitive set was expanded under draft PR #29 to formalize the P1–P19 catalog, contracts, and multi-agent topologies [^evt-wg-workflows-and-process-integration-pr-29]. PR #54 subsequently mapped primitives P1–P12 directly into the [single-agent-human-approval](../architectures/single-agent-human-approval.md) reference architecture [^evt-wg-workflows-and-process-integration-pr-54].

# References
- Workflows and Process Integration Working Group: [working-groups/workflows-and-process-integration](../working-groups/workflows-and-process-integration.md)
- Single-Agent Human Approval: [architectures/single-agent-human-approval](../architectures/single-agent-human-approval.md)

[^evt-wg-workflows-and-process-integration-pr-29]: https://github.com/aaif/wg-workflows-and-process-integration/pull/29
[^evt-wg-workflows-and-process-integration-pr-54]: https://github.com/aaif/wg-workflows-and-process-integration/pull/54
