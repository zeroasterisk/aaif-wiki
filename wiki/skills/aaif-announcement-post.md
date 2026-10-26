---
type: skill
title: AAIF Event Announcement Skill
description: LinkedIn launch copy generation skill enforcing privacy protection, attendee
  disclosure controls, and standard community disclaimers.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/README.md
tags:
- aaif
- skills
- social-media
- privacy
- community-events
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T10:55:55.482485+00:00'
sources:
- id: evt-community-events-file-b33563055168-f722dd04
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/README.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:20:05-07:00'
- id: evt-community-events-file-eca12c0a30e2-4eaff5f4
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/CONTRIBUTING.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:20:05-07:00'
- id: evt-community-events-file-133151709c55-005d77f9
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-announcement-post/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
---

# Overview
The `aaif-announcement-post` skill guides AI agents in generating scannable, builder-focused LinkedIn announcement posts when registration opens for AAIF community events[^evt-community-events-file-133151709c55-005d77f9]. It enforces concise structure, typographic style constraints, mandatory governance disclaimers, and rigorous privacy boundaries that prevent the leakage of attendee or organizer personal data[^evt-community-events-file-133151709c55-005d77f9].

# Architecture / Specification
The skill combines automated event data retrieval with deterministic output constraints[^evt-community-events-file-133151709c55-005d77f9]:
- **Input Resolution:** Fetches verified event logistics from chapter tracker documents in Google Drive using `fetch_tracker.py` or extracts details from explicit user prompts[^evt-community-events-file-133151709c55-005d77f9].
- **Copy Structure:** Formats output into an approximately 120-word post comprising a one-line hook, logistical details (what, when, where), speaker highlights with a single core takeaway, and an RSVP call-to-action linking registration platforms like Luma or Gradual.AI[^evt-community-events-file-133151709c55-005d77f9]. Visual decoration is limited to at most one emoji and three hashtags[^evt-community-events-file-133151709c55-005d77f9].
- **Public-Copy Privacy Rule:** Strictly bars publishing private personal details, including email addresses, phone numbers, venue door access codes, and unannounced attendee names[^evt-community-events-file-133151709c55-005d77f9]. Agents are forbidden from echoing private values in conversational transcripts even to explain omissions or request confirmation[^evt-community-events-file-133151709c55-005d77f9].
- **Mandatory Legal Footers:** Enforces inclusion of standard trailing links to the Linux Foundation Code of Conduct and Privacy Policy on all public-facing attendee drafts[^evt-community-events-file-133151709c55-005d77f9].
- **Framework Integration:** Follows the file-based packaging structure defined in [standards/agent-skills](../standards/agent-skills.md) and complements operational coordination in [skills/community-event-operations](../skills/community-event-operations.md).

# Lifecycle History
Merged into the `aaif-events` agent plugin to ensure community marketing conforms to AAIF brand voice, non-commercial peer sharing, and privacy standards[^evt-community-events-file-133151709c55-005d77f9][^evt-community-events-file-eca12c0a30e2-4eaff5f4].

[^evt-community-events-file-133151709c55-005d77f9]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-announcement-post/SKILL.md
[^evt-community-events-file-eca12c0a30e2-4eaff5f4]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/CONTRIBUTING.md
