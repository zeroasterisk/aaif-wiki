---
type: standard
title: Agent Resource Discovery (ARD)
description: Decentralized discovery, verification, and admission specification enabling
  agents to find, trust, and instrument capabilities across five lifecycle stages.
resource: https://github.com/aaif/wg-observability-and-traceability/issues/49
tags:
- standard
- discovery
- trust
- observability
- otlp
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T10:18:17.522815+00:00'
sources:
- id: evt-wg-observability-and-traceability-issue-49
  resource: https://github.com/aaif/wg-observability-and-traceability/issues/49
  author: 91pavan
  last_modified: '2026-09-02T05:53:28+00:00'
---

# Overview
Agent Resource Discovery (ARD) is a decentralized specification and lifecycle architecture enabling AI agents to discover, verify, govern, and admit external resources, tools, and skills across system boundaries[^evt-wg-observability-and-traceability-issue-49]. ARD ensures that agent resource acquisition is subject to deterministic trust evaluation, governance checks, and end-to-end telemetry rather than unverified dynamic loading[^evt-wg-observability-and-traceability-issue-49].

Instrumentation and telemetry standards for ARD are reviewed in collaboration with the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md).

# Architecture / Specification
ARD defines a five-stage capability acquisition lifecycle, each emitting structured telemetry correlated via W3C Trace Context and exported through standard OTLP pipelines[^evt-wg-observability-and-traceability-issue-49]:

1. **Discovery:** The initial search, querying, and identification of prospective external resources or endpoints.
2. **Provenance:** Tracing the authoring origin, release signature, and supply chain integrity of the discovered capability.
3. **Governance:** Evaluating environmental policies, runtime constraints, and organizational permission boundaries.
4. **Trust:** Cryptographic verification, reputation scoring, and attestation checks assessing capability reliability.
5. **Decision:** Explicit admission, conditional quarantine, or rejection of the resource prior to runtime loading.

Admitted resources emit correlation spans linking the admission decision directly to subsequent activation and execution inside runtimes such as [Goose](../resources/goose.md) or proxy layers such as Agent Gateway, ensuring that quarantined capabilities produce zero unauthorized execution spans[^evt-wg-observability-and-traceability-issue-49].

# Lifecycle History
- **September 2026:** PoC validation established export of all five lifecycle stages via OpenTelemetry (OTLP JSON fixtures) and correlation with skill activation in Agent Gateway and Goose[^evt-wg-observability-and-traceability-issue-49].

[^evt-wg-observability-and-traceability-issue-49]: https://github.com/aaif/wg-observability-and-traceability/issues/49
