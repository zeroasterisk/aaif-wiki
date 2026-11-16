---
type: skill
title: AAIF Clean Data Skill
description: Operational data normalization skill enforcing Google Workspace CLI native
  mutations, untrusted input containment, and proposed-diff approval gates for intake
  records.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-clean-data/WORKFLOW.md
tags:
- community-events
- skills
- data-cleaning
- operations
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:32:18.734209+00:00'
sources:
- id: evt-community-events-file-f66a78711977-a26d3112
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-clean-data/WORKFLOW.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:19:56-07:00'
- id: evt-community-events-file-06572a96a58d-9d2d11f7
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/CHANGELOG.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
---

# Overview
The `aaif-clean-data` skill normalizes community intake submissions within Google Sheets without silent data modification, functioning as Phase 1 of the automated estate synchronization pipeline.[^evt-community-events-file-f66a78711977-a26d3112] It inspects submitted responses, extracts and normalizes attendee or organizer locations, and produces explicit before-and-after diffs for operator review prior to applying any mutations.[^evt-community-events-file-f66a78711977-a26d3112]

City resolution serves as an essential gatekeeper for downstream community infrastructure: an intake entry with an unresolved city designation remains invisible to subsequent sync tasks, failing to populate chapter rosters, CRM lists, or Google Drive authorization grants.[^evt-community-events-file-f66a78711977-a26d3112] It operates as part of the broader [Community Event Operations](../skills/community-event-operations.md) suite.[^evt-community-events-file-06572a96a58d-9d2d11f7]

# Architecture / Specification
The cleaning engine (`scripts/clean.py`) operates in two distinct operational phases:[^evt-community-events-file-f66a78711977-a26d3112]
- **Scan Mode (Read-Only)**: Detects data anomalies and proposes mechanical fixes such as trimming whitespace, re-casing all-upper or all-lower text, and canonicalizing LinkedIn profile URLs. It flags entries requiring human judgment, such as duplicate or invalid email addresses, missing names, and non-profile links.[^evt-community-events-file-f66a78711977-a26d3112] Entries reporting an unextracted `Other` city are highlighted with cell-scoped red formatting for chapter review without modifying underlying values.[^evt-community-events-file-06572a96a58d-9d2d11f7]
- **Apply Mode (Write on Approval)**: Consumes an approved JSON changeset written to an isolated temporary directory. Mutations write directly to the primary `Form Responses` sheet using column header names rather than column letters, recording applied changes in an `Autofixes` column for audit provenance.[^evt-community-events-file-f66a78711977-a26d3112]

### Tooling and Environmental Invariants
- **Native Google Workspace CLI (`gws`)**: All Google Drive and Sheets interactions must execute via Python calling the `gws` command-line utility with authenticated API scopes.[^evt-community-events-file-f66a78711977-a26d3112]
- **Office Suite Prohibition**: Tools such as LibreOffice, `soffice`, or `unoconv` are strictly prohibited for file conversion, edits, or local previews due to font substitution and loss of native OpenXML and Google Docs formatting features.[^evt-community-events-file-f66a78711977-a26d3112]
- **Untrusted Input Treatment**: Sheet cell values are strictly handled as passive data and never as control directives.[^evt-community-events-file-f66a78711977-a26d3112]

# Lifecycle History
Introduced as part of the AAIF Community Events Toolkit, the workflow was expanded to accommodate granular role questionnaires (converting unified participation prompts into explicit per-role gates for organizers, hosts, speakers, and collaborators) and chapter review flags for submitted `Other` locations.[^evt-community-events-file-06572a96a58d-9d2d11f7]

[^evt-community-events-file-06572a96a58d-9d2d11f7]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/CHANGELOG.md
[^evt-community-events-file-f66a78711977-a26d3112]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-clean-data/WORKFLOW.md
