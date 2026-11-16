---
type: skill
title: aaif-create-chapter
description: Operational provisioning and rebranding skill that creates and renames
  AAIF city chapters, generates customized Drive assets, and renders localized Web
  Banners.
resource: https://github.com/aaif/community-events/pull/65
tags:
- community
- automation
- skills
- provisioning
- google-workspace
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:41:03.714942+00:00'
sources:
- id: evt-community-events-pr-65
  resource: https://github.com/aaif/community-events/pull/65
  author: rparundekar
  last_modified: '2026-11-03T21:50:00+00:00'
---

# Overview
The `aaif-create-chapter` skill automates the operational provisioning, asset replication, and rebranding required when establishing or renaming an Agentic AI Foundation (AAIF) city chapter [^evt-community-events-pr-65]. It clones templated Google Drive estates, rewrites Open Office XML (OOXML) text representations, and ensures graphical chapter collateral—such as square web banners—accurately reflect local chapter nomenclature [^evt-community-events-pr-65].

# Architecture / Specification
The provisioning pipeline operates as a sequence of templating, text substitution, raster rendering, and metadata verification steps [^evt-community-events-pr-65]:

## Asset Rebranding and Template Cloning
When a chapter is initialized, template folders containing presentation decks, sheets, and collateral are cloned. Text modifications to OOXML files replace template placeholders with the official chapter name [^evt-community-events-pr-65].

## Web Banner Generation Pipeline
Because graphical assets store text rasterized into image pixels rather than editable OOXML text runs, `Web Banner.png` cannot be rebranded solely via string replacement [^evt-community-events-pr-65]. Chapter banner generation uses `render_web_banner.py` [^evt-community-events-pr-65]:
- **Slide Source**: Derives the 2000x2000 banner image directly from slide four of the chapter's rebranded presentation deck (`Banners (…)/Square Logo.pptx`) [^evt-community-events-pr-65].
- **Server-Side Rasterization**: Exports the slide via Google Slides native export API (`slides_export.render_slide_png`) without relying on local headless office suites [^evt-community-events-pr-65].
- **Content Verification**: Validates that slide text explicitly matches "AAIF Community Events" concatenated with the exact chapter name before rendering, repeating this check on the drawn output [^evt-community-events-pr-65].
- **Drive Metadata Stamping**: Stamps the uploaded `Web Banner.png` file in Google Drive `appProperties` with the source presentation's `md5Checksum` and chapter name, allowing idempotent re-runs to skip unchanged assets and re-render only when decks change or renames occur [^evt-community-events-pr-65].
- **Failure Handling**: Clean provisioning writes exit with code 2 if banner generation fails; `rename_chapter` invocations exit with code 1 upon banner render failures [^evt-community-events-pr-65].

# Lifecycle History
Previously, binary template copies caused newly created and renamed chapters to retain template city names in their square banners [^evt-community-events-pr-65]. PR #65 introduced dynamic slide export, text validation guards, and Google Drive checksum caching to resolve estate-wide branding inconsistencies [^evt-community-events-pr-65].

# References
- Upstream skill pipeline: [community-event-operations](../skills/community-event-operations.md)
- Diagnostic verification: [aaif-check-setup](../skills/aaif-check-setup.md)

[^evt-community-events-pr-65]: https://github.com/aaif/community-events/pull/65
