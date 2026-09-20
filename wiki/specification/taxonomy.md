---
type: specification
title: Taxonomy Data Schema Specification
description: SKOS-Lite-compliant data schema and staging rules for defining, categorizing,
  and linking agentic AI terms across the shared taxonomy.
resource: https://github.com/aaif/ws-taxonomy-landscape/blob/09a1b58155e0789614835fbd1e75005c6c337ee3/docs/data-schemas.md
tags:
- taxonomy
- schema
- specification
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T18:03:32.041820+00:00'
sources:
- id: evt-ws-taxonomy-landscape-file-8cefa3760c72-41fe6e97
  resource: https://github.com/aaif/ws-taxonomy-landscape/blob/09a1b58155e0789614835fbd1e75005c6c337ee3/docs/data-schemas.md
  author: Julianna Langston
  last_modified: '2026-09-16T13:39:37-04:00'
- id: evt-ws-taxonomy-landscape-file-a54ff182c7e8-35ff909a
  resource: https://github.com/aaif/ws-taxonomy-landscape/blob/09a1b58155e0789614835fbd1e75005c6c337ee3/AGENTS.md
  author: Julianna Langston
  last_modified: '2026-09-16T13:39:37-04:00'
- id: evt-ws-taxonomy-landscape-file-eca12c0a30e2-333c16a8
  resource: https://github.com/aaif/ws-taxonomy-landscape/blob/09a1b58155e0789614835fbd1e75005c6c337ee3/CONTRIBUTING.md
  author: Julianna Langston
  last_modified: '2026-09-16T13:39:37-04:00'
---

# Overview
The Taxonomy Data Schema defines the SKOS-Lite-compliant metadata format used in `taxonomy-data.js` to structure agentic AI terminology, hierarchical relationships, and cross-working-group mappings[^evt-ws-taxonomy-landscape-file-8cefa3760c72-41fe6e97] [^evt-ws-taxonomy-landscape-file-eca12c0a30e2-333c16a8].

# Architecture / Specification
Entries in `taxonomy-data.js` conform to the following properties:
- `term` (String, required): Unique display term in sentence case[^evt-ws-taxonomy-landscape-file-8cefa3760c72-41fe6e97].
- `category` (String, deferred): High-level taxonomy grouping bucket; currently deferred to keep initial intake lightweight[^evt-ws-taxonomy-landscape-file-8cefa3760c72-41fe6e97].
- `aliases` (Array of Strings, required): Synonyms or historical alternate spellings[^evt-ws-taxonomy-landscape-file-8cefa3760c72-41fe6e97].
- `broaderTerm` (String or null, deferred): Parent concept identifier in SKOS hierarchy; currently deferred to preserve flat initial intake[^evt-ws-taxonomy-landscape-file-8cefa3760c72-41fe6e97].
- `definition` (String, required/deferred): Pre-competitive definition. While terms are admitted before definitions are finalized, placeholder text is required[^evt-ws-taxonomy-landscape-file-8cefa3760c72-41fe6e97].
- `scopeNote` (String, optional): WG boundary clarifications, intake history, or meeting dates[^evt-ws-taxonomy-landscape-file-8cefa3760c72-41fe6e97].
- `relatedTerms` / `contrastsWith` (Array of Strings, optional): Associative linkages connecting related concepts and explicit contrast pairs[^evt-ws-taxonomy-landscape-file-8cefa3760c72-41fe6e97] [^evt-ws-taxonomy-landscape-file-a54ff182c7e8-35ff909a].
- `workgroups` (Array of Strings, required): Technical working groups sharing ownership or interest in the term[^evt-ws-taxonomy-landscape-file-8cefa3760c72-41fe6e97].

[^evt-ws-taxonomy-landscape-file-8cefa3760c72-41fe6e97]: https://github.com/aaif/ws-taxonomy-landscape/blob/09a1b58155e0789614835fbd1e75005c6c337ee3/docs/data-schemas.md
[^evt-ws-taxonomy-landscape-file-a54ff182c7e8-35ff909a]: https://github.com/aaif/ws-taxonomy-landscape/blob/09a1b58155e0789614835fbd1e75005c6c337ee3/AGENTS.md
[^evt-ws-taxonomy-landscape-file-eca12c0a30e2-333c16a8]: https://github.com/aaif/ws-taxonomy-landscape/blob/09a1b58155e0789614835fbd1e75005c6c337ee3/CONTRIBUTING.md
