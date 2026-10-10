---
type: resource
title: Datadog AI Agent Observability
description: Reference architecture evaluating Datadog LLM Observability, APM distributed
  tracing, and infrastructure monitoring for AI agent platforms.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-DATADOG.md
tags:
- observability
- datadog
- apm
- llm-observability
- monitoring
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T14:55:28.695732+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-DATADOG.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

Datadog provides an integrated commercial observability platform offering Application Performance Monitoring (APM), host telemetry, and dedicated LLM Observability features for AI agents [^evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df]. It delivers end-to-end ingestion, visualization, cost attribution, and alerting within a single SaaS ecosystem [^evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df].

Assessed under the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), Datadog illustrates an integrated SaaS pattern contrasted with unbundled open-source plumbing frameworks such as [OpenTelemetry](../resources/opentelemetry.md) [^evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df].

# Architecture / Specification

The platform architecture comprises three main tiers [^evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df]:

- **SDK Instrumentation**: Applications use `ddtrace.llmobs` to trace agent execution, tool invocations, prompts, token counts, and estimated model costs [^evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df].
- **Datadog Agent**: Host or container-level daemons collect APM spans, metrics, and system logs, forwarding them over authenticated HTTPS connections [^evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df].
- **SaaS Platform**: Datadog ingests traces, correlates agent workflows with backend microservice latency, and presents evaluation dashboards and cost tracking interfaces [^evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df].

[^evt-wg-observability-and-traceability-file-70d9c41ccfb1-1a3eb2df]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-DATADOG.md
