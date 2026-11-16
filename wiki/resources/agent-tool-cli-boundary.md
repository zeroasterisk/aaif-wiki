---
type: resource
title: Agent to Tool CLI Boundary Specification
description: Observability reference matrix and context propagation model analyzing
  direct agent subprocess invocations, environment-variable carriers, and span lifecycle
  boundaries.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/35
tags:
- observability
- tools
- cli
- spans
- telemetry
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:13:40.113419+00:00'
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
The Agent-to-Tool CLI boundary specification details how an agent runtime observes, traces, and governs direct local subprocess invocations executing external command-line tools.[^evt-wg-observability-and-traceability-pr-35] It establishes a concrete realization of the broader cross-boundary gap model tracked in issue #29, bridging canonical tool execution semantics with operating system process lifecycles.[^evt-wg-observability-and-traceability-issue-29][^evt-wg-observability-and-traceability-pr-35]

The specification defines standard propagation conventions using OpenTelemetry environment-variable context carriers and establishes execution span attribution across synchronous, asynchronous, and background subprocesses.[^evt-wg-observability-and-traceability-pr-35]

# Architecture / Specification
The boundary distinguishes between the canonical Agent-to-Tool semantic contract and the operational Agent Runtime to Local Process execution layer.[^evt-wg-observability-and-traceability-pr-35]

## Context Propagation and Environment Variables
- **Context Carrier**: Subprocess tracing leverages the OpenTelemetry Release Candidate specification for environment-variable context carriers (including TRACEPARENT, TRACESTATE, and BAGGAGE).[^evt-wg-observability-and-traceability-pr-35]
- **Span Reservation**: Pre-execution span-ID reservation allows the parent agent runtime to inject trace context before spawning child processes, preventing detached traces in non-interactive CLI executions.[^evt-wg-observability-and-traceability-pr-35]
- **Span Relationships**: Direct synchronous commands maintain parent-child hierarchy between execute_tool and child CLI spans, whereas detached or long-running background tasks leverage OpenTelemetry Span Links to avoid blocking agent execution loops.[^evt-wg-observability-and-traceability-pr-35]

[^evt-wg-observability-and-traceability-issue-29]: https://github.com/aaif/wg-observability-and-traceability/issues/29
[^evt-wg-observability-and-traceability-pr-35]: https://github.com/aaif/wg-observability-and-traceability/pull/35
