---
type: resource
title: OpenSandbox
description: Open-source general-purpose sandbox platform providing lifecycle APIs,
  in-sandbox command daemons, and container/microVM runtimes for agent execution.
resource: https://github.com/aaif/project-proposals/issues/26
tags:
- sandbox
- runtime-isolation
- mcp
- containers
- security
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:22:44.663639+00:00'
sources:
- id: evt-project-proposals-issue-26
  resource: https://github.com/aaif/project-proposals/issues/26
  author: hittyt
  last_modified: '2026-10-08T07:30:54+00:00'
---

# Overview

OpenSandbox is an open-source sandbox platform engineered to isolate AI agent execution, code interpretation, browser automation, and reinforcement learning workloads across Docker and Kubernetes environments [^evt-project-proposals-issue-26]. Initiated by Alibaba Group and submitted as an AAIF project proposal, OpenSandbox establishes unified lifecycle and in-sandbox execution APIs paired with network egress enforcement and microVM runtime isolation [^evt-project-proposals-issue-26].

# Architecture / Specification

OpenSandbox provides an isolated execution substrate comprising [^evt-project-proposals-issue-26]:

- **Lifecycle Control Plane**: APIs to create, list, inspect, snapshot, pause, resume, and terminate sandbox instances.
- **In-Sandbox Daemon**: Standardized APIs for command execution, interactive shells, streaming I/O, file system modifications, and resource metrics.
- **Runtime Isolation**: Execution backend options spanning standard Docker containers, Kubernetes controllers, and hardened container/microVM runtimes such as gVisor, Kata Containers, and Firecracker.
- **Client Integrations**: Multi-language SDKs (Python, TypeScript, Go, Java, C#/.NET), a dedicated CLI, and an MCP server (`opensandbox-mcp`) allowing agents like Claude Code or Cursor to interact with isolated filesystems and run shell commands.

# Lifecycle History

Open-sourced in December 2025 and proposed to the Agentic AI Foundation in May 2026, the project serves as runtime isolation infrastructure across enterprise agent deployments and open-source evaluation pipelines [^evt-project-proposals-issue-26].

[^evt-project-proposals-issue-26]: https://github.com/aaif/project-proposals/issues/26
