---
type: workstream
title: Taxonomy and Landscape Workstream
description: Cross-cutting AAIF workstream curating shared SKOS-Lite agentic AI vocabularies,
  contribution workflows, and ecosystem market maps.
resource: https://github.com/aaif/ws-taxonomy-landscape/pull/68
tags:
- aaif
- workstream
- taxonomy
- landscape
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:49:55.277955+00:00'
sources:
- id: evt-ws-taxonomy-landscape-pr-68
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/68
  author: julianna-ciq
  last_modified: '2026-09-29T07:10:47+00:00'
- id: evt-ws-taxonomy-landscape-pr-80
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/80
  author: julianna-ciq
  last_modified: '2026-09-29T11:33:06+00:00'
- id: evt-ws-taxonomy-landscape-pr-82
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/82
  author: julianna-ciq
  last_modified: '2026-09-29T11:33:39+00:00'
- id: evt-ws-taxonomy-landscape-pr-83
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/83
  author: julianna-ciq
  last_modified: '2026-09-29T10:42:45+00:00'
---

# Overview
The Taxonomy and Landscape Workstream is a cross-cutting AAIF initiative responsible for maintaining the foundational SKOS-Lite vocabulary of agentic AI terminology, coordinating term contributions across Working Groups, and maintaining the interactive ecosystem market map ([`../ecosystem/agentic-ai-landscape.md`](../ecosystem/agentic-ai-landscape.md))[^evt-ws-taxonomy-landscape-pr-83].

# Architecture / Specification
The workstream operates a structured terminology curation process to maintain conceptual integrity across AAIF domains[^evt-ws-taxonomy-landscape-pr-83]:
- **Contribution Pipeline**: Working groups propose domain-specific terms via assigned delegates who submit proposals into the taxonomy repository for schema validation and cross-WG review[^evt-ws-taxonomy-landscape-pr-83].
- **Review Outcomes**: Proposed terms undergo triage resulting in `KEEP` (accepted into taxonomy), `CULL` (rejected or consolidated), or `DEBATE` (referred for technical deliberation)[^evt-ws-taxonomy-landscape-pr-83].
- **Universal Vocabularies**: Curates cross-domain baseline terms including Subagents, Agent Swarms, and Context ([`../taxonomy/universal-agent-terms.md`](../taxonomy/universal-agent-terms.md)) alongside domain-specific sets such as core workflow terms ([`../taxonomy/core-workflow-terms.md`](../taxonomy/core-workflow-terms.md)) and commerce terms ([`../taxonomy/agentic-commerce-terms.md`](../taxonomy/agentic-commerce-terms.md))[^evt-ws-taxonomy-landscape-pr-68][^evt-ws-taxonomy-landscape-pr-80][^evt-ws-taxonomy-landscape-pr-82].

# Lifecycle History
- **PR #68**: Merged universal term *Subagent* into taxonomy data definitions[^evt-ws-taxonomy-landscape-pr-68].
- **PR #83**: Clarified end-to-end contribution workflow, review outcome taxonomy (`KEEP`/`CULL`/`DEBATE`), and delegate governance rules[^evt-ws-taxonomy-landscape-pr-83].

[^evt-ws-taxonomy-landscape-pr-68]: https://github.com/aaif/ws-taxonomy-landscape/pull/68
[^evt-ws-taxonomy-landscape-pr-80]: https://github.com/aaif/ws-taxonomy-landscape/pull/80
[^evt-ws-taxonomy-landscape-pr-82]: https://github.com/aaif/ws-taxonomy-landscape/pull/82
[^evt-ws-taxonomy-landscape-pr-83]: https://github.com/aaif/ws-taxonomy-landscape/pull/83
