---
type: resource
title: Agent-to-Tool CLI Boundary Architecture
description: Observability reference architecture and telemetry propagation matrix
  for AI agents invoking local CLI subprocess tools.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/35
tags:
- observability
- opentelemetry
- cli
- tracing
- w3c-trace-context
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:07:35.894934+00:00'
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
The Agent-to-Tool CLI boundary reference architecture specifies observability propagation, trace context handoff, and execution span modeling when an AI agent runtime invokes a local CLI subprocess tool [^evt-wg-observability-and-traceability-pr-35]. It distinguishes the canonical semantic Agent→Tool boundary from the operational Agent Runtime→Local Process execution boundary [^evt-wg-observability-and-traceability-pr-35].

# Architecture / Specification
The boundary model evaluates eight core observability dimensions across agent execution: identity, context, relationship, lifecycle, outcome, provenance, security, and timing [^evt-wg-observability-and-traceability-issue-29] [^evt-wg-observability-and-traceability-pr-35]. Context propagation maps standard carriers across the local process boundary:
- **Context Propagation**: Utilizes W3C Trace Context, W3C Baggage, and the OpenTelemetry environment variable context carrier convention to inject trace state into subprocess environments [^evt-wg-observability-and-traceability-pr-35].
- **Span Management**: Separates high-level GenAI `execute_tool` spans from local CLI process invocation spans, supporting pre-execution span ID reservation and span links for detached or background tasks [^evt-wg-observability-and-traceability-pr-35].
- **Evidence Integrity**: Treats attribution and execution integrity as cross-cutting guarantees across the runtime invocation lifecycle [^evt-wg-observability-and-traceability-pr-35].

# References
- Cross-boundary observability gap model [^evt-wg-observability-and-traceability-issue-29]
- Working group coordination in `../working-groups/observability-and-traceability.md`
- Related vendor-neutral telemetry in `../resources/opentelemetry.md`

[^evt-wg-observability-and-traceability-issue-29]: https://github.com/aaif/wg-observability-and-traceability/issues/29
[^evt-wg-observability-and-traceability-pr-35]: https://github.com/aaif/wg-observability-and-traceability/pull/35
