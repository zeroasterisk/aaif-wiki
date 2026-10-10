---
type: resource
title: Agentic AI Workflow Patterns Comparison
description: Comparative taxonomy and operational analysis evaluating agentic workflow
  orchestration patterns, complexity tiers, and agency levels across major AI ecosystems.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/docs/agentic-workflow-patterns-comparison.md
tags:
- resources
- workflows
- orchestration
- patterns
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T14:59:02.868270+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-d47ac6a6752f-a44a75ab
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/docs/agentic-workflow-patterns-comparison.md
  author: Mario Zagar
  last_modified: '2026-08-25T07:58:21-07:00'
- id: evt-wg-workflows-and-process-integration-pr-33
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/33
  author: mzagar
  last_modified: '2026-08-25T14:58:22+00:00'
---

# Overview
The Agentic AI Workflow Patterns Comparison is a reference analysis cataloging agentic workflow design patterns across AWS, Azure, Google Cloud, and Anthropic architectures[^evt-wg-workflows-and-process-integration-file-d47ac6a6752f-a44a75ab]. It classifies patterns by agency level, operational complexity, cost implications, and control guarantees to assist engineers in selecting appropriate workflow topologies[^evt-wg-workflows-and-process-integration-file-d47ac6a6752f-a44a75ab].

# Architecture / Specification
The resource categorizes patterns across standard orchestration tiers[^evt-wg-workflows-and-process-integration-file-d47ac6a6752f-a44a75ab]:
- **Augmented and Deterministic**: Prompt Chaining, Routing, and LLM-Augmented Workflows featuring deterministic activity paths with model-driven classification and programmatic validation gates.
- **Autonomous & ReAct**: Single-Agent ReAct and autonomous loop patterns executing dynamic tool selection, memory lookups, and environmental feedback.
- **Multi-Agent Coordination**: Sequential pipelines, parallel fan-out/fan-in, coordinator-worker delegations, hierarchical task decompositions, and swarm debate roundtables.
- **Control & Review**: Review-and-critique loops, iterative refinement, and human-in-the-loop approval gates for safety and auditability.

Following working group conventions, workflow sub-steps are formally specified as activities to maintain alignment across the AAIF taxonomy[^evt-wg-workflows-and-process-integration-pr-33].

# References
- Maintained by the [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md)[^evt-wg-workflows-and-process-integration-file-d47ac6a6752f-a44a75ab].
- Aligned with [Workflow Architecture Principles](../guidelines/workflow-architecture-principles.md).

[^evt-wg-workflows-and-process-integration-file-d47ac6a6752f-a44a75ab]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/docs/agentic-workflow-patterns-comparison.md
[^evt-wg-workflows-and-process-integration-pr-33]: https://github.com/aaif/wg-workflows-and-process-integration/pull/33
