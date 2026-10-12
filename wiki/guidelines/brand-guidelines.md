---
type: guideline
title: Brand Guidelines
description: Visual, typographic, and design asset standards governing Agentic AI
  Foundation digital assets, event collateral, and document typography.
resource: https://github.com/aaif/community-events/pull/34
tags:
- branding
- design
- typography
- guidelines
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T02:59:01.454235+00:00'
sources:
- id: evt-community-events-pr-34
  resource: https://github.com/aaif/community-events/pull/34
  author: rparundekar
  last_modified: '2026-09-16T17:47:07+00:00'
- id: evt-community-events-pr-39
  resource: https://github.com/aaif/community-events/pull/39
  author: rparundekar
  last_modified: '2026-09-16T17:47:06+00:00'
---

# Overview
The AAIF Brand Guidelines govern the visual identity, design tokens, typography, and asset generation standards across foundation documents, online properties, and chapter materials[^evt-community-events-pr-34][^evt-community-events-pr-39]. These standards establish consistent aesthetic constraints, document layout parameters, and deterministic generation rules for community collateral[^evt-community-events-pr-39].

# Architecture / Specification

## Typographic Standards and Font Embedding Policies
Foundation documents and tracking sheets utilize a defined hierarchy combining Instrument Sans for prose and JetBrains Mono for code and tabular metadata[^evt-community-events-pr-34]. For OOXML documents (`.docx`), assets enforce strict embedding rules:
- **Declared, Never Embedded**: JetBrains Mono and Instrument Sans are declared in document styles but deliberately stripped of embedded font binaries (`ox.NEVER_EMBED` policy), avoiding approximately 210 KB per file overhead while relying on native rendering within cloud document environments like Google Docs[^evt-community-events-pr-34].
- **Metric Fallback Embedding**: Fallback fonts such as Manrope are embedded to ensure visual consistency for external readers lacking default access to primary brand typography[^evt-community-events-pr-34].

## Design Tokens and Asset Rendering
Community event badges, chapter icons, and presentation decks derive styling directly from `design/aaif-tokens.css`[^evt-community-events-pr-39]:
- **Color and Palette Tokens**: Renders consume standardized `ink`, `paper`, and `hairline` CSS tokens alongside deterministic per-chapter color palettes[^evt-community-events-pr-39].
- **Renderer Requirements**: Vector and badge rendering pipelines mandate headless Chrome as the approved rendering engine to guarantee deterministic CSS font loading and SVG layout parity[^evt-community-events-pr-39].
- **Asset Placement**: Chapter badges and generated scene artwork are stored in dedicated per-chapter `Badges/` and `Icons/` subfolders within chapter-managed storage environments[^evt-community-events-pr-39].

[^evt-community-events-pr-34]: https://github.com/aaif/community-events/pull/34
[^evt-community-events-pr-39]: https://github.com/aaif/community-events/pull/39
