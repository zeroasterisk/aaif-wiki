---
type: architecture
title: Datadog
description: Full-stack commercial observability platform providing APM distributed
  tracing, LLM Observability SDKs, and infrastructure monitoring for AI agents.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-DATADOG.md
tags:
- observability
- apm
- llm-observability
- commercial-platform
- tracing
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:32:16.200381+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-DATADOG.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

Datadog is an integrated SaaS observability platform providing end-to-end distributed tracing, metrics, logging, and dedicated LLM Observability for AI agent workflows [^evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df]. It combines host/container agents with language-specific APM and LLM tracing SDKs to capture agent, tool, workflow, and model invocation telemetry [^evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df].

Evaluated within the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), Datadog provides a complete vendor pipeline spanning collection, ingestion, storage, visualization, and alerting [^evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df].

# Architecture / Specification

The platform architecture is structured across application instrumentation, local collectors, and SaaS analytics [^evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df]:

- **LLM Observability SDK**: `ddtrace.llmobs` instruments AI agent code with dedicated spans (`agent`, `workflow`, `tool`, `llm`), capturing prompt/completion text, token counts, model metadata, latency, and estimated cost [^evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df].
- **Datadog Agent**: Host/daemon container collecting traces (port 8126), metrics, and logs, aggregating and buffering telemetry before egress [^evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df].
- **Correlated APM Pipeline**: Unifies LLM span trees with traditional distributed traces from gateways, databases, queues, and external APIs [^evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df].

[^evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-DATADOG.md
