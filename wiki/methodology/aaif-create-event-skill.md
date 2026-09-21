---
type: methodology
title: AAIF Create Event Skill
description: Operational agent skill for creating AAIF events by cloning template
  tracker sections, calculating phase task schedules, and provisioning Luma event
  pages.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-create-event/SKILL.md
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
- id: evt-community-events-file-4c2672b57ca1-235a67fc
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-create-event/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-08-22T00:44:21-07:00'
---

# Overview
The `aaif-create-event` skill automates the creation and scheduling of new events for AAIF chapters and online series [^evt-community-events-file-4c2672b57ca1-235a67fc]. It clones template sections within Google Drive `Event Tracker.docx` documents, calculates backward-scheduled phase task due dates from the target event date, and prepares live event pages on Luma [^evt-community-events-file-4c2672b57ca1-235a67fc].

# Architecture / Specification
The skill coordinates Google Workspace Drive operations and local OOXML manipulation [^evt-community-events-file-4c2672b57ca1-235a67fc]:
- **Template Ingestion and Cloning**: Locates and downloads the appropriate chapter or online tracker to an ephemeral directory via `gws` [^evt-community-events-file-4c2672b57ca1-235a67fc]. The deterministic script `create_event.py` clones the example event structure (in-person for chapters, online for series) while preventing duplicate titles [^evt-community-events-file-4c2672b57ca1-235a67fc].
- **Cadence Computation**: Automatically calculates every pre-event and post-event phase task due date backward and forward from the target event date, preserving exact template cadence [^evt-community-events-file-4c2672b57ca1-235a67fc].
- **Human Approval Gate for Live Publication**: Conforms to the [Human Approval Gate](../patterns/human-approval-gate.md) pattern by drafting a full proposal for the live Luma event page and creating the live page only upon explicit operator confirmation [^evt-community-events-file-4c2672b57ca1-235a67fc].
- **Format and Privacy Guardrails**: Enforces `gws` and Python-only editing to prevent OOXML degradation from desktop office suites, and mandates temporary workspace storage to avoid committing PII to Git [^evt-community-events-file-4c2672b57ca1-235a67fc].

[^evt-community-events-file-4c2672b57ca1-235a67fc]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-create-event/SKILL.md
