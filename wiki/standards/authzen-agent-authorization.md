---
type: standard
title: AuthZEN Agent Authorization (AARP and COAZ)
description: Draft specifications stewarded by the OpenID Foundation defining prerequisite
  policy checks and MCP tool authorization profiles.
resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/oidf-authzen-agents.yaml
tags:
- external
- standards
- openid-foundation
- authorization
- mcp
- security
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T01:47:57.406359+00:00'
sources:
- id: evt-ext-frmoretto-agentic-standards-map-85d122-file-842244016ea9-8610d756
  resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/oidf-authzen-agents.yaml
  author: frmoretto
  last_modified: '2026-10-14T04:52:24+02:00'
---

# Overview
AuthZEN Agent Authorization is a suite of draft specifications stewarded by the OpenID Foundation AuthZEN Working Group providing standardized access control architectures for agentic AI systems[^evt-ext-frmoretto-agentic-standards-map-85d122-file-842244016ea9-8610d756]. Adopted as working group drafts in June 2026, the specifications define profiles for validating policy prerequisites and intercepting agent tool executions[^evt-ext-frmoretto-agentic-standards-map-85d122-file-842244016ea9-8610d756].

# Architecture / Specification
The AuthZEN agent framework comprises two complementary specifications:
- **Agent Authorization Request Profile (AARP)**: Specifies mechanisms for evaluating policy prerequisites before authorization decisions are rendered. Prerequisites include capturing explicit human approvals, tracking user consent, and evaluating runtime hardware or software attestations[^evt-ext-frmoretto-agentic-standards-map-85d122-file-842244016ea9-8610d756].
- **Client-Oriented Agent Authorization (COAZ)**: A specialized authorization profile for `../standards/model-context-protocol.md` (MCP) tool execution. COAZ maps MCP protocol operations and parameter schemas into the standard AuthZEN Subject-Action-Resource-Context (SARC) policy model[^evt-ext-frmoretto-agentic-standards-map-85d122-file-842244016ea9-8610d756].

### Strategic Alignment
The specifications build upon the OpenID Foundation's whitepaper "Identity Management for Agentic AI", which outlines requirements for securing agent interactions against unauthorized tool invocations and coordinates with standards such as `../standards/ietf-webbotauth.md` and `../standards/ap2.md`[^evt-ext-frmoretto-agentic-standards-map-85d122-file-842244016ea9-8610d756].

# Lifecycle History
- **2025-10-07**: OpenID Foundation published the "Identity Management for Agentic AI" whitepaper establishing the agent security problem space[^evt-ext-frmoretto-agentic-standards-map-85d122-file-842244016ea9-8610d756].
- **2026-06-15**: AuthZEN Working Group officially adopted AARP and COAZ as Working Group Drafts for community review and interoperability testing[^evt-ext-frmoretto-agentic-standards-map-85d122-file-842244016ea9-8610d756].

[^evt-ext-frmoretto-agentic-standards-map-85d122-file-842244016ea9-8610d756]: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/oidf-authzen-agents.yaml
