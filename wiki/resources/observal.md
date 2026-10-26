---
type: resource
title: Observal
description: Self-hosted registry, multi-harness configuration renderer, and insight
  engine governing agentic resources and client-side execution.
resource: https://github.com/aaif/project-proposals/issues/59
tags:
- registry
- mcp
- agent-skills
- observability
- governance
- a2a
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T11:12:22.882582+00:00'
sources:
- id: evt-project-proposals-issue-59
  resource: https://github.com/aaif/project-proposals/issues/59
  author: Haz3-jolt
  last_modified: '2026-10-14T19:19:53+00:00'
---

# Overview
Observal is an open-source (Apache-2.0), self-hosted registry and system of record for agentic resources, including Agent Skills, Model Context Protocol (MCP) servers, hooks, prompts, sandboxes, and bundling agent configurations.[^evt-project-proposals-issue-59] Operating beside the live request path rather than acting as an inline proxy, Observal manages artifacts prior to execution by rendering native client configurations and evaluates performance post-session via client trace ingestion and LLM-assisted insights.[^evt-project-proposals-issue-59]

# Architecture / Specification
Observal provides artifact governance, cross-client installation, and post-session telemetry mediation:[^evt-project-proposals-issue-59]
- **Resource Registry**: Versioned catalog supporting team namespaces, visibility controls, and pull-request review workflows across five agentic resource types.[^evt-project-proposals-issue-59]
- **Multi-Harness Configuration**: Generates native harness configurations and lockfiles across ten agent runtimes, including Claude Code, Codex, Cursor, Kiro, Copilot in VS Code, Copilot CLI, OpenCode, Antigravity, [Goose](goose.md), and Pi.[^evt-project-proposals-issue-59]
- **Open Protocol Integration**: Publishes approved resources using [Agentic Resource Discovery](../standards/agentic-resource-discovery.md) (ARD v0.91) entries with `urn:air:` identifiers at `/.well-known/ard.json`, executes agent-to-agent delegation via [A2A](../standards/agent-network-protocol.md) Task definitions through a bundled MCP server, and aligns with the [Agent Skills](../standards/agent-skills.md) specification.[^evt-project-proposals-issue-59]
- **Client Traces and Insights**: Client hooks capture session execution data—including prompt context, tool invocations, MCP round trips, token usage, and errors—pinned directly to installed artifact versions, generating diagnostic failure insights via LiteLLM.[^evt-project-proposals-issue-59]
- **Self-Hosted Infrastructure**: Deploys on Postgres, ClickHouse, and Redis via Docker Compose or Kubernetes without external data egress, providing unified SSO, SCIM, and audit logging.[^evt-project-proposals-issue-59]

Unlike inline traffic proxies such as [Agentgateway](agentgateway.md) that mediate active network requests, Observal operates at install time and post-session, drawing evidence directly from client-side hooks.[^evt-project-proposals-issue-59]

# Lifecycle History
Observal was submitted to the AAIF Technical Committee as an open project proposal in Issue #59 on October 14, 2026, following 46 prior independent open-source releases.[^evt-project-proposals-issue-59]

[^evt-project-proposals-issue-59]: https://github.com/aaif/project-proposals/issues/59
