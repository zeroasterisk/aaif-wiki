---
type: resource
title: Nono Kernel-Enforced Agent Runtime
description: Open-source agent runtime security tool providing kernel-enforced sandboxing,
  credential isolation, and deterministic audit trail generation.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/52
tags:
- observability
- security
- runtime
- sandboxing
- tracing
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:07:52.630853+00:00'
sources:
- id: evt-wg-observability-and-traceability-pr-52
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/52
  author: Salkimmich
  last_modified: '2026-09-24T03:32:21+00:00'
---

# Overview

Nono is an open-source agent runtime security platform designed to enforce fine-grained operational boundaries, credential isolation, and deterministic audit trails for autonomous workloads executing at the system boundary.

Operating beneath L7 application logic, nono isolates tool execution and agent subprocesses using operating-system primitives, generating signed audit records for external verification across the Agent-to-Gateway and Agent-to-Runtime boundaries [^evt-wg-observability-and-traceability-pr-52].

# Architecture / Specification

## SAF-M-74 Classification and Enforcement

Within the AAIF observability and security taxonomy, nono aligns with the SAF-M-74 runtime class [^evt-wg-observability-and-traceability-pr-52]:
- **Enforcement Layer**: Kernel-level sandboxing separating host processes from agent tool execution environments.
- **Audit Schemas**: Seven-record session audit structures verified against nono's alpha hashing scheme and golden test vectors [^evt-wg-observability-and-traceability-pr-52].
- **Boundary Mediation**: Monitors and constrains interactions across the Agent → Gateway / Runtime boundary and Agent → Tool execution paths [^evt-wg-observability-and-traceability-pr-52].

## Observability and Distributed Tracing Gaps

Analysis within the Observability & Traceability Working Group highlighted that nono's baseline sandbox isolation does not propagate W3C distributed trace context headers into execution sandboxes [^evt-wg-observability-and-traceability-pr-52]:
- **Context Propagation**: Environment variables such as `TRACEPARENT`, `TRACESTATE`, and `BAGGAGE` are blocked by default sandbox environment sanitization.
- **Audit Linkage**: Subprocess and kernel audit records currently lack an explicit upstream `trace_id` reference, decoupling runtime telemetry from high-level LLM orchestrator traces [^evt-wg-observability-and-traceability-pr-52].
- **Planned Remediation**: Introduction of a configurable default allow-list for W3C trace context propagation and OTLP exporter integration [^evt-wg-observability-and-traceability-pr-52].

# References

- Cross-Boundary Model: [./cross-boundary-observability-model.md](./cross-boundary-observability-model.md)
- Attested Isolated Runtime Pattern: [../patterns/attested-isolated-runtime.md](../patterns/attested-isolated-runtime.md)

[^evt-wg-observability-and-traceability-pr-52]: https://github.com/aaif/wg-observability-and-traceability/pull/52
