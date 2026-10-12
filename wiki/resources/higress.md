---
type: resource
title: Higress
description: Cloud-native AI gateway and CNCF Sandbox project providing MCP server
  hosting, LLM API routing, and agent traffic governance.
resource: https://github.com/aaif/aaif-landscape/pull/18
tags:
- gateway
- mcp
- orchestration
- infrastructure
- cncf
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T02:49:11.305907+00:00'
sources:
- id: evt-aaif-landscape-pr-18
  resource: https://github.com/aaif/aaif-landscape/pull/18
  author: ralf0131
  last_modified: '2026-08-18T23:20:32+00:00'
---

# Overview
Higress is an open-source, cloud-native AI gateway built on Envoy and Istio that provides a unified control plane for LLM API management, Model Context Protocol (MCP) server hosting, and AI agent traffic governance[^evt-aaif-landscape-pr-18]. Originally developed by Alibaba and hosted as a Cloud Native Computing Foundation (CNCF) Sandbox project, Higress is positioned in the [Agentic AI Landscape](agentic-ai-landscape.md) within the Orchestration & Multi-Agent subcategory alongside gateway systems like Solo.io's `agentgateway`[^evt-aaif-landscape-pr-18].

# Architecture / Specification
Higress bridges infrastructure traffic routing with agent protocol boundaries:
- **Model Context Protocol (MCP) Server Hosting & Registry**: Exposes built-in hosting, registry, and routing mechanisms for MCP tool servers across heterogeneous backends[^evt-aaif-landscape-pr-18].
- **Unified AI Traffic Management**: Intercepts and routes model inference requests, agent-to-agent communication streams, and external tool calls through an Envoy proxy data plane[^evt-aaif-landscape-pr-18].
- **Policy and Observability Boundary**: Implements rate limiting, token-aware routing, authentication, and traffic security policies at the protocol boundary before requests reach foundational models or downstream agent tools[^evt-aaif-landscape-pr-18].

# References
- Upstream Repository: https://github.com/alibaba/higress [^evt-aaif-landscape-pr-18]
- Boundary Interoperability: [Agent-MCP Server Boundary](agent-mcp-server-boundary.md)
- Related Gateways: [Context Forge](context-forge.md)

[^evt-aaif-landscape-pr-18]: https://github.com/aaif/aaif-landscape/pull/18
