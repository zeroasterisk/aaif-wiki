---
type: standard
title: EMV Agentic Payments Framework
description: Draft framework for card-based agentic payments and consumer intent registration
  stewarded by EMVCo.
resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/emvco-agentic-payments-framework.yaml
tags:
- external
- emvco
- payments
- intent-services
- card-payments
- standards
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T01:39:51.865388+00:00'
sources:
- id: evt-ext-frmoretto-agentic-standards-map-85d122-file-0b3b3b53a31a-01544476
  resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/emvco-agentic-payments-framework.yaml
  author: frmoretto
  last_modified: '2026-10-14T06:28:09+02:00'
---

# Overview

The EMV Agentic Payments Framework is a card payments specification framework stewarded by EMVCo[^evt-ext-frmoretto-agentic-standards-map-85d122-file-0b3b3b53a31a-01544476]. It defines architectural principles and interface layers to enable card transactions when a consumer delegates purchasing authority to an AI agent[^evt-ext-frmoretto-agentic-standards-map-85d122-file-0b3b3b53a31a-01544476].

This framework relates to agentic payment patterns evaluated by the [Agentic Commerce Working Group](../working-groups/agentic-commerce.md) and overlaps conceptually with the mandate delegation mechanisms in [AP2](../standards/ap2.md).

# Architecture / Specification

The specification focuses on secure payment processing across agentic delegation chains[^evt-ext-frmoretto-agentic-standards-map-85d122-file-0b3b3b53a31a-01544476]:
- **Intent Services**: Introduces a shared infrastructural layer intended to register, reference, retrieve, and manage consumer-authorized intent before, during, and after a transaction occurs[^evt-ext-frmoretto-agentic-standards-map-85d122-file-0b3b3b53a31a-01544476].
- **Governance and Coordination**: Stewarded by EMVCo's Agentic Payments Task Force with ongoing engagement across external standards organizations including the FIDO Alliance, the OpenID Foundation, the OpenWallet Foundation, and the World Wide Web Consortium (W3C)[^evt-ext-frmoretto-agentic-standards-map-85d122-file-0b3b3b53a31a-01544476].
- **Future Scope Considerations**: Potential future iterations may incorporate Know Your Agent (KYA) capabilities and Agentic Transaction Indicators to signal agent involvement to card networks[^evt-ext-frmoretto-agentic-standards-map-85d122-file-0b3b3b53a31a-01544476].

# Lifecycle History

- **2026-09-01**: EMVCo released the draft document 'EMV Agentic Payments Framework for Specifications v1.0' for public industry feedback[^evt-ext-frmoretto-agentic-standards-map-85d122-file-0b3b3b53a31a-01544476].
- **2026-09-30**: Public comment period on the v1.0 draft closed[^evt-ext-frmoretto-agentic-standards-map-85d122-file-0b3b3b53a31a-01544476].

# References

- [EMVCo Agentic Payments Framework in Agentic Standards Map](https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/emvco-agentic-payments-framework.yaml)[^evt-ext-frmoretto-agentic-standards-map-85d122-file-0b3b3b53a31a-01544476]

[^evt-ext-frmoretto-agentic-standards-map-85d122-file-0b3b3b53a31a-01544476]: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/emvco-agentic-payments-framework.yaml
