---
type: taxonomy
title: Workflow Primitives
description: Canonical building-block vocabulary (P1–P19) defining execution steps,
  boundary contracts, triggers, and control gates across agentic workflows.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/29
tags:
- taxonomy
- workflows
- primitives
- architecture
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:15:25.259758+00:00'
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
Workflow primitives provide a vendor-neutral, canonical vocabulary (P1 through P19) defining structural execution units, boundary contracts, and control flows for agentic process architectures.[^evt-wg-workflows-and-process-integration-pr-29] Developed by the [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md), these primitives serve as foundational building blocks for both single-agent and multi-agent reference architectures.[^evt-wg-workflows-and-process-integration-pr-29]

# Architecture / Specification
The primitive vocabulary formalizes reusable components and cross-boundary contracts:

- **Core Primitives (P1–P19)**: Standardized functional units including `Trigger`, `AgentStep`, `Budget`, and `Handoff` that compose complex agent execution paths.[^evt-wg-workflows-and-process-integration-pr-29]
- **Single-Agent Human Approval Profile**: Reference architectures such as [Single-Agent Human Approval](../architectures/single-agent-human-approval.md) utilize a dedicated 12-primitive subset (P1 through P12) to structure approval gates, verification checkpoints, and execution isolation.[^evt-wg-workflows-and-process-integration-pr-54]
- **Boundary Contracts**: Explicit data and state transition specifications, including the `AgentStep` boundary contract and formal `Handoff` requirements that each primitive-crossing step must satisfy.[^evt-wg-workflows-and-process-integration-pr-29]
- **Topological Assemblies**: Primitives compose into defined multi-agent structural topologies (T1 through T6) governing fan-out, delegation, and consolidation patterns.[^evt-wg-workflows-and-process-integration-pr-29]

# Lifecycle History
The Workflows and Process Integration Working Group drafted the P1–P19 primitive catalog alongside boundary contracts and supporting topology guidance to establish common execution semantics across AAIF workflow architectures.[^evt-wg-workflows-and-process-integration-pr-29][^evt-wg-workflows-and-process-integration-pr-54]

[^evt-wg-workflows-and-process-integration-pr-29]: https://github.com/aaif/wg-workflows-and-process-integration/pull/29
[^evt-wg-workflows-and-process-integration-pr-54]: https://github.com/aaif/wg-workflows-and-process-integration/pull/54
