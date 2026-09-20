---
type: skill
title: Create AAIF Online Series
description: An agent skill for scaffolding new AAIF online event series folders,
  documents, and design assets in Google Drive.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-create-online-series/SKILL.md
tags:
- skill
- community
- events
- automation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:57:33.111839+00:00'
sources:
- id: evt-community-events-file-2e96153bc720-e7b736d6
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-create-online-series/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-08-27T15:52:49-07:00'
---

# Overview

The `aaif-create-online-series` skill provisions new AAIF online event series (such as reading groups, paper clubs, or webinars) under the top-level `Online/` Google Drive directory [^evt-community-events-file-2e96153bc720-e7b736d6]. It acts as the online counterpart to chapter creation, cloning the `TemplateSeries` folder and rebranding all contained assets for non-venue recurring programs [^evt-community-events-file-2e96153bc720-e7b736d6].

# Architecture / Specification

The skill operates under strict tooling and file manipulation constraints [^evt-community-events-file-2e96153bc720-e7b736d6]:
- **Drive Execution Model**: All Google Drive reads, copies, and updates are executed via the `gws` CLI driven through Python [^evt-community-events-file-2e96153bc720-e7b736d6]. Desktop office suites like LibreOffice and `soffice` are prohibited to prevent font substitution and OOXML degradation [^evt-community-events-file-2e96153bc720-e7b736d6].
- **Rebranding Rules**: Performs case-matched token replacement across document content and file names, substituting San Francisco template defaults with series names and Luma slugs (`aaif-<slug>`) [^evt-community-events-file-2e96153bc720-e7b736d6].
- **Artifact Scaffolding**: Seeds an online-oriented `Event Tracker.docx` runbook (covering join links, streaming moderation, and recording workflows instead of venue logistics), `Attendee CRM.xlsx`, and presentation templates [^evt-community-events-file-2e96153bc720-e7b736d6].

# References

- [`skills/aaif-create-event`](../skills/aaif-create-event.md)
- [`skills/aaif-update-event`](../skills/aaif-update-event.md)

[^evt-community-events-file-2e96153bc720-e7b736d6]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-create-online-series/SKILL.md
