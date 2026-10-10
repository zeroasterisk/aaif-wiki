---
type: working-group
title: Taxonomy and Landscape Workstream
description: Horizontal AAIF technical initiative governing cross-domain taxonomy
  curation, SKOS-Lite vocabularies, and ecosystem mapping across Foundation working
  groups.
resource: https://github.com/aaif/ws-taxonomy-landscape/blob/6ac90f517a064054d4113b3331c8c06e380258b8/CONTRIBUTING.md
tags:
- governance
- taxonomy
- landscape
- working-group
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:22:28.785976+00:00'
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
The Taxonomy and Landscape Workstream is a horizontal initiative within the Agentic AI Foundation (AAIF) tasked with maintaining a unified cross-domain vocabulary and global ecosystem landscape across all Foundation Technical Working Groups[^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77]. The workstream coordinates terminology across specialized domains, standardizes definitions, and ensures conceptual interoperability across agentic systems[^evt-ws-taxonomy-landscape-pr-83].

# Governance and Roles
The workstream distributes curation responsibilities across three operational tiers[^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77]:
- **Contributors**: Open community participants, working group members, and external partners who submit pull requests, propose glossary additions, and log issues.
- **Domain Editors**: Nominated technical experts representing the seven active Technical Working Groups (such as [Identity & Trust](../working-groups/identity-and-trust.md), [Observability & Traceability](../working-groups/observability-and-traceability.md), and [Security & Privacy](../working-groups/security-and-privacy.md)) who actively author and steward entries in their respective domains.
- **Maintainers**: Workstream chairs (Junjie Bu and Gala Malbasic) holding repository write access and final administrative merge authority.

# Contribution Lifecycle and Review
Taxonomy updates follow a structured multi-stage intake and consensus workflow[^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77][^evt-ws-taxonomy-landscape-pr-83]:
1. **Working Group Inception**: Prospective terms originate within individual domain Working Groups.
2. **Intake Nomination**: Domain delegates log terms into the central taxonomy tracking sheet and coordinate via communication channels.
3. **Workstream Review and Triage**: During weekly workstream meetings, terms are evaluated for practical relevance, novelty, non-redundancy, and working group ownership. Terms receive one of three formal dispositions:
   - `KEEP`: Approved for formal pull request authoring.
   - `CULL`: Rejected from inclusion.
   - `DEBATE`: Held for broader consensus and clarification.
4. **Pull Request Submission**: The owning delegate submits a SKOS-Lite-compliant pull request providing a concise single-sentence definition and supplementary details in `scopeNote`.
5. **Cross-Working-Group Approval**: Merging a single-term pull request requires approvals from at least two Domain Editors representing distinct Technical Working Groups. Any Domain Editor retains veto authority.
6. **Rebase and Merge**: Approved pull requests are merged via GitHub's rebase-and-merge strategy, transitioning tracking records to `FINALIZED`.

# Scope Limitations
The workstream is actively accepting and processing taxonomy glossary additions only; contributions proposing ecosystem landscape modifications remain deferred pending formal landscape review workflow ratification[^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77].

[^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77]: https://github.com/aaif/ws-taxonomy-landscape/blob/6ac90f517a064054d4113b3331c8c06e380258b8/CONTRIBUTING.md
[^evt-ws-taxonomy-landscape-pr-83]: https://github.com/aaif/ws-taxonomy-landscape/pull/83
