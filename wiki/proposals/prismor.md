---
type: proposal
title: Prismor
description: Self-hosted runtime control plane and MCP gateway evaluating policy-as-code
  before agent tool execution.
resource: https://github.com/aaif/project-proposals/issues/51
tags:
- proposals
- security
- mcp
- policy-engine
- gateways
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:25:43.661013+00:00'
sources:
- id: evt-project-proposals-issue-51
  resource: https://github.com/aaif/project-proposals/issues/51
  author: Ar9av
  last_modified: '2026-10-02T02:31:33+00:00'
---

# Overview
Prismor is an Apache-2.0, self-hosted control plane for AI agents that intercepts tool calls to enforce policy-as-code before execution.[^evt-project-proposals-issue-51] Evaluated actions result in allow, block, transform, or human approval verdicts, providing runtime isolation and governance across agent harnesses and MCP servers.[^evt-project-proposals-issue-51]

# Architecture / Specification
Prismor enforces policy across three primary operational surfaces:[^evt-project-proposals-issue-51]
- **Coding-Agent Hooks:** Interceptors tailored for coding agent harnesses and CLI runtimes.
- **In-Process SDK Adapters:** Native language libraries wrapping agent framework executions (e.g., LangChain, OpenAI Agents SDK).
- **MCP Gateway:** A reverse proxy fronting downstream Model Context Protocol servers that validates `tools/call` invocations against policy prior to forwarding, while scanning returned payloads before context re-injection.[^evt-project-proposals-issue-51]

Policy rules are authored in versioned YAML and support two operational enforcement modes:[^evt-project-proposals-issue-51]
- `observe`: Non-blocking passive telemetry logging to evaluate rule matches prior to enforcement.
- `enforce`: Active gate blocking unauthorized actions, modifying arguments, or requiring cryptographic or human approval gates (see [human-approval-gate](../patterns/human-approval-gate.md)).

# References
- Proposed under [project-lifecycle-policy](../governance/project-lifecycle-policy.md) intake.

[^evt-project-proposals-issue-51]: https://github.com/aaif/project-proposals/issues/51
