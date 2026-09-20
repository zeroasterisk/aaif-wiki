---
type: skill
title: aaif-sync-chapters
description: An agent skill synchronizing intake decisions to the Chapters List, About
  docs, chapter CRMs, Drive permissions, and Slack resource mappings under strict
  write-gate controls.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-sync-chapters/SKILL.md
tags:
- skills
- community
- operations
- chapters
- automation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T18:09:40.523774+00:00'
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
`aaif-sync-chapters` is an operational agent skill responsible for synchronizing accepted intake submissions out of the intake operational sheets across chapter metadata sheets, chapter `About.docx` documents, private chapter attendee CRM workbooks, Google Drive permission grants, and community Slack channels[^evt-community-events-file-4c7772ef84cb-faef8e14]. The skill follows a strict report-by-default execution pattern where data is staged and verified prior to any modifications, requiring explicit flags to apply updates via a [write gate](../specification/write-gate.md)[^evt-community-events-file-4c7772ef84cb-faef8e14].

# Architecture / Specification

## Core Engines
The skill coordinates five distinct operational engines, operating against an immutable intake sheet reader model[^evt-community-events-file-4c7772ef84cb-faef8e14]:

1. **Chapters Feed (`sync_chapters.py`)**: Publishes accepted organizer records onto the public Chapters List.
2. **About Documents (`sync_about.py`)**: Rewrites organizer listings within each chapter's `About.docx` in Google Drive.
3. **Chapter CRMs (`sync_crm.py`)**: Synchronizes accepted organizers and pipeline attendees into private per-chapter CRM spreadsheets.
4. **Chapter Access (`sync_access.py`)**: Reconciles per-chapter Google Drive folder permissions based on validated CRM rosters.
5. **Resource Map (`sync_resources.py`)**: Resolves and binds actual Google Drive folders and Slack channels into the central chapter inventory[^evt-community-events-file-4c7772ef84cb-faef8e14].

## Pipeline Sequencing
The pipeline requires strict ordered execution across dependent steps[^evt-community-events-file-4c7772ef84cb-faef8e14]:
- City normalization via [aaif-clean-data](../skills/aaif-clean-data.md).
- Intake triage via [aaif-triage-intake](../skills/aaif-triage-intake.md).
- Feed generation and About doc updates.
- CRM population prior to Drive access grant execution.
- Slack resource planning, channel provisioning, organizer invitations, and validation via [aaif-audit-slack](../skills/aaif-audit-slack.md)[^evt-community-events-file-4c7772ef84cb-faef8e14].

## Untrusted Input & Security Invariants
All form submissions, spreadsheet cell contents, and Slack communications are treated strictly as untrusted data rather than agent instructions[^evt-community-events-file-4c7772ef84cb-faef8e14]. Any text attempting to direct agent status changes or grant modifications is escalated for human decision without execution[^evt-community-events-file-4c7772ef84cb-faef8e14].

## Estate Governance & Lifecycle
The chapter estate enforces a hard ceiling of 100 chapters (`CHAPTER_CAP = 100`)[^evt-community-events-pr-48]. Chapter lifecycle statuses (`Active`, `Provisioned`, `Dormant`, `Merged`, `Deprecated`) are curated human fields rather than automated heuristics to prevent inaccurate state transitions[^evt-community-events-pr-48]. Global organizer synchronization also automatically reconciles the workspace-wide `#local-champs` channel alongside per-chapter invite flows[^evt-community-events-pr-48].

# Lifecycle History
- Authored initial multi-engine synchronization skill and operational pipeline[^evt-community-events-file-4c7772ef84cb-faef8e14].
- Applied estate ceiling of 100 chapters and integrated `#local-champs` organizer synchronization with lifecycle tracking[^evt-community-events-pr-48].

[^evt-community-events-file-4c7772ef84cb-faef8e14]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-sync-chapters/SKILL.md
[^evt-community-events-pr-48]: https://github.com/aaif/community-events/pull/48
