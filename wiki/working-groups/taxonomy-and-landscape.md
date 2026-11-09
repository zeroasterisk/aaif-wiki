---
type: working-group
title: Taxonomy & Landscape Workstream
description: Cross-cutting AAIF workstream curating a shared SKOS-Lite taxonomy and
  ecosystem map across foundation technical working groups.
resource: https://github.com/aaif/ws-taxonomy-landscape/blob/b930afdb296bbce8613943327810e30a7b3d9ba5/charter/charter.md
tags:
- taxonomy
- landscape
- governance
- skos
- standards
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:28:02.902619+00:00'
sources:
- id: evt-ws-taxonomy-landscape-file-b41aaf03f7ac-e6083ea5
  resource: https://github.com/aaif/ws-taxonomy-landscape/blob/b930afdb296bbce8613943327810e30a7b3d9ba5/charter/charter.md
  author: leonardog
  last_modified: '2026-10-26T08:52:39-07:00'
- id: evt-ws-taxonomy-landscape-file-a54ff182c7e8-65b1abe3
  resource: https://github.com/aaif/ws-taxonomy-landscape/blob/b930afdb296bbce8613943327810e30a7b3d9ba5/AGENTS.md
  author: leonardog
  last_modified: '2026-10-26T08:52:39-07:00'
- id: evt-ws-taxonomy-landscape-file-53e532051b05-bb61ada3
  resource: https://github.com/aaif/ws-taxonomy-landscape/blob/b930afdb296bbce8613943327810e30a7b3d9ba5/docs/local-development.md
  author: leonardog
  last_modified: '2026-10-26T08:52:39-07:00'
- id: evt-ws-taxonomy-landscape-file-8cefa3760c72-6a955025
  resource: https://github.com/aaif/ws-taxonomy-landscape/blob/b930afdb296bbce8613943327810e30a7b3d9ba5/docs/data-schemas.md
  author: leonardog
  last_modified: '2026-10-26T08:52:39-07:00'
---

# Overview
The Taxonomy & Landscape Workstream serves as the horizontal architectural bridge across all top-level technical working groups in the Agentic AI Foundation (AAIF)[^evt-ws-taxonomy-landscape-file-a54ff182c7e8-65b1abe3]. Approved on June 21, 2026, the workstream is chaired by Junjie Bu (Google) and co-chaired by Gala Malbasic (Bloomberg)[^evt-ws-taxonomy-landscape-file-b41aaf03f7ac-e6083ea5]. Its core mandate is curating an authoritative, pre-competitive living vocabulary (`taxonomy/taxonomy.json`) and an interactive CNCF-style ecosystem landscape (`landscape.yml`) to eliminate terminology silos, prevent duplicated ecosystem research, and provide an enterprise architectural blueprint[^evt-ws-taxonomy-landscape-file-b41aaf03f7ac-e6083ea5].

# Architecture / Specification
The workstream enforces the "Horizontal Index" architectural principle to preserve domain sovereignty across specialized working groups:
- **Horizontal Index (In-Scope):** Consolidation, harmonization, and cross-cutting arbitration of core concepts affecting two or more working groups, published via a SKOS-Lite metadata schema (`prefLabel`, `altLabel`, `broaderTerm`, `scopeNote`, `relatedTerms`, `contrastsWith`)[^evt-ws-taxonomy-landscape-file-a54ff182c7e8-65b1abe3][^evt-ws-taxonomy-landscape-file-b41aaf03f7ac-e6083ea5].
- **Domain Payloads (Out-of-Scope):** Deep vertical whitepapers, wire protocol designs, and execution-level helper schemas remain the exclusive purview of vertical working groups such as [Security & Privacy](../working-groups/security-and-privacy.md) and [Observability & Traceability](../working-groups/observability-and-traceability.md)[^evt-ws-taxonomy-landscape-file-a54ff182c7e8-65b1abe3][^evt-ws-taxonomy-landscape-file-b41aaf03f7ac-e6083ea5].
- **Operational Scope Constraint:** Only taxonomy modifications are currently admitted; landscape contributions remain paused until an approved intake process is formally established[^evt-ws-taxonomy-landscape-file-53e532051b05-bb61ada3][^evt-ws-taxonomy-landscape-file-a54ff182c7e8-65b1abe3].
- **Epistemological Disambiguation:** Mandates explicit counterpart differentiation for adjacent concepts (such as Tool versus Skill or Primitive versus Protocol) via `contrastsWith` and `relatedTerms`, preventing conflation into ambiguous definitions[^evt-ws-taxonomy-landscape-file-a54ff182c7e8-65b1abe3].
- **Anti-Erasure Safeguards:** Deletion or aliasing of established terms requires written concurrence from the owning working group's designated Domain Editor[^evt-ws-taxonomy-landscape-file-a54ff182c7e8-65b1abe3].

# Governance & Operations
- **Meeting Cadence:** Weekly on Mondays at 8:30 AM PT / 11:30 AM ET / 4:30 PM BST (30 minutes)[^evt-ws-taxonomy-landscape-file-b41aaf03f7ac-e6083ea5].
- **Channels:** Mailing list `ws-taxonomy-landscape@lists.aaif.io`, Discord `#ws-taxonomy-landscape`, and GitHub repository `aaif/ws-taxonomy-landscape`[^evt-ws-taxonomy-landscape-file-b41aaf03f7ac-e6083ea5].
- **Key Performance Indicators:** Falsifiable metrics including citation utility across AAIF specifications, corporate contribution limits (no single corporate entity exceeding 50% of merged entries), ecosystem coverage (each active WG maintaining at least 10 reviewed terms), and quarterly arbitration velocity[^evt-ws-taxonomy-landscape-file-a54ff182c7e8-65b1abe3].

# Lifecycle History
- 2026-06-21: Workstream charter formally approved with Junjie Bu and Gala Malbasic as chairs[^evt-ws-taxonomy-landscape-file-b41aaf03f7ac-e6083ea5].
- 2026-07-27: Workstream consensus established initial flat check-in policy, deferring `category`, `broaderTerm`, and `definition` backfilling during phase-one term ingestion[^evt-ws-taxonomy-landscape-file-8cefa3760c72-6a955025].

[^evt-ws-taxonomy-landscape-file-53e532051b05-bb61ada3]: https://github.com/aaif/ws-taxonomy-landscape/blob/b930afdb296bbce8613943327810e30a7b3d9ba5/docs/local-development.md
[^evt-ws-taxonomy-landscape-file-8cefa3760c72-6a955025]: https://github.com/aaif/ws-taxonomy-landscape/blob/b930afdb296bbce8613943327810e30a7b3d9ba5/docs/data-schemas.md
[^evt-ws-taxonomy-landscape-file-a54ff182c7e8-65b1abe3]: https://github.com/aaif/ws-taxonomy-landscape/blob/b930afdb296bbce8613943327810e30a7b3d9ba5/AGENTS.md
[^evt-ws-taxonomy-landscape-file-b41aaf03f7ac-e6083ea5]: https://github.com/aaif/ws-taxonomy-landscape/blob/b930afdb296bbce8613943327810e30a7b3d9ba5/charter/charter.md
