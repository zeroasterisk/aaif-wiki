---
type: standard
title: IETF Agent Communication Protocols (agentproto)
description: Agentic dialog management protocol and lifecycle specification stewarded
  by the Internet Engineering Task Force (IETF).
resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/ietf-agentproto.yaml
tags:
- external
- ietf
- agentproto
- dialog-management
- lifecycle
- protocols
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T01:39:51.865388+00:00'
sources:
- id: evt-ext-frmoretto-agentic-standards-map-85d122-file-0653f2bd3154-342600a3
  resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/ietf-agentproto.yaml
  author: frmoretto
  last_modified: '2026-10-14T06:46:06+02:00'
---

# Overview

IETF agentproto (Agent Communication Protocols) is an agentic dialog management protocol track stewarded by the Internet Engineering Task Force (IETF)[^evt-ext-frmoretto-agentic-standards-map-85d122-file-0653f2bd3154-342600a3]. The working group standardizes dialog identifiers, lifecycle semantics, and dialog context propagation over existing IETF network protocols without replacing application-layer communication models or creating novel transport layers[^evt-ext-frmoretto-agentic-standards-map-85d122-file-0653f2bd3154-342600a3].

Within the AAIF knowledge base, this protocol complements the dialog recovery research prototype in [AgentProto Dialog Recovery](../resources/agentproto-dialog-recovery.md) and cross-venue landscape tracking in [Agentic Standards Map](../resources/agentic-standards-map.md).

# Architecture / Specification

The specification standardizes stateful dialog tracking across autonomous systems[^evt-ext-frmoretto-agentic-standards-map-85d122-file-0653f2bd3154-342600a3]:
- **Dialog Lifecycle and Identifiers**: Establishes unambiguous dialog session identifiers, status transitions, and propagation conventions for conversational context across participants[^evt-ext-frmoretto-agentic-standards-map-85d122-file-0653f2bd3154-342600a3].
- **Resumption Semantics**: Under candidate requirements, dialog resumption requires authorization verification, failure signaling when checks fail, and leaving unresolved transactions uncommitted rather than automatically resending[^evt-ext-frmoretto-agentic-standards-map-85d122-file-0653f2bd3154-342600a3].
- **Working Group Coordination**: Coordinates dependencies with related IETF working groups, including OAuth/webbotauth/WIMSE for identity and authorization, WebTransport/MoQ/QUIC/httpbis for data transport, SCITT/RATS for evidence and attestation, and vCon for conversational data formats[^evt-ext-frmoretto-agentic-standards-map-85d122-file-0653f2bd3154-342600a3].
- **Scope Exclusions**: Audit data structure definitions and consumption are explicitly out of scope, although dialog identifiers may be referenced in audit trails[^evt-ext-frmoretto-agentic-standards-map-85d122-file-0653f2bd3154-342600a3]. Specific commerce and purchase flows are not included in the charter[^evt-ext-frmoretto-agentic-standards-map-85d122-file-0653f2bd3154-342600a3].

# Lifecycle History

- **2026-10-08**: The Internet Engineering Steering Group (IESG) approved charter `charter-ietf-agentproto-01`, activating the agentproto working group in the Applications and Real-Time (ART) area[^evt-ext-frmoretto-agentic-standards-map-85d122-file-0653f2bd3154-342600a3].
- **2026-10-12**: Working group chairs initiated candidate selection for the Use Cases and Requirements deliverable between `draft-agentic-ai-usecases-requirements` and `draft-rosenberg-agentproto-usecases`[^evt-ext-frmoretto-agentic-standards-map-85d122-file-0653f2bd3154-342600a3].

# References

- [IETF agentproto in Agentic Standards Map](https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/ietf-agentproto.yaml)[^evt-ext-frmoretto-agentic-standards-map-85d122-file-0653f2bd3154-342600a3]

[^evt-ext-frmoretto-agentic-standards-map-85d122-file-0653f2bd3154-342600a3]: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/ietf-agentproto.yaml
