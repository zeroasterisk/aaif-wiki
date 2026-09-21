---
type: methodology
title: AAIF Event Status Skill
description: Operational agent skill for querying overdue and upcoming tasks and Luma
  registration statistics across AAIF chapter and online series trackers.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-event-status/SKILL.md
tags:
- methodology
- skills
- community-events
- operations
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T10:00:54.879118+00:00'
sources:
- id: evt-community-events-file-2a0ccd906b70-c47bfe51
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-event-status/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-08-22T00:44:21-07:00'
---

# Overview
The `aaif-event-status` skill provides a read-only reporting workflow for Agentic AI Foundation chapter and online series events [^evt-community-events-file-2a0ccd906b70-c47bfe51]. It inspects `Event Tracker.docx` files located in Google Drive to identify overdue and upcoming tasks due within seven days, grouped by owner, and queries live Luma registration counts for published events [^evt-community-events-file-2a0ccd906b70-c47bfe51].

# Architecture / Specification
The skill operates under a strict tooling rule requiring Google Drive interaction through the `gws` command-line interface and local deterministic document parsing via Python [^evt-community-events-file-2a0ccd906b70-c47bfe51]. Desktop office suites like LibreOffice and `unoconv` are explicitly prohibited to prevent font substitutions and OOXML corruption [^evt-community-events-file-2a0ccd906b70-c47bfe51].

The execution flow consists of three stages [^evt-community-events-file-2a0ccd906b70-c47bfe51]:
1. **Tracker Discovery**: Locates the chapter or online series folder under designated Drive parent IDs (`1IQ1K7aVOKUUkxAcfLuNjdETEnmavvtjx` for Chapters or `1g2vHrqDHfh9wBkDJryJIl8wqXA4J-d4i` for Online) and resolves the `Event Tracker.docx` file ID [^evt-community-events-file-2a0ccd906b70-c47bfe51].
2. **Isolated Ingestion**: Downloads the tracker file into a temporary local working directory to protect organizer and speaker data from being committed to source control [^evt-community-events-file-2a0ccd906b70-c47bfe51].
3. **Deterministic Digest & Telemetry**: Executes `event_status.py` against the tracker to evaluate task due dates relative to the current date and queries read-only Luma guest lists (counts for going, waitlist, and checked-in attendees) [^evt-community-events-file-2a0ccd906b70-c47bfe51].

[^evt-community-events-file-2a0ccd906b70-c47bfe51]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-event-status/SKILL.md
