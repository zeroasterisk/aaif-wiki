---
type: taxonomy
title: Tool Poisoning
description: Supply-chain attack where an agent tool or tool definition is deliberately
  crafted or modified to execute malicious actions or alter agent behavior.
resource: https://github.com/aaif/ws-taxonomy-landscape/pull/88
tags:
- taxonomy
- security
- supply-chain
- tools
- threat-modeling
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:20:48.792446+00:00'
sources:
- id: evt-ws-taxonomy-landscape-pr-88
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/88
  author: GeeksikhSecurity
  last_modified: '2026-10-09T12:40:04+00:00'
---

# Overview
Tool poisoning is an agent tool supply-chain attack pattern where a tool or tool definition (such as a Model Context Protocol server manifest) is inherently malicious from its point of creation or publication.[^evt-ws-taxonomy-landscape-pr-88] In agentic deployments, poisoned tool definitions manipulate how foundation models select, parameterize, or execute functions, potentially triggering unauthorized tool calls, indirect prompt injection, or sensitive data exfiltration.[^evt-ws-taxonomy-landscape-pr-88]

Within the AAIF taxonomy, tool poisoning is distinguished from a [rug pull](rug-pull.md) by timing: tool poisoning characterizes tools that are malicious from the outset, whereas a rug pull involves a previously trusted and verified tool turning malicious after initial approval.[^evt-ws-taxonomy-landscape-pr-88]

# Architecture / Specification
The concept aligns with MITRE ATLAS technique AML.T0110 (AI Agent Tool Poisoning) and OWASP MCP Top 10 vulnerabilities.[^evt-ws-taxonomy-landscape-pr-88] Adversaries exploit the natural language descriptions consumed by model orchestrators to misrepresent tool capabilities or embed covert instructions. Mitigation strategies require mandatory [tool definition verification](tool-definition-verification.md), strict policy-as-code proxies, and architectural isolation such as [proposal-execution splits](../patterns/proposal-execution-split.md).[^evt-ws-taxonomy-landscape-pr-88]

# Lifecycle History
Introduced in PR #88 of the [Taxonomy and Landscape Workstream](../working-groups/taxonomy-and-landscape.md) as part of a cross-working-group vocabulary proposal aligned with the [Security and Privacy Working Group](../working-groups/security-and-privacy.md) and [Governance, Risk and Regulatory Alignment Working Group](../working-groups/governance-risk-and-regulatory.md).[^evt-ws-taxonomy-landscape-pr-88]

[^evt-ws-taxonomy-landscape-pr-88]: https://github.com/aaif/ws-taxonomy-landscape/pull/88
