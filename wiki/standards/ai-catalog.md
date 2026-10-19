---
type: standard
title: AI Catalog
description: Open specification and discovery mechanism indexing AI tools, agents,
  and capabilities across flexible publisher-anchored endpoints.
resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/lf-ai-catalog.yaml
tags:
- external
- standards
- discovery
- ai-catalog
- identity
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T01:41:02.362510+00:00'
sources:
- id: evt-ext-frmoretto-agentic-standards-map-85d122-file-1dc63a622af1-34fe162d
  resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/lf-ai-catalog.yaml
  author: frmoretto
  last_modified: '2026-10-14T06:46:06+02:00'
---

# Overview

AI Catalog is an open JSON specification and discovery mechanism developed in a temporary working repository maintained by the Linux Foundation.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-1dc63a622af1-34fe162d] It structures machine-readable indexes of AI agents, skills, tools, and model endpoints to simplify automated discovery across heterogeneous platforms. The project is governed by a four-seat Technical Steering Committee (TSC), with two seats nominated by the MCP core maintainers and two by the A2A TSC.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-1dc63a622af1-34fe162d]

Within the broader discovery ecosystem, AI Catalog maintains a loose coupling with [Agentic Resource Discovery (ARD)](../standards/agentic-resource-discovery.md), serving as an artifact-level indexing format rather than a unified transport protocol.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-1dc63a622af1-34fe162d]

# Architecture / Specification

AI Catalog standardizes how publishers declare catalogs and assert cryptographic provenance over listed components:[^evt-ext-frmoretto-agentic-standards-map-85d122-file-1dc63a622af1-34fe162d]

- **Flexible Endpoint Hosting:** Per Architectural Decision Record ADR-0011, hosting catalogs at `/.well-known/` conventional URIs is optional by design rather than mandatory; catalogues may be served from arbitrary URLs.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-1dc63a622af1-34fe162d]
- **Identifier Separation:** Artifact identity is formally separated from registry hosting coordinates per ADR-0021, utilizing `urn:air` names anchored to publisher domains.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-1dc63a622af1-34fe162d]
- **Trust Manifest Verification:** Publishers assert authority through signed Entry Trust Manifests verified via `did:web` resolution, establishing publisher-domain control without asserting subjective reputation scores.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-1dc63a622af1-34fe162d]
- **Policy and Terms Binding:** Manifests bind structured fields for `termsOfServiceUrl` and `privacyPolicyUrl`, while commercial access, pricing, and monetization metadata are delegated to modular extensions.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-1dc63a622af1-34fe162d]

# Lifecycle History

- 2026-04-02: ADR-0011 accepted, establishing that conventional well-known discovery paths are optional and catalogues may be served from any URL.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-1dc63a622af1-34fe162d]
- 2026-06-19: Community proposal filed (issue #46) requesting formal transition under the Agentic AI Foundation.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-1dc63a622af1-34fe162d]
- 2026-10-01: PR #110 merged, incorporating `did:web` signature verification for Entry Trust Manifests.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-1dc63a622af1-34fe162d]
- 2026-10-03: Issue #46 closed as completed; repository remains in temporary Linux Foundation location pending permanent governance transition.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-1dc63a622af1-34fe162d]
- 2026-10-08: PR #119 merged defining standardized implementation classifications.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-1dc63a622af1-34fe162d]

# References

- GitHub Repository: [Agent-Card/ai-catalog](https://github.com/Agent-Card/ai-catalog)
- Standards Landscape Entry: [lf-ai-catalog.yaml](https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/lf-ai-catalog.yaml)

[^evt-ext-frmoretto-agentic-standards-map-85d122-file-1dc63a622af1-34fe162d]: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/lf-ai-catalog.yaml
