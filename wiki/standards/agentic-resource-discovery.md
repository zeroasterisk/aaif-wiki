---
type: standard
title: Agentic Resource Discovery (ARD)
description: Decentralized discovery, verification, and admission specification enabling
  agents to find, trust, admit, and observe external resources.
resource: https://github.com/aaif/wg-observability-and-traceability/issues/49
tags:
- discovery
- governance
- observability
- standards
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T09:51:54.026492+00:00'
sources:
- id: evt-wg-observability-and-traceability-issue-49
  resource: https://github.com/aaif/wg-observability-and-traceability/issues/49
  author: 91pavan
  last_modified: '2026-09-02T05:53:28+00:00'
---

# Overview
Agentic Resource Discovery (ARD) is an open specification defining decentralized discovery, capability negotiation, provenance verification, and policy admission for AI agent resources and external skills. Developed in collaboration with the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), ARD establishes observable pipelines spanning gateway boundaries to ensure trusted resource evaluation prior to execution[^evt-wg-observability-and-traceability-issue-49].

# Architecture / Specification

## Five-Stage Lifecycle Telemetry
ARD structures capability discovery and governance through five explicit lifecycle stages observable via standard OpenTelemetry Protocol (OTLP) pipelines[^evt-wg-observability-and-traceability-issue-49]:
1. **Discovery**: Resolution and retrieval of candidate agent tools, skills, and endpoints across external catalogs or registries.
2. **Provenance**: Verification of resource origin, cryptographic signatures, and package attestation.
3. **Governance**: Policy validation ensuring capabilities conform to administrative guardrails and organization boundary rules.
4. **Trust Evaluation**: Runtime risk assessment and reputation verification.
5. **Admission Decision**: Formal gating determining whether a capability is admitted, quarantined, or rejected.

## Gateway and Runtime Correlation
To guarantee end-to-end auditability across architectural boundaries, ARD integrates with mediation components like [Agent Gateway](../resources/agentgateway.md) and agent harnesses such as [Goose](../resources/goose.md)[^evt-wg-observability-and-traceability-issue-49]:
- **W3C Trace Context Propagation**: Propagates trace context headers across gateway discovery evaluations and runtime skill execution to correlate admission decisions directly with subsequent invocations[^evt-wg-observability-and-traceability-issue-49].
- **Quarantine Observability**: Telemetry emitted for quarantined or rejected capabilities records policy denial decisions without generating spurious downstream execution spans[^evt-wg-observability-and-traceability-issue-49].

# Lifecycle History
- **Implementation Validation**: Initiated lifecycle observability validation PoC linking Agent Gateway policy enforcement with Goose skill activation spans over standard OTLP JSON fixtures[^evt-wg-observability-and-traceability-issue-49].

[^evt-wg-observability-and-traceability-issue-49]: https://github.com/aaif/wg-observability-and-traceability/issues/49
