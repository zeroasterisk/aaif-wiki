---
type: standard
title: ToolSurface
description: Normative schema, static safety predicates, and rule-based conformance
  suite standardizing safe, unpoisoned Model Context Protocol (MCP) tool descriptions.
resource: https://github.com/aaif/project-proposals/issues/64
tags:
- mcp
- tools
- security
- prompt-injection
- standard
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:27:56.077041+00:00'
sources:
- id: evt-project-proposals-issue-64
  resource: https://github.com/aaif/project-proposals/issues/64
  author: raihan-js
  last_modified: '2026-10-27T12:26:53+00:00'
---

# Overview

ToolSurface is an open specification that governs the safety of the `description` field in Model Context Protocol (MCP) tool registrations.[^evt-project-proposals-issue-64] While the Model Context Protocol specifies tool invocation transport and JSON Schema validation for tool inputs, it does not constrain the free-text description block where prompt-injection, secondary coercion, and tool-poisoning payloads typically reside.[^evt-project-proposals-issue-64]

ToolSurface defines a canonical schema and static validation rules that prevent tool authors or compromised MCP endpoints from embedding imperative system instructions into tool descriptions without altering the underlying MCP wire protocol.[^evt-project-proposals-issue-64]

# Architecture / Specification

ToolSurface introduces three primary components to enforce description safety:[^evt-project-proposals-issue-64]

- **Normative Description Schema:** Replaces unconstrained prose with a structured JSON object containing five defined fields: a required `purpose`, alongside optional `params`, `returns`, `side_effects`, and `examples` fields. Any free-text directives outside these keys violate conformance.[^evt-project-proposals-issue-64]
- **Static Safety Predicates:** A deterministic, dependency-free validation rule set that rejects descriptions containing cross-tool imperatives (e.g., ordering an agent to call another tool), embedded credentials, system paths, or security-justification coercion phrases.[^evt-project-proposals-issue-64]
- **Rule-Scored Conformance Suite:** A third-party test framework that verifies implementations against frozen corpora (derived from ToolSieve and the 367-instance MCPTox benchmark subset). Conformance is established without an LLM judge by computing attack success rates (ASR) and utility-completion scores under Wilson 95% confidence intervals.[^evt-project-proposals-issue-64]

ToolSurface provides a Python reference implementation containing `canonicalise(description)` and `validate(description)` routines for integration into tool registries, gateways, and agent runtimes.[^evt-project-proposals-issue-64]

# Lifecycle History

- **2026-10:** Developed as an open specification originating from the ToolSieve research project and MCPTox benchmark.[^evt-project-proposals-issue-64]
- **2026-10:** Submitted as an AAIF Sandbox project proposal licensed under the Community Specification License 1.0.[^evt-project-proposals-issue-64]

[^evt-project-proposals-issue-64]: https://github.com/aaif/project-proposals/issues/64
