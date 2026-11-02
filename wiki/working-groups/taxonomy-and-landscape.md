---
type: working-group
title: Taxonomy and Landscape Workstream
description: Cross-cutting AAIF workstream harmonizing agentic AI terminology across
  vertical working groups and maintaining horizontal data schemas.
resource: https://github.com/aaif/ws-taxonomy-landscape/blob/6ac90f517a064054d4113b3331c8c06e380258b8/CONTRIBUTING.md
tags:
- governance
- taxonomy
- working-group
- schemas
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:18:31.048652+00:00'
sources:
- id: evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77
  resource: https://github.com/aaif/ws-taxonomy-landscape/blob/6ac90f517a064054d4113b3331c8c06e380258b8/CONTRIBUTING.md
  author: Julianna Langston
  last_modified: '2026-10-07T08:37:23-04:00'
- id: evt-ws-taxonomy-landscape-pr-83
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/83
  author: julianna-ciq
  last_modified: '2026-10-07T12:37:24+00:00'
- id: evt-ws-taxonomy-landscape-pr-89
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/89
  author: julianna-ciq
  last_modified: '2026-10-07T12:36:51+00:00'
---

# Overview

The Taxonomy and Landscape Workstream is a cross-cutting body within the Agentic AI Foundation (AAIF) tasked with maintaining a shared, horizontal vocabulary across all seven active Technical Working Groups and developing the foundation's ecosystem landscape [^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77]. While the workstream's charter encompasses both taxonomy and ecosystem market mapping, contributions are currently restricted strictly to taxonomy terms; landscape contribution workflows remain deferred on the future roadmap [^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77].

Operational workflows coordinate with vertical groups such as [Security and Privacy](security-and-privacy.md) and [Workflows and Process Integration](workflows-and-process-integration.md) using automated schema validation and contributor skills like [Taxonomy Contributions](../skills/taxonomy-contributions.md).

# Architecture / Specification

## Roles and Governance

The workstream structures participation across three functional tiers to maintain data integrity and distribute editorial responsibilities [^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77]:

- **Contributors**: Open to any community participant or external partner to propose terms or raise issues.
- **Domain Editors**: Nominated technical delegates representing each of the seven active Technical Working Groups. Domain Editors author domain-specific terms, guide definitions, and hold review and veto authority.
- **Maintainers**: Workstream co-chairs Junjie Bu and Gala Malbasic, who retain repository write access and execute final merges [^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77].

## Term Lifecycle and Review Workflow

Terms undergo a structured intake and consensus lifecycle prior to repository admission [^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77], [^evt-ws-taxonomy-landscape-pr-83]:

1. **Intake**: A working group delegate stages a candidate term in the central intake spreadsheet and signals the request in the community communications channel.
2. **Triage Vote**: Outstanding terms are reviewed during weekly meetings for practical real-world usage, novelty, and working-group ownership. The workstream assigns one of three formal dispositions:
   - `KEEP`: The term is accepted and authorized for pull request submission.
   - `CULL`: The term is rejected.
   - `DEBATE`: The term requires further cross-group deliberation.
3. **Pull Request Submission**: The owning delegate opens a pull request providing a single-sentence definition and an optional `scopeNote` for context. Pull requests for terms without a prior `KEEP` vote are closed automatically.
4. **Cross-Group Approval**: Pull requests require approvals from at least two Domain Editors representing distinct Technical Working Groups. Any delegate may exercise veto power.
5. **Finalization**: Maintainers merge approved pull requests using GitHub's rebase-and-merge strategy, updating the spreadsheet entry to `FINALIZED` [^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77].

## Build and Verification Tooling

Taxonomy entries are stored in structured JavaScript dictionaries (`taxonomy-data.js`) adhering to a SKOS-Lite schema [^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77]. Build verification includes automated schema validation (`tools/validate-taxonomy.mjs`) alongside automated generation and continuous integration verification of human-readable Markdown documentation (`tools/generate-taxonomy-markdown.mjs`) enforced via pre-commit hooks [^evt-ws-taxonomy-landscape-pr-89].

[^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77]: https://github.com/aaif/ws-taxonomy-landscape/blob/6ac90f517a064054d4113b3331c8c06e380258b8/CONTRIBUTING.md
[^evt-ws-taxonomy-landscape-pr-83]: https://github.com/aaif/ws-taxonomy-landscape/pull/83
[^evt-ws-taxonomy-landscape-pr-89]: https://github.com/aaif/ws-taxonomy-landscape/pull/89
