---
type: proposal
title: MCP Gateway & Registry
description: Centralized control plane and catalog for discovering, proxying, and
  governing access to MCP servers, A2A agents, and reusable skills.
resource: https://github.com/aaif/project-proposals/issues/29
tags:
- mcp
- registry
- gateway
- a2a
- governance
- security
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:14:45.253933+00:00'
sources:
- id: evt-project-proposals-issue-29
  resource: https://github.com/aaif/project-proposals/issues/29
  author: aarora79
  last_modified: '2026-09-24T05:53:05+00:00'
---

# Overview

The MCP Gateway & Registry is an open-source platform designed to centralize and govern enterprise access to AI assets, specifically Model Context Protocol (MCP) servers, Agent-to-Agent (A2A) protocol agents, and reusable agent skills [^evt-project-proposals-issue-29]. It addresses credential sprawl, security blindspots, and integration overhead by acting as a single, governed control plane between AI development tools, coding assistants, autonomous agents, and backend tools.

# Architecture / Specification

The project implements four core functional layers [^evt-project-proposals-issue-29]:

1. **MCP Server Gateway**: A proxy providing single-point ingress to multiple MCP servers with fine-grained authorization at the tool and method level, virtual MCP server aggregation, and real-time observability.
2. **MCP Servers Registry**: Discovery and governance catalog implementing the upstream Anthropic MCP Registry REST API v0.1 specification.
3. **Agent Registry & A2A Communication Hub**: Agent card registration and semantic search discovery for direct peer-to-peer agent-to-agent communication via the A2A protocol.
4. **Agent Skills Registry**: Catalog for versioned, reusable skills providing per-skill credential management and integrated security scanning.

### Security and Federation

The platform integrates with enterprise Identity Providers (Keycloak, Microsoft Entra ID, Okta, Auth0, Amazon Cognito) for developer and machine-to-machine authentication [^evt-project-proposals-issue-29]. It incorporates automated security scanning for MCP servers, agents, and skills via Cisco AI Defense. The architecture supports three federation patterns:
- Peer-to-peer registry federation across autonomous enterprise instances.
- Upstream server sync with the Anthropic MCP Registry.
- Federation with AWS Agent Registry / Amazon Bedrock AgentCore.

# Lifecycle History

Submitted to the Agentic AI Foundation under Apache 2.0 licensing, originating from community development in May 2025 [^evt-project-proposals-issue-29]. It is positioned as complementary to client-side agent runtimes such as [Goose](../reference-architectures/goose.md) and repository context conventions like AGENTS.md, as well as data-plane proxy proposals.

# References

- [Agent-to-Agent Protocol and MCP Registry Proposal](https://github.com/aaif/project-proposals/issues/29)
- [Goose Reference Architecture](../reference-architectures/goose.md)
- [Agent Behavior Trace Model](../proposals/agent-behavior-trace-model.md)

[^evt-project-proposals-issue-29]: https://github.com/aaif/project-proposals/issues/29
