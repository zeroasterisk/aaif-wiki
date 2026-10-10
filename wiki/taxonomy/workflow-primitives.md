---
type: taxonomy
title: Workflow Primitives
description: Standardized vocabulary of modular workflow building blocks, boundary
  contracts, and handoff specifications for single- and multi-agent reference architectures.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/29
tags:
- workflows
- primitives
- orchestration
- reference-architectures
- contracts
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:20:41.806737+00:00'
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

Workflow Primitives are the standardized, modular building blocks defined by the [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md) to compose reliable single-agent and multi-agent systems.[^evt-wg-workflows-and-process-integration-pr-29] Designated across catalog series (P1 through P19), these primitives define discrete functional roles such as Triggers, AgentSteps, Budgets, and Handoffs, enabling formal composition according to foundational [workflow architecture principles](../guidelines/workflow-architecture-principles.md).[^evt-wg-workflows-and-process-integration-pr-29][^evt-wg-workflows-and-process-integration-pr-54]

Each primitive crossing is governed by rigorous interface contracts to enforce predictable execution, state continuity, and policy compliance across system boundaries.[^evt-wg-workflows-and-process-integration-pr-29]

# Architecture / Specification

The primitive framework standardizes workflow mechanics across reference architectures, including [single-agent human approval architectures](../architectures/single-agent-human-approval.md) and multi-agent topology patterns (T1–T6):[^evt-wg-workflows-and-process-integration-pr-29][^evt-wg-workflows-and-process-integration-pr-54]

- **Primitive Vocabulary (P1–P19)**: Identifies atomic workflow components including invocation triggers, autonomous agent steps, constraint evaluators, budget limits, human intervention gates, and delegation handoffs.[^evt-wg-workflows-and-process-integration-pr-29]
- **AgentStep Boundary Contracts**: Defines deterministic input/output schemas and execution invariants required whenever an agent step is executed.
- **Handoff Contracts**: Specifies state transfer, context propagation, and authorization invariants required when transferring execution responsibility between autonomous agents or between agents and human operators.[^evt-wg-workflows-and-process-integration-pr-29]

# Lifecycle History

- **2026-08**: Workflows & Process Integration WG introduced the primitive-based architecture drafts and supporting contracts (PR #29, PR #54).[^evt-wg-workflows-and-process-integration-pr-29][^evt-wg-workflows-and-process-integration-pr-54]

[^evt-wg-workflows-and-process-integration-pr-29]: https://github.com/aaif/wg-workflows-and-process-integration/pull/29
[^evt-wg-workflows-and-process-integration-pr-54]: https://github.com/aaif/wg-workflows-and-process-integration/pull/54
