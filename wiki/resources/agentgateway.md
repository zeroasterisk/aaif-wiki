---
type: resource
title: AgentGateway
description: Open-source traffic mediation and policy enforcement proxy managing MCP
  and A2A communications as an AAIF project.
resource: https://github.com/aaif/wg-security-and-privacy/pull/38
tags:
- mcp
- gateway
- proxy
- security
- aaif-project
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:24:23.493689+00:00'
sources:
- id: evt-wg-security-and-privacy-pr-38
  resource: https://github.com/aaif/wg-security-and-privacy/pull/38
  author: barka-bee
  last_modified: '2026-10-12T11:44:58+00:00'
---

# Overview

AgentGateway is an open-source traffic mediation and policy enforcement proxy governed under the Agentic AI Foundation, designed to manage Model Context Protocol (MCP) and Agent-to-Agent (A2A) network communications [^evt-wg-security-and-privacy-pr-38]. Within the foundation's architectural guidance, it operates as an authoritative network checkpoint deployed alongside in-process runtime hooks [^evt-wg-security-and-privacy-pr-38].

# Architecture / Specification

AgentGateway provides network-level boundary controls across external agent communications [^evt-wg-security-and-privacy-pr-38]:

- **Consolidated Endpoint**: Provides a single network ingress and egress point mediating access to remote MCP servers [^evt-wg-security-and-privacy-pr-38].
- **Authentication & OAuth**: Manages authentication handshakes, token exchange, and OAuth lifecycle flows on behalf of communicating agents [^evt-wg-security-and-privacy-pr-38].
- **Granular Permission Policies**: Enforces per-tool execution policies on the wire before invocations reach target servers [^evt-wg-security-and-privacy-pr-38].
- **Payload Capture**: Collects and structures complete invocation payloads to produce audit logs and action events [^evt-wg-security-and-privacy-pr-38].
- **Hook Co-Design**: Coordinates with runtime interception hooks defined in the [Agentic AI Security Best Practices](../guidelines/agentic-ai-security-best-practices.md), where local hooks assess in-process call context while AgentGateway secures the perimeter network path [^evt-wg-security-and-privacy-pr-38].

# Lifecycle History

- Documented as an AAIF project and incorporated into Section 3.1 and Section 7 of the Security and Privacy Working Group's best practices guide via PR #38 [^evt-wg-security-and-privacy-pr-38].

[^evt-wg-security-and-privacy-pr-38]: https://github.com/aaif/wg-security-and-privacy/pull/38
