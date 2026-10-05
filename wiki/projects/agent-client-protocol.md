---
type: project
title: Agent Client Protocol (ACP)
description: Standardized communication protocol connecting code editors and IDEs
  to AI coding agents across local and remote transports.
resource: https://github.com/aaif/project-proposals/issues/1
tags:
- protocol
- ide
- coding-agents
- project-proposal
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:22:41.158584+00:00'
sources:
- id: evt-project-proposals-issue-1
  resource: https://github.com/aaif/project-proposals/issues/1
  author: benbrandt
  last_modified: '2026-05-21T16:03:28+00:00'
---

# Overview
The Agent Client Protocol (ACP) standardizes communication between code editors or IDEs and AI coding agents, providing a common interface layer analogous to how the Language Server Protocol (LSP) standardized language server tooling[^evt-project-proposals-issue-1]. ACP was created by Zed Industries and co-developed with JetBrains to solve the $M \times N$ integration challenge where every new agent-editor combination previously demanded custom integration[^evt-project-proposals-issue-1].

ACP has been proposed for AAIF project adoption under the sponsorship of Technical Committee members[^evt-project-proposals-issue-1].

# Architecture / Specification
ACP focuses on the developer-tooling and agent UX session layer while maintaining synergy with broader data connectivity standards[^evt-project-proposals-issue-1]:
- **Transport Layers**: Implements JSON-RPC over standard input/output (`stdio`) for local agents, with active implementations for HTTP and WebSocket transports for remote agent execution[^evt-project-proposals-issue-1].
- **MCP Complementarity**: ACP standardizes editor-to-agent interactions, complementing the Model Context Protocol (MCP) which handles model-to-tool and model-to-data connectivity. ACP reuses MCP JSON representations and allows client IDEs to configure MCP servers for attached agents[^evt-project-proposals-issue-1].
- **Ecosystem Implementations**: Integrates with multiple client environments including Zed, JetBrains IDEs, Neovim, and Emacs, as well as agents including Goose, Cline, Cursor, OpenHands, and GitHub Copilot[^evt-project-proposals-issue-1].

# Governance & Process
ACP is licensed under Apache 2.0 and operates an open Request for Dialog (RFD) process for protocol specification changes and architectural decision-making[^evt-project-proposals-issue-1].

[^evt-project-proposals-issue-1]: https://github.com/aaif/project-proposals/issues/1
