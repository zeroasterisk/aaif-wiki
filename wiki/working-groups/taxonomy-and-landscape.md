---
type: working-group
title: Taxonomy and Landscape Working Group
description: Cross-cutting AAIF workstream establishing unified agentic terminology,
  schema-validated taxonomies, and ecosystem maps across working groups.
resource: https://github.com/aaif/ws-taxonomy-landscape/pull/89
tags:
- working-group
- taxonomy
- landscape
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T11:00:39.514262+00:00'
sources:
- id: evt-ws-taxonomy-landscape-pr-89
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/89
  author: julianna-ciq
  last_modified: '2026-10-07T12:36:51+00:00'
---

# Overview
The Taxonomy and Landscape Working Group maintains the core conceptual vocabulary, categorization models, and landscape surveys for the Agentic AI Foundation. It establishes shared definitions across all technical workstreams to prevent terminology fragmentation [^evt-ws-taxonomy-landscape-pr-89].

# Architecture / Specification

## Schema and Term Generation Automation
Taxonomy definitions are maintained in structured source files (`taxonomy-data.js`) and validated through continuous integration harnesses [^evt-ws-taxonomy-landscape-pr-89]:
- **Markdown Generation**: The `tools/generate-taxonomy-markdown.mjs` utility renders human-readable reference documentation directly from canonical structured data [^evt-ws-taxonomy-landscape-pr-89].
- **Drift Prevention and CI Verification**: Pre-commit hooks installed via npm prepare hooks, alongside automated CI test suites (`node tools/generate-taxonomy-markdown.mjs --verify`), ensure generated documentation remains in lockstep with underlying taxonomy definitions [^evt-ws-taxonomy-landscape-pr-89].
- **Syntax and Schema Validation**: Custom validation scripts (`tools/validate-taxonomy.mjs`) verify structural schema adherence and syntactic invariants prior to merging [^evt-ws-taxonomy-landscape-pr-89].

# References
- Taxonomy contribution skill: [../skills/taxonomy-contributions.md](../skills/taxonomy-contributions.md)
- Ecosystem landscape: [../resources/agentic-ai-landscape.md](../resources/agentic-ai-landscape.md)

[^evt-ws-taxonomy-landscape-pr-89]: https://github.com/aaif/ws-taxonomy-landscape/pull/89
