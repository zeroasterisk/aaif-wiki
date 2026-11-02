---
type: resource
title: AgentGateway
description: Open-source traffic mediation and policy enforcement proxy managing MCP
  and A2A communications as a network checkpoint feeding runtime execution hooks.
resource: https://github.com/aaif/wg-security-and-privacy/issues/30
tags:
- proxy
- mcp
- a2a
- gateway
- enforcement
- security
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:15:51.752089+00:00'
sources:
- id: evt-wg-security-and-privacy-issue-30
  resource: https://github.com/aaif/wg-security-and-privacy/issues/30
  author: barka-bee
  last_modified: '2026-10-05T13:51:53+00:00'
---

# Overview

AgentGateway is an open-source traffic mediation proxy and perimeter enforcement engine governing Model Context Protocol (MCP) and Agent-to-Agent (A2A) network communications. Accepted into the Agentic AI Foundation in June 2026, the project acts as a network-level policy checkpoint that mediates transport boundaries, standardizes protocol auth, and records full-fidelity request and response audit logs [^evt-wg-security-and-privacy-issue-30].

# Architecture / Specification

## Network Boundary Role
AgentGateway operates at the network ingress and egress points for distributed agent systems [^evt-wg-security-and-privacy-issue-30]:
- **Protocol Translation**: Terminates remote MCP and A2A sessions over HTTP, SSE, and WebSocket transports, normalizing authentication headers and mapping OAuth credentials [^evt-wg-security-and-privacy-issue-30].
- **Centralized Telemetry**: Intercepts request and response payloads across remote MCP servers, streaming structured audit records to security monitoring and observability backends [^evt-wg-security-and-privacy-issue-30].
- **Perimeter Access Control**: Applies coarse-grained permission checks, network allowlists, and traffic rate limits across multi-tenant agent deployments [^evt-wg-security-and-privacy-issue-30].

## Coordination with In-Loop Hooks
Within the broader security architecture (../guidelines/agentic-ai-security-best-practices.md), AgentGateway acts as a perimeter control rather than an isolated policy engine [^evt-wg-security-and-privacy-issue-30]:
- **Transport Coverage**: Network gateways cannot inspect local `stdio` MCP processes, shell commands, or SDK-native function calls [^evt-wg-security-and-privacy-issue-30].
- **Prompt Context Gap**: Gateways evaluate invocations at the wire level without visibility into the conversational trajectory or prompting context that produced them [^evt-wg-security-and-privacy-issue-30].
- **Complementary Architecture**: AgentGateway captures remote network payloads and validates perimeter credentials, while runtime hooks embedded directly inside the agent loop enforce context-aware policies and least-privilege constraints across all transport types [^evt-wg-security-and-privacy-issue-30].

# Lifecycle History
Onboarded as an AAIF project in June 2026, AgentGateway's position within defense-in-depth frameworks was refined in Security and Privacy Working Group discussions to define its boundary alongside in-loop agent hooks [^evt-wg-security-and-privacy-issue-30].

[^evt-wg-security-and-privacy-issue-30]: https://github.com/aaif/wg-security-and-privacy/issues/30
