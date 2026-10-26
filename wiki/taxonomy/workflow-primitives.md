---
type: taxonomy
title: Workflow Primitives
description: Standardized vocabulary of composable execution blocks and boundary contracts
  structuring single-agent and multi-agent reference architectures.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/29
tags:
- workflow
- primitives
- contracts
- taxonomy
- wg-workflows-and-process-integration
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T10:49:39.325201+00:00'
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
Workflow primitives are standardized, composable operational units and execution boundaries defined by the [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md) to serve as shared building blocks across single-agent and multi-agent reference architectures[^evt-wg-workflows-and-process-integration-pr-29]. Spanning an indexed catalog from P1 through P19, these primitives decouple architectural patterns from proprietary orchestrator frameworks and establish consistent execution semantics across system boundaries[^evt-wg-workflows-and-process-integration-pr-29].

By establishing explicit structural invariants across transitions, workflow primitives ensure that autonomous planning cycles, tool invocations, approval gates, and multi-agent delegations maintain verifiable state durability, resource budgets, and deterministic policy constraints[^evt-wg-workflows-and-process-integration-pr-29][^evt-wg-workflows-and-process-integration-pr-54].

# Architecture / Specification
The primitive vocabulary defines core workflow components, including fundamental building blocks such as `Trigger`, `AgentStep`, `Budget`, and `Handoff`[^evt-wg-workflows-and-process-integration-pr-29].

### Boundary Contracts
Every execution transition crossing a primitive threshold must satisfy formal boundary contracts[^evt-wg-workflows-and-process-integration-pr-29]:
- **AgentStep Boundary Contract**: Defines pre-condition validation, state isolation, and telemetry propagation requirements before and after individual autonomous agent iterations.
- **Handoff Contract**: Mandates schema validation, authorization verification, and execution context preservation whenever control transfers between agents or transitions to human reviewers.

### Topology and Reference Architecture Integration
Primitives are assembled to compose both single-agent and multi-agent architectures:
- **Single-Agent Patterns**: Employs primitives P1 through P12 to implement durable waits, validation gates, and approval structures in workflows such as [Single-Agent Human Approval](../architectures/single-agent-human-approval.md)[^evt-wg-workflows-and-process-integration-pr-54].
- **Multi-Agent Topologies**: Arranges primitives into six canonical multi-agent topological structures (T1 through T6) defining supervision hierarchies, peer handoffs, and swarm networks[^evt-wg-workflows-and-process-integration-pr-29].

# Lifecycle History
Drafted in the Workflows and Process Integration Working Group to bridge horizontal taxonomy efforts with actionable reference architectures and topology models[^evt-wg-workflows-and-process-integration-pr-29][^evt-wg-workflows-and-process-integration-pr-54].

[^evt-wg-workflows-and-process-integration-pr-29]: https://github.com/aaif/wg-workflows-and-process-integration/pull/29
[^evt-wg-workflows-and-process-integration-pr-54]: https://github.com/aaif/wg-workflows-and-process-integration/pull/54
