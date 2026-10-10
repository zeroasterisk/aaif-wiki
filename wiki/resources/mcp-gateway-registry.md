---
type: resource
title: MCP Gateway & Registry
description: Centralized control plane and discovery catalog providing authentication,
  access control, and registry federation for MCP servers, agents, and skills
resource: https://github.com/aaif/project-proposals/issues/29
tags:
- mcp
- gateway
- registry
- governance
- a2a
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:10:52.026714+00:00'
sources:
- id: evt-project-proposals-issue-29
  resource: https://github.com/aaif/project-proposals/issues/29
  author: aarora79
  last_modified: '2026-09-24T05:53:05+00:00'
---

# Overview
MCP Gateway & Registry is an open-source governance and discovery platform providing a unified control plane for centralizing access to Model Context Protocol (MCP) servers, AI agents, and reusable agent skills.[^evt-project-proposals-issue-29]

# Architecture / Specification
The platform is organized into four core functional layers:[^evt-project-proposals-issue-29]
- **MCP Server Gateway**: Acts as a reverse proxy for MCP servers, enforcing enterprise single sign-on (Keycloak, Microsoft Entra ID, Okta, Auth0, Amazon Cognito), fine-grained tool/method authorization, compliance audit trails, and real-time telemetry.
- **MCP Servers Registry**: Implements the Anthropic MCP Registry REST API v0.1 specification, enabling dynamic tool discovery, semantic search, and virtual MCP server aggregations across coding assistants and client runtimes such as [goose](../resources/goose.md).
- **Agent Registry and A2A Communication Hub**: Hosts Agent-to-Agent (A2A) protocol agent cards for authenticated capability discovery while allowing agents to communicate directly peer-to-peer.
- **Agent Skills Registry**: Manages reusable modular skills with isolated credential storage and security scanning.

The system supports peer-to-peer registry federation across autonomous enterprise deployments as well as upstream synchronization with external registries.[^evt-project-proposals-issue-29]

# Lifecycle History
Initiated in May 2025, the project was submitted under Apache 2.0 licensing as an Agentic AI Foundation project proposal.[^evt-project-proposals-issue-29]

[^evt-project-proposals-issue-29]: https://github.com/aaif/project-proposals/issues/29
