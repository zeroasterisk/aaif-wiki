---
type: skill
title: AAIF Event Announcement Post Skill
description: LinkedIn launch copy generation skill enforcing privacy protection, attendee
  disclosure controls, and mandatory Linux Foundation policy footers.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-announcement-post/SKILL.md
tags:
- community-events
- skills
- social-media
- marketing
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:32:18.734209+00:00'
sources:
- id: evt-community-events-file-133151709c55-005d77f9
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-announcement-post/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
---

# Overview
The `aaif-announcement-post` skill drafts LinkedIn announcement posts for AAIF chapter and virtual events when RSVPs open.[^evt-community-events-file-133151709c55-005d77f9] Operating under strict privacy and house voice constraints, the skill generates concise (~120 words), scannable copy structured around a single hook, logistical details (what, when, where), speaker topics with clear takeaways, and a direct call to action linked to official registration platforms such as Luma or Gradual.AI.[^evt-community-events-file-133151709c55-005d77f9]

# Architecture / Specification
The skill enforces editorial constraints, automated tracker retrieval, and mandatory compliance footers:[^evt-community-events-file-133151709c55-005d77f9]

### Editorial and Privacy Invariants
- **House Voice**: Emphasizes practitioner practices over vendor promotional copy, prioritizing specific technical substance and builder-to-builder tone with a maximum of one emoji and three hashtags.[^evt-community-events-file-133151709c55-005d77f9]
- **Public-Copy Rule**: Prohibits the publication of non-public personal details, including email addresses, phone numbers, venue door codes, or attendee names from intake sheets.[^evt-community-events-file-133151709c55-005d77f9] In assistant transcripts and generated drafts, omitted details must be referred to by field name rather than echoing private values.[^evt-community-events-file-133151709c55-005d77f9]
- **Mandatory Policy Footer**: Every published post must terminate with links to the Linux Foundation Code of Conduct (`https://events.linuxfoundation.org/about/code-of-conduct`) and Privacy Policy (`https://www.linuxfoundation.org/legal/privacy-policy`).[^evt-community-events-file-133151709c55-005d77f9]

### Tracker Ingestion
Event details can be parsed from manual user input or automatically fetched from the remote chapter event tracker using `fetch_tracker.py`:[^evt-community-events-file-133151709c55-005d77f9]
```bash
python3 <skill-root>/../aaif-event-status/scripts/fetch_tracker.py "<Chapter or Series>" --event "<Event Title>"
```
The tracker utility resolves Google Drive directories via authenticated `gws` tooling and withholds private venue and speaker contact coordinates at the extraction layer.[^evt-community-events-file-133151709c55-005d77f9]

[^evt-community-events-file-133151709c55-005d77f9]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-announcement-post/SKILL.md
