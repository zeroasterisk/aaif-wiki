---
type: skill
title: AAIF Attendee Reminder Skill
description: Operational agent skill drafting concise, logistics-focused attendee
  reminder communications and RSVP updates for AAIF community events under strict
  PII controls.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-attendee-reminder/SKILL.md
tags:
- skills
- community
- operations
- privacy
- events
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T11:01:50.430523+00:00'
sources:
- id: evt-community-events-file-ede28c6c866a-7315ad6e
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-attendee-reminder/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
---

# Overview

The AAIF Attendee Reminder skill (`aaif-attendee-reminder`) guides conversational AI agents in drafting pre-event reminder notices for registered attendees of Agentic AI Foundation community gatherings.[^evt-community-events-file-ede28c6c866a-7315ad6e] Reminders are scheduled approximately one week before an event and the morning of the event, adhering to a concise (~70 words), logistics-first format that highlights date, time, venue entry procedures, and speaker details while prompting recipients to update RSVPs if their attendance plans change.[^evt-community-events-file-ede28c6c866a-7315ad6e]

# Architecture / Specification

## Content and Formatting Standards

The skill enforces an objective, builder-to-builder tone centered on signal rather than promotional metrics.[^evt-community-events-file-ede28c6c866a-7315ad6e] Drafted copy must conclude with a standardized footer referencing the Linux Foundation Code of Conduct and Privacy Policy.[^evt-community-events-file-ede28c6c866a-7315ad6e]

## Public-Copy and Privacy Safeguards

To prevent personal identifiable information (PII) leakage across published channels, the skill enforces strict redaction invariants:[^evt-community-events-file-ede28c6c866a-7315ad6e]
- **Field Redaction**: Contact data such as speaker email addresses, phone numbers, attendee names from intake rosters, and venue door codes are withheld from copy.
- **Descriptive Substitution**: Non-publishable logistics are described abstractly (for example, noting that entry codes are emailed privately by venue managers) rather than printed directly.
- **Transcript Hygiene**: Agents are prohibited from echoing redacted values back to operators, even to explain an omission or confirm data removal.

## Tracker Resolution and Automation

Event logistics are fetched dynamically from chapter tracker sheets using `fetch_tracker.py` from the companion status skill.[^evt-community-events-file-ede28c6c866a-7315ad6e] Queries match exact titles or unique substrings, rejecting ambiguous queries to prevent sending misattributed event notices.[^evt-community-events-file-ede28c6c866a-7315ad6e] All tracker data downloaded to temporary scratch disks is purged following copy generation.

# References

- [Agent Plugin Portability Guidelines](../guidelines/agent-plugin-portability.md)
- [AAIF Backup Skill](./aaif-backup.md)
- [AAIF Check Setup Skill](./aaif-check-setup.md)

[^evt-community-events-file-ede28c6c866a-7315ad6e]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-attendee-reminder/SKILL.md
