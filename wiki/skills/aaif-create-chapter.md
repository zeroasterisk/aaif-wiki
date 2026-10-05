---
type: skill
title: AAIF Create Chapter
description: Standardized automation skill creating and provisioning new AAIF city
  chapters by cloning TemplateCity and rebranding drive assets.
resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-create-chapter/SKILL.md
tags:
- skills
- community
- automation
- ooxml
- chapters
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:57:03.341179+00:00'
sources:
- id: evt-community-events-file-d236c244f6dc-d6812bc7
  resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-create-chapter/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-09-30T18:54:05-07:00'
- id: evt-community-events-file-ec8a86dec4ad-08c3cbb3
  resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-create-chapter/references/rename-chapter.md
  author: Rahul Parundekar
  last_modified: '2026-09-30T18:54:05-07:00'
---

# Overview
The `aaif-create-chapter` skill provisions new AAIF city chapters in Google Drive by cloning the `TemplateCity` template directory and executing multi-surface asset rebranding.[^evt-community-events-file-d236c244f6dc-d6812bc7] It ensures chapter collateral—including event trackers, attendee CRMs, slide decks, and banner assets—consistently adopts the new chapter's identity, coordinates, and Luma registration targets without manual document manipulation.[^evt-community-events-file-d236c244f6dc-d6812bc7]

# Architecture / Specification
## Tooling and Mutation Strategy
Chapter generation and asset customization enforce strict tooling guardrails:
- **`gws` CLI and Python**: All Drive file discovery, replication, and metadata updates execute via the `gws` Google Workspace CLI driven from Python scripts.[^evt-community-events-file-d236c244f6dc-d6812bc7]
- **Native Formats vs OOXML Surgery**: Native Google Workspace files (`application/vnd.google-apps.*`) are modified using the Docs, Sheets, or Slides APIs. Stored Office files (`.docx`, `.pptx`, `.xlsx`) undergo direct byte-level OOXML surgery on internal zip parts to preserve embedded fonts and untouched structures.[^evt-community-events-file-d236c244f6dc-d6812bc7]
- **Prohibition on Desktop Suites**: Tools like LibreOffice (`soffice`) and `unoconv` are explicitly banned due to font substitution issues and silent dropping of unhandled OOXML attributes.[^evt-community-events-file-d236c244f6dc-d6812bc7] Local preview rendering is delegated to headless API exports.[^evt-community-events-file-d236c244f6dc-d6812bc7]

## Rebranding and Token Substitution
Chapter cloning replaces template placeholders while preserving event-specific fillable fields (dates, speakers, agenda placeholders):[^evt-community-events-file-d236c244f6dc-d6812bc7]
- **City Names**: Replaces `San Francisco` / `SAN FRANCISCO` with the new target city name, preserving casing.[^evt-community-events-file-d236c244f6dc-d6812bc7]
- **Abbreviations**: Replaces `SF` tokens with full city name casing appropriate to the context.[^evt-community-events-file-d236c244f6dc-d6812bc7]
- **Luma Slugs**: Rewrites `aaif-sanfrancisco` URLs and link references to `aaif-<slug>` according to slug conventions.[^evt-community-events-file-d236c244f6dc-d6812bc7]
- **Map Dot Positioning**: Repositions the network location indicator dot and `<CITY> · TONIGHT` marker on slide 5 of `Event Template/Slides.pptx` using geocoded latitude/longitude coordinates.[^evt-community-events-file-d236c244f6dc-d6812bc7]

## Chapter Renaming Protocol
In-place chapter renames are executed across four distinct operational surfaces via `rename_chapter.py`:[^evt-community-events-file-ec8a86dec4ad-08c3cbb3]
1. The Google Drive chapter folder name.[^evt-community-events-file-ec8a86dec4ad-08c3cbb3]
2. File and subfolder filenames.[^evt-community-events-file-ec8a86dec4ad-08c3cbb3]
3. OOXML text within `.docx`, `.pptx`, and `.xlsx` archives.[^evt-community-events-file-ec8a86dec4ad-08c3cbb3]
4. Document metadata properties (`docProps`).[^evt-community-events-file-ec8a86dec4ad-08c3cbb3]

To protect live registrations, Luma slugs are decoupled from name changes and are only updated if explicitly requested with `--slug-from` and `--slug-to` flags.[^evt-community-events-file-ec8a86dec4ad-08c3cbb3] Relationship parts (`.rels`) only receive slug mutations to prevent dangling relationship corruption.[^evt-community-events-file-ec8a86dec4ad-08c3cbb3]

[^evt-community-events-file-d236c244f6dc-d6812bc7]: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-create-chapter/SKILL.md
[^evt-community-events-file-ec8a86dec4ad-08c3cbb3]: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-create-chapter/references/rename-chapter.md
