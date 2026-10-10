---
type: resource
title: OpenEnv
description: Unified execution environment framework for agentic reinforcement learning
  exposing Gymnasium-style APIs and MCP tool interfaces.
resource: https://github.com/aaif/project-proposals/issues/50
tags:
- reinforcement-learning
- environments
- mcp
- containers
- benchmarking
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:21:10.371889+00:00'
sources:
- id: evt-project-proposals-issue-50
  resource: https://github.com/aaif/project-proposals/issues/50
  author: burtenshaw
  last_modified: '2026-10-07T00:40:00+00:00'
---

# Overview
OpenEnv is an open-source framework for creating, containerizing, and orchestrating isolated execution environments for agentic reinforcement learning (RL) [^evt-project-proposals-issue-50]. It provides Gymnasium-style lifecycle primitives (`reset`, `step`, `state`) while exposing environment tools to agents using the Model Context Protocol (MCP) [^evt-project-proposals-issue-50].

# Architecture / Specification
OpenEnv resolves tooling fragmentation across RL post-training stacks by standardizing the interface between models, environments, and harnesses [^evt-project-proposals-issue-50]:
- **Gymnasium-Style API**: Exposes standard episode lifecycle controls for trainers, handling environment resets, step transitions, observation state capture, and reward calculation [^evt-project-proposals-issue-50].
- **MCP Tool Interface**: Uses MCP as the model-to-environment interaction layer, ensuring agent tools used in training mirror those available in production deployment [^evt-project-proposals-issue-50].
- **Containerized Packaging**: Encapsulates environments within OCI containers distributed via Hugging Face Hub, enabling portable execution across local runtimes, cloud sandboxes (such as Modal, Daytona, and Azure Container Apps), and distributed RL training harnesses [^evt-project-proposals-issue-50].
- **Agent Harness Integration**: Provides adapter patterns (such as RFC 005) enabling coding agents like [Goose](../resources/goose.md) to undergo RL training within isolated environments while retaining their internal control loops [^evt-project-proposals-issue-50].

# Lifecycle History
OpenEnv was initially developed in October 2025 as a joint initiative between Hugging Face and Meta-PyTorch, transitioning to multi-vendor Technical Committee stewardship under Hugging Face in June 2026 before being proposed for AAIF hosting in 2026 [^evt-project-proposals-issue-50].

[^evt-project-proposals-issue-50]: https://github.com/aaif/project-proposals/issues/50
