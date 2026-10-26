---
type: skill
title: AAIF Online Series Provisioning Skill
description: Automated provisioning skill cloning templates and rebranding Drive assets
  for recurring online programs without physical venues.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/README.md
tags:
- aaif
- skills
- automation
- google-drive
- ooxml
- online-events
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T10:55:55.482485+00:00'
sources:
- id: evt-community-events-file-b33563055168-f722dd04
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/README.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:20:05-07:00'
- id: evt-community-events-file-eca12c0a30e2-4eaff5f4
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/CONTRIBUTING.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:20:05-07:00'
- id: evt-community-events-file-2e96153bc720-8848e516
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-create-online-series/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
---

# Overview
The `aaif-create-online-series` skill automates the creation and asset rebranding of new AAIF online initiatives (such as paper clubs, reading groups, and technical webinars) within Google Drive[^evt-community-events-file-2e96153bc720-8848e516]. Functioning as the virtual counterpart to in-person chapter creation in [skills/aaif-create-chapter](../skills/aaif-create-chapter.md), it clones the master `TemplateSeries` workspace into the dedicated `Online/` folder and rebrands file contents and directory names to match the new series identity[^evt-community-events-file-2e96153bc720-8848e516].

# Architecture / Specification
The provisioning process implements strict asset management and rendering boundaries[^evt-community-events-file-2e96153bc720-8848e516]:
- **Tooling Constraints:** Mandates that all Google Drive reads, writes, and transformations occur exclusively via Python scripting using the `gws` CLI[^evt-community-events-file-2e96153bc720-8848e516]. It explicitly forbids desktop office suites (e.g., LibreOffice or `soffice`) to avoid font substitution and OOXML syntax degradation[^evt-community-events-file-2e96153bc720-8848e516].
- **Asset Bundle Structure:** Provisions an online-specific runbook (`Event Tracker.docx` customized for virtual join links, streaming platforms, tech checks, chat moderation, and recording workflows instead of venue/catering logistics), an `Attendee CRM.xlsx`, and presentation banner decks (`.pptx`)[^evt-community-events-file-2e96153bc720-8848e516].
- **Rebranding Transformations:** Performs case-sensitive token replacement across file content and file names, substituting template placeholders (`San Francisco`, abbreviation `SF`, and Luma slug `aaif-sanfrancisco`) with the new series title and slug[^evt-community-events-file-2e96153bc720-8848e516].
- **Folder Segregation:** Preserves architectural boundaries by placing virtual event programs under `Online/`, strictly separated from physical municipal communities under `Chapters/`[^evt-community-events-file-2e96153bc720-8848e516].

# Lifecycle History
Created to support AAIF virtual working groups and global online series, standardizing asset creation under the unified `aaif-events` plugin architecture[^evt-community-events-file-2e96153bc720-8848e516][^evt-community-events-file-eca12c0a30e2-4eaff5f4].

[^evt-community-events-file-2e96153bc720-8848e516]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-create-online-series/SKILL.md
[^evt-community-events-file-eca12c0a30e2-4eaff5f4]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/CONTRIBUTING.md
