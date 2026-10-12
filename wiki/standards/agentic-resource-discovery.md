---
type: standard
title: Agentic Resource Discovery
description: Decentralized specification and discovery architecture enabling agents
  to find and verify AI resources via static catalogs and dynamic registries.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/meeting-minutes/2026-07-09.md
tags:
- standard
- discovery
- registry
- trust
- spiffe
- ans
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:03:51.203894+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-4b349715463d-4901531a
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/meeting-minutes/2026-07-09.md
  author: Pavan Sudheendra
  last_modified: '2026-07-09T16:05:08+01:00'
---

# Overview

The Agentic Resource Discovery (ARD) specification is a decentralized architecture enabling AI agents to discover, evaluate, and verify tools, models, skills, and remote capabilities.[^evt-wg-observability-and-traceability-file-4b349715463d-4901531a] Developed in collaboration across industry partners, ARD pairs static capability indexing with dynamic query endpoints and cryptographic trust manifests to prevent rogue tool execution and untrusted capability invocation.[^evt-wg-observability-and-traceability-file-4b349715463d-4901531a]

# Architecture / Specification

### Dual Discovery Modalities
ARD defines two complementary mechanisms for discovering agentic resources:[^evt-wg-observability-and-traceability-file-4b349715463d-4901531a]
1. **Catalog (Static Indexing)**: Declarative, machine-readable manifests publishing static metadata, schema signatures, natural language search keywords, and security parameters for offline indexing and compilation.
2. **Registry (Dynamic Service)**: Active query interface providing REST APIs for dynamic runtime lookup, health state, latency metrics, and real-time capability routing.

### Trust and Identification Layer
To ensure resource authenticity, ARD embeds decentralized identity standards:[^evt-wg-observability-and-traceability-file-4b349715463d-4901531a]
- **SPIFFE Support**: Cryptographic workload identity verification for containerized agent tools and endpoints.
- **ANS Integration**: Compatibility with Agent Network Standards (ANS) for inter-agent routing and capability discovery.
- **Trust Manifests**: Signed resource attestation records validating publisher provenance and security posture before admission to runtime contexts.

# Lifecycle History

- **2026-07-09**: Presented to the Observability & Traceability Working Group following a joint multi-company announcement; alignment identified with agent identity and registry focus areas.[^evt-wg-observability-and-traceability-file-4b349715463d-4901531a]

# References

- Related Working Groups: [Observability & Traceability](../working-groups/observability-and-traceability.md), [Identity and Trust](../working-groups/identity-and-trust.md)
- Related Standards: [Agent Network Protocol](agent-network-protocol.md), [Agent Skills](agent-skills.md)
- Related Resources: [MCP Gateway Registry](../resources/mcp-gateway-registry.md)

[^evt-wg-observability-and-traceability-file-4b349715463d-4901531a]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/meeting-minutes/2026-07-09.md
