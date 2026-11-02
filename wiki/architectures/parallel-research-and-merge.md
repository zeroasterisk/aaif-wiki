---
type: architecture
title: Parallel Research and Merge Reference Architecture
description: Multi-agent reference architecture coordinating concurrent, isolated
  subagent research across disparate domains before merging findings into a unified
  output.
resource: https://github.com/aaif/wg-workflows-and-process-integration/issues/55
tags:
- workflows
- multi-agent
- orchestration
- reference-architecture
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:21:01.683717+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-issue-55
  resource: https://github.com/aaif/wg-workflows-and-process-integration/issues/55
  author: mzagar
  last_modified: '2026-10-10T01:10:11+00:00'
---

# Overview

The Parallel Research and Merge reference architecture governs multi-agent workflows where independent subagents concurrently execute targeted information gathering, synthesis, or analysis tasks without direct inter-agent communication, returning artifacts to a centralized coordinator for consolidation [^evt-wg-workflows-and-process-integration-issue-55].

# Architecture / Specification

The architecture defines distinct execution phases:
1. **Task Partitioning**: A primary coordinating agent or runtime decomposes an analytical objective into distinct research tasks.
2. **Isolated Concurrency**: Subagents operate in parallel execution envelopes with isolated context windows and independent tool access, maintaining separation without direct agent-to-agent signaling [^evt-wg-workflows-and-process-integration-issue-55].
3. **Result Reconciliation**: Completed research outputs are aggregated and merged through deterministic acceptance criteria or synthesizer models, detecting contradictions across concurrent branches.

# Lifecycle History

Initiated by the Workflows and Process Integration Working Group following consensus in architectural sync meetings to establish baseline reference architectures for non-communicating parallel subagents prior to complex multi-agent dialog patterns [^evt-wg-workflows-and-process-integration-issue-55].

# References

- [Parallel Fan-Out and Join](../patterns/parallel-fan-out-and-join.md)
- [Branch Isolation](../patterns/branch-isolation.md)
- [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md)

[^evt-wg-workflows-and-process-integration-issue-55]: https://github.com/aaif/wg-workflows-and-process-integration/issues/55
