---
type: skill
title: AAIF Taxonomy Contributions Skill
description: Standardized agent skill guiding contribution routing, pre-drafting validation,
  and schema compliance for the Taxonomy and Landscape workstream.
resource: https://github.com/aaif/public-agents/pull/3
tags:
- skills
- taxonomy
- landscape
- contributions
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:35:56.076242+00:00'
sources:
- id: evt-public-agents-pr-3
  resource: https://github.com/aaif/public-agents/pull/3
  author: asish-singh
  last_modified: '2026-08-22T12:50:41+00:00'
---

# Overview
The `aaif-taxonomy-contributions` skill provides structured instructions and validation logic for AI agents preparing contributions to the AAIF Taxonomy and Landscape workstream [^evt-public-agents-pr-3]. It automates contribution triage, pre-submission checks, and adherence to data schemas [^evt-public-agents-pr-3].

# Architecture / Specification
The skill addresses common contributor routing errors and enforces quality bars [^evt-public-agents-pr-3]:
- **Contribution Routing**: Directs agents to file issues or attend weekly syncs rather than opening premature pull requests for deferred taxonomy fields [^evt-public-agents-pr-3].
- **Pre-Draft Checks**: Verifies that proposed terms or landscape tools are not already registered or under active review in open pull requests [^evt-public-agents-pr-3].
- **Schema & Quality Verification**: Strips marketing language and superlatives from landscape candidate descriptions while conforming entries to the schema [^evt-public-agents-pr-3].
- **Dynamic Specification Retrieval**: Directs agents to fetch live repository documentation before drafting, ensuring resilience against schema changes [^evt-public-agents-pr-3].

# References
- [Taxonomy and Landscape Workstream](../workstreams/taxonomy-and-landscape.md)
- [Public Agent Skills](../ecosystem/public-agent-skills.md)

[^evt-public-agents-pr-3]: https://github.com/aaif/public-agents/pull/3
