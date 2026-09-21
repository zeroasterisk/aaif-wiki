---
type: reference-architecture
title: 'Reference Architecture: Langfuse'
description: Reference architecture for Langfuse LLM observability backend capturing
  hierarchical execution traces, token costs, and generation evaluations.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-LANGFUSE.md
tags:
- observability
- reference-architecture
- langfuse
- tracing
- evaluations
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T09:56:30.127413+00:00'
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
Langfuse is an open-source LLM observability platform and telemetry sink designed to ingest hierarchical execution traces from AI agent runtimes, capturing span timing, model generation metadata, token costs, and input/output payloads for debugging and evaluation[^evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44]. It operates as an external observability backend receiving structured batches of traces, spans, and generation observations from client runtimes like Goose[^evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44].

# Architecture / Specification
Agent runtimes interface with Langfuse through batch ingestion APIs (HTTP basic authentication) via dedicated observation subscriber layers[^evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44]. The integration flattens agent execution spans, correlates observation UUIDs with root trace identifiers, and periodically flushes asynchronous batches[^evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44]. Telemetry ingestion enables visualization of complex multi-turn agent loops, prompt management, cost tracking, and programmatic evaluation scoring[^evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44].

# References
- Langfuse Reference Architecture by [../working-groups/observability-and-traceability.md](observability-and-traceability.md)[^evt-wg-observability-and-traceability-pr-20]

[^evt-wg-observability-and-traceability-file-f704e4b7956f-e57d4c44]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-LANGFUSE.md
[^evt-wg-observability-and-traceability-pr-20]: https://github.com/aaif/wg-observability-and-traceability/pull/20
