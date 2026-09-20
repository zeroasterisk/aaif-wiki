---
type: skill
title: AAIF Update Event Skill
description: An agent skill for updating AAIF event details, recalculating task due
  dates, and flagging stale marketing assets.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-update-event/SKILL.md
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
- id: evt-community-events-file-93107e013b3e-73d6f037
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-update-event/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-08-22T00:44:21-07:00'
---

# Overview
The `aaif-update-event` skill applies structured modifications to existing chapter or online events within `Event Tracker.docx` files [^evt-community-events-file-93107e013b3e-73d6f037]. It updates detail fields, adjusts milestone task schedules when event dates move, and flags stale downstream marketing assets.

# Architecture / Specification
- **Field Mutation**: Matches target events by exact title or unique substring, applying updates to fields such as speakers, venue, platform, or capacity [^evt-community-events-file-93107e013b3e-73d6f037].
- **Schedule Recomputation**: When an event date changes, task deadlines across all planning phases are recalculated relative to the new date while maintaining day-of task times [^evt-community-events-file-93107e013b3e-73d6f037].
- **Asset Invalidation Reporting**: Flags downstream assets (banners, slide decks, social posts, Luma covers) that require regeneration following metadata or date updates without executing unverified overwrites [^evt-community-events-file-93107e013b3e-73d6f037].
- **Luma Sync Gate**: Previews differential updates to Luma event pages and pushes changes only upon explicit user approval, avoiding unsolicited guest email notifications unless specifically requested [^evt-community-events-file-93107e013b3e-73d6f037].

Related skills include [aaif-create-event.md](aaif-create-event.md) and [../specification/human-approval-gate.md](../specification/human-approval-gate.md).

[^evt-community-events-file-93107e013b3e-73d6f037]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-update-event/SKILL.md
