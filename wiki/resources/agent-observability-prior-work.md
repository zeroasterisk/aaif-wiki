---
type: resource
title: Agent Observability Prior Work Landscape
description: Comparative landscape survey evaluating specifications, platforms, and
  hosted protocols across agent observability, runtime tracing, and security telemetry.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/working-documents/PRIOR-WORK.md
tags:
- observability
- tracing
- opentelemetry
- telemetry
- landscape
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:06:52.448943+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/working-documents/PRIOR-WORK.md
  author: Pavan Sudheendra
  last_modified: '2026-09-26T04:52:07+01:00'
---

# Overview

The Agent Observability Prior Work Landscape is an authoritative working group survey maintained by the Observability and Traceability Working Group that catalogs existing specifications, instrumentation libraries, and observability backends across the agentic ecosystem [^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853]. It establishes a neutral baseline for evaluating runtime telemetry maturity, identifying cross-vendor instrumentation gaps, and framing the AAIF's standardization priorities across LLM execution, protocol boundaries, and distributed agent swarms.

The survey evaluates efforts according to scope, specification maturity, license, and architectural focus rather than competitive rankings [^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853]. It spans telemetry generation across model APIs, tool execution boundaries, agent-to-agent delegation, and environment-level signals.

# Architecture / Specification

### Landscape Structure

The landscape categorizes agent observability efforts into primary operational sectors [^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853]:

1. **Vendor-Neutral Telemetry Specifications**: Foundational standards defining data models and semantic conventions, notably OpenTelemetry GenAI Semantic Conventions (now housed in `open-telemetry/semantic-conventions-genai`) detailing spans for `create-agent`, `invoke-agent`, `invoke-workflow`, `execute-tool`, and `plan` operations [^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853].
2. **Security and Integrity Schemas**: Governance and audit data models including the OWASP Agent Observability Standard (AOS)—decoupling Instrument, Trace, and Inspect specifications—and the Open Cybersecurity Schema Framework (OCSF) v1.9, which introduces AI Operation, AI Agent, Delegation, and Record Integrity classes [^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853].
3. **Cross-Agent Protocols & Frameworks**: Protocol-level telemetry and propagation substrates including AGNTCY Observe SDK, A2A traceability extensions, and Model Context Protocol (MCP) telemetry mediation [^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853].
4. **Application & Library Auto-Instrumentation**: Frameworks capturing LLM and agent execution runs, including Monocle (LF AI & Data), OpenInference, OpenLLMetry, and OpenLIT [^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853].
5. **Evaluation, Tracing, and MLOps Backends**: Specialized analytical backends spanning Langfuse, Arize Phoenix, MLflow Tracing, W&B Weave, LangSmith, and Helicone [^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853].
6. **Environment-Derived Signals**: Non-invasive runtime and kernel observability, notably eBPF-based instrumentation via OpenTelemetry BPF Instrumentation (OBI) to provide non-repudiable network and system telemetry [^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853].

### Cross-Working Group Integration

The survey informs the WG's development of the `../standards/agent-behavior-trace-model.md` and provides grounding for cross-boundary telemetry mapping analyzed in `../resources/cross-boundary-observability-model.md` [^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853].

# Lifecycle History

- **2026-03-15**: Initial landscape survey drafted in the Observability and Traceability Working Group [^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853].
- **2026-08-13**: Mid-2026 refresh merged, incorporating OTel GenAI's dedicated repository migration, OCSF 1.9 agent security schemas, AOS specification modularization, AGNTCY Observe SDK `sdk-v1.0.43`, and A2A's donation into AAIF [^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853].

[^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/working-documents/PRIOR-WORK.md
