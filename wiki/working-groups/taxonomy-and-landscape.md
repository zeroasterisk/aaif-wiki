---
type: working-group
title: Taxonomy and Landscape Workstream
description: Cross-cutting AAIF workstream standardizing agentic AI terminology, SKOS-Lite
  vocabulary schemas, and multi-working-group review processes.
resource: https://github.com/aaif/ws-taxonomy-landscape/blob/6ac90f517a064054d4113b3331c8c06e380258b8/CONTRIBUTING.md
tags:
- governance
- taxonomy
- standards
- terminology
- skos
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:43:47.138332+00:00'
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
The Taxonomy & Landscape Workstream is a cross-cutting initiative within the Agentic AI Foundation (AAIF) tasked with maintaining a shared, horizontal vocabulary across technical working groups and cataloging the broader agentic ecosystem[^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77]. The workstream is co-chaired by Maintainers Junjie Bu and Gala Malbasic[^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77].

Current active operations are exclusively focused on the shared Taxonomy glossary, while submissions to the ecosystem Landscape remain deferred until formal intake processes are accepted[^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77].

# Architecture / Specification
The workstream operates a structured tripartite governance model to curate and validate terminology[^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77]:
- **Contributors (Anyone):** Community members and working group participants who propose new glossary terms, submit pull requests, or file taxonomy issues[^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77].
- **Domain Editors (Working Group Delegates):** Nominated technical delegates representing each of the seven active AAIF Technical Working Groups (including [Identity and Trust](../working-groups/identity-and-trust.md), [Observability and Traceability](../working-groups/observability-and-traceability.md), and [Workflows and Process Integration](../working-groups/workflows-and-process-integration.md)). Domain Editors act as primary curators who author and guide entries within their domain[^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77].
- **Maintainers (Workstream Chairs):** Maintainers hold administrative write access and final merging authority on the repository[^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77].

### Contribution and Review Lifecycle
1. **Working Group Sourcing:** Terms are initially formulated within individual technical working groups[^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77].
2. **Staging & Queueing:** A delegate brings the term into the centralized taxonomy spreadsheet and flags it in the dedicated Discord channel[^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77].
3. **Weekly Workstream Triage:** During weekly meetings, terms are reviewed for real-world usage, novelty, relevance, and correct working group attribution[^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77]. Terms receive one of three formal votes[^evt-ws-taxonomy-landscape-pr-83]:
   - `KEEP`: The term is accepted and cleared for a definition pull request[^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77].
   - `CULL`: The term is rejected[^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77].
   - `DEBATE`: The term requires broader discussion before acceptance[^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77].
4. **Pull Request Submission:** Once marked `KEEP`, a delegate from the owning working group submits a pull request with a single-sentence definition and supplementary details in `scopeNote` conformant to SKOS-Lite schemas[^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77].
5. **Cross-Domain Peer Approval:** Pull requests require approval from at least two Domain Editors representing different working groups; any delegate holds veto authority[^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77].
6. **Rebase Merge & Finalization:** Maintainers merge approved pull requests using a rebase-and-merge strategy, marking the spreadsheet item as `FINALIZED`[^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77][^evt-ws-taxonomy-landscape-pr-83].

# Lifecycle History
The taxonomy contribution workflow was formalized to establish the explicit KEEP/CULL/DEBATE evaluation lifecycle, cross-working-group review thresholds, and scope fencing favoring the core taxonomy over ecosystem landscape mapping[^evt-ws-taxonomy-landscape-pr-83].

[^evt-ws-taxonomy-landscape-file-eca12c0a30e2-92c6cc77]: https://github.com/aaif/ws-taxonomy-landscape/blob/6ac90f517a064054d4113b3331c8c06e380258b8/CONTRIBUTING.md
[^evt-ws-taxonomy-landscape-pr-83]: https://github.com/aaif/ws-taxonomy-landscape/pull/83
