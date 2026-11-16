---
type: resource
title: nono
description: Open-source agent runtime security tool providing kernel-enforced sandboxing,
  credential isolation, and Sigstore-based instruction verification.
resource: https://github.com/aaif/project-proposals/issues/61
tags:
- security
- sandbox
- runtime
- proposal
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:35:58.956192+00:00'
sources:
- id: evt-project-proposals-issue-61
  resource: https://github.com/aaif/project-proposals/issues/61
  author: lukehinds
  last_modified: '2026-10-17T08:06:23+00:00'
---

# Overview

`nono` is an open-source agent runtime security tool designed to isolate agent processes, tools, credentials, and configuration files via kernel-enforced sandboxing with minimal overhead and zero setup.[^evt-project-proposals-issue-61] It applies composable security policies residing outside the agent's direct control to secure coding agents, general-purpose autonomous runtimes, custom agent frameworks, and Model Context Protocol (MCP) servers.[^evt-project-proposals-issue-61]

Created in February 2026 by Luke Hinds, nono was submitted as a Sandbox project proposal to the Agentic AI Foundation with Technical Committee sponsorship from Bloomberg.[^evt-project-proposals-issue-61]

# Architecture / Specification

Nono operates as host-level security infrastructure complementary to network-layer proxies such as `agentgateway`:[^evt-project-proposals-issue-61]
- **Kernel-Enforced Sandboxing:** Restricts agent file system access, network socket creation, and child process execution according to per-command profiles.
- **Instruction and Skill Attestation:** Integrates Sigstore cryptographic signatures to verify the provenance and integrity of agent instruction files (such as `AGENTS.md`), blocking tampered or unverified prompt directives at the operating system access layer.[^evt-project-proposals-issue-61]
- **Credential Protection:** Keeps sensitive API keys, authorization tokens, and secrets isolated from untrusted tool calls and rogue agent workflows.[^evt-project-proposals-issue-61]
- **Ecosystem Integration:** Enforces least-privilege constraints across runtimes such as [Goose](../resources/goose.md), Claude Code, OpenCode, and frameworks including ADK, Pydantic AI, and LangChain.[^evt-project-proposals-issue-61]

# Lifecycle History

- **February 2026:** Initial creation by Luke Hinds.[^evt-project-proposals-issue-61]
- **October 2026:** Submitted under Issue #61 to the AAIF Technical Committee for entry as an AAIF Sandbox project, sponsored by Sambhav Kothari.[^evt-project-proposals-issue-61]

[^evt-project-proposals-issue-61]: https://github.com/aaif/project-proposals/issues/61
