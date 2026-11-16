---
type: working-group
title: Taxonomy & Landscape Workstream
description: Cross-cutting AAIF workstream harmonizing agentic terminology across
  working groups and curating an authoritative ecosystem market map.
resource: https://github.com/aaif/ws-taxonomy-landscape/blob/719905a88f11ab6846080313dfe4b8c423411235/charter/charter.md
tags:
- governance
- taxonomy
- landscape
- skos
- workstream
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:38:09.419537+00:00'
sources:
- id: evt-ws-taxonomy-landscape-file-b41aaf03f7ac-e6083ea5
  resource: https://github.com/aaif/ws-taxonomy-landscape/blob/719905a88f11ab6846080313dfe4b8c423411235/charter/charter.md
  author: leonardog
  last_modified: '2026-10-26T08:52:39-07:00'
- id: evt-ws-taxonomy-landscape-file-a54ff182c7e8-65b1abe3
  resource: https://github.com/aaif/ws-taxonomy-landscape/blob/719905a88f11ab6846080313dfe4b8c423411235/AGENTS.md
  author: leonardog
  last_modified: '2026-10-26T08:52:39-07:00'
- id: evt-ws-taxonomy-landscape-file-8cefa3760c72-6a955025
  resource: https://github.com/aaif/ws-taxonomy-landscape/blob/719905a88f11ab6846080313dfe4b8c423411235/docs/data-schemas.md
  author: leonardog
  last_modified: '2026-10-26T08:52:39-07:00'
- id: evt-ws-taxonomy-landscape-file-53e532051b05-bb61ada3
  resource: https://github.com/aaif/ws-taxonomy-landscape/blob/719905a88f11ab6846080313dfe4b8c423411235/docs/local-development.md
  author: leonardog
  last_modified: '2026-10-26T08:52:39-07:00'
- id: evt-wg-observability-and-traceability-file-60f28464dd94-2a91d869
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/81dc934a316e97895677257cdc0977f5c3498ea2/reporting/2026-09-report.md
  author: Pavan Sudheendra
  last_modified: '2026-10-27T05:12:49+00:00'
---

# Overview

The Taxonomy & Landscape Workstream is a cross-cutting Agentic AI Foundation (AAIF) body chartered to curate a shared glossary of agentic AI concepts and maintain an authoritative, CNCF-style ecosystem architecture map.[^evt-ws-taxonomy-landscape-file-b41aaf03f7ac-e6083ea5] Chaired by Junjie Bu (Google) and Gala Malbasic (Bloomberg), the workstream acts as a horizontal coordination bridge linking all vertical technical working groups to eliminate terminology silos, prevent duplicate market surveying, and deliver a unified technology blueprint for industry practitioners.[^evt-ws-taxonomy-landscape-file-b41aaf03f7ac-e6083ea5]

The workstream operates under a federated governance structure where each vertical working group designates Domain Editors who hold review authority over terms relevant to their respective subject matter domains.[^evt-ws-taxonomy-landscape-file-b41aaf03f7ac-e6083ea5] While its initial charter encompasses both terminology consolidation and ecosystem landscape mapping, active contribution is strictly limited to the taxonomy repository while the landscape contribution workflow remains in development on the roadmap.[^evt-ws-taxonomy-landscape-file-53e532051b05-bb61ada3]

# Architecture / Specification

### The Horizontal Index Principle

To preserve domain sovereignty and avoid jurisdictional conflict across vertical working groups, the workstream enforces the "Horizontal Index" principle:[^evt-ws-taxonomy-landscape-file-a54ff182c7e8-65b1abe3]
- **Consolidation over Creation:** The workstream does not author specialized domain definitions from scratch; rather, it ingests, standardizes, and harmonizes glossaries developed by vertical working groups.[^evt-ws-taxonomy-landscape-file-a54ff182c7e8-65b1abe3]
- **In-Scope Index:** Foundational vocabulary and cross-cutting concepts spanning two or more working groups, along with universal ecosystem taxonomy structures, fall under workstream management.[^evt-ws-taxonomy-landscape-file-a54ff182c7e8-65b1abe3]
- **Out-of-Scope Payload:** Deep-dive domain whitepapers, specialized internal technical helpers, code-level wire protocol schemas, and low-level protocol designs remain the exclusive purview of their respective vertical groups.[^evt-ws-taxonomy-landscape-file-b41aaf03f7ac-e6083ea5]

