---
type: standard
title: Agentic Resource Discovery
description: Decentralized discovery, verification, and admission specification enabling
  agents to find, trust, and consume tools and skills with lifecycle telemetry.
resource: https://github.com/aaif/wg-observability-and-traceability/issues/49
tags:
- discovery
- security
- skills
- telemetry
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:05:28.687293+00:00'
sources:
- id: evt-wg-observability-and-traceability-issue-49
  resource: https://github.com/aaif/wg-observability-and-traceability/issues/49
  author: 91pavan
  last_modified: '2026-09-02T05:53:28+00:00'
---

# Overview
Agentic Resource Discovery (ARD) is a decentralized discovery, verification, and admission specification enabling AI agents to locate, evaluate, and invoke tools, context sources, and skills across trust boundaries. The framework standardizes metadata negotiation, cryptographic verification of capabilities, and policy admission pipelines, while providing end-to-end telemetry correlating discovery decisions with downstream skill execution.

# Architecture / Specification
The ARD lifecycle model standardizes evaluation stages enforced by mediation gateways and runtime harnesses:
- **Five-Stage Lifecycle Telemetry:** Enforces observable state transitions covering discovery, provenance verification, governance checking, trust evaluation, and admission decisions[^evt-wg-observability-and-traceability-issue-49]. Each stage emits structured events exportable via standard OpenTelemetry Protocol (OTLP) pipelines[^evt-wg-observability-and-traceability-issue-49].
- **Skill Activation Correlation:** Bridges discovery and runtime activation by propagating W3C Trace Context between policy intermediaries such as [Agent Gateway](../resources/agentgateway.md) and agent harnesses like [Goose](../resources/goose.md)[^evt-wg-observability-and-traceability-issue-49]. Admitted skills correlate subsequent activation and execution spans back to their governing admission decision, while quarantined skills emit audit events without generating simulated execution spans[^evt-wg-observability-and-traceability-issue-49].
- **Policy and Namespace Boundaries:** Validates experimental `ard.*` and `gen_ai.skill.*` namespaces across multi-agent environments to verify capability boundaries without requiring vendor-specific observability platforms[^evt-wg-observability-and-traceability-issue-49].

# Lifecycle History
The ARD lifecycle validation was established as a joint proof-of-concept between the LLM Primitives and Protocol Observability Feature Group and the Security workstream, testing cross-boundary admission and execution tracing using [Agent Gateway](../resources/agentgateway.md) and [Goose](../resources/goose.md)[^evt-wg-observability-and-traceability-issue-49].

[^evt-wg-observability-and-traceability-issue-49]: https://github.com/aaif/wg-observability-and-traceability/issues/49
