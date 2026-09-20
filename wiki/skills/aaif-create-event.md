---
type: skill
title: AAIF Create Event Skill
description: An agent skill for scaffolding new chapter or online events in Event
  Tracker documents and drafting Luma event listings.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-create-event/SKILL.md
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
- id: evt-community-events-file-4c2672b57ca1-235a67fc
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-create-event/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-08-22T00:44:21-07:00'
---

# Overview
The `aaif-create-event` skill automates the creation and scheduling of new events for AAIF chapters and online series by cloning template sections in `Event Tracker.docx` files and computing task due dates [^evt-community-events-file-4c2672b57ca1-235a67fc]. It also supports staging live event publication on Luma with explicit human confirmation.

# Architecture / Specification
- **Tracker Templating**: Clones the example event block from the relevant chapter (in-person) or series (online) tracker and populates metadata such as title, date, theme, venue/platform, and speakers [^evt-community-events-file-4c2672b57ca1-235a67fc].
- **Cadence Back-Calculation**: Automatically computes phase task due dates backward from the target event date based on template cadences [^evt-community-events-file-4c2672b57ca1-235a67fc].
- **Human-in-the-Loop Luma Creation**: Presents an event creation proposal first and publishes live to Luma only after explicit human confirmation [^evt-community-events-file-4c2672b57ca1-235a67fc], implementing the [../specification/human-approval-gate.md](../specification/human-approval-gate.md) pattern.
- **Tooling Constraints**: Mandates deterministic Python manipulation via `gws` and prohibits desktop office converters to preserve brand fonts and OOXML structure [^evt-community-events-file-4c2672b57ca1-235a67fc].

Related skill concepts include [../specification/agent-skill.md](../specification/agent-skill.md) and [aaif-event-status.md](aaif-event-status.md).

[^evt-community-events-file-4c2672b57ca1-235a67fc]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-create-event/SKILL.md
