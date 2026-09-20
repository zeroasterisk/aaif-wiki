---
type: deliverable
title: OpenTelemetry Reference Architecture
description: A reference architecture evaluating OpenTelemetry (OTel) pipelines and
  GenAI semantic conventions as telemetry substrate for AI agent infrastructure.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-OTEL.md
tags:
- observability
- opentelemetry
- reference-architecture
- telemetry
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:51:45.199677+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-OTEL.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
- id: evt-wg-observability-and-traceability-file-69d00b3de313-41c8aea6
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/README.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview
The OpenTelemetry Reference Architecture defines how traces, metrics, and logs are instrumented, collected, processed, and exported across AI agent infrastructure, LLM gateways, and tool-execution servers[^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a]. Curated by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), it positions OpenTelemetry (OTel) as the vendor-neutral telemetry plumbing connecting AI workflows to downstream observability backends[^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a].

# Architecture / Specification
The reference architecture spans the complete data pipeline from client SDK instrumentation to collector export[^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a]:
- **Application Instrumentation**: AI agents, LLM gateways, and MCP servers instrument operations using OTel SDKs and standardized `gen_ai.*` semantic conventions[^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a].
- **Wire Protocol**: Transmits telemetry over OpenTelemetry Protocol (OTLP) via gRPC (port 4317) or HTTP/protobuf (port 4318)[^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a].
- **OTel Collector Pipeline**: Ingests signals via receivers, applies batching and processing, and routes standardized spans to target backends[^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a].

[^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-OTEL.md
