---
type: resource
title: ContextForge
description: Open-source registry and gateway proxy federating MCP, A2A, and REST/gRPC
  interfaces with centralized governance and discovery.
resource: https://github.com/aaif/project-proposals/issues/39
tags:
- gateways
- mcp
- a2a
- governance
- observability
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:12:58.013933+00:00'
sources:
- id: evt-project-proposals-issue-39
  resource: https://github.com/aaif/project-proposals/issues/39
  author: jtborek206
  last_modified: '2026-09-29T22:18:43+00:00'
---

# Overview
ContextForge is an open-source registry and proxy platform that federates Model Context Protocol (MCP), Agent-to-Agent (A2A), and REST/gRPC interfaces with centralized discovery, policy governance, and observability [^evt-project-proposals-issue-39]. It provides an extensible integration layer designed to manage agent-to-tool and agent-to-agent interactions across development and production environments [^evt-project-proposals-issue-39].

# Architecture / Specification
ContextForge serves as a management and federation plane for agent tool and capability runtimes [^evt-project-proposals-issue-39]:
- **Protocol Federation**: Aggregates disparate interfaces including MCP, A2A, REST, and gRPC endpoints behind a unified gateway [^evt-project-proposals-issue-39].
- **Extensible Plugin System**: Features a modular architecture supporting custom transports, authentication mechanisms, policy controls, and integrations without modifying the core gateway [^evt-project-proposals-issue-39].
- **Registry and Discovery**: Provides centralized catalogs for publishing, browsing, and resolving available tools, prompts, resources, and agent capabilities [^evt-project-proposals-issue-39].
- **Governance and Observability**: Enforces centralized access policies, telemetry collection, and compliance verification across tool calls [^evt-project-proposals-issue-39].

# Lifecycle History
ContextForge was submitted to the Agentic AI Foundation as a hosted project proposal in July 2026 under the Apache License 2.0 [^evt-project-proposals-issue-39].

# References
- AAIF Project Proposals: [Issue #39](https://github.com/aaif/project-proposals/issues/39) [^evt-project-proposals-issue-39]

[^evt-project-proposals-issue-39]: https://github.com/aaif/project-proposals/issues/39
