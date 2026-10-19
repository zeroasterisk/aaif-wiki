---
type: standard
title: Personal Agent Protocol
description: Draft specification stewarded by Sierra and Meta standardizing agent
  discovery via well-known URIs and OAuth-based merchant interaction.
resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/pap.yaml
tags:
- external
- standards
- discovery
- identity
- oauth
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T01:41:52.210479+00:00'
sources:
- id: evt-ext-frmoretto-agentic-standards-map-85d122-file-2f451706c871-86785c08
  resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/pap.yaml
  author: frmoretto
  last_modified: '2026-10-14T06:28:09+02:00'
---

# Overview

The Personal Agent Protocol (PAP, colloquially "Poppy") is an open protocol specification stewarded by Sierra in collaboration with Meta and industry partners [^evt-ext-frmoretto-agentic-standards-map-85d122-file-2f451706c871-86785c08]. It is not an AAIF project or position. The protocol defines how personal user agents discover company services, negotiate authorization over OAuth, and perform tasks across web domains [^evt-ext-frmoretto-agentic-standards-map-85d122-file-2f451706c871-86785c08].

While PAP permits discovery documents to redirect across HTTPS endpoints, other protocols such as the [Universal Commerce Protocol](../standards/universal-commerce-protocol.md) impose strict anti-redirect policies on their discovery profile [^evt-ext-frmoretto-agentic-standards-map-85d122-file-2f451706c871-86785c08].

# Architecture / Specification

PAP structures agent-to-business interaction across three key areas [^evt-ext-frmoretto-agentic-standards-map-85d122-file-2f451706c871-86785c08]:

1. **Discovery**: Participating companies host a discovery document at `https://{domain}/.well-known/poppy.json` over HTTPS. Agents are required to follow HTTPS redirects to find service endpoints [^evt-ext-frmoretto-agentic-standards-map-85d122-file-2f451706c871-86785c08].
2. **Agent Identity**: Agents identify using an HTTPS URL client identifier (`client_id`) that resolves to a metadata document containing a `jwks_uri` and designating `private_key_jwt` for `token_endpoint_auth_method` [^evt-ext-frmoretto-agentic-standards-map-85d122-file-2f451706c871-86785c08]. Companies maintain local allowlists, registries, or revocation records for these identifiers [^evt-ext-frmoretto-agentic-standards-map-85d122-file-2f451706c871-86785c08].
3. **Authorization and Scope**: Operations sessions use OAuth, granting customers control over read-only versus write permissions. The operations specification notes that an execution confirmation proves receipt but does not prove the end user viewed or approved specific terms [^evt-ext-frmoretto-agentic-standards-map-85d122-file-2f451706c871-86785c08].

The Draft 0.1 specification excludes payment processing, push notifications, and rich message attachments [^evt-ext-frmoretto-agentic-standards-map-85d122-file-2f451706c871-86785c08].

# Lifecycle History

- 2026-10-06: Sierra and Meta announce the Personal Agent Protocol alongside initial industry partners [^evt-ext-frmoretto-agentic-standards-map-85d122-file-2f451706c871-86785c08].
- 2026-10-09: Draft 0.1 published under the Apache License 2.0 (excluding names and logos) with 35 design partners [^evt-ext-frmoretto-agentic-standards-map-85d122-file-2f451706c871-86785c08].

# References

- Standards Map Entry: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/pap.yaml [^evt-ext-frmoretto-agentic-standards-map-85d122-file-2f451706c871-86785c08]

[^evt-ext-frmoretto-agentic-standards-map-85d122-file-2f451706c871-86785c08]: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/pap.yaml
