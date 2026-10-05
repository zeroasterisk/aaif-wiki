---
type: proposal
title: ContextForge
description: Open-source gateway registry and federation proxy providing governance,
  discovery, and observability across MCP, A2A, and REST/gRPC interfaces.
resource: https://github.com/aaif/project-proposals/issues/39
tags:
- mcp
- gateway
- registry
- governance
- project-proposal
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:17:44.098129+00:00'
sources:
- id: evt-project-proposals-issue-39
  resource: https://github.com/aaif/project-proposals/issues/39
  author: jtborek206
  last_modified: '2026-09-29T22:18:43+00:00'
---

# Overview
ContextForge is an extensible open-source registry, gateway proxy, and governance control plane designed to federate Model Context Protocol (MCP), Agent-to-Agent (A2A), and REST/gRPC communication across enterprise agent ecosystems.[^evt-project-proposals-issue-39]

# Architecture / Specification
ContextForge establishes centralized management and discovery for distributed agent tools and endpoints:[^evt-project-proposals-issue-39]
- **Multi-Protocol Federation**: Bridges MCP servers, A2A agents, and legacy REST/gRPC services into a unified access and routing layer.[^evt-project-proposals-issue-39]
- **Governance and Security**: Implements dynamic policy enforcement, authentication, and compliance validation before releasing tool access to client agents, complementing gateway infrastructure like `../proposals/mcp-gateway-registry.md`.[^evt-project-proposals-issue-39]
- **Plugin Architecture**: Enables modular expansion of transports, security controls, telemetry instrumentation, and protocol adapters without modifying the core gateway daemon.[^evt-project-proposals-issue-39]

# Lifecycle History
Initiated within IBM Consulting and maintained as open-source under the Apache-2.0 license, ContextForge was submitted to the AAIF Technical Committee (`../governance/technical-committee.md`) as a hosted project proposal transitioning toward foundation open governance.[^evt-project-proposals-issue-39]

[^evt-project-proposals-issue-39]: https://github.com/aaif/project-proposals/issues/39
