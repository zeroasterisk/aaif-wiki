---
type: methodology
title: AAIF Attendee Reminder Skill
description: Operational agent skill for generating logistics-focused pre-event reminder
  notifications sent to registered RSVPs before AAIF events.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-attendee-reminder/SKILL.md
tags:
- aaif
- skills
- community
- events
- notifications
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T10:13:26.839716+00:00'
sources:
- id: evt-community-events-file-ede28c6c866a-cf49f096
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-attendee-reminder/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T21:34:23-07:00'
---

# Overview

The AAIF Attendee Reminder Skill (`aaif-attendee-reminder`) composes concise, logistics-first messages sent to registered attendees approximately one week prior to and on the morning of an AAIF gathering [^evt-community-events-file-ede28c6c866a-cf49f096].

# Architecture / Specification

### Communication Cadence and Rules
- **Length and Tone**: Target ~70 words with direct, logistics-focused instructions [^evt-community-events-file-ede28c6c866a-cf49f096].
- **Key Content Elements**: Door opening time, location and venue access guidance, talk highlights, and an RSVP release call-to-action for waitlist management.
- **Privacy & Entry Details**: Door codes and private entry instructions are described rather than hardcoded in public trackers [^evt-community-events-file-ede28c6c866a-cf49f096].
- **Governance Compliance**: Mandates inclusion of standard references to the [Linux Foundation Code of Conduct](https://events.linuxfoundation.org/about/code-of-conduct) and [Privacy Policy](https://www.linuxfoundation.org/legal/privacy-policy) [^evt-community-events-file-ede28c6c866a-cf49f096], linking to [`../governance/code-of-conduct.md`](../governance/code-of-conduct.md).

[^evt-community-events-file-ede28c6c866a-cf49f096]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-attendee-reminder/SKILL.md
