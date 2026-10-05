---
type: skill
title: AAIF Luma Event Description Skill
description: Standardized automation skill generating structured, vendor-neutral Luma
  event page descriptions and agendas for community meetups.
resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-luma-description/SKILL.md
tags:
- skills
- community
- events
- luma
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:56:40.298719+00:00'
sources:
- id: evt-community-events-file-a4874490bd2a-eeb8e84e
  resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-luma-description/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-09-30T18:54:05-07:00'
---

# Overview
`aaif-luma-description` is an automation skill for generating public event listing copy on Luma for AAIF community meetups [^evt-community-events-file-a4874490bd2a-eeb8e84e]. It structures event listings into an introduction, topic highlights ("What we'll cover"), target audience ("Who should come"), and a timed agenda within approximately 180 words [^evt-community-events-file-a4874490bd2a-eeb8e84e].

# Architecture / Specification
The skill resolves event data via `fetch_tracker.py` from `../skills/aaif-event-status.md` and applies standardized formatting rules [^evt-community-events-file-a4874490bd2a-eeb8e84e].

### Formatting and Compliance Rules
- **Vendor-Neutral Closing**: Concludes event descriptions with explicit statements reinforcing AAIF's vendor-neutral and builder-first ethos [^evt-community-events-file-a4874490bd2a-eeb8e84e].
- **Standard Governance Footer**: Appends standing links to the Linux Foundation Code of Conduct and Privacy Policy as a footer [^evt-community-events-file-a4874490bd2a-eeb8e84e].
- **Privacy and Data Masking**: Follows the AAIF public-copy rule by withholding unpublishable intake details, private door access codes, and speaker contact info [^evt-community-events-file-a4874490bd2a-eeb8e84e].

[^evt-community-events-file-a4874490bd2a-eeb8e84e]: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-luma-description/SKILL.md
