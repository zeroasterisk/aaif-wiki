---
type: reference-architecture
title: OpenTelemetry for Agentic Systems
description: Reference architecture specifying OpenTelemetry SDK instrumentation,
  OTLP pipelines, and GenAI semantic conventions for distributed agent tracing and
  identity propagation.
resource: https://github.com/aaif/wg-observability-and-traceability/issues/50
tags:
- observability
- opentelemetry
- tracing
- identity
- reference-architecture
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:06:53.330462+00:00'
sources:
- id: evt-wg-observability-and-traceability-issue-50
  resource: https://github.com/aaif/wg-observability-and-traceability/issues/50
  author: npgovintarajan
  last_modified: '2026-09-10T17:27:43+00:00'
---

# Overview

This reference architecture specifies how OpenTelemetry SDKs, Collector pipelines, and GenAI semantic conventions instrument multi-agent workflows, tool execution boundaries, and asynchronous execution loops.[^evt-wg-observability-and-traceability-issue-50]

# Architecture / Specification

## Agent Identity & Context Propagation

Agent identity context must survive non-HTTP, asynchronous boundaries such as job queues, event streams, tool execution sandboxes, and streaming LLM completions using standard W3C Baggage propagation:[^evt-wg-observability-and-traceability-issue-50]

- **Standard Span Attributes**: Standardized semantic attributes capture invocation state, including `agent.id`, `agent.role`, `agent.invocation_id`, `agent.principal.type`, and `agent.delegation_depth`.[^evt-wg-observability-and-traceability-issue-50]
- **Causal Lineage Tracing**: Preserves caller identity across invocation chains spanning User Request -> Orchestrator Agent -> Sub-Agent -> Downstream Tool/Resource.[^evt-wg-observability-and-traceability-issue-50]
- **Telemetry Sanitization & Boundaries**: Strict filtering rules prohibit raw tokens, private keys, message signatures, or user-identifiable payloads from entering standard APM backends, restricting them to dedicated secure audit stores.[^evt-wg-observability-and-traceability-issue-50]

# Lifecycle History

- Proposed telemetry specification and baggage propagation model for agent identity scoping under the Observability and Traceability Working Group.[^evt-wg-observability-and-traceability-issue-50]

[^evt-wg-observability-and-traceability-issue-50]: https://github.com/aaif/wg-observability-and-traceability/issues/50
