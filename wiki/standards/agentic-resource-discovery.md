---
type: standard
title: Agentic Resource Discovery Specification
description: Decentralized discovery, verification, and admission specification enabling
  agents to find, trust, and verify AI resources via catalogs and dynamic registries.
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
  at: '2026-11-02T09:38:13.242968+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-4b349715463d-4901531a
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/meeting-minutes/2026-07-09.md
  author: Pavan Sudheendra
  last_modified: '2026-07-09T16:05:08+01:00'
---

# Overview
The Agentic Resource Discovery (ARD) specification defines a decentralized architecture for discovering, evaluating, and verifying AI tools, capabilities, and agent resources across administrative boundaries[^evt-wg-observability-and-traceability-file-4b349715463d-4901531a]. Jointly announced by a multi-vendor consortium of 11 organizations, ARD standardizes how autonomous agents locate trusted endpoints while enforcing provenance and identity guarantees.

# Architecture / Specification
The ARD specification is structured around two core functional components[^evt-wg-observability-and-traceability-file-4b349715463d-4901531a]:

- **Catalog (Static Indexing)**: Declarative, machine-readable manifests enabling offline search, capability indexing, and structural schema inspection.
- **Registry (Dynamic REST API)**: Active control plane exposing RESTful endpoints for runtime admission, health validation, and dynamic capability lookup.

### Trust and Identification Model
ARD integrates with decentralized identity and security frameworks to establish cryptographically verifiable discovery:

- **Identity Federation**: Leverages SPIFFE (Secure Production Identity Framework for Everyone) and ANS (Agent Name Service) standards to authenticate agents and resource providers[^evt-wg-observability-and-traceability-file-4b349715463d-4901531a].
- **Trust Manifests**: Encodes cryptographic attestation and authorization requirements within discovery metadata, enabling consuming agents to verify endpoint integrity prior to execution.
- **Natural Language Search**: Implements semantic and natural language discovery layers that resolve plain-language agent requests to verified interface contracts[^evt-wg-observability-and-traceability-file-4b349715463d-4901531a].

# Lifecycle History
- **2026-07-09**: Presented to the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) by Junjie Bu following joint industry announcement; initiated cross-group reviews on identity standards, ANS integration, and telemetry trace correlation[^evt-wg-observability-and-traceability-file-4b349715463d-4901531a].

[^evt-wg-observability-and-traceability-file-4b349715463d-4901531a]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/meeting-minutes/2026-07-09.md
