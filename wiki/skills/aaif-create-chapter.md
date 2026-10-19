---
type: skill
title: AAIF Create Chapter Skill
description: Automated chapter provisioning skill cloning TemplateCity Drive assets,
  executing OOXML rebranding, and geocoding map coordinates for new AAIF city locations.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-create-chapter/SKILL.md
tags:
- skills
- community
- automation
- geocoding
- branding
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T11:09:07.266888+00:00'
sources:
- id: evt-community-events-file-d236c244f6dc-0c36b708
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-create-chapter/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
---

# Overview
The `aaif-create-chapter` skill automates the launch and provisioning of new AAIF city chapters within the Foundation's Google Drive infrastructure[^evt-community-events-file-d236c244f6dc-0c36b708]. Operating under the [Community Event Operations](community-event-operations.md) suite, it clones the standard `TemplateCity` directory structure—encompassing event trackers, attendee spreadsheets, and presentation slide templates—and systematically rebrands assets from the San Francisco baseline to the target municipality[^evt-community-events-file-d236c244f6dc-0c36b708].

In addition to text transformations, the skill resolves physical geographic coordinates to reposition visual map markers across presentation decks, ensuring brand compliance without requiring manual design adjustments[^evt-community-events-file-d236c244f6dc-0c36b708].

# Architecture / Specification

## Asset Transformation Pipeline
Chapter creation requires Python 3 and authenticated `gws` CLI access to the Google Drive `Chapters` workspace[^evt-community-events-file-d236c244f6dc-0c36b708]. The engine creates a new chapter folder containing:
- `Event Tracker.docx`
- `Attendee CRM.xlsx`
- `Event Template/` and `Banners (...)/` subdirectories housing design assets (`Slides.pptx`)[^evt-community-events-file-d236c244f6dc-0c36b708].

### Rebranding Substitution Matrix
The provisioning pipeline systematically swaps municipal tokens while isolating template placeholders (such as speaker bios, dates, or neighborhood venues)[^evt-community-events-file-d236c244f6dc-0c36b708]:

| Source Token | Target Replacement | Rules & Context |
|---|---|---|
| `San Francisco` / `SAN FRANCISCO` | Target City Name | Case-matched replacement across text and file names[^evt-community-events-file-d236c244f6dc-0c36b708] |
| `SF` Abbreviation | Full City Name | Converted to uppercase in all-caps headings and title case in body copy[^evt-community-events-file-d236c244f6dc-0c36b708] |
| `aaif-sanfrancisco` | `aaif-<slug>` | Replaces Luma calendar handles and hyperlink URLs[^evt-community-events-file-d236c244f6dc-0c36b708] |
| File / Folder Names | Renamed City Name | Propagates name changes to files such as `<City> CRM.xlsx`[^evt-community-events-file-d236c244f6dc-0c36b708] |

### Map Dot Geocoding
On Slide 5 ("THE NETWORK") of `Event Template/Slides.pptx`, the engine repositions the green "you-are-here" indicator and its `<CITY> · TONIGHT` label[^evt-community-events-file-d236c244f6dc-0c36b708]. Coordinates are derived from CLI parameters (`--lat`/`--lon`) or resolved automatically using Nominatim keyless geocoding[^evt-community-events-file-d236c244f6dc-0c36b708]. If geocoding fails or operates offline, the dot remains at San Francisco with an explicit warning rather than aborting execution[^evt-community-events-file-d236c244f6dc-0c36b708].

## Execution Invariants
- **No Desktop Office Suites**: Office binary manipulation is performed via zip-level OOXML surgery or Google APIs; tools like LibreOffice (`soffice`) are strictly banned to prevent font corruption[^evt-community-events-file-d236c244f6dc-0c36b708].
- **State Recovery**: Supports `--resume` and `--repair-existing` flags to recover cleanly from partial network failures or incomplete Google Drive transfers[^evt-community-events-file-d236c244f6dc-0c36b708].

[^evt-community-events-file-d236c244f6dc-0c36b708]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-create-chapter/SKILL.md
