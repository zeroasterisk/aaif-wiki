---
type: skill
title: AAIF Event Status Skill
description: An agent skill for reporting overdue and due-soon chapter and online
  event tasks alongside Luma registration stats.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-event-status/SKILL.md
tags:
- skill
- events
- community
- gws
- luma
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:55:54.344066+00:00'
sources:
- id: evt-community-events-file-2a0ccd906b70-c47bfe51
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-event-status/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-08-22T00:44:21-07:00'
---

# Overview
The `aaif-event-status` skill enables AI agents to inspect task health and registration metrics across AAIF chapters and online event series [^evt-community-events-file-2a0ccd906b70-c47bfe51]. It parses an `Event Tracker.docx` document stored in Google Drive to identify overdue and upcoming tasks grouped by task owner, and retrieves read-only registration statistics from Luma.

# Architecture / Specification
The skill operates under strict tooling and privacy constraints:
- **Execution Model**: Agents drive Google Drive interactions via the `gws` CLI while Python scripts perform deterministic local parsing [^evt-community-events-file-2a0ccd906b70-c47bfe51].
- **Local Processing**: Event tracker documents are downloaded to temporary directories for local parsing and are never committed to version control to prevent organizer and venue PII leakage [^evt-community-events-file-2a0ccd906b70-c47bfe51].
- **Task Categorization**: Status calculations evaluate deadlines relative to the current date, grouping overdue tasks and tasks due within seven days by owner while preserving clock-time day-of tasks [^evt-community-events-file-2a0ccd906b70-c47bfe51].
- **Luma Integration**: Gathers read-only attendance metrics including going, waitlist, and check-in counts for published events [^evt-community-events-file-2a0ccd906b70-c47bfe51].

Related skill definitions include [../specification/agent-skill.md](../specification/agent-skill.md) and event lifecycle tools like [aaif-create-event.md](aaif-create-event.md).

[^evt-community-events-file-2a0ccd906b70-c47bfe51]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-event-status/SKILL.md
