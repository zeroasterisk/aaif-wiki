---
type: standard
title: Agent Behavior Trace Model
description: Telemetry specification and OpenTelemetry semantic conformance framework
  standardizing session continuity, causal tool lineage, and agent execution spans.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/meeting-minutes/2026-09-30.md
tags:
- standard
- telemetry
- opentelemetry
- trace-model
- observability
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T10:58:12.596856+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-fc392a405330-7a0995cd
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/meeting-minutes/2026-09-30.md
  author: Pavan Sudheendra
  last_modified: '2026-10-05T18:02:05+01:00'
---

# Overview
The Agent Behavior Trace Model is an open telemetry framework maintained by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) to standardize execution spans, causal context propagation, and agent session tracking[^evt-wg-observability-and-traceability-file-fc392a405330-7a0995cd]. The specification addresses semantic inconsistencies in how agent SDKs instrument reasoning loops, tool interactions, and delegation boundaries.

# Architecture / Specification
While early work explored an independent telemetry serialization model, the technical direction focuses on an OpenTelemetry semantic conformance framework[^evt-wg-observability-and-traceability-file-fc392a405330-7a0995cd]. Because most production agent frameworks and software development kits already integrate with OpenTelemetry but apply inconsistent semantic attributes and span hierarchies, the specification focuses on:
- **Semantic Gap Remediation**: Documenting discrepancies and omissions across agent runtimes when emitting OpenTelemetry standard GenAI and span attributes[^evt-wg-observability-and-traceability-file-fc392a405330-7a0995cd].
- **Conformance Test Suite**: Providing automated validation tools within the foundation's repositories to test whether SDK telemetry streams conform to standardized agent lifecycle and boundary semantics[^evt-wg-observability-and-traceability-file-fc392a405330-7a0995cd].
- **Upstream Standardization**: Contributing refined semantic conventions and schema improvements directly to upstream OpenTelemetry working groups rather than creating an isolated standalone protocol[^evt-wg-observability-and-traceability-file-fc392a405330-7a0995cd].

# Lifecycle History
The project was reframed during the September 2026 Observability and Traceability Working Group discussions to pivot from developing a disparate trace format toward establishing an OpenTelemetry semantic conformance suite and upstream contribution track[^evt-wg-observability-and-traceability-file-fc392a405330-7a0995cd].

[^evt-wg-observability-and-traceability-file-fc392a405330-7a0995cd]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/meeting-minutes/2026-09-30.md
