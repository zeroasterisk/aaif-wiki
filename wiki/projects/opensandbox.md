---
type: project
title: OpenSandbox
description: Open-source general-purpose sandbox platform providing unified lifecycle
  and execution APIs for isolated AI agent workloads.
resource: https://github.com/aaif/project-proposals/issues/26
tags:
- sandbox
- runtime
- isolation
- mcp
- containers
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:48:18.218698+00:00'
sources:
- id: evt-project-proposals-issue-26
  resource: https://github.com/aaif/project-proposals/issues/26
  author: hittyt
  last_modified: '2026-09-28T08:06:42+00:00'
---

# Overview
OpenSandbox is an open-source, general-purpose sandbox platform designed for safely running AI-generated code, coding agents, browser automation, and reinforcement learning workloads[^evt-project-proposals-issue-26]. Proposed for AAIF hosting, OpenSandbox provides a vendor-neutral isolation substrate across container and microVM execution layers[^evt-project-proposals-issue-26].

# Architecture / Specification
The platform is organized as a unified control plane and execution daemon architecture supported by multi-language SDKs and tooling[^evt-project-proposals-issue-26]:
- **Sandbox Lifecycle APIs**: Standardizes remote management interfaces for provisioning, inspecting, renewing, pausing, snapshotting, and terminating sandbox environments[^evt-project-proposals-issue-26].
- **In-Sandbox Execution Daemon**: Exposes execution endpoints for shell commands, code execution, filesystem manipulation, and streaming telemetry[^evt-project-proposals-issue-26].
- **Network & Runtime Isolation**: Implements granular per-sandbox ingress and egress network filtering alongside support for Docker, Kubernetes, and hardened runtimes such as gVisor, Kata Containers, and Firecracker microVMs[^evt-project-proposals-issue-26].
- **MCP Integration**: Ships with `opensandbox-mcp`, allowing Model Context Protocol clients to create sandboxes and execute operations through standard tool calls[^evt-project-proposals-issue-26].

Related concepts: `../patterns/attested-isolated-runtime.md`, `../reference-architectures/goose.md`, `../projects/mcp-gateway-registry.md`.

# References
- [OpenSandbox AAIF Proposal](https://github.com/aaif/project-proposals/issues/26)

[^evt-project-proposals-issue-26]: https://github.com/aaif/project-proposals/issues/26
