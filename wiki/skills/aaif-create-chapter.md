---
type: skill
title: aaif-create-chapter
description: Operational provisioning and lifecycle skill managing TemplateCity cloning,
  OOXML rebrand transformations, map dot repositioning, and four-surface chapter renames.
resource: https://github.com/aaif/community-events/blob/f46c3425e92d63c336889819e21e8af88cc4abff/skills/aaif-create-chapter/SKILL.md
tags:
- community
- operations
- skills
- chapters
- gws
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:33:44.152648+00:00'
sources:
- id: evt-community-events-file-d236c244f6dc-7c3a1e3a
  resource: https://github.com/aaif/community-events/blob/f46c3425e92d63c336889819e21e8af88cc4abff/skills/aaif-create-chapter/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-11-03T13:48:31-08:00'
- id: evt-community-events-file-ec8a86dec4ad-ba23000c
  resource: https://github.com/aaif/community-events/blob/f46c3425e92d63c336889819e21e8af88cc4abff/skills/aaif-create-chapter/references/rename-chapter.md
  author: Rahul Parundekar
  last_modified: '2026-11-03T13:48:31-08:00'
---

# Overview

The `aaif-create-chapter` operational skill provisions new AAIF city chapters within the Google Drive estate by cloning the standard `TemplateCity` directory, performing deterministic string and asset rebranding, recalculating geographic coordinate indicators, and executing multi-surface chapter renames [^evt-community-events-file-d236c244f6dc-7c3a1e3a] [^evt-community-events-file-ec8a86dec4ad-ba23000c].

# Architecture / Specification

### Tooling Invariants and File Handling

All Google Drive operations are mediated strictly through Python calling the `gws` command-line utility [^evt-community-events-file-d236c244f6dc-7c3a1e3a]. File manipulation follows strict format separation:
- Native Google Workspace assets (`application/vnd.google-apps.*`) must be modified via the Google Docs, Sheets, or Slides APIs [^evt-community-events-file-d236c244f6dc-7c3a1e3a].
- Stored Office files (`.docx`, `.pptx`, `.xlsx`) undergo in-memory OOXML zip-part surgery to preserve embedded brand typography and untouched structural elements [^evt-community-events-file-d236c244f6dc-7c3a1e3a].
- Desktop office tooling such as LibreOffice (`soffice`) and `unoconv` are categorically prohibited for rendering or editing because they substitute system fonts and corrupt proprietary OOXML elements [^evt-community-events-file-d236c244f6dc-7c3a1e3a].

### Rebranding Scope and Map Dot Positioning

Chapter creation replaces the template tokens `San Francisco`, `SF` abbreviation variants, Luma slugs (`aaif-<slug>`), and corresponding file/folder labels, leaving event-specific speaker and scheduling placeholders untouched [^evt-community-events-file-d236c244f6dc-7c3a1e3a]. In addition, the skill repositions the network map marker on slide 5 ("THE NETWORK") of `Event Template/Slides.pptx` to the target city's real geographic coordinates via keyless Nominatim lookups or explicit `--lat`/`--lon` arguments [^evt-community-events-file-d236c244f6dc-7c3a1e3a].

### Four-Surface In-Place Chapter Renaming

When renaming an existing chapter via `scripts/rename_chapter.py`, the skill coordinates updates across four decoupled surfaces [^evt-community-events-file-ec8a86dec4ad-ba23000c]:
1. **Chapter Folder**: Top-level directory renaming on Google Drive [^evt-community-events-file-ec8a86dec4ad-ba23000c].
2. **File and Subfolder Names**: Nested file assets and icon directories [^evt-community-events-file-ec8a86dec4ad-ba23000c].
3. **OOXML Text**: Internal text runs inside `.docx`, `.pptx`, and `.xlsx` document parts [^evt-community-events-file-ec8a86dec4ad-ba23000c].
4. **Document Metadata**: Standard OOXML core properties (`docProps`) [^evt-community-events-file-ec8a86dec4ad-ba23000c].

Luma slugs are explicitly decoupled from the city name pass to prevent link breakage on live community pages, relationship files (`.rels`) only receive slug changes, and pre-change assets are archived under `backups/rename-<UTC>/` prior to Drive upload [^evt-community-events-file-ec8a86dec4ad-ba23000c].

# References

- [`../guidelines/brand-guidelines.md`](../guidelines/brand-guidelines.md)
- [`../skills/community-event-operations.md`](../skills/community-event-operations.md)
- [`../skills/aaif-sync.md`](../skills/aaif-sync.md)

[^evt-community-events-file-d236c244f6dc-7c3a1e3a]: https://github.com/aaif/community-events/blob/f46c3425e92d63c336889819e21e8af88cc4abff/skills/aaif-create-chapter/SKILL.md
[^evt-community-events-file-ec8a86dec4ad-ba23000c]: https://github.com/aaif/community-events/blob/f46c3425e92d63c336889819e21e8af88cc4abff/skills/aaif-create-chapter/references/rename-chapter.md
