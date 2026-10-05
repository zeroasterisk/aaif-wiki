---
type: skill
title: AAIF Online Series Provisioning Skill
description: Standardized automation skill provisioning online event series directories
  and rebranding collateral assets from master templates.
resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-create-online-series/SKILL.md
tags:
- skills
- community
- automation
- ooxml
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:55:38.670960+00:00'
sources:
- id: evt-community-events-file-2e96153bc720-02e706ca
  resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-create-online-series/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-09-30T18:54:05-07:00'
---

# Overview

The `aaif-create-online-series` skill provisions recurring AAIF online programs—such as reading groups, paper clubs, and technical webinars—by cloning the `TemplateSeries` folder within Google Drive's top-level `Online/` directory [^evt-community-events-file-2e96153bc720-02e706ca]. It performs byte-level OOXML rebranding on Office files to establish an online-optimized runbook without physical venue overhead [^evt-community-events-file-2e96153bc720-02e706ca].

# Architecture / Specification

## Online Series vs. City Chapters
While in-person chapters created via [`aaif-create-chapter`](./aaif-create-chapter.md) manage venue contracts, A/V logistics, and physical access controls, online series utilize a dedicated runbook focused on virtual platforms, streaming links, technical dry runs, recording pipelines, and chat moderation [^evt-community-events-file-2e96153bc720-02e706ca].

## Rebranding Transformations
The provisioning script modifies specific identity tokens across document zip packages while keeping event content placeholders intact [^evt-community-events-file-2e96153bc720-02e706ca]:
- **Series Name Tokens**: Replaces template tokens (e.g., `San Francisco`, `SAN FRANCISCO`, `SF`) with matching case-preserved series identifiers [^evt-community-events-file-2e96153bc720-02e706ca].
- **Platform Slugs**: Updates Luma URLs and hyperlink targets to the assigned series slug [^evt-community-events-file-2e96153bc720-02e706ca].
- **Asset File Paths**: Renames CRM workbooks, event trackers, and design presentation bundles accordingly [^evt-community-events-file-2e96153bc720-02e706ca].

# References
- [`aaif-create-chapter`](./aaif-create-chapter.md)
- [`aaif-event-status`](./aaif-event-status.md)
- [`brand-guidelines`](../policies-guidelines/brand-guidelines.md)

[^evt-community-events-file-2e96153bc720-02e706ca]: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-create-online-series/SKILL.md
