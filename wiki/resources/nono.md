---
type: resource
title: nono Agent Runtime Sandbox
description: Open-source agent runtime security tool providing kernel-enforced sandboxing,
  credential isolation, and deterministic cross-boundary audit logs.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/52
tags:
- runtime
- sandbox
- security
- observability
- reference-architecture
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:06:09.211306+00:00'
sources:
- id: evt-wg-observability-and-traceability-pr-52
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/52
  author: Salkimmich
  last_modified: '2026-09-24T03:32:21+00:00'
---

# Overview
`nono` is an open-source agent runtime security framework that executes untrusted AI agent workloads inside kernel-enforced sandboxes with strict credential isolation[^evt-wg-observability-and-traceability-pr-52]. Evaluated under the Primitives and Protocol Observability focus group of the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), `nono` serves as a reference architecture satisfying the SAF-M-74 runtime class by providing hardware- and kernel-level process boundaries, credential protection, and cryptographic execution logs[^evt-wg-observability-and-traceability-pr-52].

# Architecture / Specification
`nono` establishes boundary observability and runtime protection across agent-to-gateway and agent-to-tool boundaries[^evt-wg-observability-and-traceability-pr-52]:
- **Kernel-Enforced Execution Boundary**: Enforces process isolation below Layer 7 to prevent compromised agents or hijacked tools from accessing unauthorized host filesystems or network interfaces[^evt-wg-observability-and-traceability-pr-52].
- **Cryptographic Audit Hashing**: Emits deterministic execution logs validated against golden test vectors and alpha hashing schemes to prove runtime integrity[^evt-wg-observability-and-traceability-pr-52].
- **Trace Context Propagation Limitations**: Current runtime realizations do not propagate standard W3C distributed tracing context (`traceparent`, `tracestate`, `baggage`) into sandboxed execution environments by default, requiring explicit environment variable allow-lists and trace identifier mappings on audit records for full OpenTelemetry correlation[^evt-wg-observability-and-traceability-pr-52].
- **Human-in-the-Loop Integration**: Surfaces runtime evidence records for Agent-to-Human (HITL) checkpoints and authorization delegations[^evt-wg-observability-and-traceability-pr-52].

# Lifecycle History
Reviewed in the Observability and Traceability Working Group under reference architecture `AAIF-REF-ARCH-NONO`, establishing baseline telemetry rows and identifying downstream OTLP export requirements[^evt-wg-observability-and-traceability-pr-52].

[^evt-wg-observability-and-traceability-pr-52]: https://github.com/aaif/wg-observability-and-traceability/pull/52
