---
type: skill
title: Community Event Operations
description: Procedural orchestration pipeline and spreadsheet reconciliation engine
  managing AAIF chapter event intake, role gating, and CRM synchronization.
resource: https://github.com/aaif/community-events/pull/59
tags:
- skill
- operations
- community
- automation
- sheets
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T10:53:12.499283+00:00'
sources:
- id: evt-community-events-pr-59
  resource: https://github.com/aaif/community-events/pull/59
  author: rparundekar
  last_modified: '2026-10-09T18:08:39+00:00'
---

# Overview
Community Event Operations provides automated operational tooling and data reconciliation workflows for AAIF community chapter events, synchronizing participant intake submissions across role-specific tracking sheets and chapter CRMs [^evt-community-events-pr-59]. The pipeline automates the ingestion, filtering, and triage of community submissions while maintaining referential integrity across Google Sheets formulas and external directory integrations [^evt-community-events-pr-59].

# Architecture / Specification
The operations framework manages intake filtering, deduplication, and downstream synchronization across several distinct components:
- **Per-Role Multi-Gate Filtering**: Processes intake responses where applicants answer individual Yes/No questions per role (organizing, speaking, hosting venues, or collaborating) rather than a single selection, permitting applicants to qualify across multiple role tabs simultaneously [^evt-community-events-pr-59].
- **Formula Guards and Migration Integrity**: Employs formula migration tooling (`migrate_intake_role_gates.py`) to safely transition live spreadsheet formulas, injecting explicit guards that emit `MISSING FORM COLUMN: <question>` rather than silently blanking tab rows on column schema alterations [^evt-community-events-pr-59].
- **Role Tab Orchestration**: Routes verified applications into dedicated management tabs (`Organizers`, `Hosts`, `Speakers`, and `Collaborators`), maintaining positional alignment for typed triage status and reviewer columns against append-only formula outputs [^evt-community-events-pr-59].
- **CRM Synchronization Engine**: Reconciles survey interest text and chapter-level tracking rows, rebuilding legacy composite interest fields for downstream CRM parity while enforcing mandatory presence of role gate questions [^evt-community-events-pr-59].

# Lifecycle History
Maintained by community operations maintainers. Updated in PR #59 to replace single-choice interest intake with multi-role Yes/No questions, add the non-synced `Collaborators` role tab on Intake Ops, and implement schema guards across formula filters [^evt-community-events-pr-59].

# References
- [AAIF Community Events PR #59](https://github.com/aaif/community-events/pull/59)
- Relates to [AAIF Create Chapter](../skills/aaif-create-chapter.md)

[^evt-community-events-pr-59]: https://github.com/aaif/community-events/pull/59
