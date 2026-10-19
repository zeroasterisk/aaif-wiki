---
type: resource
title: Agentic Standards Map
description: Independent comparative catalog and cross-venue landscape tracking agent
  commerce, identity, discovery, and payment specifications.
resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/mastercard-agent-pay.yaml
tags:
- external
- standards
- landscape
- commerce
- identity
- discovery
- payments
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T01:51:39.108682+00:00'
sources:
- id: evt-ext-frmoretto-agentic-standards-map-85d122-file-b284c7b2f467-be09154e
  resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/mastercard-agent-pay.yaml
  author: frmoretto
  last_modified: '2026-10-14T06:46:06+02:00'
- id: evt-ext-frmoretto-agentic-standards-map-85d122-file-b6e427b588e4-53205881
  resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/pact.yaml
  author: frmoretto
  last_modified: '2026-10-14T04:52:24+02:00'
- id: evt-ext-frmoretto-agentic-standards-map-85d122-file-be2d45123576-7507142b
  resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/gs1-digital-link.yaml
  author: frmoretto
  last_modified: '2026-10-14T04:52:24+02:00'
- id: evt-ext-frmoretto-agentic-standards-map-85d122-file-bf96ac33a19a-a404b5c0
  resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/aaif-identity-trust.yaml
  author: frmoretto
  last_modified: '2026-10-14T06:28:09+02:00'
- id: evt-ext-frmoretto-agentic-standards-map-85d122-file-c347d8770adb-bfcfd8ae
  resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/ietf-individual-seller-drafts.yaml
  author: frmoretto
  last_modified: '2026-10-14T06:28:09+02:00'
- id: evt-ext-frmoretto-agentic-standards-map-85d122-file-c5793003b540-04312fc6
  resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/untp-identity-resolver.yaml
  author: frmoretto
  last_modified: '2026-10-14T06:28:09+02:00'
---

# Overview
The Agentic Standards Map is an independent comparative catalog stewarded by Francesco Marinoni Moretto tracking cross-venue agent protocols across identity, commerce, discovery, and payments [^evt-ext-frmoretto-agentic-standards-map-85d122-file-b284c7b2f467-be09154e]. The project systematically maps overlapping specifications, protocol boundaries, and verification seams across major standards developing organizations and commercial initiatives [^evt-ext-frmoretto-agentic-standards-map-85d122-file-b284c7b2f467-be09154e] [^evt-ext-frmoretto-agentic-standards-map-85d122-file-b6e427b588e4-53205881].

The landscape covers both AAIF projects and external initiatives from bodies such as the IETF, W3C, FIDO Alliance, GS1, UN/CEFACT, and industry vendors [^evt-ext-frmoretto-agentic-standards-map-85d122-file-be2d45123576-7507142b] [^evt-ext-frmoretto-agentic-standards-map-85d122-file-c5793003b540-04312fc6].

# Tracked Specifications and Landscape Coverage
The repository inventories specifications across several operational seams:

- **Agent Identity & Delegation**: Tracks specifications including [Personal Agent Consent & Trust Protocol (PACT)](../standards/pact.md) by Decagon/Instinct, [KyaPay](../standards/kyapay.md), and active discussions within the [AAIF Identity and Trust Working Group](../working-groups/identity-and-trust.md) regarding [TRACE](../standards/trace.md) integration [^evt-ext-frmoretto-agentic-standards-map-85d122-file-b6e427b588e4-53205881] [^evt-ext-frmoretto-agentic-standards-map-85d122-file-bf96ac33a19a-a404b5c0].
- **Payment & Commercial Acceptance**: Analyzes payment frameworks such as [Mastercard Agent Pay](../standards/mastercard-agent-pay.md), [Visa Trusted Agent Protocol](../standards/visa-trusted-agent-protocol.md), [AP2](../standards/ap2.md), and [IETF Web Bot Auth](../standards/ietf-webbotauth.md) [^evt-ext-frmoretto-agentic-standards-map-85d122-file-b284c7b2f467-be09154e].
- **Discovery and Resolution**: Tracks product and entity resolution standards, including GS1 Digital Link Syntax 1.7.0 [^evt-ext-frmoretto-agentic-standards-map-85d122-file-be2d45123576-7507142b], UN/CEFACT UN Transparency Protocol Identity Resolver (v0.7.0) [^evt-ext-frmoretto-agentic-standards-map-85d122-file-c5793003b540-04312fc6], and individual IETF drafts for offering discovery and merchant identity assertions [^evt-ext-frmoretto-agentic-standards-map-85d122-file-c347d8770adb-bfcfd8ae].
- **Agent Communication & Protocols**: Catalogs inter-agent interaction models such as [Agent-to-Agent (A2A)](../standards/a2a.md) and [Personal Agent Protocol](../standards/personal-agent-protocol.md) [^evt-ext-frmoretto-agentic-standards-map-85d122-file-b6e427b588e4-53205881].

# References
- [Agentic Standards Map Repository](https://github.com/frmoretto/agentic-standards-map) [^evt-ext-frmoretto-agentic-standards-map-85d122-file-b284c7b2f467-be09154e]

[^evt-ext-frmoretto-agentic-standards-map-85d122-file-b284c7b2f467-be09154e]: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/mastercard-agent-pay.yaml
[^evt-ext-frmoretto-agentic-standards-map-85d122-file-b6e427b588e4-53205881]: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/pact.yaml
[^evt-ext-frmoretto-agentic-standards-map-85d122-file-be2d45123576-7507142b]: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/gs1-digital-link.yaml
[^evt-ext-frmoretto-agentic-standards-map-85d122-file-bf96ac33a19a-a404b5c0]: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/aaif-identity-trust.yaml
[^evt-ext-frmoretto-agentic-standards-map-85d122-file-c347d8770adb-bfcfd8ae]: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/ietf-individual-seller-drafts.yaml
[^evt-ext-frmoretto-agentic-standards-map-85d122-file-c5793003b540-04312fc6]: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/untp-identity-resolver.yaml
