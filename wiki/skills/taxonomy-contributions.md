---
type: skill
title: Taxonomy and Landscape Contributions Skill
description: Operational agent skill assisting contributors in routing, preparing,
  and validating schema-conformant terms and landscape entries.
resource: https://github.com/aaif/public-agents/pull/3
tags:
- skills
- taxonomy
- landscape
- contributions
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:33:25.457551+00:00'
sources:
- id: evt-public-agents-pr-3
  resource: https://github.com/aaif/public-agents/pull/3
  author: asish-singh
  last_modified: '2026-10-11T18:18:20+00:00'
---

# Overview
The `aaif-taxonomy-contributions` skill guides AI agents and contributors in routing, drafting, and validating terminology proposals and landscape additions for the Common Taxonomy and Landscape workstream (`aaif/ws-taxonomy-landscape`) [^evt-public-agents-pr-3]. It automates pre-drafting validation and normalizes proposals into accepted community schemas [^evt-public-agents-pr-3].

# Architecture / Specification
The skill consolidates disparate contribution rules across schema definitions, contributing guides, and codebase comments into an executable agent decision model:

- **Contribution Routing**: Dispatches proposed additions to the appropriate contribution channel—such as submitting an issue for deferred terminology versus filing a pull request for complete landscape entries—preventing common triage misdirections [^evt-public-agents-pr-3].
- **Pre-Drafting Collision Checks**: Inspects the target repository for active pull requests or existing taxonomy entries prior to drafting, preventing duplicate term proposals [^evt-public-agents-pr-3].
- **Pre-Competitive Style Enforcement**: Scans and sanitizes submitted descriptions by stripping ungrounded marketing superlatives (e.g., 'the best open-source platform') to maintain the pre-competitive, objective tone required by landscape schemas [^evt-public-agents-pr-3].
- **Template and Schema Conformance**: Formats proposals into standardized `Define` issue templates and ensures required metadata fields—including name, homepage URL, pre-competitive description, and member status—conform to schema constraints [^evt-public-agents-pr-3].
- **Adaptive Context Retrieval**: Instructs agents to dynamically fetch upstream schema documentation before drafting, ensuring graceful adaptation to evolving workstream processes [^evt-public-agents-pr-3].

# Lifecycle History
Empirical evaluation demonstrated that an agent equipped with `aaif-taxonomy-contributions` executed schema-conformant landscape entries in 6 targeted tool calls compared to 15 exploratory calls required by an unassisted baseline [^evt-public-agents-pr-3].

# References
- [Taxonomy and Landscape Workstream](../working-groups/taxonomy-and-landscape.md)
- [Agentic AI Landscape](../resources/agentic-ai-landscape.md)

[^evt-public-agents-pr-3]: https://github.com/aaif/public-agents/pull/3