### SKOS-Lite Data Schema and Deferred Fields Policy

Taxonomy definitions are stored in `taxonomy/taxonomy.json` using a normalized Simple Knowledge Organization System (SKOS) Lite representation:[^evt-ws-taxonomy-landscape-file-8cefa3760c72-6a955025]
- **Core Attributes:** Entries mandate `term` (unique sentence-case string), `aliases` (array of true synonyms), `workgroups` (array of sponsoring working groups), `scopeNote`, `relatedTerms` (`skos:related`), and `contrastsWith`.[^evt-ws-taxonomy-landscape-file-8cefa3760c72-6a955025]
- **Deferred Fields (as of 2026-07-27):** Under workstream consensus, terms are admitted ahead of final definitions to avoid premature rigidity. The `definition` attribute holds a standardized pending placeholder (`Definition pending — term accepted; definition under working group discussion.`), while `category` is initialized to empty string (`""`) and `broaderTerm` is initialized to `null` pending hierarchical mapping between groups.[^evt-ws-taxonomy-landscape-file-8cefa3760c72-6a955025]
- **Workgroup Assignment Rules:** The value `"Universal"` is explicitly disallowed; entries with cross-cutting relevance across all groups use an empty array (`[]`) and document contextual boundaries within `scopeNote`.[^evt-ws-taxonomy-landscape-file-8cefa3760c72-6a955025]

### Epistemological Disambiguation Protocol

When reconciling cross-cutting terminology intersections, contributors and automated systems must apply the Paired Contrast Disambiguation Protocol:[^evt-ws-taxonomy-landscape-file-a54ff182c7e8-65b1abe3]
1. **Counterpart Disambiguation:** Terms that derive operational clarity by contrast (such as Tool versus Skill or Deterministic versus Agentic workflows) must not be merged into generic catch-all entries.[^evt-ws-taxonomy-landscape-file-a54ff182c7e8-65b1abe3]
2. **Mandatory Associative Linking:** Each term must link explicitly via `relatedTerms` or `contrastsWith`, and its eventual definition must document boundary differences.[^evt-ws-taxonomy-landscape-file-a54ff182c7e8-65b1abe3]
3. **Anti-Erasure Guardrails:** No concept may be deleted or collapsed into an alias without written sign-off from the owning Domain Editor.[^evt-ws-taxonomy-landscape-file-a54ff182c7e8-65b1abe3]

# Lifecycle History

- **2026-06-21:** Workstream charter approved with weekly synchronization cadence, establishing Junjie Bu and Gala Malbasic as co-chairs.[^evt-ws-taxonomy-landscape-file-b41aaf03f7ac-e6083ea5]
- **2026-07-27:** Workstream established the deferred fields policy (`category`, `broaderTerm`, and `definition` staged as pending) to facilitate broad term intake across foundational groups.[^evt-ws-taxonomy-landscape-file-8cefa3760c72-6a955025]
- **2026-09-28:** Successfully integrated seven core observability concepts (Reasoning, Agent Trajectory, Context Propagation, Context Assembly, Memory Access, Retrieval, and Traceability) from the [Observability & Traceability Working Group](../working-groups/observability-and-traceability.md).[^evt-wg-observability-and-traceability-file-60f28464dd94-2a91d869]

# References

[^evt-ws-taxonomy-landscape-file-b41aaf03f7ac-e6083ea5]: AAIF Taxonomy & Landscape Workstream Charter (`charter/charter.md`).
[^evt-ws-taxonomy-landscape-file-a54ff182c7e8-65b1abe3]: Autonomous Agent & Contributor Guidance (`AGENTS.md`).
[^evt-ws-taxonomy-landscape-file-8cefa3760c72-6a955025]: Data Schema Specifications & Guidelines (`docs/data-schemas.md`).
[^evt-ws-taxonomy-landscape-file-53e532051b05-bb61ada3]: Local Development & Git Workflow Guide (`docs/local-development.md`).
[^evt-wg-observability-and-traceability-file-60f28464dd94-2a91d869]: Observability & Traceability Working Group September 2026 Report (`reporting/2026-09-report.md`).
