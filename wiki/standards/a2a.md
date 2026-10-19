---
type: standard
title: Agent-to-Agent Protocol (A2A)
description: Open protocol standardizing agent-to-agent communication, AgentCard manifests,
  and task lifecycle coordination.
resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/a2a-discovery.yaml
tags:
- external
- standards
- protocols
- a2a
- aaif
- discovery
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T01:47:57.406359+00:00'
sources:
- id: evt-ext-frmoretto-agentic-standards-map-85d122-file-8077c2a39f6e-fa46d5dc
  resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/a2a-discovery.yaml
  author: frmoretto
  last_modified: '2026-10-14T06:46:06+02:00'
---

# Overview
The Agent-to-Agent (A2A) protocol is a project of the Agentic AI Foundation (AAIF), a Linux Foundation directed fund, designed to enable secure, structured interaction between autonomous AI agents across security domains[^evt-ext-frmoretto-agentic-standards-map-85d122-file-8077c2a39f6e-fa46d5dc]. A2A establishes mechanisms for mutual discovery, capability advertisement via AgentCards, and end-to-end task delegation[^evt-ext-frmoretto-agentic-standards-map-85d122-file-8077c2a39f6e-fa46d5dc].

# Architecture / Specification

### Discovery Mechanisms
A2A standardizes agent location and capability lookup using well-known URI endpoints[^evt-ext-frmoretto-agentic-standards-map-85d122-file-8077c2a39f6e-fa46d5dc]:
- **Default Endpoint**: The protocol standardizes `/.well-known/agent-card.json` for publishing an agent's capability card and public keys[^evt-ext-frmoretto-agentic-standards-map-85d122-file-8077c2a39f6e-fa46d5dc].
- **Multi-Agent Discovery Proposals**: For hosts hosting multiple agents, active open proposals include `/.well-known/ai-catalog.json` (PR #2240) linking to `../standards/ai-catalog.md`, `/.well-known/agent-card-list.json` (issue #2276), and a standardized `ListAgents` RPC endpoint (issue #2248)[^evt-ext-frmoretto-agentic-standards-map-85d122-file-8077c2a39f6e-fa46d5dc].
- **Boundary Limitations**: The core A2A specification explicitly does not define a curated registry standard or centralized discovery API, deferring external cataloging and trust metadata to companion specifications like `../standards/ai-catalog.md`[^evt-ext-frmoretto-agentic-standards-map-85d122-file-8077c2a39f6e-fa46d5dc].

### Task and State Lifecycle
A2A coordinates distributed multi-agent interactions through standardized lifecycle states and delegation handoffs. For commerce operations, A2A supports credential-bearing mandate extensions defined by `../standards/ap2.md`.

# Lifecycle History
- **2026-05-28**: A2A v1.0.1 released[^evt-ext-frmoretto-agentic-standards-map-85d122-file-8077c2a39f6e-fa46d5dc].
- **2026-09-16**: Pull request #2240 opened proposing `/.well-known/ai-catalog.json` as a preferred multi-agent discovery path[^evt-ext-frmoretto-agentic-standards-map-85d122-file-8077c2a39f6e-fa46d5dc].
- **2026-10-01**: Proposal issue #2276 submitted proposing `/.well-known/agent-card-list.json` for multi-agent hosts[^evt-ext-frmoretto-agentic-standards-map-85d122-file-8077c2a39f6e-fa46d5dc].
- **2026-10-07**: HTTP Archive custom-metrics PR #176 merged to track global deployment of `/.well-known/agent-card.json` endpoints[^evt-ext-frmoretto-agentic-standards-map-85d122-file-8077c2a39f6e-fa46d5dc].

[^evt-ext-frmoretto-agentic-standards-map-85d122-file-8077c2a39f6e-fa46d5dc]: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/a2a-discovery.yaml
