---
type: reference-architecture
title: Agent-to-Tool CLI Boundary Observability
description: Observability architecture specifying context propagation, span ownership,
  and telemetry capture across the Agent-to-Tool semantic boundary realized via local
  CLI subprocesses.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/35
tags:
- observability
- opentelemetry
- cli
- tools
- distributed-tracing
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:11:45.448655+00:00'
sources:
- id: evt-wg-observability-and-traceability-pr-35
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/35
  author: fangxiu-wf
  last_modified: '2026-09-19T04:53:44+00:00'
- id: evt-wg-observability-and-traceability-issue-29
  resource: https://github.com/aaif/wg-observability-and-traceability/issues/29
  author: 91pavan
  last_modified: '2026-09-19T04:53:41+00:00'
---

# Overview
The Agent-to-Tool CLI Boundary reference architecture formalizes observability across the transition between an agent execution runtime and local CLI tool subprocesses [^evt-wg-observability-and-traceability-pr-35]. It distinguishes the canonical semantic Agent-to-Tool interaction from the operational Agent Runtime to Local Process boundary that executes it [^evt-wg-observability-and-traceability-pr-35].

# Architecture / Specification
The realization maps eight cross-boundary observability dimensions across execution layers [^evt-wg-observability-and-traceability-pr-35]:
- **Context Propagation**: Employs W3C Trace Context and W3C Baggage propagated through process boundaries using the OpenTelemetry environment-variable context carrier specification [^evt-wg-observability-and-traceability-pr-35].
- **Span Ownership and Composition**: Coordinates `execute_tool` spans from the agent runtime with subprocess CLI caller spans. Pre-execution span-ID reservation enables child processes to attach telemetry deterministically to runtime-managed parent contexts [^evt-wg-observability-and-traceability-pr-35].
- **Asynchronous Execution**: Distinguishes synchronous child invocations from detached or background jobs, linking the latter via OpenTelemetry Span Links rather than strict parent-child nesting [^evt-wg-observability-and-traceability-pr-35].
- **Evidence Integrity**: Treats telemetry authenticity as a cross-cutting concern to reconcile declared tool actions against independent operational telemetry [^evt-wg-observability-and-traceability-pr-35] [^evt-wg-observability-and-traceability-issue-29].

This architecture integrates with standard OpenTelemetry pipelines defined in [OpenTelemetry SDK Instrumentation](../reference-architectures/opentelemetry.md) and relates to foundational definitions in [Core Workflow Terms](../taxonomy/core-workflow-terms.md) [^evt-wg-observability-and-traceability-pr-35].

# References
- [AAIF Observability & Traceability Working Group](../working-groups/observability-and-traceability.md)
- [OpenTelemetry Reference Architecture](../reference-architectures/opentelemetry.md)

[^evt-wg-observability-and-traceability-issue-29]: https://github.com/aaif/wg-observability-and-traceability/issues/29
[^evt-wg-observability-and-traceability-pr-35]: https://github.com/aaif/wg-observability-and-traceability/pull/35
