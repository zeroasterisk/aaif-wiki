---
type: standard
title: Agent Behavior Trace Model
description: Open telemetry and correlation framework capturing causal agent execution,
  tool invocations, approval gates, and multi-turn conversational intervals across
  distributed systems.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/71
tags:
- observability
- opentelemetry
- tracing
- telemetry
- agent-behavior
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:33:38.696754+00:00'
sources:
- id: evt-wg-observability-and-traceability-pr-71
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/71
  author: mr-lee
  last_modified: '2026-11-02T02:43:16+00:00'
- id: evt-wg-observability-and-traceability-pr-72
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/72
  author: mr-lee
  last_modified: '2026-11-02T02:43:22+00:00'
---

# Overview

The Agent Behavior Trace Model is an open telemetry and tracing specification developed by the [Observability and Traceability WG](../working-groups/observability-and-traceability.md) to define standard instrumentation, span hierarchies, and semantic conventions for agent execution.[^evt-wg-observability-and-traceability-pr-71] It extends core OpenTelemetry distributed tracing standards to capture autonomous loops, external tool calls, human checkpoints, and execution turns across heterogeneous agent runtimes.[^evt-wg-observability-and-traceability-pr-72]

# Architecture / Specification

### OpenTelemetry Integration Gaps

The model establishes solutions for seven documented operational gaps observed across coding agents, agent SDKs, and AI gateways using OpenTelemetry semantic conventions:[^evt-wg-observability-and-traceability-pr-71]

1. Missing standard conventions for autonomous multi-step loops.
2. Inconsistent interpretation of agent-to-agent boundaries and parent-child span linking.
3. Non-adoption of standard attributes across proprietary model gateway proxies.
4. Instrumentation defects leading to broken causal graphs during asynchronous delegate dispatch.
5. Incomplete contextual attribution for tool execution results and transient sandbox side-effects.
6. Fragmented representation of human-in-the-loop pause and resumption events.
7. Uncorrelated cost, token usage, and latency attribution across federated subagent swarms.

### Turn and Step Modeling

To align agent execution traces with conversational and operational lifecycles, the model specifies standardized hierarchical intervals for upstream inclusion in the OpenTelemetry GenAI Special Interest Group (SIG):[^evt-wg-observability-and-traceability-pr-72]

- **Turn**: A high-level interaction interval bounded by an incoming trigger or user intent and the delivery of a terminal response or handoff.
- **Agent Step** (aliased as **Step**): A discrete operational iteration within a turn comprising reasoning, action proposal, and execution dispatch.
- **Turn Segment**: An OpenTelemetry-specific span unit demarcating streaming chunks or sub-phases within a turn.

Formal inclusion of Turn and Agent Step within shared AAIF vocabularies coordinates through term sheets in the [Taxonomy and Landscape Workstream](../working-groups/taxonomy-and-landscape.md).[^evt-wg-observability-and-traceability-pr-72]

# Lifecycle History

- **October 2026**: Added working document gap analysis detailing seven telemetry deficiencies across coding agents and SDKs.[^evt-wg-observability-and-traceability-pr-71]
- **October 2026**: Formulated turn and agent step proposal (`AGENT-BEHAVIOR-TRACE-MODEL-TURN.md`) scheduled for upstream review with the OpenTelemetry GenAI SIG.[^evt-wg-observability-and-traceability-pr-72]

# References

- [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md)
- [Taxonomy and Landscape Workstream](../working-groups/taxonomy-and-landscape.md)
- [OpenTelemetry Reference Architecture](../resources/opentelemetry.md)

[^evt-wg-observability-and-traceability-pr-71]: https://github.com/aaif/wg-observability-and-traceability/pull/71
[^evt-wg-observability-and-traceability-pr-72]: https://github.com/aaif/wg-observability-and-traceability/pull/72
