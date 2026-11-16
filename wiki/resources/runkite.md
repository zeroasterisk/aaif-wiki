---
type: resource
title: Runkite
description: Open-source self-hosted control plane for AI agents separating operational
  run lifecycle, approval gates, and spend accounting from model-loop execution.
resource: https://github.com/aaif/project-proposals/issues/69
tags:
- resource
- control-plane
- orchestration
- mcp
- sandbox-proposal
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:43:19.607440+00:00'
sources:
- id: evt-project-proposals-issue-69
  resource: https://github.com/aaif/project-proposals/issues/69
  author: sharanharsoor
  last_modified: '2026-11-08T18:47:26+00:00'
---

# Overview
Runkite is an open-source, self-hosted control plane for AI agents that decouples operational agent management from framework-specific model-loop implementations.[^evt-project-proposals-issue-69] Implemented as a Go core binary with SQLite/Postgres persistence and Redis queuing, Runkite coordinates run admission, dispatch, connector access, human approvals, spend accounting, and operational audit logging while orchestrating external Python and TypeScript runners over gRPC.[^evt-project-proposals-issue-69]

In March 2026, founder Sharan Harsoor submitted Runkite as a project proposal for admission into the AAIF Sandbox lifecycle stage.[^evt-project-proposals-issue-69]

# Architecture / Specification

## System Architecture
Runkite divides agent infrastructure into distinct operational layers:[^evt-project-proposals-issue-69]
- **Control Plane Binary:** Implemented in Go under Apache-2.0, providing HTTP endpoints for thread and run management, streaming events over Server-Sent Events (SSE) and WebSockets, and hosting an embedded operations UI.[^evt-project-proposals-issue-69]
- **Runner Protocol:** A gRPC contract connecting the control plane to language-specific runners (Python, TypeScript) that execute agent tasks using their native SDKs.[^evt-project-proposals-issue-69]
- **Connector and Decision Gateways:** Exposes configured agents as Model Context Protocol (MCP) tools and provides a pre-call policy decision API for independent application loops, dynamically resolving secret references at session time.[^evt-project-proposals-issue-69]

## Protocol and Framework Integrations
Runkite implements public streamable HTTP `/mcp` endpoints using the official MCP Go SDK, allowing external MCP clients to invoke managed agent runs as standard tools while mediating outbound connector access through explicit approval gates.[^evt-project-proposals-issue-69]

# Lifecycle History
- **2026-03-02:** Project proposal submitted to AAIF Project Proposals repository requesting Sandbox stage admission (`evt-project-proposals-issue-69`).[^evt-project-proposals-issue-69]

# References
- AAIF Project Proposal Issue #69: Runkite.[^evt-project-proposals-issue-69]

[^evt-project-proposals-issue-69]: https://github.com/aaif/project-proposals/issues/69
