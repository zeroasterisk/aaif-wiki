---
type: standard
title: IETF Web Bot Auth
description: Draft standard defining cryptographic HTTP message signatures and public
  key directories for authenticating automated agent clients.
resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/ietf-webbotauth.yaml
tags:
- external
- ietf
- authentication
- identity
- http-signatures
- agent-verification
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T01:43:52.637607+00:00'
sources:
- id: evt-ext-frmoretto-agentic-standards-map-85d122-file-4a46e5ac39a4-f791a38f
  resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/ietf-webbotauth.yaml
  author: frmoretto
  last_modified: '2026-10-14T06:46:06+02:00'
---

# Overview
Web Bot Auth is an automated client authentication protocol stewarded by the Internet Engineering Task Force (IETF).[^evt-ext-frmoretto-agentic-standards-map-85d122-file-4a46e5ac39a4-f791a38f] Developed within the Web Bot Auth Working Group (`webbotauth`), the protocol establishes standardized cryptographic authentication for automated web clients using asymmetric HTTP message signatures and publicly resolvable key directories.

# Architecture / Specification
- Cryptographic HTTP Request Signatures: Client agents sign outbound HTTP messages using asymmetric private keys linked to an authoritative `Signature-Agent` URL identifying the agent operator and public key directory.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-4a46e5ac39a4-f791a38f]
- Public Key Directory Resolution: Content delivery networks (CDNs) and merchant-side verifiers fetch and cache the client's public keys to verify cryptographic signatures without maintaining pre-shared static secrets.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-4a46e5ac39a4-f791a38f]
- Directory Freshness and Revocation Dynamics:
  - Working group participants debate bounds between HTTP cache lifetimes (`Cache-Control: max-age`) and cryptographic signature expiration timestamps (`expires`).
  - Immediate agent deactivation is implemented by removing public keys from the resolved directory, requiring verifiers to bound cached key sets to prevent delayed revocations during payment disputes.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-4a46e5ac39a4-f791a38f]
- Segregation of Automated Traffic:
  - Specification guidance advises operators against reusing signing keys across different agent purposes.
  - Companion crawler best practices distinguish autonomous web crawlers from interactive user-directed AI agents; distinct per-purpose `Signature-Agent` identifiers are an open participant proposal (garyillyes/cbcp PR #23), not adopted text.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-4a46e5ac39a4-f791a38f]
- Deployment: Interoperates with agentic commerce flows and links to the Universal Commerce Protocol (UCP). Shopify reported production use (2026-08-19); Akamai described itself as a verifier, without a production claim.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-4a46e5ac39a4-f791a38f]

# Lifecycle History
- 2026-04-21: Individual draft `draft-illyes-webbotauth-cbcp-00` published defining crawler best practices.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-4a46e5ac39a4-f791a38f]
- 2026-09-01: IETF Web Bot Auth Working Group formally adopts `draft-ietf-webbotauth-httpsig-protocol-00` as a WG document.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-4a46e5ac39a4-f791a38f]
- 2026-09-15: Two-hour working group session requested for IETF 127.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-4a46e5ac39a4-f791a38f]
- 2026-10-05: Companion crawler best practices updated to decouple voluntary crawl rules from user-directed AI agent traffic.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-4a46e5ac39a4-f791a38f]

# References
- [Universal Commerce Protocol](../standards/universal-commerce-protocol.md)
- [Identity and Trust Working Group](../working-groups/identity-and-trust.md)
- [Agentic Commerce Working Group](../working-groups/agentic-commerce.md)

[^evt-ext-frmoretto-agentic-standards-map-85d122-file-4a46e5ac39a4-f791a38f]: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/ietf-webbotauth.yaml
