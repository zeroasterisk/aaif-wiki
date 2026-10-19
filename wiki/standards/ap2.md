---
type: standard
title: Agent Payments Protocol (AP2)
description: Open agent payments protocol whose core specification was donated to the
  FIDO Alliance, establishing mandate delegation, action constraints, and cryptographically
  verified checkout.
resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/fido-agentic-standards.yaml
tags:
- external
- standards
- payments
- fido
- delegation
- commerce
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T01:49:26.649242+00:00'
sources:
- id: evt-ext-frmoretto-agentic-standards-map-85d122-file-8eee6c9b516b-e0de98e0
  resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/fido-agentic-standards.yaml
  author: frmoretto
  last_modified: '2026-10-14T06:46:06+02:00'
- id: evt-ext-frmoretto-agentic-standards-map-85d122-file-955ebfe208df-4fecd4ef
  resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/w3c-gs1-ecommerce-workshop.yaml
  author: frmoretto
  last_modified: '2026-10-14T06:32:08+02:00'
- id: evt-wg-agentic-commerce-file-baf22ae9aa4b-28feda26
  resource: https://github.com/aaif/wg-agentic-commerce/blob/8458b003a68de58c8bc24900ebd931d3112eb7ca/reporting/2026-02-report.md
  author: Ilya Grigorik
  last_modified: '2026-08-03T22:02:18-07:00'
- id: evt-wg-agentic-commerce-file-fa4050a9f626-c7520564
  resource: https://github.com/aaif/wg-agentic-commerce/blob/8458b003a68de58c8bc24900ebd931d3112eb7ca/reporting/2026-07-report.md
  author: Ilya Grigorik
  last_modified: '2026-08-03T22:02:18-07:00'
---

# Overview
The Agent Payments Protocol (AP2) is an open agent payments protocol whose core specification was donated to the FIDO Alliance (Payments Technical Working Group); the repository remains at google-agentic-commerce/AP2[^evt-ext-frmoretto-agentic-standards-map-85d122-file-8eee6c9b516b-e0de98e0]. Originally initiated by Google, AP2 establishes cryptographic mandates, user delegation bounds, and action verification for automated agent transactions[^evt-ext-frmoretto-agentic-standards-map-85d122-file-8eee6c9b516b-e0de98e0].

AP2 is discussed by the AAIF [Agentic Commerce Working Group](../working-groups/agentic-commerce.md)[^evt-wg-agentic-commerce-file-baf22ae9aa4b-28feda26][^evt-wg-agentic-commerce-file-fa4050a9f626-c7520564] and complements protocols such as the [Agentic Commerce Protocol](./agentic-commerce-protocol.md).

# Architecture / Specification
AP2 defines protocol specifications and signature bindings that allow autonomous agents to present signed payment authorizations to merchants and payment service providers[^evt-ext-frmoretto-agentic-standards-map-85d122-file-8eee6c9b516b-e0de98e0]:
- **Working Group Governance**: Within the FIDO Alliance, payment and delegation specifications are managed by the Payments Technical Working Group (chaired by members from Mastercard and Visa), while broader authentication standards are developed within the Agentic Authentication Technical Working Group (chaired by CVS Health, Google, and OpenAI; vice-chaired by Amazon, Google, and Okta)[^evt-ext-frmoretto-agentic-standards-map-85d122-file-8eee6c9b516b-e0de98e0].
- **Mandate Delegation**: AP2 standardizes cryptographically signed intent objects and delegation scopes, aligning with parallel efforts such as Mastercard's Verifiable Intent specifications[^evt-ext-frmoretto-agentic-standards-map-85d122-file-8eee6c9b516b-e0de98e0][^evt-ext-frmoretto-agentic-standards-map-85d122-file-955ebfe208df-4fecd4ef].
- **Execution Boundaries**: Distinguishes agent-initiated shopping exploration from bound commit-time purchase actions, enforcing explicit verification gates for transactions exceeding delegated authority.

# Lifecycle History
- **2026-04-28**: FIDO Alliance announces the Agentic Authentication Technical Working Group and launches work in the Payments Technical Working Group incorporating AP2 and Verifiable Intent contributions[^evt-ext-frmoretto-agentic-standards-map-85d122-file-8eee6c9b516b-e0de98e0].

A FIDO Payments TWG statement to the W3C/GS1 E-commerce Workshop notes that AP2 and Verifiable Intent are now under review within the PTWG[^evt-ext-frmoretto-agentic-standards-map-85d122-file-955ebfe208df-4fecd4ef].

# References
- [Google Agentic Commerce AP2 Repository](https://github.com/google-agentic-commerce/AP2)
- [FIDO Standards Reference Entry](https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/fido-agentic-standards.yaml)

[^evt-ext-frmoretto-agentic-standards-map-85d122-file-8eee6c9b516b-e0de98e0]: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/fido-agentic-standards.yaml
[^evt-ext-frmoretto-agentic-standards-map-85d122-file-955ebfe208df-4fecd4ef]: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/w3c-gs1-ecommerce-workshop.yaml
[^evt-wg-agentic-commerce-file-baf22ae9aa4b-28feda26]: https://github.com/aaif/wg-agentic-commerce/blob/8458b003a68de58c8bc24900ebd931d3112eb7ca/reporting/2026-02-report.md
[^evt-wg-agentic-commerce-file-fa4050a9f626-c7520564]: https://github.com/aaif/wg-agentic-commerce/blob/8458b003a68de58c8bc24900ebd931d3112eb7ca/reporting/2026-07-report.md
