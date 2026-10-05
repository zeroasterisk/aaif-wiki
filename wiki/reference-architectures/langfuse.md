---
type: reference-architecture
title: Langfuse LLM Observability Architecture
description: Reference architecture for Langfuse LLM observability capturing hierarchical
  agent execution traces, span timing, generation token metrics, and input/output
  payloads via asynchronous batch ingestion.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-LANGFUSE.md
tags:
- langfuse
- llm-observability
- tracing
- agents
- generations
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:00:16.963486+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-LANGFUSE.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

The Langfuse reference architecture specifies how AI agent frameworks capture and export hierarchical execution traces, span durations, model generation parameters, token usage metrics, and prompt/response payloads to the Langfuse observability platform.[^evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44]

Positioned as an external LLM evaluation and observability sink, Langfuse provides hierarchical trace tree visualization, token cost calculations, latency decomposition, and dataset scoring. Agent runtimes such as [Goose](../reference-architectures/goose.md) connect via non-blocking asynchronous HTTP batch managers, transforming internal runtime spans into structured generation observations.[^evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44]

# Architecture / Specification

### Instrumentation and Batch Pipeline

1. **Span Hierarchy**: The agent captures nested execution spans (`agent_reply` → `provider_chat` → `tool_execution`) using the framework's native tracing layer.[^evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44]
2. **Observation Layer**: Maps span IDs to observation UUIDs, maps logging levels, and flattens metadata into Langfuse-compatible schemas containing model configurations, input tokens, and execution outputs.[^evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44]
3. **Batch Manager**: Accumulates observation records in memory and flushes them periodically (e.g., every 5 seconds) over HTTP POST to Langfuse Cloud or self-hosted ingestion endpoints using basic authentication.[^evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44]
4. **Fault Tolerance**: Ingestion network failures or endpoint timeouts are handled non-destructively, ensuring that agent execution proceeds unimpeded even when the telemetry backend is unreachable.[^evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44]

# References

- [Langfuse Repository](https://github.com/langfuse/langfuse)
- [Goose Agent Runtime Architecture](../reference-architectures/goose.md)
- [OpenTelemetry Architecture](../reference-architectures/opentelemetry.md)

[^evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-LANGFUSE.md
