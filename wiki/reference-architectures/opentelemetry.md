---
type: architecture
title: 'Reference Architecture: OpenTelemetry'
description: Vendor-neutral observability framework and collector pipeline for instrumenting,
  processing, and exporting AI agent traces, metrics, and logs.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-OTEL.md
tags:
- observability
- opentelemetry
- tracing
- otlp
- metrics
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:31:53.717543+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-OTEL.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview
OpenTelemetry (OTel) provides a vendor-neutral observability framework that standardizes the collection, processing, and export of traces, metrics, and logs across AI agent infrastructure [^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a]. Maintained under the guidance of the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), this reference architecture defines telemetry pipelines connecting instrumented AI agents, LLM gateways, and MCP servers to downstream observability backends [^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a].

# Architecture / Specification
The OpenTelemetry architecture for agentic systems operates across three core layers [^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a]:
- **Instrumented Applications**: AI agents, LLM gateways, and tool servers emit trace spans and metrics formatted with standardized semantic conventions (`gen_ai.*` attributes) using language SDKs [^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a].
- **Wire Protocol**: Telemetry is transmitted over OpenTelemetry Protocol (OTLP) via gRPC (port 4317) or HTTP/Protobuf/JSON (port 4318) [^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a].
- **Collector Pipeline**: The OpenTelemetry Collector receives telemetry through pluggable receivers, applies filtering and batch processing, and routes signals via exporters to target storage backends [^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a].

[^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-OTEL.md
