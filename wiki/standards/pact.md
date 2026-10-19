---
type: standard
title: Personal Agent Consent & Trust Protocol
description: Open specification stewarded by Decagon and Instinct standardizing personal
  agent authentication, OAuth device delegation, and action receipts.
resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/pact.yaml
tags:
- external
- delegation
- identity
- a2a
- receipts
- specification
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T01:51:39.108682+00:00'
sources:
- id: evt-ext-frmoretto-agentic-standards-map-85d122-file-b6e427b588e4-53205881
  resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/pact.yaml
  author: frmoretto
  last_modified: '2026-10-14T04:52:24+02:00'
---

# Overview
The Personal Agent Consent & Trust Protocol (PACT) is an open specification stewarded by Decagon with Instinct establishing consent, delegation, and identity verification for personal AI agents interacting with business support agents [^evt-ext-frmoretto-agentic-standards-map-85d122-file-b6e427b588e4-53205881]. It enables customer-owned personal agents to discover service capabilities and authenticate requests while maintaining a strict separation between agent identity and user authority [^evt-ext-frmoretto-agentic-standards-map-85d122-file-b6e427b588e4-53205881].

PACT builds directly on top of [Agent-to-Agent (A2A)](../standards/a2a.md) 1.0, leveraging Agent Cards for service discovery and establishing cryptographic audit trails for actions executed by provider agents on behalf of users [^evt-ext-frmoretto-agentic-standards-map-85d122-file-b6e427b588e4-53205881].

# Architecture / Specification
The protocol standardizes discovery, caller assertion, authorization delegation, and receipt verification:

- **Endpoint Discovery**: Business support endpoints publish an Agent Card at `https://{brandDomain}/.well-known/agent-card.json`, which serves the card manifest or redirects to the provider URL [^evt-ext-frmoretto-agentic-standards-map-85d122-file-b6e427b588e4-53205881].
- **Agent Identity Assertion**: Personal agents sign every request with a JSON Web Token (JWT) using ES256 or RS256 algorithms, validated against public keys published by the personal agent [^evt-ext-frmoretto-agentic-standards-map-85d122-file-b6e427b588e4-53205881]. This asserts the identity of the calling agent for a subject without claiming customer account ownership [^evt-ext-frmoretto-agentic-standards-map-85d122-file-b6e427b588e4-53205881].
- **Delegated Authority**: To execute actions requiring user authority, the customer authenticates directly with the brand—never sharing credentials with the personal agent—via an OAuth 2.0 Device Authorization Grant (RFC 8628) flow to authorize brand-defined scopes [^evt-ext-frmoretto-agentic-standards-map-85d122-file-b6e427b588e4-53205881].
- **Signed Action Receipts**: Providers return signed receipts for replies executed under delegation tokens, containing grant IDs, user references, scopes utilized, actions taken, and timestamps [^evt-ext-frmoretto-agentic-standards-map-85d122-file-b6e427b588e4-53205881].
- **Scope Boundaries**: PACT does not specify a centralized agent registry or reserved global scopes; brand providers define their own authorization scopes independently [^evt-ext-frmoretto-agentic-standards-map-85d122-file-b6e427b588e4-53205881].

# References
- [PACT Landscape Entry](https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/pact.yaml) [^evt-ext-frmoretto-agentic-standards-map-85d122-file-b6e427b588e4-53205881]
- [Open PACT Protocol Specification Repository](https://github.com/openpactprotocol/openpactprotocol) [^evt-ext-frmoretto-agentic-standards-map-85d122-file-b6e427b588e4-53205881]

[^evt-ext-frmoretto-agentic-standards-map-85d122-file-b6e427b588e4-53205881]: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/pact.yaml
