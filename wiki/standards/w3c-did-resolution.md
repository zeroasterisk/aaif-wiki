---
type: standard
title: W3C DID Resolution
description: W3C Candidate Recommendation standardizing Decentralized Identifier resolution
  and DID URL dereferencing algorithms across decentralized trust infrastructures.
resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/w3c-did-resolution.yaml
tags:
- external
- standards
- w3c
- identity
- did
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T01:41:02.362510+00:00'
sources:
- id: evt-ext-frmoretto-agentic-standards-map-85d122-file-22c4c749706d-f4a378b4
  resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/w3c-did-resolution.yaml
  author: frmoretto
  last_modified: '2026-10-14T06:46:06+02:00'
---

# Overview

W3C DID Resolution is a decentralized identity specification at W3C Candidate Recommendation stage (Candidate Recommendation Draft 2026-10-01), developed by the World Wide Web Consortium (W3C) Decentralized Identifier (DID) Working Group.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-22c4c749706d-f4a378b4] The specification formally establishes how software components resolve a Decentralized Identifier into a conforming DID document and how DID URLs containing path, query, and fragment components are dereferenced into target resources.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-22c4c749706d-f4a378b4] It serves as a foundational resolution layer for cross-domain agent identity schemes, providing the dereferencing substrate used by decentralized frameworks such as [DIF Trusted AI Agents](../standards/dif-trusted-ai-agents.md) and resolution workflows evaluated in the [Identity and Trust Working Group](../working-groups/identity-and-trust.md).[^evt-ext-frmoretto-agentic-standards-map-85d122-file-22c4c749706d-f4a378b4]

# Architecture / Specification

The specification defines concrete interfaces and processing pipelines for resolving and dereferencing decentralized credentials:[^evt-ext-frmoretto-agentic-standards-map-85d122-file-22c4c749706d-f4a378b4]

- **Resolution vs. Dereferencing:** Formally distinguishes `Resolve()`, which fetches the root DID document representing the subject, from `Dereference()`, which retrieves specific cryptographic keys, service endpoints, or secondary metadata resources referenced by a DID URL.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-22c4c749706d-f4a378b4]
- **Unified Function Signature:** Following Working Group resolution on 2026-09-10, the core specification avoids an isolated abstract `Dereference()` function signature separate from the primary resolution contract.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-22c4c749706d-f4a378b4]
- **Modular Dereferencing Handlers:** Refactored under PR #344 to transition the dereferencing algorithm to a handler architecture, modifying legacy built-in handling of parameters such as `relativeRef` and `serviceType` commonly utilized in digital product passport deployments.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-22c4c749706d-f4a378b4]

# Lifecycle History

- 2026-08-06: Published as W3C Candidate Recommendation Snapshot.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-22c4c749706d-f4a378b4]
- 2026-09-10: Working Group formally resolved not to define an abstract `Dereference()` function signature distinct from `Resolve()`.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-22c4c749706d-f4a378b4]
- 2026-10-01: Candidate Recommendation Draft marked sections 5, 6, 8, 10 and the DID URL dereferencing feature as at risk.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-22c4c749706d-f4a378b4]
- 2026-10-05: W3C patent review exclusion opportunity closed without exclusions.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-22c4c749706d-f4a378b4]
- 2026-10-08: Working Group held a poll on PR #344 (8 for, 1 against), followed by a chair's decision to merge the isolated dereferencing handler algorithm; the minutes do not record the poll as a resolution.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-22c4c749706d-f4a378b4]
- 2026-10-13: PR #344 merged into main branch (commit `0956c93`).[^evt-ext-frmoretto-agentic-standards-map-85d122-file-22c4c749706d-f4a378b4]

# References

- GitHub Repository: [w3c/did-resolution](https://github.com/w3c/did-resolution)
- Standards Landscape Entry: [w3c-did-resolution.yaml](https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/w3c-did-resolution.yaml)

[^evt-ext-frmoretto-agentic-standards-map-85d122-file-22c4c749706d-f4a378b4]: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/w3c-did-resolution.yaml
