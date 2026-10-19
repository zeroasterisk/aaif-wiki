---
type: resource
title: Agent Observability Prior Work Landscape
description: Comparative landscape survey and evaluation of external standards, specifications,
  and platforms across agent observability.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/working-documents/PRIOR-WORK.md
tags:
- observability
- standards
- landscape
- opentelemetry
- tracing
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T10:39:12.145225+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/working-documents/PRIOR-WORK.md
  author: Pavan Sudheendra
  last_modified: '2026-09-26T04:52:07+01:00'
---

# Overview
The Agent Observability Prior Work Landscape (`PRIOR-WORK.md`) is a comprehensive survey maintained by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) assessing existing industry specifications, instrumentation frameworks, and telemetry platforms for agentic systems [^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853]. First compiled in March 2026 and refreshed through August 2026, the survey analyzes gaps, specification maturity, and opportunities for alignment across open and proprietary observability initiatives [^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853].

# Architecture / Specification
The landscape benchmarks efforts across several functional sectors [^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853]:
- **OpenTelemetry GenAI Semantic Conventions**: Dedicated repository (`open-telemetry/semantic-conventions-genai`) defining spans, events, and metrics for LLM calls, agent creation/invocation, workflow execution, tool runs, and planning [^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853].
- **Security and Compliance Frameworks**: OWASP Agent Observability Standard (AOS) separating instrument, trace, and inspect tiers with AgBOM integrations, and the Open Cybersecurity Schema Framework (OCSF) Schema 1.9 incorporating AI Operation, AI Agent identity, and delegation records [^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853].
- **Multi-Agent and Protocol Tracing**: AGNTCY Observe SDK for cross-agent context propagation, [Agent-to-Agent (A2A)](../taxonomy/agent-to-agent.md) protocol tracing extensions, and [OpenTelemetry](../resources/opentelemetry.md) eBPF runtime instrumentation [^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853].
- **Application and Evaluation Frameworks**: OpenInference, MLflow Tracing, [Langfuse](../resources/langfuse.md), LF AI & Data Monocle auto-instrumentation, and Cursor [Agent Trace](../standards/agent-trace.md) [^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853].

# Lifecycle History
Originally drafted on 2026-03-15, the survey underwent a major refresh between June and August 2026 [^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853]. Key updates included tracking OpenTelemetry's migration of GenAI specifications into a dedicated repository, the release of OCSF 1.9 agent profiles, AGNTCY Observe SDK v1.0.43, and the shifting focus of academic research toward observability as an active security monitoring substrate [^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853].

[^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/working-documents/PRIOR-WORK.md
