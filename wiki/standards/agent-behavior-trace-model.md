---
type: standard
title: Agent Behavior Trace Model
description: Open telemetry and behavioral trace specification defining agent turn
  boundaries, causal execution links, and test kits for evidence-grade verification.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/57
tags:
- standards
- observability
- tracing
- telemetry
- conformance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:24:45.883098+00:00'
sources:
- id: evt-wg-observability-and-traceability-pr-57
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/57
  author: astrogilda
  last_modified: '2026-10-10T02:46:49+00:00'
---

# Overview

The Agent Behavior Trace Model is an open telemetry specification defining semantic conventions and causal graph structures for AI agent executions [^evt-wg-observability-and-traceability-pr-57]. It captures agent turn boundaries, prompt/response cycles, tool dispatches, and verification evidence into standardized trace formats compatible with OpenTelemetry (OTLP).

The specification is maintained by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md).

# Architecture / Specification

### Conformance and Trace Test Kit

The specification includes an automated test kit covering effect and evidence-grade trace verification [^evt-wg-observability-and-traceability-pr-57]:
- **OTLP/JSON Test Vectors**: Standard test cases covering duplicate receipts, missing receipts, valid and invalid cryptographic signatures, ticket ID alterations, and cross-tenant action ID reuse [^evt-wg-observability-and-traceability-pr-57].
- **Contextual Query Parsing**: Readers extract query contexts from foundational manifests (`basis.json`) prior to asserting expected graph states [^evt-wg-observability-and-traceability-pr-57].
- **Evidence Qualification Boundaries**: Separation of signature validity checking from real-world effect correlation, distinguishing synthetic verification vectors from full tenant effect correlation [^evt-wg-observability-and-traceability-pr-57].

### Telemetry Structure

- **Turn Spans**: Bounded spans encapsulating single model reasoning cycles.
- **Tool Execution Events**: Child spans linking tool invocations with returned payloads and status codes.
- **Evidence Receipts**: Cryptographically signed proof bundles binding agent observations to underlying system artifacts.

# Lifecycle History

- Trace-model CI test kit introduced with test vectors for receipt validation, signature status, and multi-tenant action isolation [^evt-wg-observability-and-traceability-pr-57].

[^evt-wg-observability-and-traceability-pr-57]: https://github.com/aaif/wg-observability-and-traceability/pull/57
