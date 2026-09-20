---
type: skill
title: AAIF Speaker Invite Skill
description: An agent skill for composing concise, peer-to-peer speaker invitation
  messages and direct outreach for AAIF events.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-speaker-invite/SKILL.md
tags:
- skills
- community
- operations
- speakers
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T18:06:33.978077+00:00'
sources:
- id: evt-community-events-file-8035c6f18e40-b8c48319
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-speaker-invite/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T21:34:23-07:00'
---

# Overview
The `aaif-speaker-invite` skill generates concise, peer-to-peer speaker invitation messages (~90 words) tailored for email or direct messaging to prospective AAIF event presenters[^evt-community-events-file-8035c6f18e40-b8c48319].

# Architecture / Specification
The skill formats outreach copy to be builder-to-builder, avoiding corporate tone or marketing jargon while clearly communicating logistics and talk expectations[^evt-community-events-file-8035c6f18e40-b8c48319].

### Structural Elements
- **Logistical Clarity**: Outlines talk duration (e.g., 25 minutes), specific technical topic suggestions, date, city chapter, venue location, expected audience composition, and flexibility on timing[^evt-community-events-file-8035c6f18e40-b8c48319].
- **Voice & Policy**: Emphasizes vendor neutrality, zero sales pitches, and community-driven knowledge sharing[^evt-community-events-file-8035c6f18e40-b8c48319].
- **Input Pipeline**: Retrieves context from event tracker records or coordinates with `../skills/aaif-event-status.md` and `../skills/aaif-triage-intake.md`[^evt-community-events-file-8035c6f18e40-b8c48319].

# References
- `skills/aaif-speaker-invite/SKILL.md` in `aaif/community-events`[^evt-community-events-file-8035c6f18e40-b8c48319].

[^evt-community-events-file-8035c6f18e40-b8c48319]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-speaker-invite/SKILL.md
