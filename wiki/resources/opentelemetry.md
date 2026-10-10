---
type: resource
title: OpenTelemetry for AI Agents
description: Reference architecture for vendor-neutral agent telemetry collection,
  OTLP pipelines, and gen_ai semantic conventions.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-OTEL.md
tags:
- observability
- opentelemetry
- tracing
- otlp
- metrics
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T14:55:28.695732+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-OTEL.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

OpenTelemetry (OTel) provides a vendor-neutral observability framework defining how traces, metrics, and logs are instrumented, collected, processed, and exported across AI agent infrastructure [^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a]. Developed as an open standard, OTel spans the full telemetry path from application SDKs through OpenTelemetry Protocol (OTLP) collectors to analytical backends [^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a].

Within the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), OTel serves as a primary reference telemetry substrate for standardizing agent spans, tool execution attributes, and LLM gateway interactions [^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a].

# Architecture / Specification

The OTel reference pipeline separates instrumentation from storage and visualization [^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a]:

- **Application Instrumentation**: AI agents, LLM gateways, and Model Context Protocol (MCP) servers record spans using standardized `gen_ai.*` semantic conventions [^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a].
- **Transport Protocol (OTLP)**: Telemetry is serialized using Protocol Buffers or JSON over gRPC (port 4317) or HTTP (port 4318) [^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a].
- **OTel Collector Pipeline**: Ingestion receivers forward data through batching, redaction, and sampling processors before routing to configured storage backends via exporter plugins [^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a].

[^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-OTEL.md
