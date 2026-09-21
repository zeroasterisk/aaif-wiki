---
type: reference-architecture
title: OpenTelemetry for AI Agent Infrastructure
description: Reference architecture for OpenTelemetry telemetry collection, processing,
  and gen_ai semantic conventions across AI agent workflows.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-OTEL.md
tags:
- observability
- opentelemetry
- tracing
- reference-architecture
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T09:55:00.429590+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-OTEL.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

OpenTelemetry (OTel) provides a vendor-neutral observability framework defining how traces, metrics, and logs are instrumented, collected, processed, and exported across AI agent infrastructure [^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a]. Developed as an industry telemetry substrate and evaluated by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), OTel standardizes span hierarchies and attribute definitions for LLM gateways, Model Context Protocol (MCP) servers, and agent runtimes [^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a].

# Architecture / Specification

The OTel reference architecture spans application instrumentation, wire protocols, and collector processing pipelines [^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a]:

- **Instrumentation & Semantic Conventions**: Agent runtimes and LLM gateways use language SDKs (such as Python, Java, and Go) to emit traces adhering to standardized `gen_ai.*` semantic conventions capturing prompt configurations, token counts, model identifiers, and tool execution spans [^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a].
- **Transport (OTLP)**: OpenTelemetry Protocol (OTLP) transports telemetry over gRPC (port 4317) or HTTP/Protobuf/JSON (port 4318) [^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a].
- **Collector Pipeline**: The OTel Collector receives telemetry from multiple sources, processes records via batching, filtering, and attribute redaction, and exports them to backend storage and visualization platforms [^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a].

[^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-OTEL.md
