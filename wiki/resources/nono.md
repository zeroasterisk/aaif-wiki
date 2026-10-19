---
type: resource
title: nono
description: Open-source agent runtime security tool providing kernel-enforced sandboxing,
  credential isolation, and Sigstore-based instruction attestation.
resource: https://github.com/aaif/project-proposals/issues/61
tags:
- security
- runtime
- sandboxing
- credentials
- sigstore
- proposals
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T11:15:47.474225+00:00'
sources:
- id: evt-project-proposals-issue-61
  resource: https://github.com/aaif/project-proposals/issues/61
  author: lukehinds
  last_modified: '2026-10-17T08:06:23+00:00'
---

# Overview
nono is an open-source agent runtime security tool designed to secure AI agents, their tools, credentials, and configuration files via kernel-enforced sandboxing with composable policies and low latency [^evt-project-proposals-issue-61]. Created in February 2026 by Luke Hinds, nono isolates host and execution privileges for general-purpose and coding agents including [Goose](goose.md), Claude Code, Codex, and OpenCode, as well as frameworks such as ADK, Pydantic AI, and LangChain [^evt-project-proposals-issue-61].

# Architecture / Specification
nono enforces least privilege and policy-driven isolation around the agent process, its child executions, and connected external servers [^evt-project-proposals-issue-61]:

- **Kernel-Enforced Sandboxing:** Restricts file system visibility, host capabilities, and sub-process execution paths for running agents and tools [^evt-project-proposals-issue-61].
- **Model Context Protocol (MCP) Server Confinement:** Isolates MCP server processes to explicitly defined network endpoints, files, and credentials, providing OS-level guardrails beneath application-level authorization [^evt-project-proposals-issue-61].
- **Sigstore Instruction Attestation:** Integrates Sigstore cryptographic signatures to verify the provenance and integrity of agent instruction files such as `AGENTS.md`, rejecting unsigned or tampered prompts before runtime ingestion [^evt-project-proposals-issue-61].
- **Host vs. Network Demarcation:** Operates on the host side of agent execution, relaying outbound network traffic to mediation proxies like [Agent Gateway](agentgateway.md) or performing optional host-level network filtering [^evt-project-proposals-issue-61].
- **Policy as Code:** Implements composable, per-command security policies governing CI pipelines and production enterprise toolchains outside the agent's internal reasoning loop [^evt-project-proposals-issue-61].

# Lifecycle History
In March 2026, nono was proposed for intake into the AAIF Sandbox stage under Technical Committee sponsorship from Sambhav Kothari [^evt-project-proposals-issue-61].

# References
- GitHub Repository: https://github.com/nolabs-ai/nono
- Proposal Issue: https://github.com/aaif/project-proposals/issues/61

[^evt-project-proposals-issue-61]: https://github.com/aaif/project-proposals/issues/61
