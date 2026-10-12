---
type: standard
title: Agent Resource Discovery
description: Specification and observability framework for discovering, evaluating,
  and admitting AI skills and resources through policy gateways and agent runtimes.
resource: https://github.com/aaif/wg-observability-and-traceability/issues/49
tags:
- standards
- discovery
- governance
- mcp
- skills
- observability
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T02:55:22.043720+00:00'
sources:
- id: evt-wg-observability-and-traceability-issue-49
  resource: https://github.com/aaif/wg-observability-and-traceability/issues/49
  author: 91pavan
  last_modified: '2026-09-02T05:53:28+00:00'
---

# Overview
Agent Resource Discovery (ARD) is an open specification and protocol observability framework for dynamically discovering, verifying, and admitting agent skills, tools, and endpoints across policy enforcement boundaries. By defining telemetry across discovery, provenance, governance, and policy evaluation phases, ARD allows agent gateways and execution environments to make verifiable admission decisions and correlate admitted capabilities with subsequent skill execution.

# Architecture / Specification
The ARD lifecycle instrumentation framework standardizes telemetry and state evaluation across five sequential stages [^evt-wg-observability-and-traceability-issue-49]:

1. **Discovery**: Querying and locating candidate agent resources, endpoints, and tool packages.
2. **Provenance**: Validating origin manifests, signatures, and publisher attestation records.
3. **Governance**: Evaluating capabilities against local policy engines and organizational constraints.
4. **Trust**: Appraising cryptographic assertions, delegation credentials, and trust scores.
5. **Decision**: Emitting an admission determination, resulting either in capability enablement or quarantine.

Observability data across these stages is exported via standard [OpenTelemetry](../resources/opentelemetry.md) (OTLP) pipelines using the experimental `ard.*` namespace [^evt-wg-observability-and-traceability-issue-49]. To maintain end-to-end lineage, admission records propagate W3C Trace Context headers into runtime environments such as [Goose](../resources/goose.md) to correlate admitted skills with downstream execution spans (`gen_ai.skill.*`) [^evt-wg-observability-and-traceability-issue-49]. Quarantined or rejected capabilities record evaluation decisions without generating synthetic execution spans [^evt-wg-observability-and-traceability-issue-49].

# Lifecycle History
Tracking under the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), an active proof of concept validates ARD lifecycle telemetry across Agent Gateway and Goose, testing cross-agent portability and standard OTLP JSON export compatibility [^evt-wg-observability-and-traceability-issue-49].

[^evt-wg-observability-and-traceability-issue-49]: https://github.com/aaif/wg-observability-and-traceability/issues/49
