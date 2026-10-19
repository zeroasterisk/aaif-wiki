---
type: standard
title: Universal Commerce Protocol
description: Open commerce protocol specifying modular shopping discovery, lodging
  booking, catalog queries, and verifiable checkout handoffs.
resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/ucp.yaml
tags:
- external
- standards
- commerce
- checkout
- payments
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T01:41:02.362510+00:00'
sources:
- id: evt-ext-frmoretto-agentic-standards-map-85d122-file-242accfd2746-be7fa731
  resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/ucp.yaml
  author: frmoretto
  last_modified: '2026-10-14T21:36:08+02:00'
---

# Overview

Universal Commerce Protocol (UCP) is an open commerce specification governed by a Governing Council plus a Tech Council and Domain Tech Councils, with members drawn mostly from Google and Shopify.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-242accfd2746-be7fa731] UCP standardizes protocol bindings across REST and Model Context Protocol (MCP) endpoints to allow AI agents to browse merchant offerings, negotiate structured orders, verify policy terms, and execute authenticated transactions.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-242accfd2746-be7fa731] The protocol interfaces with mandate verification architectures such as [AP2](../standards/ap2.md) and relates to capability modeling evaluated by the [Agentic Commerce Working Group](../working-groups/agentic-commerce.md).[^evt-ext-frmoretto-agentic-standards-map-85d122-file-242accfd2746-be7fa731]

# Architecture / Specification

UCP modularizes commerce capabilities across several domain packages and foundational protocol invariants:[^evt-ext-frmoretto-agentic-standards-map-85d122-file-242accfd2746-be7fa731]

- **Strict Profile Hosting and Redirect Ban:** Profile endpoints (`/.well-known/ucp`) and dereferenced identity URLs strictly prohibit HTTP redirects (`3xx`); implementations must reject redirects to mitigate Server-Side Request Forgery (SSRF) and ensure unambiguous host binding.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-242accfd2746-be7fa731] Profile responses must include `Cache-Control: public` with a `max-age` of at least 60 seconds and an `ETag` or `Last-Modified` validator.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-242accfd2746-be7fa731]
- **Natural-Language Ask Capability (`dev.ucp.common.ask`):** Provides informational question-and-answer interactions concerning product specs, policies, and store information.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-242accfd2746-be7fa731] By invariant, `ask` endpoints are indicative rather than authoritative; businesses must not mutate resource states in response to an ask query, and platforms must prioritize structured catalog attributes over natural language responses in disputes.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-242accfd2746-be7fa731]
- **Lodging Booking:** Standardizes property booking via explicit property and stay identifiers, intentionally scoping upper-funnel hotel discovery and room search outside the core booking transaction.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-242accfd2746-be7fa731]
- **Dual-Audience Signatures & Mandates:** Platforms embed cryptographic mandates verifying human user consent, while merchants sign checkout terms and webhook payloads to ensure non-repudiation.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-242accfd2746-be7fa731]

# Lifecycle History

- 2026-02-17: Commit 0426800 introduced cryptographic request/response signing and profile redirect bans.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-242accfd2746-be7fa731]
- 2026-07-03: Dual-audience signature guidelines merged in PR #483 for Web Bot Auth compatibility.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-242accfd2746-be7fa731]
- 2026-07-23: PR #572 merged, formalizing structured merchant policy declarations (`policies[]`).[^evt-ext-frmoretto-agentic-standards-map-85d122-file-242accfd2746-be7fa731]
- 2026-08-25: Specification release v2026-08-25 tagged.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-242accfd2746-be7fa731]
- 2026-09-24: Lodging booking capability merged in PR #780.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-242accfd2746-be7fa731]
- 2026-10-07: Informational inquiry capability `dev.ucp.common.ask` merged in PR #538.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-242accfd2746-be7fa731]

# References

- GitHub Repository: [Universal-Commerce-Protocol/ucp](https://github.com/Universal-Commerce-Protocol/ucp)
- Landscape Entry: [ucp.yaml](https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/ucp.yaml)

[^evt-ext-frmoretto-agentic-standards-map-85d122-file-242accfd2746-be7fa731]: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/ucp.yaml
