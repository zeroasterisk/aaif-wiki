---
type: guideline
title: AAIF Brand Guidelines and Design System
description: Visual identity rules, typography tokens, dual surface palettes, component
  styling, and agent motif usage policies for AAIF assets.
resource: https://github.com/aaif/community-events/blob/a411604181e6a15dc2278221bc7501c8bb3c49fc/DESIGN.md
tags:
- branding
- design-system
- tokens
- typography
- guidelines
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:34:12.987397+00:00'
sources:
- id: evt-community-events-file-3dc5dd454e08-bbae69b7
  resource: https://github.com/aaif/community-events/blob/a411604181e6a15dc2278221bc7501c8bb3c49fc/DESIGN.md
  author: Rahul Parundekar
  last_modified: '2026-11-01T22:38:32-08:00'
---

# Overview
The AAIF Design System defines the visual standards, typographic hierarchy, token extraction architecture, and rendering constraints across human-facing interfaces, generated reports, slide decks, and community assets [^evt-community-events-file-3dc5dd454e08-bbae69b7]. The design system strictly enforces a flat, monochrome-led identity with two distinct surfaces (white editorial and black plate) and explicitly disallows automated dark-mode inversions [^evt-community-events-file-3dc5dd454e08-bbae69b7].

# Architecture / Specification

## Source of Truth and Token Architecture
- **Canonical Bundle**: `design/aaif-design-system.html` serves as the authoritative, self-extracting single source of truth containing design tokens, component specifications, agent motif assets, and reference one-pager layouts [^evt-community-events-file-3dc5dd454e08-bbae69b7].
- **Generated Token File**: `design/aaif-tokens.css` contains the extracted `:root` token declarations consumed verbatim by report-styling scripts (`report_style.py`). It is regenerated using `scripts/extract_design_tokens.py`, and CI enforces freshness using `--check` [^evt-community-events-file-3dc5dd454e08-bbae69b7].
- **Official Assets**: Official vector marks (`assets/aaif-mark.svg`, `assets/aaif-mark-square.svg`, and `assets/aaif-logo-white.svg`) must be used verbatim without redrawing [^evt-community-events-file-3dc5dd454e08-bbae69b7].

## Typographic and Color Rules
- **Typeface**: Instrument Sans (OFL) is the exclusive typeface (weights 400, 500, 600, 700) for both display and interface copy; system monospace is reserved strictly for metadata and eyebrows, never body copy [^evt-community-events-file-3dc5dd454e08-bbae69b7].
- **Heading Metrics**: Headings are set at weight 500 with tracking `-0.02em` and line height between 1.05 and 1.15; bold weights are avoided except for h5/h6 set at weight 600 [^evt-community-events-file-3dc5dd454e08-bbae69b7].
- **Color Roles**: Black (`--accent: var(--ink)`) is the primary action accent; spectrum hues (`--spec-1` through `--spec-10`, e.g., coral as `--spec-8`) serve exclusively as subordinate accents within an individual surface [^evt-community-events-file-3dc5dd454e08-bbae69b7].
- **Flat Surface Depth**: Drop shadows are eliminated entirely. Depth is achieved through 1px hairlines, inset strokes, and paper tinting (`--paper` page ground, `--paper-2` section banding, `--paper-3` tinted panels) [^evt-community-events-file-3dc5dd454e08-bbae69b7]. Cards, statistics, tables, and chips maintain square corners (`border-radius: 0`), reserving rounded pills strictly for standalone badges and buttons [^evt-community-events-file-3dc5dd454e08-bbae69b7].
- **No Dark Mode**: Automated `prefers-color-scheme` overrides are prohibited; components exist exclusively on white editorial or black plate surfaces as explicitly selected by designers [^evt-community-events-file-3dc5dd454e08-bbae69b7].

## Motif Usage Boundaries
- **Agent Motif Restriction**: The agent bot motif derived from mark primitives is designated solely for empty states, loaders, event graphics, and dividers [^evt-community-events-file-3dc5dd454e08-bbae69b7]. It is strictly prohibited from governance, board, press, or audit documentation [^evt-community-events-file-3dc5dd454e08-bbae69b7].

# Lifecycle History
Codified in repository design documentation and synchronized via automated token extraction tooling to ensure consistent styling across Python reporting pipelines and OOXML asset generators [^evt-community-events-file-3dc5dd454e08-bbae69b7].

[^evt-community-events-file-3dc5dd454e08-bbae69b7]: https://github.com/aaif/community-events/blob/a411604181e6a15dc2278221bc7501c8bb3c49fc/DESIGN.md
