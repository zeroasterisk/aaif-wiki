---
type: methodology
title: AAIF Create Chapter Skill
description: Operational agent skill for provisioning, rebranding, geolocating, and
  maintaining AAIF city chapter workspaces and presentation decks.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-create-chapter/SKILL.md
tags:
- methodology
- community
- operations
- skills
- chapters
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T10:12:16.047235+00:00'
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
The `aaif-create-chapter` operational skill automates the creation, rebranding, geolocation, and maintenance of AAIF city chapters across Google Drive workspace templates[^evt-community-events-file-d236c244f6dc-2b1dfa5f]. It clones the canonical `TemplateCity` folder structure—including `Event Tracker.docx`, `Attendee CRM.xlsx`, and event presentation decks—while substituting regional tokens, geolocating slide map markers, and providing batch estate maintenance sweeps[^evt-community-events-file-d236c244f6dc-2b1dfa5f][^evt-community-events-pr-46].

# Architecture / Specification
The provisioning workflow operates through the `gws` command-line interface and Python tooling, strictly utilizing native Google Workspace APIs and byte-level OOXML manipulation rather than third-party desktop office rendering engines[^evt-community-events-file-d236c244f6dc-2b1dfa5f].

## Asset Transformation and Token Replacement
During chapter provisioning, `TemplateCity` files undergo specific token replacements[^evt-community-events-file-d236c244f6dc-2b1dfa5f]:
- **City Names**: Case-matched replacement of `San Francisco` / `SAN FRANCISCO` with the new target city name.
- **Abbreviations**: Replaces `SF` abbreviations in slide decks and document headers with the full city name in title or uppercase format.
- **Luma Slugs**: Generates normalized slugs (`aaif-<slug>`) from lowercase, unaccented city names.
- **File and Folder Paths**: Rebrands filenames (e.g., `San Francisco CRM.xlsx` to `<City> CRM.xlsx`).

## Map Marker Geolocation
The skill updates the "you-are-here" indicator on slide 5 ("THE NETWORK") of `Event Template/Slides.pptx`[^evt-community-events-file-d236c244f6dc-2b1dfa5f]:
- Coordinates are extracted via explicit `--lat`/`--lon` parameters or geocoded via keyless Nominatim lookups.
- Fallback mechanisms preserve the original coordinates with a warning if resolution fails, preventing provisioning failure.

## Chapter Renaming and Estate Sweeps
The skill provides maintenance capabilities across the chapter ecosystem:
- **Chapter Renaming (`rename_chapter.py`)**: Executes in-place renames across Drive folders, CRM workbooks, About documents, and design assets without disrupting live Luma slugs[^evt-community-events-pr-45].
- **Deck Estate Sweeps (`deck_estate.py`, `backfill_projects.py`, `backfill_host_footer.py`)**: Performs bulk multi-file traversals to update host footers and project rosters across all chapter templates, ensuring consistent listing of hosted AAIF projects (`MCP`, `goose`, `AGENTS.md`, `agentgateway`, `A2A`, `Agent Router`)[^evt-community-events-pr-46].
- **Design Conformance**: Validates slide templates against the [AAIF Brand Guidelines](../guidelines/brand-guidelines.md) and WCAG AA contrast standards[^evt-community-events-file-d236c244f6dc-2b1dfa5f].

# Lifecycle History
- PR #45 introduced `rename_chapter.py` for safe four-surface chapter migrations and disconnected Drive grant resolution from Luma provisioning[^evt-community-events-pr-45].
- PR #46 extracted common estate sweep logic into `deck_estate.py` and updated presentation templates across 103 decks to display all six hosted AAIF projects[^evt-community-events-pr-46].

[^evt-community-events-file-d236c244f6dc-2b1dfa5f]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-create-chapter/SKILL.md
[^evt-community-events-pr-45]: https://github.com/aaif/community-events/pull/45
[^evt-community-events-pr-46]: https://github.com/aaif/community-events/pull/46
