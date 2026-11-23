---
type: standard
title: Agentic Resource Discovery
description: Decentralized discovery and verification specification enabling agents
  to resolve, verify, and bind AI resources via catalogs, registries, and trust manifests.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/meeting-minutes/2026-07-09.md
tags:
- aaif
- standards
- discovery
- registry
- catalog
- spiffe
- ans
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T09:40:05.409005+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-4b349715463d-4901531a
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/meeting-minutes/2026-07-09.md
  author: Pavan Sudheendra
  last_modified: '2026-07-09T16:05:08+01:00'
---

# Overview

Agentic Resource Discovery (ARD) is an open specification for discovering, querying, and cryptographically verifying AI tools, models, and agent capabilities in decentralized environments[^evt-wg-observability-and-traceability-file-4b349715463d-4901531a]. Presented by Junjie Bu in coordination with a consortium of ten industry participants, ARD enables autonomous agents to locate compatible external resources dynamically without relying on centralized single points of trust[^evt-wg-observability-and-traceability-file-4b349715463d-4901531a].

# Architecture / Specification

The ARD architecture divides resource location and admission into two complementary planes[^evt-wg-observability-and-traceability-file-4b349715463d-4901531a]:

- **Static Catalog**: A statically indexed, declarative publication format that exposes available tools, endpoints, and schemas for offline indexing or cold start discovery[^evt-wg-observability-and-traceability-file-4b349715463d-4901531a].
- **Dynamic Registry**: A runtime discovery service providing REST APIs and semantic query interfaces, allowing agents to execute natural language queries against operational tool offerings[^evt-wg-observability-and-traceability-file-4b349715463d-4901531a].

## Trust and Verification

ARD incorporates verifiable identity and boundary validation mechanisms to mitigate supply-chain attacks such as tool poisoning:

- **Decentralized Trust Models**: Integrates with SPIFFE (Secure Production Identity Framework for Everyone) and Agent Network Standard (ANS) naming conventions to attest provider identity across administrative domains[^evt-wg-observability-and-traceability-file-4b349715463d-4901531a].
- **Trust Manifests**: Cryptographically signed attestations accompanying resource registrations that certify provenance, behavioral boundaries, and policy compliance prior to agent invocation[^evt-wg-observability-and-traceability-file-4b349715463d-4901531a].

# Lifecycle History

- **2026-07-09**: Presented to the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) as a joint specification authored with ten collaborating organizations, initiating review of identity standard overlaps and traceability telemetry requirements[^evt-wg-observability-and-traceability-file-4b349715463d-4901531a].

# References

- Identity and Trust WG: [../working-groups/identity-and-trust.md](../working-groups/identity-and-trust.md)
- Observability and Traceability WG: [../working-groups/observability-and-traceability.md](../working-groups/observability-and-traceability.md)
- Agent Network Protocol: [agent-network-protocol.md](agent-network-protocol.md)
- Agent Identity Primitives: [agent-identity-primitives.md](agent-identity-primitives.md)

[^evt-wg-observability-and-traceability-file-4b349715463d-4901531a]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/meeting-minutes/2026-07-09.md
