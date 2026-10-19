---
type: standard
title: Mastercard Agent Pay
description: Commercial agentic payment acceptance framework stewarded by Mastercard
  integrating Web Bot Auth verification and dynamic agentic tokens.
resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/mastercard-agent-pay.yaml
tags:
- external
- commerce
- payments
- identity
- specification
- tokens
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T01:51:39.108682+00:00'
sources:
- id: evt-ext-frmoretto-agentic-standards-map-85d122-file-b284c7b2f467-be09154e
  resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/mastercard-agent-pay.yaml
  author: frmoretto
  last_modified: '2026-10-14T06:46:06+02:00'
---

# Overview
Mastercard Agent Pay is an agent payment acceptance framework stewarded by Mastercard for agent-initiated commercial transactions [^evt-ext-frmoretto-agentic-standards-map-85d122-file-b284c7b2f467-be09154e]. The framework establishes identity validation, pre-transaction agent verification, and tokenized execution within existing merchant payment rails [^evt-ext-frmoretto-agentic-standards-map-85d122-file-b284c7b2f467-be09154e].

Mastercard Agent Pay operates alongside merchant checkout flows, combining content delivery network (CDN) edge authentication with payment tokens designed to conform with legacy checkout form structures [^evt-ext-frmoretto-agentic-standards-map-85d122-file-b284c7b2f467-be09154e]. It interfaces with cryptographic identity mechanisms such as [IETF Web Bot Auth](../standards/ietf-webbotauth.md) and relates to parallel industry initiatives including [Visa Trusted Agent Protocol](../standards/visa-trusted-agent-protocol.md) and [KyaPay](../standards/kyapay.md).

# Architecture / Specification
The framework defines three primary operational layers:

- **Agent Registration and Verification**: Agents must register and verify authenticity before attempting transactions [^evt-ext-frmoretto-agentic-standards-map-85d122-file-b284c7b2f467-be09154e].
- **Edge Authentication via Web Bot Auth**: Leverages the emerging Web Bot Auth standard at the CDN layer (Mastercard partnered with Cloudflare to support Web Bot Auth in Agent Pay) to verify agent authenticity prior to payment initiation [^evt-ext-frmoretto-agentic-standards-map-85d122-file-b284c7b2f467-be09154e].
- **Dynamic Token Verification Code**: Emits dynamic agentic tokens structured to fit standard card payment fields, enabling autonomous transactions across existing merchant checkout forms without requiring checkout rebuilds [^evt-ext-frmoretto-agentic-standards-map-85d122-file-b284c7b2f467-be09154e].

# References
- [Mastercard Agent Pay Specification Entry](https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/mastercard-agent-pay.yaml) [^evt-ext-frmoretto-agentic-standards-map-85d122-file-b284c7b2f467-be09154e]
- [Verifiable Intent Repository](https://github.com/agent-intent/verifiable-intent) [^evt-ext-frmoretto-agentic-standards-map-85d122-file-b284c7b2f467-be09154e]

[^evt-ext-frmoretto-agentic-standards-map-85d122-file-b284c7b2f467-be09154e]: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/mastercard-agent-pay.yaml
