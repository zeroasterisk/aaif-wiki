---
type: standard
title: Agent Client Protocol
description: Open standard for communication between code editors or IDEs and AI coding
  agents over JSON-RPC or HTTP/WebSocket.
resource: https://github.com/aaif/project-proposals/issues/1
tags:
- protocol
- ide
- editor
- acp
- standards
- interoperability
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T14:43:48.299298+00:00'
sources:
- id: evt-project-proposals-issue-1
  resource: https://github.com/aaif/project-proposals/issues/1
  author: benbrandt
  last_modified: '2026-05-21T16:03:28+00:00'
---

# Overview
The Agent Client Protocol (ACP) is an open communication standard designed to connect code editors and integrated development environments (IDEs) with AI coding agents[^evt-project-proposals-issue-1]. Co-developed by Zed Industries and JetBrains, ACP decouples coding agents from editors, addressing the M×N integration problem where each client previously required custom implementations for every agent[^evt-project-proposals-issue-1].

# Architecture / Specification
ACP standardizes the client-agent interaction layer and complements the Model Context Protocol (MCP)[^evt-project-proposals-issue-1]. While MCP focuses on model-to-tool and data connectivity, ACP handles session UX and editor interactions[^evt-project-proposals-issue-1].

Key technical characteristics include:
- **Transport Layers**: Local agent support via JSON-RPC over standard I/O (`stdio`), and remote agent support via HTTP and WebSocket protocols[^evt-project-proposals-issue-1].
- **MCP Interoperability**: Reuses MCP JSON representations and allows client applications to configure MCP servers for connected agents[^evt-project-proposals-issue-1].
- **Ecosystem Adoption**: Implemented natively or via plugins across editors such as Zed, JetBrains IDEs, Neovim, and Emacs, as well as agents like Goose, Augment Code, Cline, and OpenHands[^evt-project-proposals-issue-1].

# Lifecycle History
ACP was proposed as an AAIF project under the Apache 2.0 license and submitted to the [Technical Committee](../governance/technical-committee.md) for consideration[^evt-project-proposals-issue-1]. Specification changes are managed through a public Request for Dialog (RFD) process[^evt-project-proposals-issue-1].

[^evt-project-proposals-issue-1]: https://github.com/aaif/project-proposals/issues/1
