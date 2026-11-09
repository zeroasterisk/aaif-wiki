---
type: skill
title: AAIF Event Announcement Post Skill
description: Copy generation skill drafting concise, practitioner-focused LinkedIn
  launch posts for AAIF events under strict privacy redaction and compliance footer
  rules.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-announcement-post/SKILL.md
tags:
- community
- social
- events
- marketing
- privacy
- skills
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:21:20.246093+00:00'
sources:
- id: evt-community-events-file-133151709c55-005d77f9
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-announcement-post/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
---

# Overview
`aaif-announcement-post` is an operational agent skill that drafts scannable, builder-focused LinkedIn announcement posts for AAIF chapter and online events when RSVPs open[^evt-community-events-file-133151709c55-005d77f9]. It enforces a strict public-copy governance rule that strips all non-public attendee personal data, speaker contact details, and venue access codes from output copy and conversational transcripts[^evt-community-events-file-133151709c55-005d77f9].

# Architecture / Specification
The skill consumes structured event metadata retrieved directly from chapter event trackers via `fetch_tracker.py`[^evt-community-events-file-133151709c55-005d77f9].

### Structural Constraints
- **Format**: Composed of a single-line hook, what/when/where logistics, speaker topic with one key takeaway, and an RSVP call-to-action linking to Luma or Gradual.AI[^evt-community-events-file-133151709c55-005d77f9].
- **Length & Style**: Approximately 120 words, at most one emoji, and a maximum of three hashtags, adhering to an authentic "share the practice, never sell the product" house voice[^evt-community-events-file-133151709c55-005d77f9].
- **Mandatory Compliance Footer**: Terminates with a standardized footer referencing the Linux Foundation Code of Conduct and Privacy Policy[^evt-community-events-file-133151709c55-005d77f9].

### Privacy & Data Protection Rules
All event intake records and tracker entries are treated as private data. Contact parameters—such as speaker email addresses, phone numbers, door access codes, and unverified intake names—are withheld by the ingestion utility[^evt-community-events-file-133151709c55-005d77f9]. The agent is explicitly prohibited from echoing withheld values or confirming omitted specifics in conversational responses, mandating that omitted categories be referenced only by field name[^evt-community-events-file-133151709c55-005d77f9].

[^evt-community-events-file-133151709c55-005d77f9]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-announcement-post/SKILL.md
