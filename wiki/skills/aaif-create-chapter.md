---
type: skill
title: AAIF Create Chapter Skill
description: Automated city chapter provisioning engine cloning TemplateCity in Google
  Drive and rebranding OOXML and slide assets.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-create-chapter/SKILL.md
tags:
- skills
- operations
- chapters
- google-workspace
- ooxml
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:22:52.144306+00:00'
sources:
- id: evt-community-events-file-d236c244f6dc-0c36b708
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-create-chapter/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
---

# Overview

The `aaif-create-chapter` skill provisions a new city chapter across the Agentic AI Foundation (AAIF) community estate by cloning the standard `TemplateCity` folder in Google Drive and rebranding its core template assets[^evt-community-events-file-d236c244f6dc-0c36b708]. The skill standardizes file rebranding, geocodes geographic coordinates to update slide graphics, and enforces strict manipulation boundaries to prevent Office Open XML (OOXML) corruption.

# Architecture / Specification

## Tooling and Rendering Constraints

The chapter creation engine operates under strict tooling constraints enforced via Python automation and the Google Workspace CLI (`gws`)[^evt-community-events-file-d236c244f6dc-0c36b708]:
- **Native Format Preference:** Edits to Google-native formats (`application/vnd.google-apps.*`) occur directly via Docs, Sheets, and Slides APIs[^evt-community-events-file-d236c244f6dc-0c36b708].
- **Byte-Level OOXML Surgery:** Binary Office files (`.docx`, `.pptx`, `.xlsx`) are unpacked and edited at the ZIP part level to preserve embedded font streams and non-target XML parts[^evt-community-events-file-d236c244f6dc-0c36b708].
- **Prohibition of Desktop Suites:** Headless office tools such as LibreOffice (`soffice`), `unoconv`, or local desktop suites are forbidden for edits and preview rendering, as font substitution corrupts brand typography and discards unhandled OOXML elements[^evt-community-events-file-d236c244f6dc-0c36b708]. Visual inspection requires exporting temporary files through Google APIs or dedicated rendering scripts[^evt-community-events-file-d236c244f6dc-0c36b708].

## Rebranding and Token Substitution

During provisioning, the engine rebrands specific identifier tokens while leaving per-event placeholders (dates, agendas, speaker rosters, and neighborhood markers) untouched for chapter organizers[^evt-community-events-file-d236c244f6dc-0c36b708]:
- `San Francisco` / `SAN FRANCISCO` transforms to the new city name matching case[^evt-community-events-file-d236c244f6dc-0c36b708].
- `SF` abbreviations transform into the full city name in Title Case or uppercase as context dictates[^evt-community-events-file-d236c244f6dc-0c36b708].
- Luma community slugs and hyperlink targets transform from `aaif-sanfrancisco` to `aaif-<slug>`[^evt-community-events-file-d236c244f6dc-0c36b708].
- File and directory names carrying these tokens (such as `Attendee CRM.xlsx`) are identically renamed[^evt-community-events-file-d236c244f6dc-0c36b708].

## Geographic Coordinate Mapping

In addition to text transformations, the skill relocates the graphical "you-are-here" dot and `<CITY> · TONIGHT` callout on slide 5 ("THE NETWORK") of `Event Template/Slides.pptx`[^evt-community-events-file-d236c244f6dc-0c36b708]. The engine maps coordinates derived from manual `--lat`/`--lon` parameters or automated Nominatim geocoding onto the world map projection, falling back to San Francisco with an operator warning if coordinates fail to resolve[^evt-community-events-file-d236c244f6dc-0c36b708].

# Lifecycle History

- Merged into `aaif/community-events` repository under `skills/aaif-create-chapter/SKILL.md` replacing legacy manual prompt documents with automated agent skills[^evt-community-events-file-d236c244f6dc-0c36b708].

[^evt-community-events-file-d236c244f6dc-0c36b708]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-create-chapter/SKILL.md
