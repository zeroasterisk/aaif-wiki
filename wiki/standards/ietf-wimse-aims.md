---
type: standard
title: IETF WIMSE AI Identity Management System (AIMS)
description: Informational IETF draft establishing best practices for authentication
  and authorization across autonomous AI agent interactions.
resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/ietf-wimse-aims.yaml
tags:
- external
- standards
- ietf
- identity
- authentication
- authorization
- wimse
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T01:49:26.649242+00:00'
sources:
- id: evt-ext-frmoretto-agentic-standards-map-85d122-file-9d71e88c9750-f44fed1f
  resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/ietf-wimse-aims.yaml
  author: frmoretto
  last_modified: '2026-10-14T06:28:09+02:00'
---

# Overview
The AI Identity Management System (AIMS) is an Informational specification stewarded by the Internet Engineering Task Force (IETF) Workload Identity in Multi-System Environments (WIMSE) working group[^evt-ext-frmoretto-agentic-standards-map-85d122-file-9d71e88c9750-f44fed1f]. Published as `draft-ietf-wimse-aims`, the document outlines architectural best practices for authenticating and authorizing AI agent interactions across distributed systems[^evt-ext-frmoretto-agentic-standards-map-85d122-file-9d71e88c9750-f44fed1f].

AIMS focuses on cross-domain workload identity assertion and delegation tokens.

# Architecture / Specification
The AIMS specification addresses workload identity and authorization semantics for agentic communication[^evt-ext-frmoretto-agentic-standards-map-85d122-file-9d71e88c9750-f44fed1f]:
- **Workload Identity Binding**: Defines patterns for issuing and verifying cryptographic credentials identifying AI agents as autonomous software workloads.
- **Scope and Separation**: Restricts its scope to identity verification and workload authorization; it explicitly avoids embedding commerce or merchant transaction flows, referencing external protocols such as [AP2](./ap2.md) and [Agentic Commerce Protocol](./agentic-commerce-protocol.md) for transactional requirements[^evt-ext-frmoretto-agentic-standards-map-85d122-file-9d71e88c9750-f44fed1f].
- **Evolution**: Formally adopts and consolidates identity patterns previously explored in individual submission `draft-klrc-aiagent-auth`[^evt-ext-frmoretto-agentic-standards-map-85d122-file-9d71e88c9750-f44fed1f].

# Lifecycle History
- **2026-09-09**: Formally adopted by the IETF WIMSE Working Group as an active work item[^evt-ext-frmoretto-agentic-standards-map-85d122-file-9d71e88c9750-f44fed1f].
- **2026-09-15**: Publication of initial working group draft `draft-ietf-wimse-aims-00`, succeeding `draft-klrc-aiagent-auth`[^evt-ext-frmoretto-agentic-standards-map-85d122-file-9d71e88c9750-f44fed1f].

# References
- [IETF WIMSE AIMS Entry](https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/ietf-wimse-aims.yaml)

[^evt-ext-frmoretto-agentic-standards-map-85d122-file-9d71e88c9750-f44fed1f]: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/ietf-wimse-aims.yaml
