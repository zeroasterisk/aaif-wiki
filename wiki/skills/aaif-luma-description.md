---
type: skill
title: AAIF Luma Description Skill
description: An agent skill for generating structured Luma event page copy, agendas,
  and target audience descriptions for AAIF events.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-luma-description/SKILL.md
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
- id: evt-community-events-file-a4874490bd2a-52713682
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-luma-description/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T21:34:23-07:00'
---

# Overview
The `aaif-luma-description` skill formats comprehensive event page descriptions (~180 words) for AAIF chapter events published on Luma[^evt-community-events-file-a4874490bd2a-52713682].

# Architecture / Specification
The skill organizes event registration copy into a standardized, scannable format that outlines the session theme, agenda, and participant prerequisites while enforcing foundation governance policies[^evt-community-events-file-a4874490bd2a-52713682].

### Structure & Sections
- **Overview & What We'll Cover**: Summarizes core technical presentations and interactive demo segments[^evt-community-events-file-a4874490bd2a-52713682].
- **Who Should Come**: Specifies relevant practitioner profiles and prerequisites for attending engineers[^evt-community-events-file-a4874490bd2a-52713682].
- **Agenda Breakdown**: Details time-slotted run-of-show schedules from doors open to social wrap-up[^evt-community-events-file-a4874490bd2a-52713682].
- **Mandatory Disclosures**: Appends closing statements highlighting vendor-neutrality and embeds standard links to the Linux Foundation Code of Conduct and Privacy Policy[^evt-community-events-file-a4874490bd2a-52713682].

# References
- `skills/aaif-luma-description/SKILL.md` in `aaif/community-events`[^evt-community-events-file-a4874490bd2a-52713682].

[^evt-community-events-file-a4874490bd2a-52713682]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-luma-description/SKILL.md
