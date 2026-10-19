---
type: resource
title: AgentGateway
description: Open-source traffic mediation and policy enforcement proxy managing MCP
  and A2A communications as a network-path security checkpoint.
resource: https://github.com/aaif/wg-security-and-privacy/pull/38
tags:
- proxy
- mcp
- security
- checkpoint
- traffic-mediation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T11:10:42.748405+00:00'
sources:
- id: evt-wg-security-and-privacy-pr-38
  resource: https://github.com/aaif/wg-security-and-privacy/pull/38
  author: barka-bee
  last_modified: '2026-10-12T11:44:58+00:00'
---

# Overview
AgentGateway is an open-source traffic mediation and policy enforcement proxy under the Agentic AI Foundation that governs Model Context Protocol (MCP) and Agent-to-Agent (A2A) protocol communications.[^evt-wg-security-and-privacy-pr-38] It provides network-level control and checkpointing between runtime environments and distributed tool servers.[^evt-wg-security-and-privacy-pr-38]

# Architecture / Specification
AgentGateway operates on the network communication path alongside host-level runtime hooks:[^evt-wg-security-and-privacy-pr-38]
- **Network Checkpoint**: Serves as a single controlled entry point mediating traffic destined for remote MCP servers, preventing uninspected direct outbound calls.
- **Credential and Identity Management**: Centralizes OAuth credential exchanges and upstream authorization headers.
- **Granular Access Control**: Enforces per-tool execution policies and protocol-level filtering across agent identities.
- **Audit Telemetry**: Captures tool invocation payloads and telemetry to support verifiable downstream action logs.

# References
- Security best practices checkpoint positioning: https://github.com/aaif/wg-security-and-privacy/pull/38 [^evt-wg-security-and-privacy-pr-38]

[^evt-wg-security-and-privacy-pr-38]: https://github.com/aaif/wg-security-and-privacy/pull/38
