---
type: skill
title: AAIF Event Status Digest Skill
description: Standardized automation skill providing read-only operational health
  reports, milestone deadline checks, and Luma registration statistics.
resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-event-status/SKILL.md
tags:
- skills
- community
- operations
- telemetry
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:55:38.670960+00:00'
sources:
- id: evt-community-events-file-2a0ccd906b70-3a886c30
  resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-event-status/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-09-30T18:54:05-07:00'
---

# Overview

The `aaif-event-status` skill is a deterministic, read-only operational tool that inspects an AAIF chapter or online series `Event Tracker.docx` to report overdue and upcoming task deadlines [^evt-community-events-file-2a0ccd906b70-3a886c30]. It pairs local timeline evaluation with optional Luma calendar API queries to provide real-time RSVP counts and attendee check-in metrics [^evt-community-events-file-2a0ccd906b70-3a886c30].

# Architecture / Specification

## Tooling and Execution Constraints
- **Google Workspace CLI Integration**: Operates strictly through the `gws` CLI and Python without writing back to Google Drive or Microsoft Office documents [^evt-community-events-file-2a0ccd906b70-3a886c30].
- **Rendering and Fidelity Safeguards**: Disallows desktop office suites or headless renderers such as LibreOffice (`soffice`) and `unoconv` to prevent font substitutions and OOXML corruption [^evt-community-events-file-2a0ccd906b70-3a886c30].

## Operational Workflow
1. **Tracker Retrieval**: Executes `scripts/fetch_tracker.py` to resolve the target Google Drive directory and download `Event Tracker.docx` into a secure `0700` temporary directory [^evt-community-events-file-2a0ccd906b70-3a886c30].
2. **Local Digest Computation**: Runs `scripts/event_status.py` to evaluate task due dates relative to the execution timestamp, grouping overdue items and items due within seven days by owner [^evt-community-events-file-2a0ccd906b70-3a886c30].
3. **Registration Telemetry**: Fetches participant metrics (confirmed, waitlisted, and checked-in attendees) when a Luma event URL is configured [^evt-community-events-file-2a0ccd906b70-3a886c30].

# References
- [`aaif-announcement-post`](./aaif-announcement-post.md)
- [`aaif-create-online-series`](./aaif-create-online-series.md)
- [`aaif-sync-chapters`](./aaif-sync-chapters.md)

[^evt-community-events-file-2a0ccd906b70-3a886c30]: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-event-status/SKILL.md
