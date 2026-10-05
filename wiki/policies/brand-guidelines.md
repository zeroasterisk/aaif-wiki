---
type: guideline
title: Brand Guidelines
description: Visual identity standards, design tokens, typography specifications,
  and document formatting rules for AAIF digital and presentation assets.
resource: https://github.com/aaif/community-events/pull/32
tags:
- branding
- design-tokens
- typography
- guidelines
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:09:46.675799+00:00'
sources:
- id: evt-community-events-pr-32
  resource: https://github.com/aaif/community-events/pull/32
  author: rparundekar
  last_modified: '2026-09-16T17:47:15+00:00'
- id: evt-community-events-pr-46
  resource: https://github.com/aaif/community-events/pull/46
  author: rparundekar
  last_modified: '2026-09-17T03:56:24+00:00'
---

# Overview

The AAIF Brand Guidelines define the visual identity standards, core design tokens, typography specifications, color palettes, and automated compliance rules across all Foundation digital, documentation, and office presentation assets[^evt-community-events-pr-32]. All official publications, community slide templates, and OOXML documents (PowerPoint, Word, Excel) must conform to central design tokens to maintain consistent visual hierarchy, vendor neutrality, and legibility[^evt-community-events-pr-32].

# Architecture / Specification

## Typography
AAIF standardizes typography across web, documentation, and Office/OOXML formats:
- **Primary Typeface**: Instrument Sans is the standard display and theme font across all decks, documents, and tracker body copy, replacing legacy fonts (such as Space Grotesk, Manrope, Arial, JetBrains Mono, and Calibri)[^evt-community-events-pr-32].
- **Embedding and Fallbacks**: While web platforms consume web fonts (such as WOFF2), OOXML document pipelines reconcile `word/fontTable.xml` and prune unreferenced embedded font binaries to avoid artifact bloat and font substitution distortion[^evt-community-events-pr-32].

## Palette and Design Tokens
Visual styling is managed through role-aware design token mappings rather than hardcoded hex values or stock office software defaults[^evt-community-events-pr-32]:
- **Neutrals and Inks**: Neutral styling applies AAIF token scales including `--line-2`, `--ink-4`, and `--ink-3` for borders, secondary copy, and metadata[^evt-community-events-pr-32].
- **Accent Spectrum**: Highlighting and status indicators utilize spectrum tokens such as `--spec-3`[^evt-community-events-pr-32].
- **Plate and Table Formatting**: Dark plate / black plate headers with hairline borders replace legacy navy fills[^evt-community-events-pr-32].
- **Role-Aware Application**: Document automation pipelines distinguish XML color context so that fill tokens and border tokens apply correctly without blind find-and-replace corruptions[^evt-community-events-pr-32].

## Contrast and Legibility Verification
To prevent unreadable asset combinations (such as dark ink on black plates), automated validation checks calculate the rendered fill against underlying background hierarchies (shape fill → slide background → layout → master → canvas white) to enforce strict contrast compliance before asset distribution[^evt-community-events-pr-32].

## Hosted Projects Template Identity
Standard presentation templates (such as chapter About slides) must display the current roster of hosted AAIF projects: `MCP · goose · AGENTS.md · agentgateway · A2A · Agent Router`[^evt-community-events-pr-46]. Template sweeps automatically adjust text bounding boxes and font sizing to maintain visual balance across standardized slides without text collisions or orphaned labels[^evt-community-events-pr-46].

[^evt-community-events-pr-32]: https://github.com/aaif/community-events/pull/32
[^evt-community-events-pr-46]: https://github.com/aaif/community-events/pull/46
