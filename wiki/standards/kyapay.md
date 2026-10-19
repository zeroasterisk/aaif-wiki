---
type: standard
title: KYAPay
description: Draft token and authorization specification extending OAuth to convey
  verified agent identity, human delegation, and payment credentials.
resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/kyapay.yaml
tags:
- external
- standards
- identity
- payments
- oauth
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T01:41:02.362510+00:00'
sources:
- id: evt-ext-frmoretto-agentic-standards-map-85d122-file-24a6817ef1b1-6082e1c0
  resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/kyapay.yaml
  author: frmoretto
  last_modified: '2026-10-14T06:46:06+02:00'
---

# Overview

KYAPay is an open agent identity and payment token specification stewarded by Skyfire.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-24a6817ef1b1-6082e1c0] The specification is published as a family of individual Internet-Drafts named for the Internet Engineering Task Force (IETF) OAuth Working Group but not adopted by it (no stream defined).[^evt-ext-frmoretto-agentic-standards-map-85d122-file-24a6817ef1b1-6082e1c0] KYAPay provides a structured JSON Web Token (JWT) format linking verified human principal identity, agent platform identity, and runtime agent instance parameters with optional payment method claims, allowing merchant web infrastructure and bot mitigation systems to distinguish legitimate, authorized AI agents from automated scraping or abusive traffic.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-24a6817ef1b1-6082e1c0]

KYAPay relies on existing web OAuth infrastructure rather than decentralized identifiers.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-24a6817ef1b1-6082e1c0]

# Architecture / Specification

The KYAPay architecture bundles Know-Your-Agent (KYA) and payment (PAY) verification into signed tokens:[^evt-ext-frmoretto-agentic-standards-map-85d122-file-24a6817ef1b1-6082e1c0]

- **Identity Binding:** Defines explicit claims distinguishing the human principal authorizing the agent (`hid`), the agent instance (`aid`), and the hosting agent platform domain (`apd`).[^evt-ext-frmoretto-agentic-standards-map-85d122-file-24a6817ef1b1-6082e1c0]
- **Payment Credential Transport:** Embeds verified payment capability assertions directly inside the OAuth token structure to permit low-friction checkout authorizations.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-24a6817ef1b1-6082e1c0]
- **Specification Family:** Comprises modular drafts covering core token syntax (`draft-skyfire-oauth-kyapay-token`), usage conventions (`draft-skyfire-oauth-using-kyapay-tokens`), authentication context method references (`amr-values`), human identity verification (`id-verification`), and anti-money laundering verification methods (`aml-methods`).[^evt-ext-frmoretto-agentic-standards-map-85d122-file-24a6817ef1b1-6082e1c0]
- **Verification Context:** Evaluated at merchant edges, content delivery networks (CDNs), and web application firewalls (WAFs) to dynamically allow automated interactions that carry verified delegation proofs.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-24a6817ef1b1-6082e1c0]

# Lifecycle History

- 2026-06-20: Individual Internet-Draft `draft-skyfire-oauth-kyapayprofile-02` published.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-24a6817ef1b1-6082e1c0]
- 2026-07-19: Token exchange mechanism published as `draft-skyfire-oauth-kyapay-token-exchange-01`.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-24a6817ef1b1-6082e1c0]
- 2026-10-01: Author published revision batch updating `kyapay-token-02`, `using-kyapay-tokens-01`, `amr-values-02`, `id-verification-02`, and `aml-methods-01`.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-24a6817ef1b1-6082e1c0]
- 2026-10-02: Revisions announced to the IETF OAuth mailing list for broad security and bot-management review.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-24a6817ef1b1-6082e1c0]

# References

- Standards Landscape Entry: [kyapay.yaml](https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/kyapay.yaml)

[^evt-ext-frmoretto-agentic-standards-map-85d122-file-24a6817ef1b1-6082e1c0]: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/kyapay.yaml
