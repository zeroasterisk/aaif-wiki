---
type: reference-architecture
title: Nono Kernel-Enforced Runtime
description: Reference architecture modeling kernel-enforced runtime sandboxing, cross-boundary
  execution rows, and evidence record generation.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/52
tags:
- runtime
- sandboxing
- observability
- hitl
- security
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:14:45.253933+00:00'
sources:
- id: evt-wg-observability-and-traceability-pr-52
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/52
  author: Salkimmich
  last_modified: '2026-09-24T03:32:21+00:00'
---

# Overview

Nono is a reference architecture and implementation under evaluation within the Observability and Traceability Working Group for kernel-enforced sandboxing and low-level boundary telemetry [^evt-wg-observability-and-traceability-pr-52]. It establishes deterministic security, provenance, and human-in-the-loop (HITL) boundary capture for autonomous agent execution environments.

# Architecture / Specification

The architecture provides concrete field references, golden trace vectors, and layer mappings spanning below-L7 execution boundaries [^evt-wg-observability-and-traceability-pr-52]:

- **Cross-Boundary Telemetry Rows**: Standardized interaction mappings covering Agent-to-Gateway/Runtime, Agent-to-Human (HITL), and Agent-to-Tool interactions.
- **Kernel Enforcement Layer**: Classifies security isolation and policy enforcement across kernel, broker, and proxy layers, fitting the SAF-M-74 runtime class.
- **Trace Propagation Considerations**: Identifies trace context propagation mechanics (such as W3C `TRACEPARENT`, `TRACESTATE`, and `BAGGAGE` environment allow-lists) required to correlate kernel-level audit records with application-level OTLP spans [^evt-wg-observability-and-traceability-pr-52].

# Lifecycle History

Introduced in the Observability and Traceability Working Group following the September 2026 decision to establish below-L7 primitives in the Primitives and Protocol Observability focus group [^evt-wg-observability-and-traceability-pr-52].

# References

- [Working Group PR #52: Runtime and HITL boundary rows](https://github.com/aaif/wg-observability-and-traceability/pull/52)
- [Attested Isolated Runtime Pattern](../patterns/attested-isolated-runtime.md)
- [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md)

[^evt-wg-observability-and-traceability-pr-52]: https://github.com/aaif/wg-observability-and-traceability/pull/52
