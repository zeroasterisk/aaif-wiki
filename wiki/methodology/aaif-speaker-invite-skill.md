---
type: methodology
title: AAIF Speaker Invite Skill
description: Operational agent skill for drafting concise, builder-to-builder speaker
  outreach messages and direct inquiries for AAIF events.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-speaker-invite/SKILL.md
tags:
- aaif
- skills
- community
- events
- speakers
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T10:13:26.839716+00:00'
sources:
- id: evt-community-events-file-8035c6f18e40-b8c48319
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-speaker-invite/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T21:34:23-07:00'
---

# Overview

The AAIF Speaker Invite Skill (`aaif-speaker-invite`) automates the creation of short, direct speaker invitation messages for chapter leads engaging potential presenters [^evt-community-events-file-8035c6f18e40-b8c48319]. The skill ensures outreach remains low-friction, concrete, and aligned with AAIF's vendor-neutral ethos.

# Architecture / Specification

### Outreach Guidelines
Invitations target ~90 words formatted for direct message or email delivery [^evt-community-events-file-8035c6f18e40-b8c48319]:
- **Direct Scope**: Clear specification of talk duration (e.g., 25 minutes), preferred topic, venue location, date, and audience profile.
- **Flexibility**: Explicit offer to adjust dates if scheduling conflicts arise.
- **Tone**: Peer-to-peer, conversational engineering voice devoid of corporate sales language or commercial sponsorships.
- **Context Extraction**: Pulls venue, chapter, and capacity details from tracker sheets using [`../methodology/aaif-event-status-skill.md`](../methodology/aaif-event-status-skill.md) [^evt-community-events-file-8035c6f18e40-b8c48319].

[^evt-community-events-file-8035c6f18e40-b8c48319]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-speaker-invite/SKILL.md
