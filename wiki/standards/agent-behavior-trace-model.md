---
type: standard
title: Agent Behavior Trace Model
description: Telemetry specification and causal execution trace standard defining
  turn boundaries and cross-boundary agent observations.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/60
tags:
- aaif
- observability
- opentelemetry
- tracing
- standards
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T03:11:37.577005+00:00'
sources:
- id: evt-wg-observability-and-traceability-pr-60
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/60
  author: mr-lee
  last_modified: '2026-09-30T16:55:49+00:00'
---

# Overview

The Agent Behavior Trace Model is an open telemetry specification developed by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) to define turn boundaries, causal execution graphs, and runtime behavior tracking across agentic workflows [^evt-wg-observability-and-traceability-pr-60]. The model establishes vendor-neutral telemetry conventions that map multi-turn agent deliberation, tool calls, and delegated task handoffs into structured trace events [^evt-wg-observability-and-traceability-pr-60].

# Architecture / Specification

The trace model development lifecycle is structured around four sequential, evidence-first execution phases [^evt-wg-observability-and-traceability-pr-60]:

- **Phase 1 (Agree)**: Align on core dimensions, milestone scope definitions, and evaluation metrics [^evt-wg-observability-and-traceability-pr-60].
- **Phase 2 (Evidence)**: Empirical capture and analysis of telemetry emitted by production agent frameworks, utilizing [Goose](../resources/goose.md) as the initial reference implementation [^evt-wg-observability-and-traceability-pr-60].
- **Phase 3 (Interpret)**: Maintain a shared register of observed telemetry gaps, inconsistent OpenTelemetry GenAI semantic convention implementations, and missing behavioral attributes [^evt-wg-observability-and-traceability-pr-60].
- **Phase 4 (Contribute)**: Formulate formal OpenTelemetry upstream proposals and Foundation trace specifications backed by validated runtime traces [^evt-wg-observability-and-traceability-pr-60].

# Lifecycle History

In September 2026, the working group restructured the project's execution plan from parallel theoretical tracks to a four-phase evidence-driven methodology anchored by an empirical gap register and a Goose reference implementation [^evt-wg-observability-and-traceability-pr-60].

[^evt-wg-observability-and-traceability-pr-60]: https://github.com/aaif/wg-observability-and-traceability/pull/60
