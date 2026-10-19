---
type: standard
title: ACP (disambiguation)
description: Three unrelated agent protocols share the acronym ACP -- Agent Client Protocol
  (editor-to-agent), Agentic Commerce Protocol (checkout), and Agent Communication Protocol
  (IBM BeeAI, merged into A2A).
resource: https://github.com/i-am-bee/acp/blob/e5265ca9fa06c55cd011b1e81ee927f6d80af8f6/README.md
tags:
- external
- standards
- acp
- disambiguation
status: draft
generated:
  by: agent:aaif-wiki-curator/claude-opus
  at: '2026-10-19T02:40:00+00:00'
sources:
- id: evt-project-proposals-issue-1
  resource: https://github.com/aaif/project-proposals/issues/1
  author: benbrandt
  last_modified: '2026-05-21T16:03:28+00:00'
- id: evt-ext-agentic-commerce-protocol-agentic-commerce-protocol-43140e-file-b33563055168-9191a2de
  resource: https://github.com/agentic-commerce-protocol/agentic-commerce-protocol/blob/7fdd78df677a94dce04c770644b0fbbb1401272b/README.md
  author: Sri Akula
  last_modified: '2026-06-15T16:39:13-07:00'
- id: evt-ext-i-am-bee-acp-13a961-file-b33563055168-a9e78328
  resource: https://github.com/i-am-bee/acp/blob/e5265ca9fa06c55cd011b1e81ee927f6d80af8f6/README.md
  author: i-am-bee
  last_modified: '2025-08-25T14:42:35-04:00'
---

# Overview
"ACP" names three unrelated agent protocols. Check which one a document means before
comparing them.

| Name | Layer | Steward / origin | Status |
|---|---|---|---|
| [Agent Client Protocol](./agent-client-protocol.md) | Code editor / IDE ↔ coding agent | Created by Zed Industries, co-developed with JetBrains; proposed as an AAIF project[^evt-project-proposals-issue-1] | Active |
| [Agentic Commerce Protocol](./agentic-commerce-protocol.md) | Buyer, AI agent ↔ merchant checkout | OpenAI and Stripe (Founding Maintainers)[^evt-ext-agentic-commerce-protocol-agentic-commerce-protocol-43140e-file-b33563055168-9191a2de] | Beta |
| Agent Communication Protocol | Agent ↔ agent / application / human messaging | IBM Research (BeeAI)[^evt-ext-i-am-bee-acp-13a961-file-b33563055168-a9e78328] | Archived; merged into [A2A](./a2a.md) |

# Architecture / Specification
- **Agent Client Protocol** connects editors to coding agents over JSON-RPC (stdio) or
  HTTP/WebSocket, and reuses MCP JSON representations[^evt-project-proposals-issue-1].
- **Agentic Commerce Protocol** is "an interaction model and open standard for connecting
  buyers, their AI agents, and businesses to complete purchases"[^evt-ext-agentic-commerce-protocol-agentic-commerce-protocol-43140e-file-b33563055168-9191a2de].
- **Agent Communication Protocol** was "an open protocol for communication between AI
  agents, applications, and humans" using multimodal messages[^evt-ext-i-am-bee-acp-13a961-file-b33563055168-a9e78328].
  Its functional overlap is with A2A, not with the other two ACPs.

# Lifecycle History
- 2025-08-25: the Agent Communication Protocol repository announced "ACP is now part of
  A2A under the Linux Foundation" and was archived[^evt-ext-i-am-bee-acp-13a961-file-b33563055168-a9e78328].
- 2026-04-01: Agent Client Protocol proposed as an AAIF project (issue still open)[^evt-project-proposals-issue-1].
