---
type: standard
title: Visa Trusted Agent Protocol
description: Draft specification stewarded by Visa establishing cryptographic HTTP
  message signatures and tokenized payment containers for AI agents.
resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/visa-tap.yaml
tags:
- external
- standards
- payments
- visa
- security
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T01:41:52.210479+00:00'
sources:
- id: evt-ext-frmoretto-agentic-standards-map-85d122-file-329058ec0a85-eb6416f6
  resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/visa-tap.yaml
  author: frmoretto
  last_modified: '2026-10-14T06:46:06+02:00'
- id: evt-wg-agentic-commerce-file-d22b3d6550c3-4eccf8be
  resource: https://github.com/aaif/wg-agentic-commerce/blob/8458b003a68de58c8bc24900ebd931d3112eb7ca/charter.md
  author: Christina Harter
  last_modified: '2026-05-29T14:08:09-07:00'
---

# Overview

The Visa Trusted Agent Protocol (TAP) is an industry payment and agent recognition specification stewarded by Visa [^evt-ext-frmoretto-agentic-standards-map-85d122-file-329058ec0a85-eb6416f6]. It is not an AAIF project or policy. The protocol addresses merchant interactions where an agent is previously unknown to the merchant site, operating within Visa Intelligent Commerce [^evt-ext-frmoretto-agentic-standards-map-85d122-file-329058ec0a85-eb6416f6].

The AAIF [Agentic Commerce Working Group](../working-groups/agentic-commerce.md) uses Visa TAP as an input to its Capability Map [^evt-wg-agentic-commerce-file-d22b3d6550c3-4eccf8be].

# Architecture / Specification

Visa TAP defines cryptographic verification mechanisms enabling AI agents to prove identity and authorization directly to merchants or website protection providers [^evt-ext-frmoretto-agentic-standards-map-85d122-file-329058ec0a85-eb6416f6]:

- **Agent Recognition**: An HTTP header signature based on RFC 9421 (HTTP Message Signatures) and aligned with Web Bot Auth specifications [^evt-ext-frmoretto-agentic-standards-map-85d122-file-329058ec0a85-eb6416f6].
- **Consumer/Device Identity**: A cryptographically signed token conveying verified consumer identity or originating device context [^evt-ext-frmoretto-agentic-standards-map-85d122-file-329058ec0a85-eb6416f6].
- **Payment Container**: A signed payload encapsulating payment instructions for transaction fulfillment [^evt-ext-frmoretto-agentic-standards-map-85d122-file-329058ec0a85-eb6416f6].

Merchants are not required to use this proposal and do not necessarily have to be registered with Payment Schemes [^evt-ext-frmoretto-agentic-standards-map-85d122-file-329058ec0a85-eb6416f6].

# Lifecycle History

- 2025-10-10: Visa publishes the Trusted Agent Protocol merchant specification, sample implementation repository, and Visa Product Terms [^evt-ext-frmoretto-agentic-standards-map-85d122-file-329058ec0a85-eb6416f6].

# References

- Visa TAP Repository: https://github.com/visa/trusted-agent-protocol [^evt-ext-frmoretto-agentic-standards-map-85d122-file-329058ec0a85-eb6416f6]
- Standards Map Entry: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/visa-tap.yaml [^evt-ext-frmoretto-agentic-standards-map-85d122-file-329058ec0a85-eb6416f6]

[^evt-ext-frmoretto-agentic-standards-map-85d122-file-329058ec0a85-eb6416f6]: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/visa-tap.yaml
[^evt-wg-agentic-commerce-file-d22b3d6550c3-4eccf8be]: https://github.com/aaif/wg-agentic-commerce/blob/8458b003a68de58c8bc24900ebd931d3112eb7ca/charter.md
