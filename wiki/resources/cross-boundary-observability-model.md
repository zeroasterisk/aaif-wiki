---
type: resource
title: Cross-Boundary Observability Model
description: Multi-layer observability framework mapping telemetry propagation, governance
  gaps, and context preservation across agent, runtime, tool, and human approval boundaries.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/52
tags:
- observability
- runtime
- boundaries
- telemetry
- hitl
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T10:37:58.858547+00:00'
sources:
- id: evt-wg-observability-and-traceability-pr-52
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/52
  author: Salkimmich
  last_modified: '2026-09-24T03:32:21+00:00'
---

# Overview
The Cross-Boundary Observability Model analyzes telemetry continuity, identity preservation, and security enforcement across agent operational interfaces [^evt-wg-observability-and-traceability-pr-52]. Maintained by the Observability and Traceability Working Group, the model categorizes observation capabilities and governance gaps across distinct interaction planes: Agent to Gateway/Runtime, Agent to Tool, and Agent to Human (HITL) [^evt-wg-observability-and-traceability-pr-52].

# Architecture / Specification
The framework maps interactions across layers, protocol boundaries, and enforcement points.

### Boundary Definitions
- **Agent → Gateway / Runtime**: Intercepts tool dispatches, mediation policies, and isolation parameters. In kernel-enforced runtimes (e.g., the SAF-M-74 reference class exemplified by the `nono` sandbox), enforcement occurs below L7 at the OS boundary [^evt-wg-observability-and-traceability-pr-52]. Observed implementations reveal critical telemetry constraints, such as sandbox runtimes failing to propagate standard W3C trace context (`traceparent`, `tracestate`, `baggage`) across isolation barriers [^evt-wg-observability-and-traceability-pr-52].
- **Agent → Human (HITL)**: Captures human interaction records, decision rationale, approval metadata, and delegation authority, linking human actions to machine execution chains [^evt-wg-observability-and-traceability-pr-52].
- **Agent → Tool**: Tracks invocation parameters, authorization context, and provenance values.

### Enforcement Classification
Working group proposals analyze whether `enforcement_layer` (categorized as `kernel`, `broker`, or `proxy`) should be structured as an explicit architectural boundary column or as an evaluated provenance attribute within audit schemas [^evt-wg-observability-and-traceability-pr-52].

# Lifecycle History
- **2026-09**: Incorporated lower-layer runtime and HITL boundary rows into the Primitives and Protocol Observability focus group living documents, establishing benchmark fixtures from kernel-enforced execution environments [^evt-wg-observability-and-traceability-pr-52].

[^evt-wg-observability-and-traceability-pr-52]: https://github.com/aaif/wg-observability-and-traceability/pull/52
