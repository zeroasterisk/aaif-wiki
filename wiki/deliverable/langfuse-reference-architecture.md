---
type: deliverable
title: Langfuse Reference Architecture
description: A reference architecture evaluating Langfuse LLM observability ingestion,
  hierarchical agent tracing, and generation tracking.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-LANGFUSE.md
tags:
- observability
- reference-architecture
- langfuse
- llm-tracing
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:53:26.447775+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-LANGFUSE.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
- id: evt-wg-observability-and-traceability-pr-20
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/20
  author: MatthewKhouzam
  last_modified: '2026-08-19T19:04:49+00:00'
---

# Overview

The Langfuse Reference Architecture defines how Langfuse functions as a dedicated LLM observability backend and telemetry sink for AI agent frameworks such as [Goose](../deliverable/goose-reference-architecture.md) [^evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44]. Produced by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), it details trace ingestion mechanisms, data models, cost profiles, and verification criteria for agent workflows [^evt-wg-observability-and-traceability-pr-20].

Langfuse sits outside the agent runtime, accepting structured trace and observation payloads to deliver hierarchical execution visualization, latency analysis, token cost tracking, dataset curation, and evaluation scoring [^evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44].

# Architecture / Specification

The architecture defines the observation ingestion pipeline [^evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44]:

- **Ingestion Surface**: REST batch ingestion accepting trace, span, and generation objects identified by public/secret key pairs [^evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44].
- **Client Integration Pattern**: Uses a dedicated subscriber layer in the agent runtime that maps internal lifecycle spans (e.g., `agent_reply`, `provider_chat`, `tool_execution`) into Langfuse observation records flushed asynchronously in timed batches [^evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44].
- **Data Model**: Hierarchical execution graphs capturing root agent traces, intermediate span intervals, and leaf generation metadata including token counts and model hyperparameters [^evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44].

# Lifecycle History

- 2026-06-29: Added to the Observability reference architecture catalog via landscape import [^evt-wg-observability-and-traceability-pr-20].

[^evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-LANGFUSE.md
[^evt-wg-observability-and-traceability-pr-20]: https://github.com/aaif/wg-observability-and-traceability/pull/20
