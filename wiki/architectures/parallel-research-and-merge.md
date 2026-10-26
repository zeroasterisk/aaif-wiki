---
type: architecture
title: Parallel Research and Merge
description: Multi-agent reference architecture coordinating concurrent, isolated
  subagent research across disparate sources and reconciling findings into a unified,
  referenced report.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/56
tags:
- workflow
- multi-agent
- orchestration
- research
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T11:08:56.885758+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-pr-56
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/56
  author: mzagar
  last_modified: '2026-10-23T06:14:16+00:00'
---

# Overview
The Parallel Research and Merge reference architecture coordinates multiple subagents researching separate sources concurrently and synthesizing their findings into a single structured report with source citations.[^evt-wg-workflows-and-process-integration-pr-56]

# Architecture / Specification
The architecture addresses information retrieval across distributed or heterogeneous sources where sequential processing induces latency and shared context windows cause token bloat.[^evt-wg-workflows-and-process-integration-pr-56] The workflow executes through three main phases:

1. **Query Partitioning and Dispatch**: An orchestrator decomposes a compound question into independent research subtasks, initiating concurrent execution branches via [Parallel Fan-Out and Join](../patterns/parallel-fan-out-and-join.md).[^evt-wg-workflows-and-process-integration-pr-56]
2. **Isolated Source Investigation**: Dedicated subagents conduct investigations within segregated environments governed by [Branch Isolation](../patterns/branch-isolation.md), gathering evidence and citing source records independently.[^evt-wg-workflows-and-process-integration-pr-56]
3. **Synthesis and Merge**: An aggregation agent combines findings across completed branches, reconciles discrepancies, surfaces missing data points, and compiles the final report.[^evt-wg-workflows-and-process-integration-pr-56]

The architecture relies on [Durable Wait](../patterns/durable-wait.md) for handling long-polling source queries and adheres to [Proposal-Execution Split](../patterns/proposal-execution-split.md) for boundary enforcement.[^evt-wg-workflows-and-process-integration-pr-56]

[^evt-wg-workflows-and-process-integration-pr-56]: https://github.com/aaif/wg-workflows-and-process-integration/pull/56
