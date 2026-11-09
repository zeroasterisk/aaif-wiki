---
type: skill
title: Taxonomy Contribution Workflow
description: Operational instructions and validation guardrails for contributing SKOS-Lite
  terms to the AAIF Taxonomy & Landscape Workstream repository.
resource: https://github.com/aaif/ws-taxonomy-landscape/blob/b930afdb296bbce8613943327810e30a7b3d9ba5/docs/local-development.md
tags:
- taxonomy
- skill
- git-workflow
- validation
- skos
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:28:02.902619+00:00'
sources:
- id: evt-ws-taxonomy-landscape-file-53e532051b05-bb61ada3
  resource: https://github.com/aaif/ws-taxonomy-landscape/blob/b930afdb296bbce8613943327810e30a7b3d9ba5/docs/local-development.md
  author: leonardog
  last_modified: '2026-10-26T08:52:39-07:00'
- id: evt-ws-taxonomy-landscape-file-8cefa3760c72-6a955025
  resource: https://github.com/aaif/ws-taxonomy-landscape/blob/b930afdb296bbce8613943327810e30a7b3d9ba5/docs/data-schemas.md
  author: leonardog
  last_modified: '2026-10-26T08:52:39-07:00'
- id: evt-ws-taxonomy-landscape-file-eda84dd4e776-c952cbc5
  resource: https://github.com/aaif/ws-taxonomy-landscape/blob/b930afdb296bbce8613943327810e30a7b3d9ba5/.github/workflows/validate-taxonomy.yml
  author: Leonardo Galesky
  last_modified: '2026-10-26T08:52:39-07:00'
- id: evt-ws-taxonomy-landscape-file-a54ff182c7e8-65b1abe3
  resource: https://github.com/aaif/ws-taxonomy-landscape/blob/b930afdb296bbce8613943327810e30a7b3d9ba5/AGENTS.md
  author: leonardog
  last_modified: '2026-10-26T08:52:39-07:00'
---

# Overview
The Taxonomy Contribution Workflow governs how autonomous agents and human contributors propose, validate, and document terminology additions within `aaif/ws-taxonomy-landscape`[^evt-ws-taxonomy-landscape-file-a54ff182c7e8-65b1abe3]. The workflow enforces strict JSON data schemas, phased term-first admission criteria, pre-commit validation tests, and review-gated continuous integration pipelines[^evt-ws-taxonomy-landscape-file-53e532051b05-bb61ada3][^evt-ws-taxonomy-landscape-file-eda84dd4e776-c952cbc5].

# Architecture / Specification
### Schema Constraints (`taxonomy/taxonomy.json`)
Contributions must conform to the SKOS-Lite JSON schema verified by Zod validation suites[^evt-ws-taxonomy-landscape-file-53e532051b05-bb61ada3][^evt-ws-taxonomy-landscape-file-8cefa3760c72-6a955025]:
- `term`: Sentence-case string, globally unique across the file[^evt-ws-taxonomy-landscape-file-8cefa3760c72-6a955025].
- `aliases`: Array of strings for strict synonyms; use `[]` if none[^evt-ws-taxonomy-landscape-file-8cefa3760c72-6a955025].
- `scopeNote`: Optional context, meeting references, or cross-workgroup boundary notes[^evt-ws-taxonomy-landscape-file-8cefa3760c72-6a955025].
- `relatedTerms`: Array of associative `skos:related` concepts[^evt-ws-taxonomy-landscape-file-8cefa3760c72-6a955025].
- `contrastsWith`: Array linking explicit paired counter-concepts[^evt-ws-taxonomy-landscape-file-8cefa3760c72-6a955025].
- `workgroups`: Array of owning or collaborating working groups; `"Universal"` is strictly prohibited (use `[]` if universal)[^evt-ws-taxonomy-landscape-file-8cefa3760c72-6a955025].

### Deferred Fields Protocol
Under the initial check-in consensus established on 2026-07-27, terms are admitted before final definitions are ratified[^evt-ws-taxonomy-landscape-file-8cefa3760c72-6a955025]:
- `definition`: Must use exact placeholder string `Definition pending — term accepted; definition under working group discussion.`[^evt-ws-taxonomy-landscape-file-8cefa3760c72-6a955025].
- `category`: Set to empty string `""` until ontology categories are reinstated[^evt-ws-taxonomy-landscape-file-8cefa3760c72-6a955025].
- `broaderTerm`: Set to `null` to maintain a flat initial hierarchy pending cross-WG scope mapping[^evt-ws-taxonomy-landscape-file-8cefa3760c72-6a955025].

### Local Development and Validation
1. Local preview server: Run `python3 -m http.server 8000` or `npx serve -l 8000` and inspect `http://localhost:8000/taxonomy/`[^evt-ws-taxonomy-landscape-file-53e532051b05-bb61ada3].
2. Dependency setup: `npm ci --ignore-scripts`[^evt-ws-taxonomy-landscape-file-53e532051b05-bb61ada3].
3. Automated test execution: Run `npm run check` to validate `taxonomy/taxonomy.json` against the Zod schema and run regression tests[^evt-ws-taxonomy-landscape-file-53e532051b05-bb61ada3].

### CI Security & Review Gating
CI data validation (`validate-taxonomy.yml`) is restricted to the `pull_request_review` event (when submitted or edited by maintainers) and manual `workflow_dispatch`[^evt-ws-taxonomy-landscape-file-eda84dd4e776-c952cbc5]. This mitigates compute-abuse vectors from unvetted push events while enforcing strict JSON validation before merging[^evt-ws-taxonomy-landscape-file-eda84dd4e776-c952cbc5].

[^evt-ws-taxonomy-landscape-file-53e532051b05-bb61ada3]: https://github.com/aaif/ws-taxonomy-landscape/blob/b930afdb296bbce8613943327810e30a7b3d9ba5/docs/local-development.md
[^evt-ws-taxonomy-landscape-file-8cefa3760c72-6a955025]: https://github.com/aaif/ws-taxonomy-landscape/blob/b930afdb296bbce8613943327810e30a7b3d9ba5/docs/data-schemas.md
[^evt-ws-taxonomy-landscape-file-a54ff182c7e8-65b1abe3]: https://github.com/aaif/ws-taxonomy-landscape/blob/b930afdb296bbce8613943327810e30a7b3d9ba5/AGENTS.md
[^evt-ws-taxonomy-landscape-file-eda84dd4e776-c952cbc5]: https://github.com/aaif/ws-taxonomy-landscape/blob/b930afdb296bbce8613943327810e30a7b3d9ba5/.github/workflows/validate-taxonomy.yml
