---
type: resource
title: OpenTelemetry Agent Reference Architecture
description: Vendor-neutral telemetry framework standardizing trace, metric, and log
  collection across agent harnesses, LLM gateways, and MCP servers using OTLP and
  gen_ai conventions.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-OTEL.md
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T09:47:35.806001+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-OTEL.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

OpenTelemetry (OTel) provides a vendor-neutral observability substrate standardizing how traces, metrics, and logs are instrumented, collected, and exported across AI agent infrastructures [^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a]. Developed as a cloud-native standard, OTel functions as the plumbing layer connecting agent runtimes, language model proxies, and external tool endpoints with downstream telemetry backends without imposing vendor lock-in.

Within the scope of the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), OpenTelemetry acts as the primary transport and semantic baseline for propagating causal context across protocol boundaries, complementing standardized schemas like the [Agent Behavior Trace Model](../standards/agent-behavior-trace-model.md).

# Architecture / Specification

The OTel agent reference architecture spans three distinct functional tiers [^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a]:

- **Instrumentation Layer:** Ingests execution events directly from agent harnesses, LLM gateways, and Model Context Protocol ([agent-mcp-server-boundary](agent-mcp-server-boundary.md)) servers via language SDKs (Python, Java, Go). Instrumentation adheres to OpenTelemetry Semantic Conventions v1.27.0 (`gen_ai.*`), capturing prompt tokens, completion tokens, model configurations, and tool invocation parameters.
- **Wire Protocol (OTLP 1.3.0):** Standardizes telemetry delivery over gRPC (port 4317) or HTTP/protobuf and HTTP/JSON (port 4318) with consistent context propagation headers.
- **OTel Collector Pipeline (v0.104.0):** Decouples application components from telemetry sinks. Receivers ingest OTLP, Prometheus, and external signals; processors perform batching, PII redaction, and memory-limiting; and exporters push structured telemetry to target storage systems or analytical platforms.

# References

- OpenTelemetry Specification: stable signals for traces, metrics, and logs [^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a]
- OpenTelemetry Collector v0.104.0 architecture and pipeline specification [^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a]

[^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-OTEL.md
