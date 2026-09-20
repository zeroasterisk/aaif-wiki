---
type: skill
title: aaif-create-chapter
description: An agent skill for provisioning and rebranding AAIF city chapter assets
  in Google Drive and executing estate-wide deck sweeps.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-create-chapter/SKILL.md
tags:
- skills
- chapters
- automation
- google-drive
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T18:05:08.177928+00:00'
sources:
- id: evt-community-events-file-d236c244f6dc-2b1dfa5f
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-create-chapter/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T20:45:19-07:00'
- id: evt-community-events-pr-45
  resource: https://github.com/aaif/community-events/pull/45
  author: rparundekar
  last_modified: '2026-09-16T23:35:39+00:00'
- id: evt-community-events-pr-46
  resource: https://github.com/aaif/community-events/pull/46
  author: rparundekar
  last_modified: '2026-09-17T03:56:24+00:00'
---

# Overview

The `aaif-create-chapter` skill provisions and initializes new AAIF city chapters by cloning the canonical `TemplateCity` Google Drive directory and rebranding all embedded Office and Google Workspace assets [^evt-community-events-file-d236c244f6dc-2b1dfa5f]. The skill automates city-specific token replacements, map coordinate updates, and estate-wide deck sweeps across chapter templates [^evt-community-events-pr-46].

# Architecture / Specification

Chapter provisioning and maintenance operate under strict workspace and tooling constraints [^evt-community-events-file-d236c244f6dc-2b1dfa5f]:

- **Drive Asset Cloner and Rebrander**: Clones `TemplateCity` into `Chapters/<City Name>` and transforms case-matched city names, abbreviations, and Luma slugs across `Event Tracker.docx`, `Attendee CRM.xlsx`, and PowerPoint deck templates [^evt-community-events-file-d236c244f6dc-2b1dfa5f].
- **Geospatial Dot Alignment**: Repositions the network location indicator and tonality label on slide 5 of presentation decks using explicit coordinates or Nominatim geocoding [^evt-community-events-file-d236c244f6dc-2b1dfa5f].
- **Estate Sweeps (`deck_estate.py`)**: Performs automated batch transformations across the template estate, including synchronizing hosted project rosters (MCP, goose, AGENTS.md, agentgateway, A2A, Agent Router) and updating host footer styling without altering chapter-customized wording [^evt-community-events-pr-46].
- **Chapter Rename Utility (`rename_chapter.py`)**: Executes in-place renames across Drive folder names, documents, spreadsheets, and design files while preserving canonical Luma slug bindings [^evt-community-events-pr-45].
- **Tooling Boundary**: Uses the `gws` CLI and native API rendering or OOXML ZIP manipulation exclusively, forbidding desktop suite CLI converters like LibreOffice to preserve visual tokens and embedded fonts [^evt-community-events-file-d236c244f6dc-2b1dfa5f].

# Lifecycle History

- **PR #45**: Added `rename_chapter.py` to handle full chapter renaming and asset token migration across four surfaces [^evt-community-events-pr-45].
- **PR #46**: Modularized estate sweeps into `deck_estate.py` and updated presentation templates across 103 decks to reflect all six AAIF hosted projects [^evt-community-events-pr-46].

# References

- [Agent Skill Specification](../specification/agent-skill.md)
- [Sync Chapters Skill](aaif-sync-chapters.md)

[^evt-community-events-file-d236c244f6dc-2b1dfa5f]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-create-chapter/SKILL.md
[^evt-community-events-pr-45]: https://github.com/aaif/community-events/pull/45
[^evt-community-events-pr-46]: https://github.com/aaif/community-events/pull/46
