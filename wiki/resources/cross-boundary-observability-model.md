---
type: resource
title: Cross-Boundary Observability Model
description: Reference architecture evaluating boundary telemetry propagation, control-plane
  evidence provenance, and kernel-enforced runtime tracing.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/52
tags:
- observability
- telemetry
- boundaries
- runtime
- provenance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T03:06:54.015360+00:00'
sources:
- id: evt-wg-observability-and-traceability-pr-52
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/52
  author: Salkimmich
  last_modified: '2026-09-24T03:32:21+00:00'
---

# Overview
The Cross-Boundary Observability Model is an evaluation matrix and reference architecture analyzing telemetry propagation, security attestation, and evidence provenance across critical agentic boundaries.[^evt-wg-observability-and-traceability-pr-52] Developed within the Primitives and Protocol Observability focus group of the Observability and Traceability Working Group, the model categorizes telemetry expectations between agents, runtimes, external tools, gateways, and human supervisors.[^evt-wg-observability-and-traceability-pr-52]

# Architecture / Specification
The model standardizes telemetry and security attributes across four primary operational boundaries:[^evt-wg-observability-and-traceability-pr-52]
- **Agent → Tool (MCP / CLI)**: Evaluates command payload logging, tool provenance, and security isolation at the invocation boundary.[^evt-wg-observability-and-traceability-pr-52]
- **Agent → Gateway / Runtime**: Covers interactions with policy gateways and execution engines (such as the SAF-M-74 class and the nono runtime). It models enforcement layers categorized as kernel, broker, or proxy, alongside cryptographic execution hashes and golden vector validation.[^evt-wg-observability-and-traceability-pr-52]
- **Agent → Human (HITL)**: Captures human-in-the-loop approval relationships, tracking approval checkpoints, delegation chains, and decision attribution records.[^evt-wg-observability-and-traceability-pr-52]
- **Agent → Agent (A2A)**: Evaluates mutual identity verification, authorization delegation, and distributed turn tracking.[^evt-wg-observability-and-traceability-pr-52]

A key technical challenge identified in kernel-enforced sandboxed runtimes (such as nono) is that W3C distributed trace context (`TRACEPARENT`, `TRACESTATE`, `BAGGAGE`) is not automatically propagated into the execution sandbox by default, requiring explicit environment allow-lists to correlate in-sandbox telemetry with outer workflow traces.[^evt-wg-observability-and-traceability-pr-52]

# Lifecycle History
In September 2026, PR #52 expanded the model by formalizing below-L7 kernel-enforced runtime rows, defining the Agent → Gateway/Runtime and Agent → Human matrix mappings, and documenting trace propagation boundaries in sandboxed environments.[^evt-wg-observability-and-traceability-pr-52]

# References
- [../patterns/attested-isolated-runtime.md](../patterns/attested-isolated-runtime.md)
- [../patterns/approval-checkpoint.md](../patterns/approval-checkpoint.md)
- [../standards/agent-behavior-trace-model.md](../standards/agent-behavior-trace-model.md)
- [../working-groups/observability-and-traceability.md](../working-groups/observability-and-traceability.md)

[^evt-wg-observability-and-traceability-pr-52]: https://github.com/aaif/wg-observability-and-traceability/pull/52
