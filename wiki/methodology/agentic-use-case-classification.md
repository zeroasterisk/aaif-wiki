---
type: methodology
title: Agentic Use Case Classification Framework
description: Classification framework and evidentiary methodology for cataloging production
  agentic workflows and execution structures.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/47
tags:
- methodology
- workflows
- use-cases
- classification
- taxonomy
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T10:08:50.194494+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-pr-47
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/47
  author: kevintelus
  last_modified: '2026-09-15T14:22:31+00:00'
---

# Overview
The Agentic Use Case Classification Framework provides structured criteria for inventorying, classifying, and comparing real-world agentic workflows developed across industry sectors [^evt-wg-workflows-and-process-integration-pr-47]. Curated by the [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md), it maps workflow topology, coordination patterns, autonomy levels, and validation mechanics into standardized schema fields.

# Architecture / Specification

## Topology and Execution Dimensions
The schema evaluates agentic use cases across structural execution dimensions:
- **Workflow Pattern Type**: Distinguishes sequential pipelines, parallel fan-out orchestrations, routing networks, and autonomous loops.
- **Autonomy and Human Control**: Classifies interaction models across automated, human-in-the-loop, and supervisory topologies.
- **Artifact and State Handoff**: Captures how state, prompts, tool outputs, and context transfer between participating agents.

## Open Architectural Debates
An ongoing discussion in the use case classification schema addresses ambiguous boundaries between `Parallel fan-out` (defined by concurrent sub-task timing) and `Sequential pipeline` (defined by activity dependencies where each step feeds the next) [^evt-wg-workflows-and-process-integration-pr-47]. Working group members are evaluating three candidate classification interpretations [^evt-wg-workflows-and-process-integration-pr-47]:
1. **Observed Timing**: Classifying based strictly on whether execution occurs concurrently or sequentially in time.
2. **Agent / Worker Count**: Distinguishing based on whether single or multi-agent instances participate concurrently.
3. **Data and Activity Dependency**: Classifying based solely on dependency graphs and state handoff topologies regardless of runtime concurrency.

# References
- [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md)
- [Agentic Workflow Orchestration Patterns](../methodology/agentic-workflow-orchestration-patterns.md)
- [Job-Oriented Reference Architectures](../methodology/job-oriented-reference-architectures.md)

[^evt-wg-workflows-and-process-integration-pr-47]: https://github.com/aaif/wg-workflows-and-process-integration/pull/47
