---
type: resource
title: hippo-memory
description: Local-first, zero-LLM-call persistent memory layer for AI coding agents
  and Model Context Protocol clients with git-mirrored storage.
resource: https://github.com/aaif/project-proposals/issues/73
tags:
- memory
- storage
- mcp
- context
- sqlite
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:38:13.279200+00:00'
sources:
- id: evt-project-proposals-issue-73
  resource: https://github.com/aaif/project-proposals/issues/73
  author: kitfunso
  last_modified: '2026-11-22T22:53:03+00:00'
---

# Overview
hippo-memory is an open-source, local-first memory layer designed for AI coding agents and Model Context Protocol (MCP) clients [^evt-project-proposals-issue-73]. It persists operational context, developer feedback, and learned heuristics into a local SQLite store alongside git-committable Markdown mirrors under `.hippo/`, enabling coding agents such as [Goose](../resources/goose.md), Claude Code, Codex, and Cursor to share working memory across tools without vendor lock-in [^evt-project-proposals-issue-73].

In contrast to cloud memory services that trigger model queries on memory persistence and retrieval, hippo-memory executes zero LLM calls on its standard save and recall path [^evt-project-proposals-issue-73]. Built on Node.js built-in `node:sqlite` without runtime dependencies, it packages a local Hugging Face Transformers embedding pipeline configured during initialization [^evt-project-proposals-issue-73].

# Architecture / Specification
hippo-memory provides modular state retention, synchronization, and governance primitives [^evt-project-proposals-issue-73]:

- **Biologically Inspired Memory Lifecycle**: Operates a typed provenance model (`MEMORY_ENVELOPE.md`) defining envelope metadata such as category kind, scope, owner, artifact references, session identifiers, and confidence ratings [^evt-project-proposals-issue-73]. Lifecycle routines include outcome feedback (`hippo outcome --bad`) to degrade memories associated with faulty responses, fact supersession (`hippo supersede`), decay for idle items with pinned invariants, and sleep consolidation (`hippo sleep`) [^evt-project-proposals-issue-73].
- **Git-Native Transparency**: Synchronizes local SQLite tables with plain-text Markdown mirrors in `.hippo/`, allowing teams to review, diff, and audit agent-learned memories in code reviews and pull requests [^evt-project-proposals-issue-73].
- **Self-Hosted Team Service**: Supports multi-user deployments via `hippo serve`, exposing MCP and HTTP interfaces protected by role-based authorization, per-user API tokens, and append-only audit trails [^evt-project-proposals-issue-73].
- **Protocol Integration**: Ships 13 memory control tools exposed over the Model Context Protocol, facilitating integration into agent runtimes, shell environments, and intermediary control proxies such as [agentgateway](../resources/agentgateway.md) [^evt-project-proposals-issue-73].

# Lifecycle History
hippo-memory was created in March 2026 by Kit Fun (Keith) So of KITFUNSO LTD [^evt-project-proposals-issue-73]. In November 2026, the project was proposed for Sandbox-stage hosting in the Agentic AI Foundation under issue 73 [^evt-project-proposals-issue-73]. The proposal aligns with objectives across [Working Group Agent Context & Memory](../working-groups/agent-context-and-memory.md), [Working Group Accuracy & Reliability](../working-groups/accuracy-and-reliability.md), and [Working Group Security & Privacy](../working-groups/security-and-privacy.md) [^evt-project-proposals-issue-73].

# References
- [GitHub Repository](https://github.com/kitfunso/hippo-memory) [^evt-project-proposals-issue-73]
- [AAIF Project Proposal #73](https://github.com/aaif/project-proposals/issues/73) [^evt-project-proposals-issue-73]

[^evt-project-proposals-issue-73]: https://github.com/aaif/project-proposals/issues/73
