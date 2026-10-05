---
type: reference-architecture
title: Datadog AI Observability Reference Architecture
description: Reference architecture evaluating Datadog LLM Observability SDK, APM
  distributed tracing, and agent host telemetry for AI agent pipelines.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-DATADOG.md
tags:
- observability
- datadog
- apm
- llm-observability
- saas
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T09:59:04.610410+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-DATADOG.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

The Datadog AI Observability reference architecture evaluates an integrated commercial platform for monitoring AI agents, LLM inference pipelines, and supporting infrastructure [^evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df]. It details the ingestion, tracing abstractions, and evaluation capabilities provided by Datadog APM and LLM Observability [^evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df].

# Architecture / Specification

Datadog provides an integrated pipeline from language SDKs through a host/container agent to SaaS analytics [^evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df]:

- **LLM Observability SDK (`ddtrace.llmobs`)**: Instruments agent workflows, tool calls, and LLM completions, capturing input prompts, outputs, token counts, latency, and cost metadata [^evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df].
- **APM Distributed Tracing (`dd-trace`)**: Correlates high-level agent spans with backend database queries, gateway HTTP calls, and distributed message queues [^evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df].
- **Datadog Agent**: Aggregates traces, system metrics, and log streams on port 8126 before forwarding encrypted payloads to the Datadog SaaS backend [^evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df].

# References

- [OpenTelemetry Reference Architecture](opentelemetry.md)
- [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md)

[^evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-DATADOG.md
