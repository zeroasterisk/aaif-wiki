---
type: initiative
title: Taxonomy and Landscape Workstream
description: Cross-working-group workstream curating a unified SKOS-Lite taxonomy,
  schema validation pipelines, and ecosystem landscape maps.
resource: https://github.com/aaif/ws-taxonomy-landscape/pull/68
tags:
- taxonomy
- landscape
- skos
- standards
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:17:44.098129+00:00'
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
The Taxonomy and Landscape Workstream is an AAIF cross-working-group initiative responsible for developing a canonical vocabulary, machine-readable SKOS-Lite schemas, and an interactive open-source landscape map for agentic systems.[^evt-ws-taxonomy-landscape-pr-83]

# Architecture / Specification
The workstream governs shared semantic definitions across working groups via standardized review processes and automated schema validation pipelines:[^evt-ws-taxonomy-landscape-pr-83]
- **Contribution and Review Workflow**: Working groups propose terms through delegates who shepherd definitions through KEEP, CULL, or DEBATE review outcomes, requiring cross-working-group consensus before moving to finalized status.[^evt-ws-taxonomy-landscape-pr-83]
- **Universal Vocabulary**: Defines core primitive terms across domains, including universal definitions for subagents (agents spawned by existing agents without implicit permission inheritance)[^evt-ws-taxonomy-landscape-pr-68], agent swarms (cooperative or independent subagent groups directed toward shared objectives)[^evt-ws-taxonomy-landscape-pr-80], and context (information available during agent decision steps)[^evt-ws-taxonomy-landscape-pr-82].
- **Machine-Readable Schemas**: Validates taxonomy consistency, term relationships, and scope notes using automated CI checks and schema linters.[^evt-ws-taxonomy-landscape-pr-68][^evt-ws-taxonomy-landscape-pr-80]

# Lifecycle History
The workstream operates in collaboration with the Technical Committee (`../governance/technical-committee.md`) and specialized working groups like `../working-groups/workflows-and-process-integration.md` to maintain interoperable terminology across foundation projects.[^evt-ws-taxonomy-landscape-pr-83]

[^evt-ws-taxonomy-landscape-pr-68]: https://github.com/aaif/ws-taxonomy-landscape/pull/68
[^evt-ws-taxonomy-landscape-pr-80]: https://github.com/aaif/ws-taxonomy-landscape/pull/80
[^evt-ws-taxonomy-landscape-pr-82]: https://github.com/aaif/ws-taxonomy-landscape/pull/82
[^evt-ws-taxonomy-landscape-pr-83]: https://github.com/aaif/ws-taxonomy-landscape/pull/83
