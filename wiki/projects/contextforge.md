---
type: project
title: ContextForge
description: Open-source registry and gateway federating MCP, A2A, and REST/gRPC interfaces
  with centralized governance, discovery, and observability.
resource: https://github.com/aaif/project-proposals/issues/39
tags:
- aaif
- project
- gateway
- registry
- mcp
- a2a
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:49:55.277955+00:00'
sources:
- id: evt-project-proposals-issue-39
  resource: https://github.com/aaif/project-proposals/issues/39
  author: jtborek206
  last_modified: '2026-09-29T22:18:43+00:00'
---

# Overview
ContextForge is an open-source registry and proxy control plane that federates Model Context Protocol (MCP), Agent-to-Agent (A2A), and REST/gRPC endpoints under centralized discovery, governance, and observability controls[^evt-project-proposals-issue-39]. It provides extensible infrastructure enabling developers and enterprise operators to manage tool calling, reference implementations, and access policies across heterogeneous AI agent ecosystems[^evt-project-proposals-issue-39].

# Architecture / Specification
ContextForge is built with a plugin-driven extensible architecture designed to operate across developer workstations and production clusters[^evt-project-proposals-issue-39]:
- **Protocol Federation**: Bridges MCP servers, A2A agents ([`../projects/a2a.md`](../projects/a2a.md)), and traditional REST/gRPC APIs into a unified registry and discovery surface[^evt-project-proposals-issue-39].
- **Extensible Plugin Model**: Supports over 40 modular plugins extending transports, identity, security boundaries, and telemetry integrations without modifying core runtime logic[^evt-project-proposals-issue-39].
- **Governance & Policy Plane**: Integrates centralized authentication, authorization, token-level access controls, and runtime monitoring to enforce enterprise guardrails alongside projects such as MCP Gateway and Registry ([`../projects/mcp-gateway-registry.md`](../projects/mcp-gateway-registry.md))[^evt-project-proposals-issue-39].

# Lifecycle History
- **2025–Early 2026**: Developed at IBM Consulting by Mihai Creviti to standardize MCP proxying and registry capabilities[^evt-project-proposals-issue-39].
- **July 2026**: Reached over 4,100 GitHub stars and 2.6 million downloads; submitted as an AAIF hosted project proposal transitioning from IBM stewardship to open foundation governance[^evt-project-proposals-issue-39].

[^evt-project-proposals-issue-39]: https://github.com/aaif/project-proposals/issues/39
