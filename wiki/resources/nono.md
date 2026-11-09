---
type: resource
title: nono
description: Open-source agent runtime security tool providing kernel-enforced sandboxing,
  credential isolation, and Sigstore-based instruction verification.
resource: https://github.com/aaif/project-proposals/issues/61
tags:
- security
- sandbox
- credentials
- runtime
- provenance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:24:41.212193+00:00'
sources:
- id: evt-project-proposals-issue-61
  resource: https://github.com/aaif/project-proposals/issues/61
  author: lukehinds
  last_modified: '2026-10-17T08:06:23+00:00'
---

# Overview

nono is an open-source agent runtime security tool providing low-latency, kernel-enforced sandboxing, credential isolation, and instruction verification across coding agents, custom frameworks, and Model Context Protocol (MCP) servers.[^evt-project-proposals-issue-61] Created in February 2026 by Luke Hinds, nono was proposed for entry into the [Project Lifecycle](../policies/project-lifecycle-policy.md) as an Agentic AI Foundation Sandbox project sponsored by Sambhav Kothari of Bloomberg.[^evt-project-proposals-issue-61] The tool intercepts execution at the operating system layer to enforce policy boundaries that remain external to the agent's context and control.[^evt-project-proposals-issue-61]

# Architecture / Specification

nono structures agent execution security through layered host-level protections, composable policies, and cryptographic provenance checks:[^evt-project-proposals-issue-61]

- **Kernel-Enforced Sandboxing**: Isolates agent process execution, restricting access to designated filesystem paths, system calls, and network interfaces on Linux and macOS hosts.[^evt-project-proposals-issue-61]
- **Credential Management & Isolation**: Confines secrets and sensitive tokens away from agent memory, injecting credentials strictly into authorized per-command tool invocations.[^evt-project-proposals-issue-61]
- **Instruction and Skill Provenance**: Verifies the source-code origin and integrity of policy-covered instruction files—including [AGENTS.md](../standards/agents-md.md) specifications—using Sigstore digital signatures to reject unsigned or tampered prompts at the system access level.[^evt-project-proposals-issue-61]
- **MCP Server Confinement**: Enforces least-privilege host permissions on MCP server processes, binding their reachable endpoints, local files, and environment variables.[^evt-project-proposals-issue-61]
- **Host-Network Boundary Division**: Operates at the host boundary, designed to complement network-level reverse proxies and routers such as [agentgateway](../resources/agentgateway.md) by mediating local process capability while relaying egress traffic upstream.[^evt-project-proposals-issue-61]

# Lifecycle History

The project originated in February 2026 and utilizes an open governance structure managed by a Maintainer Council, handling architectural changes through nono Enhancement Proposals (NEPs).[^evt-project-proposals-issue-61] In October 2026, nono submitted an application for AAIF Sandbox status under the Apache 2.0 license, citing production adoption across enterprise toolchains including Datadog and Okta, and formal integration with runtimes such as [Goose](../resources/goose.md).[^evt-project-proposals-issue-61]

[^evt-project-proposals-issue-61]: https://github.com/aaif/project-proposals/issues/61
