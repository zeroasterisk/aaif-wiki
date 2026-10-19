---
type: guideline
title: AAIF Brand and Visual Identity Guidelines
description: Visual identity, typography, palette tokens, asset generation, and SVG
  asset usage specifications governing official AAIF brand representations.
resource: https://github.com/aaif/community-events/pull/41
tags:
- brand
- guidelines
- design
- assets
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T11:00:39.514262+00:00'
sources:
- id: evt-community-events-pr-41
  resource: https://github.com/aaif/community-events/pull/41
  author: Suryals
  last_modified: '2026-10-07T19:22:24+00:00'
---

# Overview
The AAIF Brand Guidelines define the visual identity, typography, color palettes, and digital asset usage standards for the Agentic AI Foundation. These specifications ensure consistent visual presentation across documentation, slide decks, event collateral, and community web properties [^evt-community-events-pr-41].

# Architecture / Specification

## Canonical Logo Assets
Official vector assets reside in the central repository `assets/` directory and must be consumed directly by authors and automated generation agents [^evt-community-events-pr-41]:
- `aaif-mark.svg`: Serves as the primary full lockup, containing both the brand symbol and typographic mark despite its shortened filename.
- `aaif-icon.svg`: The standalone brand glyph intended for chapter badges, square icons, and avatars.
- `aaif-wordmark.svg`: Typographic wordmark without the standalone icon.

## Rendering Invariants
- **Never Redraw the Mark**: Agents and human contributors are strictly prohibited from redrawing, vectorizing from screenshots, or approximating the AAIF logo mark; the canonical SVGs must always be sourced directly [^evt-community-events-pr-41].
- **Palette and Typography**: Brand typography and color token tables in `DESIGN.md` establish authoritative values for digital, print, and presentation media [^evt-community-events-pr-41].

# References
- Automated brand tooling: [../skills/aaif-brand-guidelines.md](../skills/aaif-brand-guidelines.md)

[^evt-community-events-pr-41]: https://github.com/aaif/community-events/pull/41
