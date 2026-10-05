---
type: working-group
title: Security and Privacy Working Group
description: AAIF technical working group establishing threat models, defense-in-depth
  patterns, and security best practices for agentic AI systems.
resource: https://github.com/aaif/wg-security-and-privacy/pull/25
tags:
- working-group
- security
- privacy
- threat-modeling
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:58:42.587132+00:00'
sources:
- id: evt-wg-security-and-privacy-pr-25
  resource: https://github.com/aaif/wg-security-and-privacy/pull/25
  author: awfrazer
  last_modified: '2026-10-01T05:08:24+00:00'
---

# Overview
The Security and Privacy Working Group establishes security baselines, architectural threat models, defense-in-depth design patterns, and operational guidelines across the Agentic AI Foundation ecosystem[^evt-wg-security-and-privacy-pr-25].

# Architecture / Specification
The working group actively maintains multiple foundational deliverables:
- **Agentic AI Security Best Practices**: A core guide and feature matrix establishing secret management, MCP security, and tool safety baselines[^evt-wg-security-and-privacy-pr-25].
- **Threat Modeling Gap Analysis**: Systematic threat modeling targeting multi-turn agent interactions, runtime isolation, and supply chain vulnerabilities[^evt-wg-security-and-privacy-pr-25].
- **Design Patterns Catalog**: Standardized catalog of runtime defense patterns, including initial specifications for approval checkpoints, kill switches, and attested isolated runtimes[^evt-wg-security-and-privacy-pr-25].
- **Taxonomy Alignment**: Collaboration with cross-cutting workstreams to curate standardized security and agent tool supply chain vocabularies[^evt-wg-security-and-privacy-pr-25].

# References
- [`policies-guidelines/agentic-ai-security-best-practices`](../policies-guidelines/agentic-ai-security-best-practices.md)
- [`patterns/approval-checkpoint`](../patterns/approval-checkpoint.md)
- [`patterns/kill-switch`](../patterns/kill-switch.md)
- [`patterns/attested-isolated-runtime`](../patterns/attested-isolated-runtime.md)
- [`taxonomy/agent-tool-supply-chain-terms`](../taxonomy/agent-tool-supply-chain-terms.md)

[^evt-wg-security-and-privacy-pr-25]: https://github.com/aaif/wg-security-and-privacy/pull/25
