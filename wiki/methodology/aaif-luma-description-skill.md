---
type: methodology
title: AAIF Luma Description Skill
description: Operational agent skill for drafting structured Luma event page descriptions
  including audience targeting, agendas, and policy disclosures.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-luma-description/SKILL.md
tags:
- aaif
- skills
- community
- events
- luma
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T10:13:26.839716+00:00'
sources:
- id: evt-community-events-file-a4874490bd2a-52713682
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-luma-description/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T21:34:23-07:00'
---

# Overview

The AAIF Luma Description Skill (`aaif-luma-description`) generates structured copy for event registration listings hosted on Luma [^evt-community-events-file-a4874490bd2a-52713682]. It standardizes event descriptions across chapters to clearly convey technical topics, schedule breakdowns, and community participation rules.

# Architecture / Specification

### Page Structure
The description adheres to an ~180-word layout organized into four standardized blocks [^evt-community-events-file-a4874490bd2a-52713682]:
1. **Introduction**: High-level overview of the event theme.
2. **What We'll Cover**: Keynote speaker topic, deep-dive demos, and discussion areas.
3. **Who Should Come**: Intended engineering profile and relevant technical prerequisites.
4. **Agenda**: Timed run-of-show (doors, introductory remarks, talks, live demos, wrap, and networking).

### Mandatory Boilerplate & Footer
- **Vendor-Neutral Assertion**: Reaffirmation that AAIF events contain no paid slots or vendor pitches [^evt-community-events-file-a4874490bd2a-52713682].
- **Governance Footer**: Mandatory links to the [Linux Foundation Code of Conduct](https://events.linuxfoundation.org/about/code-of-conduct) and [Privacy Policy](https://www.linuxfoundation.org/legal/privacy-policy) [^evt-community-events-file-a4874490bd2a-52713682], referencing [`../governance/code-of-conduct.md`](../governance/code-of-conduct.md).

[^evt-community-events-file-a4874490bd2a-52713682]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-luma-description/SKILL.md
