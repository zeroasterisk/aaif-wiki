---
type: guideline
title: Brand Guidelines
description: Visual identity rules, typography tokens, dual surface palettes, component
  styling, and asset discoverability constraints prohibiting manual redrawing of the
  foundation mark.
resource: https://github.com/aaif/community-events/pull/41
tags:
- brand
- design
- assets
- guideline
- community
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:17:35.329762+00:00'
sources:
- id: evt-community-events-pr-41
  resource: https://github.com/aaif/community-events/pull/41
  author: Suryals
  last_modified: '2026-10-07T19:22:24+00:00'
---

# Overview
The Brand Guidelines establish the visual identity system, typographic scales, color tokens, and asset management rules for the Agentic AI Foundation across documentation, presentations, and community materials [^evt-community-events-pr-41]. The guidelines ensure consistent rendering across human and autonomous agent design workflows [^evt-community-events-pr-41].

# Architecture / Specification

## Asset Discoverability and Inventory
Official brand assets are maintained in repository `assets/` directories and documented within primary design system inventories [^evt-community-events-pr-41]. To prevent autonomous agents and contributors from misidentifying or reconstructing visual marks, inventories must explicitly document asset filenames and functional purposes in top-level specification tables [^evt-community-events-pr-41]:
- `aaif-mark.svg`: Designates the complete foundation lockup despite its filename [^evt-community-events-pr-41].
- Official logo SVGs must be directly reachable via single-hop references from top-level repository specifications [^evt-community-events-pr-41].

## Invariant Rules
- **Never Redraw the Mark**: Contributors and automated agents must never reconstruct, trace, or redraw the AAIF mark from screenshots or raster previews [^evt-community-events-pr-41]. Vector production must source directly from official SVG assets in `assets/` [^evt-community-events-pr-41].
- **Consistent Token Mapping**: Visual assets must adhere to foundation typographic hierarchies, surface palettes, and dual dark/light theme contrast baselines [^evt-community-events-pr-41].

[^evt-community-events-pr-41]: https://github.com/aaif/community-events/pull/41
