---
type: working-group
title: Taxonomy and Landscape Working Group
description: Cross-cutting AAIF workstream harmonizing shared agentic AI vocabulary,
  taxonomies, and the open-source landscape.
resource: https://github.com/aaif/ws-taxonomy-landscape/pull/79
tags:
- governance
- taxonomy
- landscape
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T03:17:27.587597+00:00'
sources:
- id: evt-ws-taxonomy-landscape-pr-79
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/79
  author: galesky-a
  last_modified: '2026-10-05T22:03:35+00:00'
- id: evt-ws-taxonomy-landscape-pr-70
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/70
  author: galesky-a
  last_modified: '2026-10-05T22:39:10+00:00'
- id: evt-ws-taxonomy-landscape-pr-71
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/71
  author: galesky-a
  last_modified: '2026-10-05T22:39:38+00:00'
- id: evt-ws-taxonomy-landscape-pr-72
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/72
  author: galesky-a
  last_modified: '2026-10-05T22:39:50+00:00'
---

# Overview
The Taxonomy and Landscape Working Group is a cross-cutting Agentic AI Foundation (AAIF) workstream standardizing shared terminology, classification schemas, and ecosystem landscapes across the agentic AI ecosystem [^evt-ws-taxonomy-landscape-pr-79]. The workstream harmonizes domain-specific concepts developed across Foundation working groups, including the [Agentic Commerce Working Group](../working-groups/agentic-commerce.md), ensuring consistency across all published taxonomy assets [^evt-ws-taxonomy-landscape-pr-70].

# Architecture / Specification
The working group maintains the central taxonomy data repository and automated CI validation pipelines. As part of structural refactoring, the taxonomy data format migrated from executable JavaScript files (`taxonomy-data.js`) to standard JSON (`taxonomy/taxonomy.json`) backed by Zod schema validation [^evt-ws-taxonomy-landscape-pr-79]. This transition removes custom parser maintenance in continuous integration, avoids executing contributor-provided script code, and yields deterministic field-level validation errors for pull requests [^evt-ws-taxonomy-landscape-pr-79].

Active taxonomy definitions integrated from domain working groups include:
- **Agent-completed transaction**: Captures transactions finalized autonomously by an AI agent [^evt-ws-taxonomy-landscape-pr-70].
- **Agent-in-the-loop transaction**: Renamed from agent-mediated transaction following community review, defining transaction flows wherein an agent participates alongside human actors [^evt-ws-taxonomy-landscape-pr-71].
- **Agent-initiated transaction**: Classifies transaction cycles originated or triggered by autonomous agent decisions [^evt-ws-taxonomy-landscape-pr-72].

# Lifecycle History
The working group moved taxonomy data storage to schema-validated JSON to resolve CI syntax-checking fragility and standardize the contributor intake process [^evt-ws-taxonomy-landscape-pr-79].

[^evt-ws-taxonomy-landscape-pr-70]: https://github.com/aaif/ws-taxonomy-landscape/pull/70
[^evt-ws-taxonomy-landscape-pr-71]: https://github.com/aaif/ws-taxonomy-landscape/pull/71
[^evt-ws-taxonomy-landscape-pr-72]: https://github.com/aaif/ws-taxonomy-landscape/pull/72
[^evt-ws-taxonomy-landscape-pr-79]: https://github.com/aaif/ws-taxonomy-landscape/pull/79
