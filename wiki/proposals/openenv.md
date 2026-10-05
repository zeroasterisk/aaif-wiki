---
type: proposal
title: OpenEnv
description: Unified reinforcement learning environment framework and execution contract
  connecting agent harnesses to isolated task containers via MCP.
resource: https://github.com/aaif/project-proposals/issues/50
tags:
- reinforcement-learning
- environments
- mcp
- project-proposal
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:17:44.098129+00:00'
sources:
- id: evt-project-proposals-issue-50
  resource: https://github.com/aaif/project-proposals/issues/50
  author: burtenshaw
  last_modified: '2026-09-29T21:03:42+00:00'
---

# Overview
OpenEnv is an open-source framework and execution contract standardizing isolated environments for agentic reinforcement learning (RL) and evaluation.[^evt-project-proposals-issue-50] It provides a unified set of Gymnasium-style lifecycle interfaces (`reset`, `step`, `state`) packaged in containerized sandboxes, using Model Context Protocol (MCP) as the communication interface between models and task environments.[^evt-project-proposals-issue-50]

# Architecture / Specification
OpenEnv standardizes agent training and evaluation workflows across heterogeneous trainers and runners:[^evt-project-proposals-issue-50]
- **Interface Contract**: Exposes standard reinforcement learning step and reset semantics while delegating tool calls and environment interactions over MCP.[^evt-project-proposals-issue-50]
- **Packaging and Distribution**: Bundles environments into portable container images distributed via repositories such as the Hugging Face Hub, decoupled from underlying sandbox runtimes (e.g., Modal, Daytona, Azure Container Apps).[^evt-project-proposals-issue-50]
- **Agentic Harness Integration**: Implements adapter patterns allowing external harnesses like Goose (`../reference-architectures/goose.md`) to execute within OpenEnv environments without altering their internal control loops.[^evt-project-proposals-issue-50]

# Lifecycle History
Originally introduced in October 2025 by Hugging Face and Meta-PyTorch, OpenEnv transitioned to multi-company Technical Committee stewardship in June 2026 before being formally submitted as an AAIF project proposal under Technical Committee sponsorship.[^evt-project-proposals-issue-50]

[^evt-project-proposals-issue-50]: https://github.com/aaif/project-proposals/issues/50
