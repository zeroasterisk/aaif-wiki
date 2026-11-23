---
type: resource
title: Agentic AI Ecosystem Landscape
description: Taxonomy catalog and ecosystem landscape mapping agentic frameworks,
  protocols, security tooling, runtime gateways, and file conventions.
resource: https://github.com/aaif/ws-taxonomy-landscape/pull/30
tags:
- landscape
- taxonomy
- ecosystem
- catalog
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:23:07.783010+00:00'
sources:
- id: evt-ws-taxonomy-landscape-pr-30
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/30
  author: asish-singh
  last_modified: '2026-10-11T18:18:09+00:00'
- id: evt-ws-taxonomy-landscape-pr-31
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/31
  author: asish-singh
  last_modified: '2026-10-11T18:18:13+00:00'
---

# Overview

The Agentic AI Ecosystem Landscape is an open taxonomy and project catalog tracking frameworks, runtime systems, protocols, guardrails, and developer tooling across the agentic technology domain [^evt-ws-taxonomy-landscape-pr-30]. Managed under the Taxonomy & Landscape Working Group, the landscape models industry initiatives according to standard data schemas, objective descriptive criteria, and non-promotional neutral criteria [^evt-ws-taxonomy-landscape-pr-30].

# Architecture / Specification

Entries in `landscape/landscape.yml` are categorized across primary domains and subcategories governed by strict validation rules:

- **Category Evolution:** Proposals have introduced dedicated subcategories to accommodate emerging architectural patterns [^evt-ws-taxonomy-landscape-pr-30]:
  - *Gateways & Control Planes:* Established under Agent Runtimes, Frameworks & Workflow Orchestration to classify traffic-mediating and routing infrastructure like [AgentGateway](../resources/agentgateway.md), distinguishing mediation layers from agentic orchestration frameworks and guardrails [^evt-ws-taxonomy-landscape-pr-30].
  - *Conventions & File Formats:* Structured under Protocols & Discovery Registries to house declarative repository guidelines such as `AGENTS.md`, distinguishing file conventions from network wire protocols like [A2A](../taxonomy/agent-to-agent.md) and [MCP](../resources/agent-mcp-server-boundary.md) [^evt-ws-taxonomy-landscape-pr-30].
- **Metadata Hygiene:** Projects undergo active URI and repository status verification to ensure canonical domain mappings (e.g., tracking repository migrations across A2A, OpenHands, and CrewAI) and maintain non-redirecting documentation endpoints [^evt-ws-taxonomy-landscape-pr-31].

[^evt-ws-taxonomy-landscape-pr-30]: https://github.com/aaif/ws-taxonomy-landscape/pull/30
[^evt-ws-taxonomy-landscape-pr-31]: https://github.com/aaif/ws-taxonomy-landscape/pull/31
