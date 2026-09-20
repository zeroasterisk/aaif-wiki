---
type: deliverable
title: Datadog Reference Architecture
description: A reference architecture evaluating Datadog LLM Observability, APM distributed
  tracing, and infrastructure monitoring for AI agent workloads.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-DATADOG.md
tags:
- observability
- apm
- llm-observability
- monitoring
- datadog
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:52:21.390792+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-DATADOG.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

The Datadog reference architecture evaluates the commercial full-stack observability platform through the lens of AI agent infrastructure and LLM telemetry requirements [^evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df]. It examines the integration of host/container Datadog Agents, APM distributed tracing (`dd-trace`), and the dedicated LLM Observability SDK (`ddtrace.llmobs`) for tracing multi-agent workflows, prompt-completion lifecycles, and tool invocations.

Unlike protocol-only specifications like the [OpenTelemetry Reference Architecture](../deliverable/opentelemetry-reference-architecture.md), Datadog provides an integrated collection, SaaS ingestion, storage, visualization, and alerting pipeline [^evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df].

# Architecture / Specification

The platform architecture spans three main layers [^evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df]:

- **Application Instrumentation**: Applications embed `ddtrace.llmobs` decorators and API calls (`LLMObs.agent()`, `LLMObs.workflow()`, `LLMObs.tool()`, `LLMObs.llm()`) alongside standard APM HTTP and database spans to track agent reasoning steps, token usage, latency, and cost attribution.
- **Agent Forwarding**: The local Datadog Agent runs trace, metrics, log, and process agents locally on the host or container node, buffering and batching telemetry to SaaS ingestion endpoints.
- **SaaS Platform**: Aggregates traces into specialized LLM Observability dashboards, APM service maps, and continuous evaluation monitors.

# Lifecycle History

Evaluated by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) as part of the commercial AI agent observability comparative review [^evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df].

[^evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-DATADOG.md
