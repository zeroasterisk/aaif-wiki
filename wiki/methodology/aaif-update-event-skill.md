---
type: methodology
title: AAIF Update Event Skill
description: Operational agent skill for modifying AAIF event details, recomputing
  task due dates, tracking stale marketing assets, and synchronizing Luma pages.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-update-event/SKILL.md
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
- id: evt-community-events-file-93107e013b3e-73d6f037
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-update-event/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-08-22T00:44:21-07:00'
---

# Overview
The `aaif-update-event` skill manages lifecycle changes for existing AAIF chapter and online series events [^evt-community-events-file-93107e013b3e-73d6f037]. It applies structured edits to detail fields (such as speakers, venue, or capacity), dynamically recomputes all task phase due dates when dates shift, flags downstream marketing assets that have become stale, and syncs updates to Luma [^evt-community-events-file-93107e013b3e-73d6f037].

# Architecture / Specification
The update workflow enforces strict deterministic and safety guarantees [^evt-community-events-file-93107e013b3e-73d6f037]:
- **Deterministic Field and Schedule Updates**: Fetches `Event Tracker.docx` via `gws`, executes `update_event.py` to match exact or unique event titles, updates metadata blocks, and recalculates relative task deadlines when an event date changes [^evt-community-events-file-93107e013b3e-73d6f037].
- **Stale Asset Notification**: Inspects which marketing collateral (such as banners, social posts, Luma covers, and presentation slide decks) are invalidated by speaker, venue, or date adjustments and reports them for subsequent regeneration [^evt-community-events-file-93107e013b3e-73d6f037].
- **Gated Luma Synchronization**: Emits a detailed diff showing proposed changes against live Luma pages and only pushes mutations following explicit operator authorization, adhering to [Human Approval Gate](../patterns/human-approval-gate.md) rules [^evt-community-events-file-93107e013b3e-73d6f037].
- **Data Protection**: Mandates isolated temporary directory handling so that modified documents containing community PII are never committed to repository history [^evt-community-events-file-93107e013b3e-73d6f037].

[^evt-community-events-file-93107e013b3e-73d6f037]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-update-event/SKILL.md
