---
type: standard
title: EMILIA Protocol
description: Experimental authority gate and action-evidence boundary architecture
  stewarded independently by EMILIA Protocol, Inc.
resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/emilia-protocol.yaml
tags:
- external
- standards
- ietf
- authorization
- mcp
- evidence
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T01:47:57.406359+00:00'
sources:
- id: evt-ext-frmoretto-agentic-standards-map-85d122-file-6eeaf0b51943-9ec7976c
  resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/emilia-protocol.yaml
  author: frmoretto
  last_modified: '2026-10-14T04:52:24+02:00'
---

# Overview
EMILIA Protocol is an experimental agent authority and action boundary framework stewarded independently by EMILIA Protocol, Inc. and author Iman Schrock[^evt-ext-frmoretto-agentic-standards-map-85d122-file-6eeaf0b51943-9ec7976c]. Documented through individual IETF Internet-Drafts and an Apache-2.0 open-source gateway implementation, EMILIA enforces authorization checks before protected tools execute and generates structured evidence chains across execution boundaries[^evt-ext-frmoretto-agentic-standards-map-85d122-file-6eeaf0b51943-9ec7976c].

# Architecture / Specification
EMILIA architecture is defined across three core components:
- **Canonical Action Identifier (CAID)**: A standardized naming scheme and identifier format uniquely identifying actions requested by an agent[^evt-ext-frmoretto-agentic-standards-map-85d122-file-6eeaf0b51943-9ec7976c].
- **Authorization Evidence Chain (AEC)**: Cryptographic linkage of preconditions, delegator mandates, and authorization proofs authorizing a particular execution[^evt-ext-frmoretto-agentic-standards-map-85d122-file-6eeaf0b51943-9ec7976c].
- **Action Evidence Boundary (AEB)**: An enforcement gate that separates four distinct categories of factual assertion: cryptographic signature validity, credential currency, satisfaction of evidence requirements, and verified real-world effects[^evt-ext-frmoretto-agentic-standards-map-85d122-file-6eeaf0b51943-9ec7976c].

### Gate Enforcement
The EMILIA Gate operates as an interception proxy ahead of protected tool runtimes, such as `../standards/model-context-protocol.md` (MCP) servers[^evt-ext-frmoretto-agentic-standards-map-85d122-file-6eeaf0b51943-9ec7976c]. For payment and critical operational actions, the gate refuses tool invocation unless accompanied by an explicit approval binding the amount, currency, recipient vendor, and target destination[^evt-ext-frmoretto-agentic-standards-map-85d122-file-6eeaf0b51943-9ec7976c].

# Lifecycle History
- **2026-03-13**: Open-source repository `emiliaprotocol/emilia-protocol` established under the Apache-2.0 license[^evt-ext-frmoretto-agentic-standards-map-85d122-file-6eeaf0b51943-9ec7976c].
- **2026-09-06**: Publication of Internet-Draft `draft-schrock-ep-architecture-03` detailing the CAID, AEC, and AEB composition[^evt-ext-frmoretto-agentic-standards-map-85d122-file-6eeaf0b51943-9ec7976c].
- **2026-09-25**: Publication of Internet-Draft `draft-schrock-action-evidence-boundary-07` defining boundary verification principles[^evt-ext-frmoretto-agentic-standards-map-85d122-file-6eeaf0b51943-9ec7976c].

[^evt-ext-frmoretto-agentic-standards-map-85d122-file-6eeaf0b51943-9ec7976c]: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/emilia-protocol.yaml
