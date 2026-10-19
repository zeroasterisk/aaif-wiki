---
type: standard
title: Payment HTTP Authentication Scheme
description: Proposed HTTP authentication scheme stewarded within the IETF defining
  standardized payment challenges and Payment-Receipt headers.
resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/ietf-httpauth-payment.yaml
tags:
- external
- standards
- ietf
- payments
- http
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T01:41:52.210479+00:00'
sources:
- id: evt-ext-frmoretto-agentic-standards-map-85d122-file-2cbab1e3cb18-eace52e8
  resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/ietf-httpauth-payment.yaml
  author: frmoretto
  last_modified: '2026-10-14T06:46:06+02:00'
---

# Overview

The Payment HTTP Authentication Scheme (`draft-httpauth-payment`) is an individual Standards Track Internet-Draft stewarded within the Internet Engineering Task Force (IETF) by authors from Tempo Labs and Stripe [^evt-ext-frmoretto-agentic-standards-map-85d122-file-2cbab1e3cb18-eace52e8]. It is not an AAIF specification or work product. The document defines an HTTP authentication scheme enabling servers to challenge HTTP clients for payment before granting access to protected web resources [^evt-ext-frmoretto-agentic-standards-map-85d122-file-2cbab1e3cb18-eace52e8].

# Architecture / Specification

The specification introduces standardized payment negotiation within standard HTTP transaction headers [^evt-ext-frmoretto-agentic-standards-map-85d122-file-2cbab1e3cb18-eace52e8]:

- **Payment Receipt**: Servers issue a `Payment-Receipt` header upon successful completion of a transaction [^evt-ext-frmoretto-agentic-standards-map-85d122-file-2cbab1e3cb18-eace52e8].
- **Receipt Structure**: The receipt data format contains four standard fields: `status`, `method`, `timestamp`, and `reference` [^evt-ext-frmoretto-agentic-standards-map-85d122-file-2cbab1e3cb18-eace52e8]. The -01 revision does not specify a digital signature field on the receipt payload [^evt-ext-frmoretto-agentic-standards-map-85d122-file-2cbab1e3cb18-eace52e8].

# Lifecycle History

- 2026-09-09: Authors from Tempo Labs and Stripe submit `draft-httpauth-payment-01` to the IETF Datatracker with intended Standards Track status [^evt-ext-frmoretto-agentic-standards-map-85d122-file-2cbab1e3cb18-eace52e8].

# References

- Standards Map Entry: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/ietf-httpauth-payment.yaml [^evt-ext-frmoretto-agentic-standards-map-85d122-file-2cbab1e3cb18-eace52e8]

[^evt-ext-frmoretto-agentic-standards-map-85d122-file-2cbab1e3cb18-eace52e8]: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/ietf-httpauth-payment.yaml
