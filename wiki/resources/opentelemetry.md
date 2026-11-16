---
type: resource
title: OpenTelemetry for AI Agent Infrastructure
description: Vendor-neutral observability framework and collector pipeline standardizing
  traces, metrics, logs, and gen_ai semantic conventions across AI agent runtimes.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-OTEL.md
tags:
- observability
- opentelemetry
- otlp
- tracing
- semantic-conventions
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:01:14.908330+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-OTEL.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview
OpenTelemetry (OTel) serves as the vendor-neutral observability substrate for AI agent infrastructure, defining how traces, metrics, and logs are instrumented, collected, processed, and exported across heterogeneous system components [^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a]. Rather than operating as an analysis backend or storage engine, OTel provides the telemetry plumbing connecting instrumented agent runtimes, LLM gateways, and tool servers to upstream observability platforms [^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a].

# Architecture / Specification
The reference architecture spans application instrumentation, wire protocols, collector routing, and semantic conventions [^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a]:

- **Components and Versions**: Evaluated against OTel Specification 1.x (stable traces, metrics, logs), OTel Collector 0.104.0, OTLP 1.3.0, and Semantic Conventions 1.27.0 [^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a].
- **Pipeline Architecture**: Instrumented applications (AI agents, LLM gateways, MCP servers, and microservices) emit telemetry via the OpenTelemetry Protocol (OTLP) over gRPC (port 4317) or HTTP/protobuf (port 4318) into the OTel Collector [^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a].
- **Collector Pipeline**: The collector handles ingestion through configurable receiver, processor, and exporter pipelines, accepting inputs from OTLP, Prometheus, Jaeger, Zipkin, file logs, and host metrics [^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a].
- **GenAI Semantic Conventions**: Standardizes agent and language model execution metadata through `gen_ai.*` attributes, capturing prompt tokens, completion tokens, model identifiers, and tool invocation spans within unified causal trace graphs [^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a].

# References
- [OpenTelemetry Specification Repository](https://github.com/open-telemetry/opentelemetry-specification)
- Related working group: [Observability and Traceability WG](../working-groups/observability-and-traceability.md)
- Related standard: [Agent Behavior Trace Model](../standards/agent-behavior-trace-model.md)

[^evt-wg-observability-and-traceability-file-1d5077c7f2d1-16c36d9a]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-OTEL.md
