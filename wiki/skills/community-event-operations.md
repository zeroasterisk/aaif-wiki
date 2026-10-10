---
type: skill
title: Community Event Operations Skills
description: Modular operational skills providing intake data cleaning, proposal-based
  data normalization, and role gate synchronization for AAIF community operations.
resource: https://github.com/aaif/community-events/blob/7812e00cb0da0153a9a93f3e19040b1f608a4901/skills/aaif-clean-data/WORKFLOW.md
tags:
- skills
- community-events
- data-normalization
- google-workspace
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:24:22.444967+00:00'
sources:
- id: evt-community-events-file-f66a78711977-35bb9a70
  resource: https://github.com/aaif/community-events/blob/7812e00cb0da0153a9a93f3e19040b1f608a4901/skills/aaif-clean-data/WORKFLOW.md
  author: Rahul Parundekar
  last_modified: '2026-10-09T10:56:24-07:00'
- id: evt-community-events-pr-59
  resource: https://github.com/aaif/community-events/pull/59
  author: rparundekar
  last_modified: '2026-10-09T18:08:39+00:00'
---

# Overview

Community Event Operations skills automate operational intake workflows, data normalization, and synchronization across applicant tracking systems and chapter registries [^evt-community-events-file-f66a78711977-35bb9a70]. The skills enforce a strict proposal-and-diff governance model where automated scripts detect malformed or incomplete entries and generate structured diffs for explicit human approval before mutating canonical source records [^evt-community-events-file-f66a78711977-35bb9a70].

# Architecture / Specification

### Intake Normalization (`aaif-clean-data`)

The intake cleaning pipeline operates as the first phase of estate synchronization (`aaif-sync`) [^evt-community-events-file-f66a78711977-35bb9a70]:

1. **Scan Mode (`clean.py scan`)**: Evaluates raw records from source forms in read-only mode, detecting mechanical formatting issues (whitespace trimming, casing corrections, LinkedIn URL canonicalization) and flagging ambiguous rows (such as missing emails, duplicate identities, or unmapped cities) [^evt-community-events-file-f66a78711977-35bb9a70].
2. **Apply Mode (`clean.py apply`)**: Consumes an approved JSON changeset (`[{"row": ..., "header": ..., "value": ...}]`) and applies updates strictly by header name to canonical `Form Responses` sheets, logging per-row audit trails in an `Autofixes` column [^evt-community-events-file-f66a78711977-35bb9a70].
3. **Tooling and Formatting Invariants**: All Drive and Workspace mutations are driven strictly via the `gws` CLI and Python APIs utilizing native Google application formats (`application/vnd.google-apps.*`). Third-party office rendering suites (such as LibreOffice or `soffice`) are strictly prohibited to prevent font substitutions and OOXML corruption [^evt-community-events-file-f66a78711977-35bb9a70].

### Multi-Role Gate Synchronization

Intake records are routed dynamically to downstream role tabs (`Organizers`, `Hosts`, `Speakers`, and `Collaborators`) via formula filters [^evt-community-events-pr-59]:

- **Role Gates Migration**: Filters evaluate independent Yes/No role responses while maintaining backward compatibility with legacy single-choice records [^evt-community-events-pr-59].
- **Defensive Error Wrapping**: Role tab formulas are wrapped with column-presence guards to surface explicit missing column errors rather than silently evaluating to blank sheets [^evt-community-events-pr-59].
- **CRM Sync Alignment**: Reconstructs unified interest metadata from composite multi-role affirmations while preserving reviewer statuses and column alignments across chapter CRM instances [^evt-community-events-pr-59].

# Lifecycle History

- Phase 1 intake data normalization and city extraction workflows established in `skills/aaif-clean-data` [^evt-community-events-file-f66a78711977-35bb9a70].
- Multi-role intake gate migration and `Collaborators` role filtering added in PR #59 [^evt-community-events-pr-59].

[^evt-community-events-file-f66a78711977-35bb9a70]: https://github.com/aaif/community-events/blob/7812e00cb0da0153a9a93f3e19040b1f608a4901/skills/aaif-clean-data/WORKFLOW.md
[^evt-community-events-pr-59]: https://github.com/aaif/community-events/pull/59
