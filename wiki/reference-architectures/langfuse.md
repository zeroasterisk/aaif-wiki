---
type: architecture
title: Langfuse Reference Architecture
description: Dedicated open-source LLM observability backend providing hierarchical
  trace ingestion, generation tracking, and evaluation metrics for AI agent frameworks.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-LANGFUSE.md
tags:
- observability
- llm-tracing
- telemetry
- evaluation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:33:25.575442+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-LANGFUSE.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

Langfuse is an open-source LLM observability and evaluation backend that records detailed hierarchical execution trees of AI agent workflows [^evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44]. It captures span timing, prompt and generation input/output payloads, model parameters, and token cost attribution for complex multi-step agent executions [^evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44].

# Architecture / Specification

Integration between agent runtimes (such as [Goose](../reference-architectures/goose.md)) and Langfuse follows a structured observation model [^evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44]:

- **Subscriber Layer**: A `tracing_subscriber::Layer` intercepts internal runtime events, mapping span lifetimes to Langfuse observation IDs and flattens metadata (inputs, outputs, model configuration) [^evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44].
- **Batch Manager**: Asynchronously accumulates observation events and flushes payloads periodically (e.g., every 5 seconds) via authenticated HTTP POST requests to `/api/public/ingestion` [^evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44].
- **Data Model**: Organizes execution into Traces containing child Spans and Generations, tracking prompt token counts, latency breakdowns, and user session identifiers [^evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44].

# References

- Langfuse Reference Architecture in [Observability and Traceability WG](../working-groups/observability-and-traceability.md) [^evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44].

[^evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-LANGFUSE.md
