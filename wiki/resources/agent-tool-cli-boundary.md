---
type: resource
title: Agent-to-Tool CLI Subprocess Boundary
description: Observability reference matrix and telemetry propagation model analyzing
  the direct agent-to-tool local CLI subprocess boundary.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/35
tags:
- observability
- opentelemetry
- subprocesses
- cli
- traceability
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:27:28.310990+00:00'
sources:
- id: evt-wg-observability-and-traceability-pr-35
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/35
  author: fangxiu-wf
  last_modified: '2026-09-19T04:53:44+00:00'
---

# Overview
The Agent-to-Tool CLI subprocess boundary analyzes telemetry propagation and causality modeling between an AI agent runtime and a tool executed as a local subprocess [^evt-wg-observability-and-traceability-pr-35]. This specification distinguishes between the canonical `Agent → Tool` semantic interaction and the underlying `Agent Runtime → Local Process` operational boundary that realizes it in local environments [^evt-wg-observability-and-traceability-pr-35].

# Architecture / Specification
The boundary realization addresses context propagation, span hierarchy, and telemetry alignment across process forks:

- **Context Carrier**: Utilizes the OpenTelemetry Release Candidate specification for environment variables (`TRACEPARENT`, `TRACESTATE`, and `BAGGAGE`) to propagate W3C Trace Context and Baggage across process boundaries [^evt-wg-observability-and-traceability-pr-35].
- **Span Composition**: Differentiates between runtime-level `execute_tool` spans and CLI process execution spans, addressing whether the agent runtime suppresses, nests, or shares spans during direct command execution [^evt-wg-observability-and-traceability-pr-35].
- **Pre-execution Span-ID Reservation**: Implements pre-execution span-ID reservation—validated in the LoongSuite pilot—enabling parent spans to register deterministic trace relationships prior to executing the tool binary [^evt-wg-observability-and-traceability-pr-35].
- **Detached and Asynchronous Work**: Recommends OpenTelemetry Span Links over direct parent-child causality when tools execute detached or asynchronous background tasks [^evt-wg-observability-and-traceability-pr-35].
- **Resource Bootstrap**: Isolates process-level OpenTelemetry resource bootstrap from invocation-level carrier contexts [^evt-wg-observability-and-traceability-pr-35].

# Lifecycle History
The boundary model was introduced by the Observability and Traceability Working Group in PR #35 as the initial concrete matrix pass addressing direct tool invocation gaps identified in issue #29 [^evt-wg-observability-and-traceability-pr-35]. It links to broader cross-boundary telemetry mapping in [Cross-Boundary Observability Model](../resources/cross-boundary-observability-model.md).

[^evt-wg-observability-and-traceability-pr-35]: https://github.com/aaif/wg-observability-and-traceability/pull/35
