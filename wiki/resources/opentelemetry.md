---
type: resource
title: OpenTelemetry
description: Vendor-neutral observability framework and collector pipeline standardizing
  traces, metrics, logs, and GenAI agent semantic conventions.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/67
tags:
- observability
- telemetry
- opentelemetry
- tracing
- standards
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:29:46.624102+00:00'
sources:
- id: evt-wg-observability-and-traceability-pr-67
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/67
  author: StevenMih
  last_modified: '2026-10-28T17:14:13+00:00'
- id: evt-wg-observability-and-traceability-file-e1eff34e54a6-f9dca54f
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/81dc934a316e97895677257cdc0977f5c3498ea2/meeting-minutes/2026-10-28.md
  author: Pavan Sudheendra
  last_modified: '2026-10-29T02:42:30+00:00'
---

# Overview
OpenTelemetry is an open-source observability framework providing vendor-neutral APIs, SDKs, and instrumentation for collecting distributed traces, metrics, and logs.[^evt-wg-observability-and-traceability-file-e1eff34e54a6-f9dca54f] Within the AAIF ecosystem, OpenTelemetry serves as the primary distributed tracing substrate, with active workstreams mapping GenAI semantic conventions to agentic workflows and verifiable evidence records.[^evt-wg-observability-and-traceability-pr-67]

# Architecture / Specification
OpenTelemetry's agentic integration focuses on extending semantic conventions and establishing clean seams to runtime governance artifacts:[^evt-wg-observability-and-traceability-pr-67]
- **Turn vs. Step Tracing**: Standardizing span hierarchies where a top-level turn captures a user interaction and nested child spans trace individual model invocations, tool calls, and execution steps.[^evt-wg-observability-and-traceability-file-e1eff34e54a6-f9dca54f]
- **Evidence Seam 1 (Span to Record Join)**: Linking OpenTelemetry trace and span identifiers directly to external signed records such as [Action Records](../taxonomy/action-record.md).[^evt-wg-observability-and-traceability-pr-67]
- **Evidence Seam 2 (Decision and Approval)**: Capturing policy evaluation results and human approval states inside telemetry spans.[^evt-wg-observability-and-traceability-pr-67]
- **Evidence Seam 3 (Effect Target and Status)**: Recording target resource identifiers, mutation state, and side-effect outcomes within trace attributes.[^evt-wg-observability-and-traceability-pr-67]
- **Evidence Seam 4 (Evidence Origin)**: Propagating cryptographic origin and witness metadata across span context.[^evt-wg-observability-and-traceability-pr-67]
- **Evidence Seam 5 (Integrity without Disclosure)**: Preserving trace content authenticity via hashes without leaking sensitive payload data in trace collectors.[^evt-wg-observability-and-traceability-pr-67]

# Lifecycle History
In October 2026, the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) drafted proposals to align OpenTelemetry semantic conventions with signed action and evidence record specifications.[^evt-wg-observability-and-traceability-pr-67]

[^evt-wg-observability-and-traceability-file-e1eff34e54a6-f9dca54f]: https://github.com/aaif/wg-observability-and-traceability/blob/81dc934a316e97895677257cdc0977f5c3498ea2/meeting-minutes/2026-10-28.md
[^evt-wg-observability-and-traceability-pr-67]: https://github.com/aaif/wg-observability-and-traceability/pull/67
