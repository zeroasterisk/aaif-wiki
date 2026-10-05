---
type: skill
title: AAIF Attendee Reminder Skill
description: Standardized automation skill drafting concise, logistics-focused reminder
  messages for registered event attendees.
resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-attendee-reminder/SKILL.md
tags:
- skills
- community
- events
- automation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:58:42.587132+00:00'
sources:
- id: evt-community-events-file-ede28c6c866a-6a45ddf8
  resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-attendee-reminder/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-09-30T18:54:05-07:00'
---

# Overview
`aaif-attendee-reminder` is an automation skill used by community organizers to generate concise, logistics-first reminder communications sent to RSVP'd attendees approximately one week prior to an event and the morning of the event[^evt-community-events-file-ede28c6c866a-6a45ddf8].

# Architecture / Specification
The skill enforces specific content structure and public disclosure boundaries:
- **Structure and Voice**: Generates short (~70 words) builder-to-builder updates prioritizing event date, time, venue entry instructions, speaker introduction, and a prompt for attendees to release tickets if unable to attend[^evt-community-events-file-ede28c6c866a-6a45ddf8].
- **Standard Footers**: Automatically appends standard Linux Foundation Code of Conduct and Privacy Policy links[^evt-community-events-file-ede28c6c866a-6a45ddf8].
- **Public-Copy Safety Rule**: Redacts private contact details such as speaker emails, direct phone numbers, and venue door codes, describing logistics generically rather than exposing unvetted secrets[^evt-community-events-file-ede28c6c866a-6a45ddf8].
- **Tracker Integration**: Queries chapter event trackers via `fetch_tracker.py` to extract event metadata without exposing private row attributes[^evt-community-events-file-ede28c6c866a-6a45ddf8].

# References
- [`skills/aaif-event-status`](../skills/aaif-event-status.md)
- [`skills/aaif-create-event`](../skills/aaif-create-event.md)
- [`governance/code-of-conduct`](../governance/code-of-conduct.md)

[^evt-community-events-file-ede28c6c866a-6a45ddf8]: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-attendee-reminder/SKILL.md
