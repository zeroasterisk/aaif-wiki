---
type: skill
title: AAIF Speaker Bio Skill
description: Standardized skill generating third-person long and one-line speaker
  bios from event tracker entries for AAIF community events.
resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-speaker-bio/SKILL.md
tags:
- skills
- community
- events
- content
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:56:09.400706+00:00'
sources:
- id: evt-community-events-file-64b0f6914598-99abd07b
  resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-speaker-bio/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-09-30T18:54:05-07:00'
---

# Overview
The `aaif-speaker-bio` skill produces standardized speaker bios for AAIF in-person events by extracting verified speaker records from event tracker files and formatting concise, hype-free copy[^evt-community-events-file-64b0f6914598-99abd07b].

# Architecture / Specification
The skill operates under strict editorial and data confidentiality constraints[^evt-community-events-file-64b0f6914598-99abd07b]:

- **Dual-Format Output**: Generates two bio variations for each speaker: a 60–80 word third-person narrative bio and an ultra-concise one-line summary capped at 18 words[^evt-community-events-file-64b0f6914598-99abd07b].
- **House Voice Standards**: Mandates concrete, practitioner-focused language emphasizing engineering lessons, technical specifics, and practical takeaways without superlatives or promotional marketing language[^evt-community-events-file-64b0f6914598-99abd07b].
- **Field Extraction**: Extracts speaker name, role, organization, current technical focus, shipped projects, talk title, and public social handles from the chapter `Event Tracker.docx` using `skills/aaif-event-status/scripts/fetch_tracker.py`[^evt-community-events-file-64b0f6914598-99abd07b].
- **Information Redaction**: Withholds contact information (such as personal email addresses and door access codes) from agent outputs and transcripts to ensure compliance with the public-copy rule[^evt-community-events-file-64b0f6914598-99abd07b].

[^evt-community-events-file-64b0f6914598-99abd07b]: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-speaker-bio/SKILL.md
