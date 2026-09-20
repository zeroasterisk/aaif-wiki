---
type: deliverable
title: Agentic AI Workflow Orchestration Patterns Comparison
description: A comparative reference matrix evaluating agentic AI workflow orchestration
  patterns across complexity, agency levels, and enterprise operational considerations.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/docs/agentic-workflow-patterns-comparison.md
tags:
- workflows
- orchestration
- patterns
- comparative-analysis
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:56:41.343367+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-d47ac6a6752f-a44a75ab
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/docs/agentic-workflow-patterns-comparison.md
  author: Mario Zagar
  last_modified: '2026-08-25T07:58:21-07:00'
---

# Overview

The Agentic AI Workflow Orchestration Patterns Comparison is a reference deliverable from the Workflows and Process Integration Working Group (`../working-groups/workflows-and-process-integration.md`) synthesizing workflow patterns from AWS, Microsoft Azure, Google Cloud, and Anthropic documentation[^evt-wg-workflows-and-process-integration-file-d47ac6a6752f-a44a75ab]. The deliverable classifies patterns by agency level and implementation complexity to guide practitioners in choosing appropriate orchestration topologies[^evt-wg-workflows-and-process-integration-file-d47ac6a6752f-a44a75ab].

# Architecture / Specification

The comparative catalog organizes recurring workflow patterns into complexity and agency tiers[^evt-wg-workflows-and-process-integration-file-d47ac6a6752f-a44a75ab]:

- **Low Complexity & Minimal/Low Agency**: LLM-Augmented Workflow, Single-Agent ReAct, Routing/Triage, and Sequential Prompt Chaining.
- **Medium Complexity & Moderate Agency**: Sequential Multi-Agent Pipelines, Parallel Fan-out/Fan-in, Iterative Loops, and Review & Critique (Maker-Checker).
- **High/Very High Complexity & Autonomous Agency**: Coordinator/Orchestrator-Workers, Autonomous ReAct Loops, Hierarchical Task Decomposition, Multi-Agent Swarms/Roundtables, and Hybrid Plan & Solve engines.
- **Control and Governance Overlays**: Human-in-the-Loop (HITL) approval gates (`../specification/human-approval-gate.md`) and deterministic custom logic integrations.

### Selection Guidance

The matrix outlines selection heuristics based on subtask determinism, debugging requirements, tool count, and multi-perspective consensus needs[^evt-wg-workflows-and-process-integration-file-d47ac6a6752f-a44a75ab].

[^evt-wg-workflows-and-process-integration-file-d47ac6a6752f-a44a75ab]: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/docs/agentic-workflow-patterns-comparison.md
