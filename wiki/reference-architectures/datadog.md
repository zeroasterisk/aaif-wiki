---
type: reference-architecture
title: Datadog Reference Architecture
description: Reference architecture assessing Datadog APM, agent telemetry collection,
  and LLM Observability for AI agent pipelines and infrastructure.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-DATADOG.md
tags:
- observability
- apm
- agent-tracing
- llm-observability
- reference-architecture
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T09:55:33.829608+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-DATADOG.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

The Datadog reference architecture evaluates commercial full-stack observability for AI agents and LLM application infrastructure [^evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df]. Maintained by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), the document analyzes the Datadog Agent, Application Performance Monitoring (APM), and dedicated LLM Observability SDK (`ddtrace.llmobs`) across collection, ingestion, and evaluation layers [^evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df].

# Architecture / Specification

Datadog's AI agent monitoring architecture integrates application-level and host-level observability [^evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df]:

- **LLM Observability SDK**: Provides specialized span types (`LLMObs.agent()`, `LLMObs.workflow()`, `LLMObs.tool()`, `LLMObs.llm()`) that capture prompt/completion payloads, model parameters, token counts, and estimated financial costs [^evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df].
- **Distributed APM Tracing**: Propagates trace context across upstream gateways, AI agents, databases, and background services using standard HTTP headers and agent protocols [^evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df].
- **Datadog Agent**: Runs in the host or container environment to aggregate traces, system metrics, and log pipelines before transmitting telemetry over TLS to Datadog's SaaS backend [^evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df].

[^evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-DATADOG.md
