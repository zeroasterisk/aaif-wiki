---
type: proposal
title: Agent Client Protocol (ACP) Proposal
description: Open protocol proposal standardizing communication between code editors/IDEs
  and AI coding agents to solve M×N integration.
resource: https://github.com/aaif/project-proposals/issues/1
tags:
- proposal
- protocol
- ide
- developer-tools
- standards
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T09:47:42.912814+00:00'
sources:
- id: evt-project-proposals-issue-1
  resource: https://github.com/aaif/project-proposals/issues/1
  author: benbrandt
  last_modified: '2026-05-21T16:03:28+00:00'
---

# Overview
The Agent Client Protocol (ACP) is an open protocol proposal submitted to the [Technical Committee](../governance/technical-committee.md) to standardize communication between code editors or IDEs and AI coding agents[^evt-project-proposals-issue-1]. Originating from Zed Industries and co-developed with JetBrains under the Apache 2.0 license, ACP aims to decouple agents from editor clients and resolve the M×N integration problem where each agent requires custom editor-specific integrations[^evt-project-proposals-issue-1].

# Architecture / Specification
ACP establishes a client-agent communication layer analogous to the Language Server Protocol (LSP) in software development tooling[^evt-project-proposals-issue-1].

### Protocol Scope and Transport
- **Editor-Agent UX Layer**: While the Model Context Protocol (MCP) standardizes agent-to-tool and agent-to-data connectivity, ACP standardizes the editor-to-agent session interaction layer[^evt-project-proposals-issue-1].
- **MCP Complementarity**: ACP re-uses MCP JSON representations where appropriate and enables clients to configure MCP servers directly for their agents[^evt-project-proposals-issue-1].
- **Transports**: Supports JSON-RPC over `stdio` for local agent execution, with HTTP/WebSocket transport implementations in progress for remote agent workflows[^evt-project-proposals-issue-1].

### Governance and Specification Process
- **Maintainers**: Lead maintainers Ben Brandt (Zed Industries) and Sergey Ignatov (JetBrains), alongside core maintainers Agus Zubiaga, Anna Zhdan, and Niko Matsakis[^evt-project-proposals-issue-1].
- **RFD Process**: Uses a public Request for Dialog (RFD) process for changes to the specification[^evt-project-proposals-issue-1].

# Lifecycle History
- **Proposal Submitted**: Submitted to `aaif/project-proposals` with Technical Committee sponsorship discussion involving David Soria Parra[^evt-project-proposals-issue-1].

[^evt-project-proposals-issue-1]: https://github.com/aaif/project-proposals/issues/1
