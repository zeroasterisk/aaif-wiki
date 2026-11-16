---
type: working-group
title: Observability and Traceability Working Group
description: Technical working group standardizing agent telemetry, causal execution
  traces, protocol boundary metrics, and identity accountability attributes.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/75
tags:
- observability
- telemetry
- tracing
- identity
- accountability
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:45:37.921247+00:00'
sources:
- id: evt-wg-observability-and-traceability-pr-75
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/75
  author: MarcMolas
  last_modified: '2026-11-12T20:50:28+00:00'
- id: evt-wg-observability-and-traceability-pr-76
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/76
  author: wlad232
  last_modified: '2026-11-14T10:09:49+00:00'
---

# Overview

The Observability and Traceability Working Group standardizes vendor-neutral telemetry models, distributed execution tracing, and protocol boundary metrics across agentic AI systems [^evt-wg-observability-and-traceability-pr-75]. Its remit includes defining causal context propagation across tool boundaries, capturing hierarchical agent task execution, and standardizing identity attribution in telemetry streams [^evt-wg-observability-and-traceability-pr-75, ^evt-wg-observability-and-traceability-pr-76].

# Architecture / Specification

The working group standardizes telemetry interfaces, semantic conventions, and correlation models for agent runtimes and tools.

## Agent Identity and Accountability Telemetry

Recent working documents develop semantic conventions for agent identity and accountability attribution within distributed traces [^evt-wg-observability-and-traceability-pr-75, ^evt-wg-observability-and-traceability-pr-76]:
- **Accountability Attribute Group**: Introduces the `agent.accountability.*` attribute namespace, including result, reference, and assurance fields [^evt-wg-observability-and-traceability-pr-75].
- **Span-to-Record References**: Employs `agent.accountability.ref` to correlate trace spans with audit records, bounded so that references neither resolve outside the deciding authority nor leak beyond its trust domain [^evt-wg-observability-and-traceability-pr-75].
- **Redaction and Sanitization Rules**: Establishes redaction rules developed jointly with the [Security and Privacy Working Group](../working-groups/security-and-privacy.md) to sanitize identity attributes across trust boundaries [^evt-wg-observability-and-traceability-pr-75, ^evt-wg-observability-and-traceability-pr-76].
- **Asynchronous Execution Tracing**: Models lifecycle events across asynchronous queues, separating approved span fields from local audit evidence while capturing dispatch refusals and post-dispatch revocations [^evt-wg-observability-and-traceability-pr-76].

# Lifecycle History

Draft proposals PR#75 and PR#76 extended the group's agent identity telemetry track (Issue #50), establishing attribution schemas and asynchronous trace semantics aligned with OpenTelemetry GenAI semantic conventions [^evt-wg-observability-and-traceability-pr-75, ^evt-wg-observability-and-traceability-pr-76].

[^evt-wg-observability-and-traceability-pr-75]: https://github.com/aaif/wg-observability-and-traceability/pull/75
[^evt-wg-observability-and-traceability-pr-76]: https://github.com/aaif/wg-observability-and-traceability/pull/76
