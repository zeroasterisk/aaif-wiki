---
type: methodology
title: AAIF Sync Chapters Skill
description: Operational agent skill for synchronizing intake decisions across the
  chapters list, About documents, chapter CRMs, Drive permissions, and Slack channels
  under strict approval gates.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-sync-chapters/SKILL.md
tags:
- community
- operations
- skills
- chapters
- slack
- drive
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T10:16:41.484339+00:00'
sources:
- id: evt-community-events-file-4c7772ef84cb-faef8e14
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-sync-chapters/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-09-18T22:54:53-07:00'
- id: evt-community-events-pr-48
  resource: https://github.com/aaif/community-events/pull/48
  author: rparundekar
  last_modified: '2026-09-19T21:54:57+00:00'
---

# Overview
The `aaif-sync-chapters` operational agent skill orchestrates multi-phase synchronization of community intake decisions across public chapter lists, individual chapter `About.docx` documents, private attendee CRMs, Google Drive folder access grants, and Slack channels[^evt-community-events-file-4c7772ef84cb-faef8e14]. Operating under strict guardrails, the skill reads data from the intake sheet without mutating intake source rows directly, runs in reporting and proposal mode by default, and only executes write operations upon explicit human confirmation[^evt-community-events-file-4c7772ef84cb-faef8e14].

# Architecture / Specification

### Synchronization Engines
The synchronization pipeline executes across five distinct engines in strict dependency order[^evt-community-events-file-4c7772ef84cb-faef8e14]:
1. **Chapters Feed (`sync_chapters.py`)**: Pushes accepted organizer names into the public Chapters List sheet.
2. **About Docs (`sync_about.py`)**: Pushes accepted organizer names into each chapter folder's `About.docx`.
3. **Chapter CRMs (`sync_crm.py`)**: Pushes accepted and pipeline members along with survey interest data into each chapter's private CRM spreadsheet (`<City> CRM.xlsx`).
4. **Chapter Access (`sync_access.py`)**: Applies per-chapter Google Drive grants to chapter folders.
5. **Resource Map (`sync_resources.py`)**: Populates Drive folder links and Slack channel identifiers in the Chapters List resource columns.

### Execution Lifecycle and Pipeline Dependencies
The complete operational loop follows a sequential dependency chain where each step reports before writing[^evt-community-events-file-4c7772ef84cb-faef8e14]:
- [AAIF Clean Data Skill](../methodology/aaif-clean-data-skill.md) resolves city names before downstream consumption.
- [AAIF Triage Intake Skill](../methodology/aaif-triage-intake-skill.md) gates decisions so only accepted candidates flow to provisioning.
- Channel provisioning (`provision_channels.py`) renames before creating channels, seeds operational staff into organizer rooms, and pins chapter Drive folder links[^evt-community-events-file-4c7772ef84cb-faef8e14].
- Organizers are invited via `invite_organizers.py` only after target channels exist, maintaining synchronization with workspace-wide leadership rooms like `#local-champs`[^evt-community-events-pr-48].
- Post-run verification is performed independently via [AAIF Audit Slack Skill](../methodology/aaif-audit-slack-skill.md)[^evt-community-events-file-4c7772ef84cb-faef8e14].

### Estate Lifecycle and Capacity Limits
The chapter estate is capped at a maximum of 100 chapters (`CHAPTER_CAP = 100`)[^evt-community-events-pr-48]. Chapters follow a defined lifecycle tracked via a human-assigned `Status` column (Active, Provisioned, Dormant, Merged, Deprecated) paired with a `Merged Into` tracking column[^evt-community-events-pr-48].

### Untrusted Input Handling
All form responses, spreadsheet cell values, and Slack messages are treated strictly as data rather than executable instructions[^evt-community-events-file-4c7772ef84cb-faef8e14]. Directives or prompt injection attempts in intake responses requesting automated status changes or permission escalations are surfaced to operators as review flags without automated execution[^evt-community-events-file-4c7772ef84cb-faef8e14].

# Lifecycle History
- 2026-09-18: PR #48 established the 100-chapter ceiling, formalized the chapter lifecycle status values, and aligned `#local-champs` membership with accepted organizers[^evt-community-events-pr-48].

[^evt-community-events-file-4c7772ef84cb-faef8e14]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-sync-chapters/SKILL.md
[^evt-community-events-pr-48]: https://github.com/aaif/community-events/pull/48
