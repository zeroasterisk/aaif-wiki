---
type: resource
title: OpenTelemetry for Agentic AI
description: Reference architecture for vendor-neutral agent telemetry collection,
  OTLP pipelines, and gen_ai semantic conventions.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/67
tags:
- observability
- opentelemetry
- telemetry
- tracing
- genai
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:30:09.197993+00:00'
sources:
- id: evt-wg-observability-and-traceability-pr-67
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/67
  author: StevenMih
  last_modified: '2026-10-28T17:14:13+00:00'
---

# Overview

OpenTelemetry (OTel) provides the vendor-neutral foundation for distributed tracing, metrics, and structured event logging across agentic AI systems through its GenAI semantic conventions (`semantic-conventions-genai`).[^evt-wg-observability-and-traceability-pr-67] Within the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), work focuses on mapping standard OTel telemetry pipelines to cryptographic audit trails and verifiable execution layers.[^evt-wg-observability-and-traceability-pr-67]

# Architecture / Specification

Recent technical proposals delineate five architectural seams required to connect standard OTel GenAI telemetry spans with signed evidence and [Action Record](../taxonomy/action-record.md) layers:[^evt-wg-observability-and-traceability-pr-67]

1. **Span-to-Record Join:** Bi-directional linkage between transient distributed tracing span identifiers and immutable, signed action or evidence record hashes.[^evt-wg-observability-and-traceability-pr-67]
2. **Decision and Approval Seam:** Recording human and policy gating outcomes, approval checkpoint identifiers, and authorization validity metadata directly alongside invocation spans.[^evt-wg-observability-and-traceability-pr-67]
3. **Effect Target and Status:** Distinguishing intended execution effects from actual environmental state mutations and post-condition verification statuses across external tools.[^evt-wg-observability-and-traceability-pr-67]
4. **Evidence Origin:** Propagating witness metadata, cryptographic provenance, and verification vantage points into span attributes as specified in the [Evidence Record Specification](../standards/evidence-record-spec.md).[^evt-wg-observability-and-traceability-pr-67]
5. **Integrity Without Disclosure:** Providing cryptographic digest verification over span payloads and tool arguments to maintain tamper-evidence without exposing sensitive data in telemetry collectors.[^evt-wg-observability-and-traceability-pr-67]

[^evt-wg-observability-and-traceability-pr-67]: https://github.com/aaif/wg-observability-and-traceability/pull/67
