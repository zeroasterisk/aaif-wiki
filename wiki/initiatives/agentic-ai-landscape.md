---
type: initiative
title: Agentic AI Landscape
description: Interactive CNCF-style ecosystem architecture map and project watchlist
  categorizing open-source software and tools for agentic AI.
resource: https://github.com/aaif/aaif-landscape/pull/18
tags:
- initiatives
- landscape
- ecosystem
- cncf
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T09:57:19.945291+00:00'
sources:
- id: evt-aaif-landscape-pr-18
  resource: https://github.com/aaif/aaif-landscape/pull/18
  author: ralf0131
  last_modified: '2026-08-18T23:20:32+00:00'
---

# Overview
The Agentic AI Landscape is an interactive ecosystem map modeled on the CNCF Landscape that categorizes open-source and standard technologies across the agentic AI infrastructure stack[^evt-aaif-landscape-pr-18].

# Architecture / Specification
The landscape organizes projects across key categories including:
- **Frameworks & Infrastructure**: Encompasses orchestration engines, multi-agent frameworks, and AI gateways. Key subcategories include **Orchestration & Multi-Agent**, which tracks multi-protocol AI gateways such as Higress and Solo.io's agentgateway that provide unified control planes for Model Context Protocol (MCP) server hosting, agent-to-agent communication, and LLM inference governance[^evt-aaif-landscape-pr-18].
- **Agent Communication & Protocols**: Protocols and client-server specifications for agent interactions.
- **Security & Observability**: Runtimes, guardrails, and telemetry tools for monitoring agent behavior.

# Lifecycle History
- Merged PR #18 added Higress (CNCF Sandbox AI Gateway) to Frameworks & Infrastructure → Orchestration & Multi-Agent[^evt-aaif-landscape-pr-18].

[^evt-aaif-landscape-pr-18]: https://github.com/aaif/aaif-landscape/pull/18
