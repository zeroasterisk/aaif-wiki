---
type: standard
title: Agent Behavior Trace Model Specification
description: Open telemetry standard defining execution context propagation, causal
  execution tracing, and turn-based decision reconciliation.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/71
tags:
- observability
- opentelemetry
- tracing
- agent-behavior
- standards
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:32:44.481487+00:00'
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
The Agent Behavior Trace Model is an open telemetry standard defining portable execution context propagation, causal execution tracing, and decision-to-action reconciliation across AI agent harnesses, multi-agent orchestrations, and tool boundaries.[^evt-wg-observability-and-traceability-pr-71] Governed by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), it aligns agent-specific operational concepts with the [OpenTelemetry](../resources/opentelemetry.md) ecosystem.[^evt-wg-observability-and-traceability-pr-71][^evt-wg-observability-and-traceability-pr-72]

# Architecture / Specification
The specification formalizes execution semantics across agent lifecycles:

- **Turn and Step Execution Model**: Defines a normalized turn structure and downstream execution units for agent interaction cycles.[^evt-wg-observability-and-traceability-pr-72] The model formalizes the concepts of a "Turn" and "Agent step" (with "Step" as an alias) for vocabulary alignment, while preserving "Turn segment" as an OpenTelemetry span construct to structure upstream GenAI Special Interest Group (SIG) proposals.[^evt-wg-observability-and-traceability-pr-72]
- **Telemetry Gap Analysis**: Identifies seven foundational gaps in how contemporary coding agents, agent SDKs, and AI gateways adopt OpenTelemetry semantic conventions.[^evt-wg-observability-and-traceability-pr-71] These encompass missing semantic conventions, divergent span interpretation issues, unadopted existing conventions, and instrumentation defects across runtime boundaries.[^evt-wg-observability-and-traceability-pr-71]

# Lifecycle History
In October 2026, the working group introduced working documents covering the seven-part OpenTelemetry gap analysis ([PR #71](https://github.com/aaif/wg-observability-and-traceability/pull/71)) and the turn proposal specification ([PR #72](https://github.com/aaif/wg-observability-and-traceability/pull/72)) to coordinate upstream alignment with the OpenTelemetry GenAI SIG.[^evt-wg-observability-and-traceability-pr-71][^evt-wg-observability-and-traceability-pr-72]

[^evt-wg-observability-and-traceability-pr-71]: https://github.com/aaif/wg-observability-and-traceability/pull/71
[^evt-wg-observability-and-traceability-pr-72]: https://github.com/aaif/wg-observability-and-traceability/pull/72
