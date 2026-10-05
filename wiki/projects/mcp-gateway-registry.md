---
type: project
title: MCP Gateway & Registry
description: Unified gateway and registry control plane for centralizing discovery,
  enterprise authentication, tool-level authorization, and A2A federation for MCP
  servers and agent skills.
resource: https://github.com/aaif/project-proposals/issues/29
tags:
- mcp
- gateway
- registry
- a2a
- access-control
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:46:37.126348+00:00'
sources:
- id: evt-project-proposals-issue-29
  resource: https://github.com/aaif/project-proposals/issues/29
  author: aarora79
  last_modified: '2026-09-24T05:53:05+00:00'
---

# Overview
MCP Gateway & Registry is an open-source unified platform and control plane that centralizes access to Model Context Protocol (MCP) servers, AI agents, and reusable agent skills.[^evt-project-proposals-issue-29] It addresses tool sprawl, credential isolation, and audit visibility across enterprise coding assistants and autonomous multi-agent environments.[^evt-project-proposals-issue-29]

# Architecture / Specification
The platform operates across four primary functional areas:[^evt-project-proposals-issue-29]
- **Unified MCP Server Gateway**: Proxies traffic to registered MCP servers, providing dynamic semantic tool discovery, tool aggregation into virtual MCP servers, and method-level access controls.
- **MCP Servers Registry**: Implements the Anthropic MCP Registry REST API v0.1 specification, enabling standards-compliant client discovery, server cataloging, and automated security scanning.
- **Agent Registry and A2A Communication Hub**: Hosts signed `../projects/a2a.md` agent cards for authenticated agent discovery, enabling direct peer-to-peer communication without proxying wire traffic.
- **Agent Skills Registry**: Maintains a governed catalog of reusable agent skills with per-skill credential isolation and security scanning.

Federation features include peer-to-peer registry federation, upstream imports from Anthropic MCP Registry, and federation with AWS Agent Registry / Amazon Bedrock AgentCore.[^evt-project-proposals-issue-29] Enterprise identity support spans Keycloak, Microsoft Entra ID, Okta, Auth0, and Amazon Cognito.[^evt-project-proposals-issue-29]

# Lifecycle History
- Submitted as an AAIF project proposal via issue #29 under Apache 2.0 licensing.[^evt-project-proposals-issue-29]

# References
- `../projects/a2a.md`
- `../reference-architectures/goose.md`
- `../governance/project-proposal-process.md`

[^evt-project-proposals-issue-29]: https://github.com/aaif/project-proposals/issues/29
