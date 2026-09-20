---
type: skill
title: AAIF Attendee Reminder Skill
description: An agent skill for drafting logistics-focused pre-event reminder messages
  to registered attendees of AAIF events.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-attendee-reminder/SKILL.md
tags:
- skills
- community
- operations
- events
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T18:06:33.978077+00:00'
sources:
- id: evt-community-events-file-ede28c6c866a-cf49f096
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-attendee-reminder/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T21:34:23-07:00'
---

# Overview
The `aaif-attendee-reminder` skill generates brief, logistics-first reminder communications (~70 words) distributed to registered attendees approximately one week out and on the morning of an AAIF event[^evt-community-events-file-ede28c6c866a-cf49f096].

# Architecture / Specification
The skill focuses on clear operational details to ensure smooth attendee arrival and accurate attendance tracking[^evt-community-events-file-ede28c6c866a-cf49f096].

### Content Guidelines
- **Logistics Focus**: Leads with confirmed event date, door opening times, venue entry instructions, and speaker topic summary[^evt-community-events-file-ede28c6c866a-cf49f096].
- **Capacity Management**: Explicitly prompts participants to update or release RSVPs if plans change, enabling waitlist fulfillment[^evt-community-events-file-ede28c6c866a-cf49f096].
- **Policy Compliance**: Incorporates standard attendee references to the Linux Foundation Code of Conduct and Privacy Policy while ensuring unannounced private attendee data is omitted[^evt-community-events-file-ede28c6c866a-cf49f096].

# References
- `skills/aaif-attendee-reminder/SKILL.md` in `aaif/community-events`[^evt-community-events-file-ede28c6c866a-cf49f096].

[^evt-community-events-file-ede28c6c866a-cf49f096]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-attendee-reminder/SKILL.md
