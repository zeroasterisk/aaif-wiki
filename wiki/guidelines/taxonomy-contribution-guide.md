---
type: guideline
title: Taxonomy Contribution Guide
description: Authoring guidelines, governance roles, review workflows, and approval
  thresholds governing vocabulary contributions across AAIF working groups.
resource: https://github.com/aaif/ws-taxonomy-landscape/blob/6ac90f517a064054d4113b3331c8c06e380258b8/CONTRIBUTING.md
tags:
- governance
- taxonomy
- guidelines
- process
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:19:34.776968+00:00'
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
The Taxonomy Contribution Guide defines the roles, submission workflows, validation criteria, and review stages for maintaining horizontal, shared terminology across the Agentic AI Foundation (AAIF)[^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77]. Governed by the [Taxonomy & Landscape Workstream](../working-groups/taxonomy-and-landscape.md), the process establishes strict consensus requirements, requiring multi-working-group review before terms are codified into the canonical glossary[^evt-ws-taxonomy-landscape-pr-83].

At present, workstream contributions are strictly limited to taxonomy terms; contributions to the ecosystem landscape remain frozen on the roadmap until a dedicated contribution and review framework is formally adopted[^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77].

# Architecture / Specification

## Governance Roles
The contribution workflow distributes curation authority across three distinct tiers[^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77]:
- **Contributors**: Any community member or external participant entitled to submit pull requests, suggest vocabulary terms, or open issues.
- **Domain Editors**: Nominated delegates representing the active AAIF Technical Working Groups who actively author, evaluate, and shepherd taxonomy entries for their respective technical domains.
- **Maintainers**: Workstream chairs (Junjie Bu and Gala Malbasic) holding repository write access and final administrative authority to rebase and merge approved pull requests.

## End-to-End Submission Workflow
Vocabulary additions follow a staged qualification lifecycle before entering the codebase[^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77][^evt-ws-taxonomy-landscape-pr-83]:
1. **Origination**: Terms are identified and formulated within individual Technical Working Groups.
2. **Workstream Intake**: A working group delegate records the proposed term in the centralized intake tracking sheet and notifies the workstream communication channel.
3. **Weekly Review and Triage**: The Taxonomy Workstream assesses terms during weekly meetings based on practical real-world usage, novelty, conceptual substance, and appropriate domain ownership. The workstream assigns one of three disposition verdicts:
   - `KEEP`: The term is accepted in principle, permitting the submission of an implementation pull request.
   - `CULL`: The term is rejected.
   - `DEBATE`: The term requires further cross-group debate and clarification.
4. **Pull Request Authoring**: A delegate from the owning working group submits a pull request containing a single-sentence definition compliant with the SKOS-Lite data schema. Supplementary context, rationale, and usage examples must be placed in the `scopeNote` field. Submitting one term per pull request is recommended. Pull requests proposing terms lacking prior `KEEP` approval are closed.
5. **Cross-Working-Group Review**: Approval requires sign-off from at least two Domain Editors representing different Technical Working Groups. Any Domain Editor possesses unilateral veto power over a proposed term. Multi-term pull requests may require higher approval thresholds.
6. **Integration**: Approved pull requests are integrated using GitHub's rebase-and-merge strategy, transitioning the tracking record to `FINALIZED`.

## Data Schema Compliance
All accepted terms must adhere to the SKOS-Lite-compliant data schema specified by the workstream, mapping display names, broader taxonomy hierarchies, owning working group attributions, concise definitions, and structured scope notes[^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77].

[^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77]: https://github.com/aaif/ws-taxonomy-landscape/blob/6ac90f517a064054d4113b3331c8c06e380258b8/CONTRIBUTING.md
[^evt-ws-taxonomy-landscape-pr-83]: https://github.com/aaif/ws-taxonomy-landscape/pull/83
