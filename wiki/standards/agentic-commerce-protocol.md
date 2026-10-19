---
type: standard
title: Agentic Commerce Protocol (ACP)
description: Open checkout and payment negotiation protocol maintained by OpenAI and
  Stripe connecting buyers, AI agents, and merchants.
resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/acp.yaml
tags:
- external
- standards
- commerce
- payments
- checkout
- mcp
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T01:49:26.649242+00:00'
sources:
- id: evt-ext-frmoretto-agentic-standards-map-85d122-file-a2ffe7ba6966-f3bec241
  resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/acp.yaml
  author: frmoretto
  last_modified: '2026-10-14T06:46:06+02:00'
- id: evt-wg-agentic-commerce-file-a439311d16f4-f0496332
  resource: https://github.com/aaif/wg-agentic-commerce/blob/8458b003a68de58c8bc24900ebd931d3112eb7ca/reporting/2026-03-report.md
  author: Ilya Grigorik
  last_modified: '2026-08-03T22:02:18-07:00'
- id: evt-wg-agentic-commerce-file-3e3f89e6a796-ee1af760
  resource: https://github.com/aaif/wg-agentic-commerce/blob/8458b003a68de58c8bc24900ebd931d3112eb7ca/reporting/2026-04-report.md
  author: Ilya Grigorik
  last_modified: '2026-08-03T22:02:18-07:00'
---

# Overview
The Agentic Commerce Protocol (ACP) is an open specification maintained by OpenAI and Stripe as Founding Maintainers; Meta is a member of its Technical Steering Committee[^evt-ext-frmoretto-agentic-standards-map-85d122-file-a2ffe7ba6966-f3bec241]. It provides a standardized interaction model for connecting buyers, autonomous AI agents, and merchants to complete purchases over REST interfaces and Model Context Protocol (MCP) bindings[^evt-ext-frmoretto-agentic-standards-map-85d122-file-a2ffe7ba6966-f3bec241].

ACP addresses checkout orchestration and session state management, intersecting with work evaluated in the AAIF [Agentic Commerce Working Group](../working-groups/agentic-commerce.md)[^evt-wg-agentic-commerce-file-a439311d16f4-f0496332][^evt-wg-agentic-commerce-file-3e3f89e6a796-ee1af760] and related payment frameworks like [AP2](./ap2.md) and [Universal Commerce Protocol](./universal-commerce-protocol.md).

# Architecture / Specification
ACP establishes data schemas and API contracts across several commerce lifecycle stages[^evt-ext-frmoretto-agentic-standards-map-85d122-file-a2ffe7ba6966-f3bec241]:
- **Checkout Sessions**: Defines structured session objects with mandatory merchant links (terms of service, privacy policy, refund policy, and shipping guidelines) and an HTTP `Signature` header on requests[^evt-ext-frmoretto-agentic-standards-map-85d122-file-a2ffe7ba6966-f3bec241].
- **Session Lifecycle vs. Order Refunds**: The specification strictly separates checkout session cancellations (which return HTTP 405 if already completed or canceled) from post-order refunds (which handle `store_credit` and `original_payment` types on finalized orders)[^evt-ext-frmoretto-agentic-standards-map-85d122-file-a2ffe7ba6966-f3bec241].
- **Product Feeds and Discovery**: Unreleased schemas define structured product feeds with barcode types (GTIN, UPC, EAN); catalog discovery operates without pre-existing agent authentication, treating agent identity and authorization as orthogonal concerns[^evt-ext-frmoretto-agentic-standards-map-85d122-file-a2ffe7ba6966-f3bec241].

# Lifecycle History
- **2026-04-17**: Dated ACP specification version (not a tagged release)[^evt-ext-frmoretto-agentic-standards-map-85d122-file-a2ffe7ba6966-f3bec241].
- **2026-04-24**: Meta joins OpenAI and Stripe on the ACP Technical Steering Committee via pull request #236[^evt-ext-frmoretto-agentic-standards-map-85d122-file-a2ffe7ba6966-f3bec241].
- **2026-07-17**: Repository main branch updated with unreleased schema specifications covering cart, checkout, delegate, and feed components[^evt-ext-frmoretto-agentic-standards-map-85d122-file-a2ffe7ba6966-f3bec241].

# References
- [Agentic Commerce Protocol Repository](https://github.com/agentic-commerce-protocol/agentic-commerce-protocol)
- [ACP Standards Reference Entry](https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/acp.yaml)

[^evt-ext-frmoretto-agentic-standards-map-85d122-file-a2ffe7ba6966-f3bec241]: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/acp.yaml
[^evt-wg-agentic-commerce-file-a439311d16f4-f0496332]: https://github.com/aaif/wg-agentic-commerce/blob/8458b003a68de58c8bc24900ebd931d3112eb7ca/reporting/2026-03-report.md
[^evt-wg-agentic-commerce-file-3e3f89e6a796-ee1af760]: https://github.com/aaif/wg-agentic-commerce/blob/8458b003a68de58c8bc24900ebd931d3112eb7ca/reporting/2026-04-report.md
