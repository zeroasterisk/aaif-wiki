---
type: resource
title: Cross-Boundary Observability Model
description: Multi-layer analysis framework evaluating agent observability gaps across
  LLM primitives, protocol boundaries, and underlying infrastructure.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/working-documents/cross-boundary-observability-model.md
tags:
- observability
- telemetry
- gap-analysis
- boundaries
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:40:40.637301+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-566afac466bc-889ed18a
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/working-documents/cross-boundary-observability-model.md
  author: Pavan Sudheendra
  last_modified: '2026-10-06T04:07:46+01:00'
- id: evt-wg-observability-and-traceability-pr-25
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/25
  author: 91pavan
  last_modified: '2026-10-06T03:07:52+00:00'
---

# Overview

The Cross-Boundary Observability Model is an analytical framework developed by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) to evaluate telemetry and observability gaps across execution boundaries in agentic systems[^evt-wg-observability-and-traceability-file-566afac466bc-889ed18a]. Rather than specifying a new telemetry protocol, the model serves as a coordination artifact for benchmarking existing standards, identifying where cross-system interoperability fails, and focusing targeted upstream contributions[^evt-wg-observability-and-traceability-file-566afac466bc-889ed18a][^evt-wg-observability-and-traceability-pr-25].

# Architecture / Specification

The model organizes observability gap analysis across three distinct operational layers to expose breakdowns in context propagation, provenance, delegation, and responsibility chains[^evt-wg-observability-and-traceability-file-566afac466bc-889ed18a]:

- **LLM Primitive Layer**: Models primary execution entities including agents, skills, tools, foundation models, and memory stores.
- **Protocol Boundary Layer**: Evaluates interaction semantics across external interfaces (such as MCP, A2A, and streaming HTTP) across discovery, negotiation, request/response, delegation, streaming, cancellation, and error handling.
- **Infrastructure Boundary Layer**: Analyzes underlying runtimes, AI gateways, microservices, and network boundaries transporting agent requests.

By evaluating cross-boundary observability questions against this layered topology, the working group systematically identifies unobserved context drops and unverified agent delegations across multi-system handoffs[^evt-wg-observability-and-traceability-file-566afac466bc-889ed18a].

# Lifecycle History

The model was proposed and merged as a working draft within the Observability and Traceability Working Group to support gap analysis and interoperability evaluations[^evt-wg-observability-and-traceability-pr-25].

[^evt-wg-observability-and-traceability-file-566afac466bc-889ed18a]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/working-documents/cross-boundary-observability-model.md
[^evt-wg-observability-and-traceability-pr-25]: https://github.com/aaif/wg-observability-and-traceability/pull/25
