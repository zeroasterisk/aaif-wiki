---
type: taxonomy
title: Workflow Primitives
description: Standardized vocabulary of modular workflow building blocks, execution
  boundary contracts, and topology primitives for agentic systems.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/29
tags:
- taxonomy
- workflows
- primitives
- contracts
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:40:40.637301+00:00'
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

Workflow primitives are standardized building blocks and boundary contracts defined by the [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md) for assembling modular single-agent and multi-agent reference architectures[^evt-wg-workflows-and-process-integration-pr-29]. They establish vendor-neutral execution units covering triggers, operational budgets, discrete agent steps, and handoff boundaries[^evt-wg-workflows-and-process-integration-pr-29][^evt-wg-workflows-and-process-integration-pr-54].

# Architecture / Specification

The primitive framework formalizes workflow decomposition into reusable components and boundary guarantees[^evt-wg-workflows-and-process-integration-pr-29]:

- **Primitive Vocabulary (P1–P19)**: Modular execution units including triggers, agent execution steps (`AgentStep`), operational budget limits (`Budget`), and handoff transfers (`Handoff`).
- **Boundary Contracts**: Explicit invariants required whenever execution crosses primitive boundaries, specifically governing `AgentStep` inputs/outputs and cross-agent `Handoff` transitions[^evt-wg-workflows-and-process-integration-pr-29].
- **Multi-Agent Topologies (T1–T6)**: Structural shapes and routing topologies governing agent coordination, supervisor hierarchies, and peer-to-peer delegation flows[^evt-wg-workflows-and-process-integration-pr-29].
- **Approval Integration**: Specialized control subsets (P1–P12) integrating deterministic checks and human approval gates into single-agent workflows, as used in the [Single-Agent Human Approval Architecture](../architectures/single-agent-human-approval.md)[^evt-wg-workflows-and-process-integration-pr-54].

# Lifecycle History

The primitive catalog was drafted to unify the underlying components of single-agent and multi-agent reference architectures into a shared taxonomic baseline[^evt-wg-workflows-and-process-integration-pr-29][^evt-wg-workflows-and-process-integration-pr-54].

[^evt-wg-workflows-and-process-integration-pr-29]: https://github.com/aaif/wg-workflows-and-process-integration/pull/29
[^evt-wg-workflows-and-process-integration-pr-54]: https://github.com/aaif/wg-workflows-and-process-integration/pull/54
