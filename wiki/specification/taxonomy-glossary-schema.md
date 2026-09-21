---
type: specification
title: AAIF Taxonomy Glossary Schema (SKOS-Lite)
description: Formal data schema specification for entries in the AAIF shared vocabulary,
  defining required fields, constraints, and the status of deferred hierarchical fields.
resource: https://github.com/aaif/ws-taxonomy-landscape/blob/09a1b58155e0789614835fbd1e75005c6c337ee3/docs/data-schemas.md
tags:
- taxonomy
- data-model
- skos
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-flash-latest
  at: '2026-09-21T10:10:35.967237+00:00'
sources:
- id: evt-ws-taxonomy-landscape-file-8cefa3760c72-41fe6e97
  resource: https://github.com/aaif/ws-taxonomy-landscape/blob/09a1b58155e0789614835fbd1e75005c6c337ee3/docs/data-schemas.md
  author: Julianna Langston
  last_modified: '2026-09-16T13:39:37-04:00'
---

# Overview
The Taxonomy Glossary Schema defines the structure for concepts stored in `taxonomy/taxonomy-data.js`, ensuring compatibility with automated parsing pipelines and UI rendering [^evt-ws-taxonomy-landscape-file-8cefa3760c72-41fe6e97]. The schema is SKOS-Lite compliant.

# Architecture / Specification
Each entry is a JavaScript object with the following key fields:

| Field | Type | Status | Description |
|---|---|---|---|
| `term` | String | Required | The preferred display term, using sentence case. Must be unique. |
| `aliases` | Array<String> | Required | Synonyms or alternate spellings. |
| `scopeNote` | String | Optional | Historical context or explanation of conceptual boundaries. |
| `relatedTerms` | Array<String> | Optional | Associative linkages (`skos:related`). |
| `contrastsWith` | Array<String> | Optional | Explicitly links paired contrasting terms. |
| `workgroups` | Array<String> | Required | The working groups that share interest or joint ownership of the term. |

**Deferred Fields (Initial Check-in):** During the initial phase (as of 2026-07-27), three critical fields are deliberately deferred to allow for flat term admission ahead of complex hierarchy mapping:

1.  `category`: Deferred. Intended to be one of five approved organizational buckets (e.g., `Agentic Threats`, `Identity & Authorization`).
2.  `broaderTerm`: Deferred. Represents the direct parent concept in the hierarchy (`skos:broader`). Root nodes use `null`.
3.  `definition`: Deferred. Until a definition is agreed upon by the workstream, entries must use the placeholder: `Definition pending — term accepted; definition under working group discussion.` [^evt-ws-taxonomy-landscape-file-8cefa3760c72-41fe6e97].

# References
See also: [../methodology/taxonomy-curation-protocol.md].

[^evt-ws-taxonomy-landscape-file-8cefa3760c72-41fe6e97]: https://github.com/aaif/ws-taxonomy-landscape/blob/09a1b58155e0789614835fbd1e75005c6c337ee3/docs/data-schemas.md
