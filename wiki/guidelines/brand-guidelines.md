---
type: guideline
title: Brand Guidelines
description: Visual, typographic, palette, and asset specifications governing Agentic
  AI Foundation digital assets, presentation decks, and document rendering pipelines.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-clean-data/WORKFLOW.md
tags:
- guidelines
- branding
- typography
- assets
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:49:29.052987+00:00'
sources:
- id: evt-community-events-file-f66a78711977-a26d3112
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-clean-data/WORKFLOW.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:19:56-07:00'
- id: evt-community-events-file-2e96153bc720-8848e516
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-create-online-series/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
- id: evt-community-events-file-4676d39ff431-bb8c2b01
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-dayof-slides/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
---

# Overview
The Brand Guidelines define visual identity, typographic standards, color palettes, and presentation formats for the Agentic AI Foundation (AAIF). These specifications ensure consistent representation across digital media, open-source repositories, community chapters, and event collateral[^evt-community-events-file-2e96153bc720-8848e516][^evt-community-events-file-4676d39ff431-bb8c2b01].

Adherence to brand specifications extends to automated tooling and document generation pipelines used by agent runtimes such as [Goose](../resources/goose.md) and Claude Desktop[^evt-community-events-file-06572a96a58d-9d2d11f7], preventing font substitution and visual degradation during automated asset assembly[^evt-community-events-file-f66a78711977-a26d3112][^evt-community-events-file-2e96153bc720-8848e516].

# Architecture / Specification

## Presentation and Slide Standards
Event presentation templates (such as the standard AAIF "Day of Event" deck) incorporate fixed, mandatory brand slides alongside modular event-specific slides[^evt-community-events-file-4676d39ff431-bb8c2b01]:
- **Fixed Brand Content**: Core foundational slides—including the "About AAIF" overview and global network metric slides—are designated as fixed brand standards and must not be reworded, reformatted, or omitted during automated deck generation[^evt-community-events-file-4676d39ff431-bb8c2b01].
- **Host Lockups and Sponsoring Attribution**: On title and welcome slides, the `HOSTED BY` banner carries the immutable AAIF organizational lockup[^evt-community-events-file-4676d39ff431-bb8c2b01]. Neighboring logo placeholders (`LOGO 1`, `LOGO 2`) are designated image drop zones for event co-hosts or chapter partners and must never be filled with plain text or replace the primary AAIF lockup[^evt-community-events-file-4676d39ff431-bb8c2b01]. Venue hosts and supporting members are formally credited in prose on dedicated concluding recognition slides[^evt-community-events-file-4676d39ff431-bb8c2b01].

## Asset Integrity and Rendering Constraints
To preserve brand typography and embedded layout fidelity, automated tools and agents managing AAIF collateral must conform to strict document processing rules[^evt-community-events-file-f66a78711977-a26d3112][^evt-community-events-file-2e96153bc720-8848e516]:
- **Prohibition of LibreOffice and Desktop Conversion Tools**: Automated environments must never use LibreOffice (`soffice`), `unoconv`, or generic desktop office suites to edit, convert, or preview AAIF documents[^evt-community-events-file-f66a78711977-a26d3112][^evt-community-events-file-2e96153bc720-8848e516]. These suites routinely substitute local system fallback fonts for official AAIF brand typefaces and discard complex OpenXML (OOXML) structures[^evt-community-events-file-f66a78711977-a26d3112].
- **Native API Rendering**: Document and slide previews must be rendered exclusively through native cloud APIs (such as exporting Google Slides or Docs to PDF/PNG via the `gws` Google Workspace CLI) rather than local headless converters[^evt-community-events-file-f66a78711977-a26d3112].
- **OOXML Structure Preservation**: Modifications to Office files (`.pptx`, `.docx`, `.xlsx`) must be performed using targeted byte-level zip part manipulation so that untouched components and embedded brand fonts remain intact[^evt-community-events-file-f66a78711977-a26d3112].

[^evt-community-events-file-2e96153bc720-8848e516]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-create-online-series/SKILL.md
[^evt-community-events-file-4676d39ff431-bb8c2b01]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-dayof-slides/SKILL.md
[^evt-community-events-file-f66a78711977-a26d3112]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-clean-data/WORKFLOW.md
