---
type: skill
title: AAIF Speaker Outreach and Invite Skill
description: Standardized automation skill drafting concise, vendor-neutral speaker
  invitation messages and direct outreach for AAIF events.
resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-speaker-invite/SKILL.md
tags:
- skills
- community
- events
- outreach
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:56:40.298719+00:00'
sources:
- id: evt-community-events-file-8035c6f18e40-cc3d7afd
  resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-speaker-invite/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-09-30T18:54:05-07:00'
---

# Overview
`aaif-speaker-invite` is an automation skill designed to draft concise, builder-to-builder speaker invitation direct messages and emails for in-person AAIF events [^evt-community-events-file-8035c6f18e40-cc3d7afd]. It produces targeted, low-friction asks (~90 words) covering talk topics, session length, event date, venue details, and estimated audience size while maintaining a vendor-neutral tone [^evt-community-events-file-8035c6f18e40-cc3d7afd].

# Architecture / Specification
The skill integrates with the AAIF event tracker utility (`fetch_tracker.py` from `../skills/aaif-event-status.md`) to resolve event details directly from Google Drive without manual copy-pasting [^evt-community-events-file-8035c6f18e40-cc3d7afd].

### Core Safeguards and House Rules
- **Public-Copy Rule**: The skill strictly forbids publishing unredacted personal contact details (such as private emails, phone numbers, or venue door codes) in drafts or agent response transcripts [^evt-community-events-file-8035c6f18e40-cc3d7afd].
- **Voice and Tone**: Emphasizes practical builder experience over product pitches ("share the practice, never sell the product") [^evt-community-events-file-8035c6f18e40-cc3d7afd].
- **Tracker Resolution**: Performs unambiguous substring or keyword lookups (`next`/`latest`) and raises errors on ambiguous event matches [^evt-community-events-file-8035c6f18e40-cc3d7afd].

[^evt-community-events-file-8035c6f18e40-cc3d7afd]: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-speaker-invite/SKILL.md
