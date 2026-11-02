---
type: skill
title: Taxonomy Contributions
description: Operational skill and contributor workflow enforcing SKOS-Lite schemas,
  horizontal indexing rules, and cross-working-group consensus for AAIF glossary terms.
resource: https://github.com/aaif/ws-taxonomy-landscape/blob/6ac90f517a064054d4113b3331c8c06e380258b8/CONTRIBUTING.md
tags:
- skills
- taxonomy
- contributions
- governance
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
---

# Overview

The Taxonomy Contributions skill standardizes the authoring, triage, and submission workflow for new terms added to the [Taxonomy and Landscape Workstream](../working-groups/taxonomy-and-landscape.md). It ensures all additions adhere to SKOS-Lite metadata requirements, follow strict formatting invariants, and satisfy foundation governance thresholds [^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77].

Contributions are predominantly stewarded by appointed Domain Editors from the technical working groups, ensuring cross-domain consistency across groups like [Security and Privacy](../working-groups/security-and-privacy.md) and [Workflows and Process Integration](../working-groups/workflows-and-process-integration.md).

# Architecture / Specification

## Contributor Workflow

1. **Propose Term**: Non-delegate contributors coordinate with their respective working group delegate, or attend the weekly taxonomy meeting to advocate for candidate terms [^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77].
2. **Triage Gate**: The candidate term must be logged in the central tracking spreadsheet and receive a formal `KEEP` vote during the weekly workstream meeting before code changes are accepted [^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77].
3. **Authoring Rules**:
   - **Single-Sentence Definition**: The primary definition field must be exactly one concise sentence [^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77].
   - **Scope Notes**: Extended clarifications, nuances, and concrete usage examples must be placed in the `scopeNote` metadata field [^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77].
   - **Granularity**: Pull requests should ideally encompass exactly one term to facilitate isolated review.
4. **Review and Veto**:
   - Requires approval from at least two Domain Editors representing different technical working groups [^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77].
   - Any delegate retains absolute veto power over a proposed term definition [^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77].
5. **Merge**: Merges are executed by workstream maintainers via Git rebase-and-merge, transitioning the tracking record to `FINALIZED` [^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77].

## Scope Constraints

The skill strictly rejects pull requests attempting modifications to the ecosystem Landscape, as landscape contributions remain frozen pending formal contribution process adoption [^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77].

[^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77]: https://github.com/aaif/ws-taxonomy-landscape/blob/6ac90f517a064054d4113b3331c8c06e380258b8/CONTRIBUTING.md
