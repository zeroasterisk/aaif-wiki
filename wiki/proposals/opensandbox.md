---
type: proposal
title: OpenSandbox
description: General-purpose sandbox platform providing unified execution APIs, multi-language
  SDKs, an MCP server, and container/microVM isolation for agentic workloads.
resource: https://github.com/aaif/project-proposals/issues/26
tags:
- proposal
- sandboxing
- runtime
- mcp
- security
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:16:10.997596+00:00'
sources:
- id: evt-project-proposals-issue-26
  resource: https://github.com/aaif/project-proposals/issues/26
  author: hittyt
  last_modified: '2026-09-28T08:06:42+00:00'
---

# Overview
OpenSandbox is an open-source, general-purpose sandbox platform submitted as an AAIF project proposal to provide isolated execution substrates for AI-generated code, coding agents, GUI/browser agents, and evaluation workflows [^evt-project-proposals-issue-26]. Originally developed by Alibaba Group, it provides standardized lifecycle and command execution APIs alongside multi-language SDKs, container/microVM isolation backends, and an MCP server interface [^evt-project-proposals-issue-26].

# Architecture / Specification
OpenSandbox provides execution and control plane primitives designed to isolate agent actions without forcing every agent framework to maintain bespoke sandboxing infrastructure [^evt-project-proposals-issue-26]:
- **Unified Lifecycle & Execution APIs:** Endpoints for creating, listing, inspecting, renewing, pausing, snapshotting, and deleting sandboxes, as well as executing shell commands, code blocks, filesystem operations, and streaming metrics [^evt-project-proposals-issue-26].
- **Isolation Options:** Runtime backends supporting standard Docker and Kubernetes controllers, with hardened microVM and secure container isolation via gVisor, Kata Containers, and Firecracker [^evt-project-proposals-issue-26].
- **MCP Integration:** An `opensandbox-mcp` server exposing sandbox management, command execution, and file I/O tools to Model Context Protocol clients [^evt-project-proposals-issue-26].
- **Multi-Language SDKs:** Client bindings spanning Python, Java/Kotlin, JavaScript/TypeScript, C#/.NET, and Go [^evt-project-proposals-issue-26].
- **Network Governance:** Per-sandbox ingress and egress network filtering policies to restrict outbound exfiltration or unauthorized calls [^evt-project-proposals-issue-26].

# Lifecycle History
The proposal was submitted to AAIF in May 2026 under the Apache 2.0 license, referencing integrations with tools such as [Goose](../reference-architectures/goose.md) and coding agents [^evt-project-proposals-issue-26].

[^evt-project-proposals-issue-26]: https://github.com/aaif/project-proposals/issues/26
