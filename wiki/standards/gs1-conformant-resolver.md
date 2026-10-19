---
type: standard
title: GS1-Conformant Resolver Standard
description: Resolution standard stewarded by GS1 mapping Digital Link URIs and product
  keys to related web data and services.
resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/gs1-conformant-resolver.yaml
tags:
- external
- gs1
- digital-link
- resolver
- product-identity
- standards
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T01:39:51.865388+00:00'
sources:
- id: evt-ext-frmoretto-agentic-standards-map-85d122-file-10654c5953e2-72cc4f5e
  resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/gs1-conformant-resolver.yaml
  author: frmoretto
  last_modified: '2026-10-14T06:28:09+02:00'
---

# Overview

The GS1-Conformant Resolver Standard is an entity identification and lookup specification stewarded by GS1[^evt-ext-frmoretto-agentic-standards-map-85d122-file-10654c5953e2-72cc4f5e]. It defines how GS1 Digital Link URIs containing primary keys—such as a Global Trade Item Number (GTIN) or Global Location Number (GLN)—resolve to authorized web resources, product passports, and machine-readable data endpoints[^evt-ext-frmoretto-agentic-standards-map-85d122-file-10654c5953e2-72cc4f5e].

For agentic applications, this standard provides deterministic item and location resolution relevant to product lookup and supply-chain operations.

# Architecture / Specification

The standard specifies deterministic resolution semantics for conformant web servers[^evt-ext-frmoretto-agentic-standards-map-85d122-file-10654c5953e2-72cc4f5e]:
- **URI Semantics**: Resolvers process GS1 Digital Link URIs where the path component conveys core entity identification keys; query strings convey attributes of the identified entity without modifying the identifier itself[^evt-ext-frmoretto-agentic-standards-map-85d122-file-10654c5953e2-72cc4f5e].
- **HTTP Status Codes**: A conformant resolver must return HTTP 400 (Bad Request) for malformed or invalid request URIs, and HTTP 404 (Not Found) for a structurally valid URI that has no associated target information[^evt-ext-frmoretto-agentic-standards-map-85d122-file-10654c5953e2-72cc4f5e].
- **Discovery Descriptor**: Resolvers advertise their capabilities via a Resolver Description File served at the well-known path `/.well-known/gs1resolver`[^evt-ext-frmoretto-agentic-standards-map-85d122-file-10654c5953e2-72cc4f5e].
- **Scope Boundaries**: Resolvers are not mandated to return identical targets across different operational deployments, nor does the specification prescribe custom behaviors for non-standard query parameters[^evt-ext-frmoretto-agentic-standards-map-85d122-file-10654c5953e2-72cc4f5e].

# Lifecycle History

- **August 2026**: GS1 published the ratified Release 1.2.1 of the GS1-Conformant Resolver Standard[^evt-ext-frmoretto-agentic-standards-map-85d122-file-10654c5953e2-72cc4f5e].

# References

- [GS1-Conformant Resolver in Agentic Standards Map](https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/gs1-conformant-resolver.yaml)[^evt-ext-frmoretto-agentic-standards-map-85d122-file-10654c5953e2-72cc4f5e]

[^evt-ext-frmoretto-agentic-standards-map-85d122-file-10654c5953e2-72cc4f5e]: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/gs1-conformant-resolver.yaml
