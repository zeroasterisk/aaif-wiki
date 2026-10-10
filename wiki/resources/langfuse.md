---
type: resource
title: Langfuse Reference Architecture
description: Reference architecture for Langfuse as an LLM observability backend capturing
  hierarchical agent execution traces, spans, and generations via batch ingestion
  APIs.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-LANGFUSE.md
tags:
- observability
- tracing
- llm
- telemetry
- reference-architecture
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T14:57:21.566178+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-LANGFUSE.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

Langfuse is an open-source LLM observability and tracing platform evaluated by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) as an external telemetry sink for AI agent runtimes[^evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44]. It ingests structured execution data—including root traces, intermediate execution spans, and generation metadata—to provide hierarchical visualization, latency profiling, token cost calculation, and evaluation dataset management[^evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44].

# Architecture / Specification

In the reference implementation with [Goose](../resources/goose.md), Langfuse operates outside the core agent loop using asynchronous batch ingestion[^evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44]:

- **Instrumentation Layer**: Implemented as an `ObservationLayer` over the Rust `tracing-subscriber` ecosystem. It tracks span lifecycles (`SpanTracker`), maps internal log levels to Langfuse observation levels, and flattens metadata into model configuration and input/output payloads[^evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44].
- **Batch Manager**: An internal `LangfuseBatchManager` buffers observation events in memory and flushes payloads periodically (e.g., every 5 seconds) over HTTP using basic authentication[^evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44].
- **Resilience and Isolation**: Ingestion failures or network partitions do not block or terminate the agent execution runtime; failures are logged while agent tool invocations and replies proceed normally[^evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44].

# Lifecycle History

- **2026-06-29**: Reference architecture published within the Observability & Traceability Working Group landscape for Langfuse v2.x integrations[^evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44].

[^evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-LANGFUSE.md
