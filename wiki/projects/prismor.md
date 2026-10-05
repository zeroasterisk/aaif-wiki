---
type: project
title: Prismor
description: Self-hosted runtime control plane for AI agents providing policy-as-code
  evaluation and tool call interception.
resource: https://github.com/aaif/project-proposals/issues/51
tags:
- project
- security
- policy
- mcp-gateway
- runtime
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T06:00:17.540946+00:00'
sources:
- id: evt-project-proposals-issue-51
  resource: https://github.com/aaif/project-proposals/issues/51
  author: Ar9av
  last_modified: '2026-10-02T02:31:33+00:00'
---

# Overview
Prismor is an open-source (Apache-2.0), self-hosted control plane for AI agents designed to evaluate and govern tool dispatches using policy-as-code[^evt-project-proposals-issue-51]. Operating as an interception layer between agent reasoning harnesses and executable capabilities, Prismor provides pre-execution inspection, verdict enforcement (allow, block, transform, or require human approval), and result redaction across diverse agent frameworks and protocols.

# Architecture / Specification
Prismor enforces policies across three primary integration surfaces[^evt-project-proposals-issue-51]:
- **Coding Agent Hooks**: Pre-execution hooks directly embedded within developer agent harnesses and coding tools.
- **In-Process SDK Adapters**: Client-side library wrappers supporting agent runtimes such as LangChain and OpenAI Agents SDK.
- **MCP Gateway**: A proxy fronting downstream Model Context Protocol servers, evaluating `tools/call` invocations against policy rules before dispatch and scanning execution responses before returning context to the model.

The engine evaluates versioned YAML policies scoped across organization, project, repository, or session boundaries[^evt-project-proposals-issue-51]. It supports both an *observe mode* for impact telemetry and an *enforce mode* for strict policy gating, emitting signed audit trails and attestation bundles to verify runtime controls[^evt-project-proposals-issue-51].

# Lifecycle History
Originally introduced on PyPI as `immunity-agent` in early 2026, the project rebranded to `prismor` in version 1.13.0[^evt-project-proposals-issue-51]. An application for hosting within the Agentic AI Foundation was formally submitted in September 2026[^evt-project-proposals-issue-51].

[^evt-project-proposals-issue-51]: https://github.com/aaif/project-proposals/issues/51
