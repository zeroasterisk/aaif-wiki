---
type: skill
title: AAIF Create Chapter Skill
description: Automated chapter provisioning, backfill reconciliation, four-surface
  renaming, and design system styling sweep engine managing AAIF community assets.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-create-chapter/references/design-system-sweep.md
tags:
- skills
- operations
- branding
- automation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T10:54:32.103515+00:00'
sources:
- id: evt-community-events-file-49f05aeb9187-b2c9a601
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-create-chapter/references/design-system-sweep.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:19:56-07:00'
---

# Overview

The `aaif-create-chapter` skill orchestrates the end-to-end lifecycle of local AAIF chapters, spanning Google Drive workspace generation, spreadsheet template instantiation, Luma calendar bindings, and continuous visual design conformance [^evt-community-events-file-49f05aeb9187-b2c9a601]. In addition to provisioning new chapter surfaces, the skill hosts the estate-wide design system sweep engine (`restyle_design_system.py`), which audits and conforms existing presentation decks and CRM workbooks to the foundation's official typography and color standards [^evt-community-events-file-49f05aeb9187-b2c9a601].

# Architecture / Specification

### Design System Sweep Engine (`restyle_design_system.py`)

The styling engine audits and updates assets across Google Drive folders against the AAIF design token definitions [^evt-community-events-file-49f05aeb9187-b2c9a601]:
- **Strict Template Scope Isolation**: The sweep selectively targets files whose filenames explicitly match known templates or chapter CRMs (e.g., `<City> CRM.xlsx`) [^evt-community-events-file-49f05aeb9187-b2c9a601]. Active event decks, organizer drafts, and completed event archives are deliberately skipped and cataloged in the audit report to prevent accidental rebranding of localized assets [^evt-community-events-file-49f05aeb9187-b2c9a601].
- **SpreadsheetML vs. DrawingML Parsing**: Workbook manipulation is constrained to `xl/styles.xml` and theme parts, leaving worksheet values and string tables untouched [^evt-community-events-file-49f05aeb9187-b2c9a601]. The engine accounts for SpreadsheetML syntax requirements (such as 8-digit ARGB hex tokens and explicit `<patternFill>` structures), avoiding the silent styling failures encountered when applying DrawingML rules to spreadsheets [^evt-community-events-file-49f05aeb9187-b2c9a601].
- **Pre-Change Immutable Archiving**: Prior to committing changes over remote files, the engine generates pristine local backups within `backups/restyle-<UTC>/` [^evt-community-events-file-49f05aeb9187-b2c9a601]. Earliest copies are preserved permanently across runs to guarantee reliable rollbacks [^evt-community-events-file-49f05aeb9187-b2c9a601].
- **Visual Contrast Repair and Asset Provisioning**: Includes programmatic WCAG AA legibility analysis against newly applied background plates and dynamically distributes chapter-specific agent art without cross-contaminating template icons [^evt-community-events-file-49f05aeb9187-b2c9a601].

[^evt-community-events-file-49f05aeb9187-b2c9a601]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-create-chapter/references/design-system-sweep.md
