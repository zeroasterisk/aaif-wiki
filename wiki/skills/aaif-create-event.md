---
type: skill
title: AAIF Create Event
description: Event scheduling and tracker provisioning skill computing backward task
  milestones and staging Luma event creation.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-create-event/SKILL.md
tags:
- skills
- community
- events
- luma
- automation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T10:57:07.430992+00:00'
sources:
- id: evt-community-events-file-4c2672b57ca1-5e9465e1
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-create-event/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
---

# Overview
`aaif-create-event` is an operational agent skill for provisioning upcoming community events within the Agentic AI Foundation (AAIF) chapter and online series infrastructure [^evt-community-events-file-4c2672b57ca1-5e9465e1]. It downloads the target chapter or series `Event Tracker.docx` from Google Drive via the `gws` command-line tool, clones template event milestone sections, computes phase task deadlines backward from the event date, and stages public Luma event creation subject to explicit human approval [^evt-community-events-file-4c2672b57ca1-5e9465e1].

# Architecture / Specification
The skill combines agent orchestration with deterministic local document editing and credentialed API integration [^evt-community-events-file-4c2672b57ca1-5e9465e1]:

- **Tooling Constraints**: Reads and writes to Google Drive are mediated strictly through Python calling the `gws` CLI [^evt-community-events-file-4c2672b57ca1-5e9465e1]. Office Open XML manipulations (.docx) execute at the byte level on local temporary files, preserving fonts and binary structures, while desktop office converters such as LibreOffice are prohibited to prevent document corruption [^evt-community-events-file-4c2672b57ca1-5e9465e1].
- **Tracker Specialization**: The skill dynamically differentiates between in-person chapter trackers (requiring `VENUE` and `LOCATION / CITY` fields) and virtual series trackers (requiring `PLATFORM` and `STREAM / JOIN LINK` fields), aborting loudly if mismatched fields are passed [^evt-community-events-file-4c2672b57ca1-5e9465e1].
- **Timeline Stamping**: Pre-event milestone task due dates are automatically calculated backward from the specified event execution date, maintaining the exact operational cadence defined in the tracker template [^evt-community-events-file-4c2672b57ca1-5e9465e1].
- **Human Approval Gate**: Interfacing with the Luma API requires per-calendar API keys managed securely via macOS Keychain or environment variables. Staging an event on Luma presents the rendered proposal first and only initiates the live push upon explicit confirmation from the human operator, implementing a strict [human approval gate](../patterns/human-approval-gate.md) [^evt-community-events-file-4c2672b57ca1-5e9465e1].

# Lifecycle History
The skill operates alongside [aaif-create-chapter](../skills/aaif-create-chapter.md) and [aaif-create-online-series](../skills/aaif-create-online-series.md), relying on preflight credential verification implemented in [aaif-check-setup](../skills/aaif-check-setup.md) [^evt-community-events-file-4c2672b57ca1-5e9465e1].

# References
- Reference implementation: `skills/aaif-create-event/SKILL.md` [^evt-community-events-file-4c2672b57ca1-5e9465e1]

[^evt-community-events-file-4c2672b57ca1-5e9465e1]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-create-event/SKILL.md
