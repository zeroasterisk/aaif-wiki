---
type: standard
title: Verifiable Intent
description: Draft specification for cryptographic agent authorization in commerce
  using layered SD-JWT credentials.
resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/verifiable-intent.yaml
tags:
- external
- standard
- commerce
- credentials
- authorization
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T01:53:06.132433+00:00'
sources:
- id: evt-ext-frmoretto-agentic-standards-map-85d122-file-ce1194c318a5-d3d9cfd8
  resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/verifiable-intent.yaml
  author: frmoretto
  last_modified: '2026-10-14T06:46:06+02:00'
---

# Overview
Verifiable Intent is a draft (v0.1) open specification for cryptographic agent authorization in commerce maintained by Mastercard and contributed to the FIDO Alliance Payments Technical Working Group [^evt-ext-frmoretto-agentic-standards-map-85d122-file-ce1194c318a5-d3d9cfd8]. Designed to work alongside protocols like [AP2](../standards/ap2.md) and commercial frameworks like [Mastercard Agent Pay](../standards/mastercard-agent-pay.md), it establishes cryptographic evidence confirming that autonomous agent actions remain strictly within the bounds delegated by a user [^evt-ext-frmoretto-agentic-standards-map-85d122-file-ce1194c318a5-d3d9cfd8].

# Architecture / Specification
Verifiable Intent structures agent mandates and user constraints through a layered Selective Disclosure JSON Web Token (SD-JWT) credential [^evt-ext-frmoretto-agentic-standards-map-85d122-file-ce1194c318a5-d3d9cfd8]:
- **Credential Layers**: Layers convey signed claims covering checkout details, merchant parameters, and user constraints [^evt-ext-frmoretto-agentic-standards-map-85d122-file-ce1194c318a5-d3d9cfd8].
- **Autonomous Execution**: In autonomous execution mode, the merchant receives a Layer 3b checkout mandate [^evt-ext-frmoretto-agentic-standards-map-85d122-file-ce1194c318a5-d3d9cfd8].
- **Scope Boundaries**: Transport protocols, key management, provider enrollment, agent platform APIs, dispute resolution, and regulatory compliance mapping are explicitly designated out of scope in the specification README [^evt-ext-frmoretto-agentic-standards-map-85d122-file-ce1194c318a5-d3d9cfd8].

# Lifecycle History
- 2026-04-20: Last commit (356c296) to the agent-intent repository [^evt-ext-frmoretto-agentic-standards-map-85d122-file-ce1194c318a5-d3d9cfd8].
- 2026-04-28: FIDO Alliance announces contribution of Verifiable Intent by Mastercard to the Payments Technical Working Group [^evt-ext-frmoretto-agentic-standards-map-85d122-file-ce1194c318a5-d3d9cfd8].

# References
- [agent-intent/verifiable-intent Repository](https://github.com/agent-intent/verifiable-intent/blob/main/README.md)
- [Verifiable Intent Design Rationale](https://github.com/agent-intent/verifiable-intent/blob/main/spec/design-rationale.md)

[^evt-ext-frmoretto-agentic-standards-map-85d122-file-ce1194c318a5-d3d9cfd8]: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/verifiable-intent.yaml
