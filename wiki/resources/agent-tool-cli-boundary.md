---
type: resource
title: Agent-to-Tool CLI Boundary Model
description: Observability reference matrix and context propagation model analyzing
  direct agent subprocess invocations across CLI and tool execution spans.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/35
tags:
- observability
- tracing
- cli
- tools
- opentelemetry
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:01:05.181025+00:00'
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
The Agent-to-Tool CLI Boundary Model maps cross-boundary telemetry propagation and span semantics when an AI agent runtime invokes a local command-line interface (CLI) tool via a subprocess[^evt-wg-observability-and-traceability-pr-35]. It distinguishes the canonical semantic boundary (Agent → Tool) from the concrete operational realization (Agent Runtime → Local Process)[^evt-wg-observability-and-traceability-pr-35].

# Architecture / Specification
The model analyzes telemetry across eight cross-boundary dimensions: identity, context, relationship, lifecycle, outcome, provenance, security, and timing[^evt-wg-observability-and-traceability-pr-35].

Key architectural considerations include:
- **Context Propagation**: Employs the OpenTelemetry Release Candidate specification for environment-variable context carriers (`TRACEPARENT`, `TRACESTATE`) alongside W3C Trace Context and Baggage, formalizing local process carrier standards[^evt-wg-observability-and-traceability-pr-35].
- **Pre-execution Span-ID Reservation**: Validated via pilot implementation, where the agent runtime allocates span IDs prior to subprocess execution to bind asynchronous process launch records accurately[^evt-wg-observability-and-traceability-pr-35].
- **Span Composition and Detached Execution**: Distinguishes GenAI `execute_tool` spans from child CLI execution spans, utilizing OpenTelemetry Span Links instead of parent-child causal hierarchies when background or detached processes are executed[^evt-wg-observability-and-traceability-pr-35].
- **Evidence and Conformance**: Establishes an implementation-neutral conformance checklist addressing pre-execution context preparation, span ownership, and cross-cutting evidence integrity[^evt-wg-observability-and-traceability-pr-35].

# Lifecycle History
Developed under the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) as part of the broader cross-boundary observability gap model initiative[^evt-wg-observability-and-traceability-issue-29][^evt-wg-observability-and-traceability-pr-35].

[^evt-wg-observability-and-traceability-issue-29]: https://github.com/aaif/wg-observability-and-traceability/issues/29
[^evt-wg-observability-and-traceability-pr-35]: https://github.com/aaif/wg-observability-and-traceability/pull/35
