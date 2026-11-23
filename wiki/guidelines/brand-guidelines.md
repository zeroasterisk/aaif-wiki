---
type: guideline
title: Brand Guidelines
description: Visual identity standards, design tokens, typography specifications,
  surface constraints, and motif rules governing Agentic AI Foundation digital and
  print artifacts.
resource: https://github.com/aaif/community-events/blob/a411604181e6a15dc2278221bc7501c8bb3c49fc/DESIGN.md
tags:
- design
- brand
- tokens
- typography
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:33:44.152648+00:00'
sources:
- id: evt-community-events-file-3dc5dd454e08-bbae69b7
  resource: https://github.com/aaif/community-events/blob/a411604181e6a15dc2278221bc7501c8bb3c49fc/DESIGN.md
  author: Rahul Parundekar
  last_modified: '2026-11-01T22:38:32-08:00'
---

# Overview

The Agentic AI Foundation (AAIF) brand and design system establishes normative visual presentation rules, typography standards, surface constraints, and graphical motif bounds across foundation reports, digital artifacts, and community assets [^evt-community-events-file-3dc5dd454e08-bbae69b7]. All generated outputs—including HTML operational reports and compiled PDF documents—must strictly conform to the shared design system tokens and layout invariants [^evt-community-events-file-3dc5dd454e08-bbae69b7].

# Architecture / Specification

### Source of Truth and Token Pipeline

The foundational source of truth is `design/aaif-design-system.html`, a self-extracting bundle defining tokens, component specifications, and sample layouts [^evt-community-events-file-3dc5dd454e08-bbae69b7]. The CSS token definitions (`design/aaif-tokens.css`) are generated from this bundle via `scripts/extract_design_tokens.py` and must never be edited manually [^evt-community-events-file-3dc5dd454e08-bbae69b7]. Continuous integration enforces token currency using automated stale-check verification [^evt-community-events-file-3dc5dd454e08-bbae69b7].

### Color Palette and Accents

- **Primary Accent**: The primary action accent is black (`--accent: var(--ink)`) [^evt-community-events-file-3dc5dd454e08-bbae69b7].
- **Spectrum Accents**: Spectrum hues (`--spec-1` through `--spec-10`) serve exclusively as internal accents within an individual surface, with only one hue leading at a time [^evt-community-events-file-3dc5dd454e08-bbae69b7]. Coral is designated as `--spec-8` and is not the organizational brand accent [^evt-community-events-file-3dc5dd454e08-bbae69b7].
- **Surfaces**: Artifacts exist on two first-class surfaces: white editorial and black plate [^evt-community-events-file-3dc5dd454e08-bbae69b7]. General reports utilize the white editorial ground (`--paper`), using `--paper-2` for occasional section banding and `--paper-3` for tinted panels [^evt-community-events-file-3dc5dd454e08-bbae69b7]. Dark mode (`prefers-color-scheme`) is strictly prohibited [^evt-community-events-file-3dc5dd454e08-bbae69b7].

### Typography and Structural Elements

- **Typeface**: Instrument Sans (SIL Open Font License) is the singular typeface across UI and display surfaces in weights 400, 500, 600, and 700 [^evt-community-events-file-3dc5dd454e08-bbae69b7]. Monospace typography is drawn from a system stack and restricted to metadata, labels, and eyebrows [^evt-community-events-file-3dc5dd454e08-bbae69b7].
- **Headings**: Primary headings utilize weight 500, tracking `-0.02em`, and line-height 1.05–1.15; weight 600 is reserved for h5/h6 levels (`--t-xl`/`--t-lg`) [^evt-community-events-file-3dc5dd454e08-bbae69b7].
- **Flat Aesthetic**: Elevation drop shadows are barred; visual separation relies on 1px hairlines, surface tinting, and inset strokes [^evt-community-events-file-3dc5dd454e08-bbae69b7]. Cards, tables, and metric chips maintain square corners (`border-radius: 0`), reserving rounded radii (`--radius-pill`) exclusively for badges and pill buttons [^evt-community-events-file-3dc5dd454e08-bbae69b7].

### Mark Integrity and Agent Motif

- **Logomark SVGs**: The official SVGs (`aaif-mark.svg`, `aaif-mark-square.svg`, and `aaif-logo-white.svg`) must be used directly without redrawing or geometric approximations [^evt-community-events-file-3dc5dd454e08-bbae69b7].
- **Agent Motif**: The robot illustration constructed from logomark primitives is limited to empty states, loading indicators, event collateral, and visual dividers; it is strictly banned from governance, board, or press communications [^evt-community-events-file-3dc5dd454e08-bbae69b7].

# References

- [`../skills/aaif-brand-guidelines.md`](../skills/aaif-brand-guidelines.md)
- [`../skills/community-event-operations.md`](../skills/community-event-operations.md)

[^evt-community-events-file-3dc5dd454e08-bbae69b7]: https://github.com/aaif/community-events/blob/a411604181e6a15dc2278221bc7501c8bb3c49fc/DESIGN.md
