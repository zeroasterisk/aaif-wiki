---
type: governance
title: AAIF Brand Foundation
description: Visual design standards, token specifications, OOXML document styling
  rules, and typography embedding policies for AAIF assets.
resource: https://github.com/aaif/community-events/pull/32
tags:
- governance
- brand
- design-system
- tokens
- typography
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T18:04:33.485834+00:00'
sources:
- id: evt-community-events-pr-32
  resource: https://github.com/aaif/community-events/pull/32
  author: rparundekar
  last_modified: '2026-09-16T17:47:15+00:00'
- id: evt-community-events-pr-34
  resource: https://github.com/aaif/community-events/pull/34
  author: rparundekar
  last_modified: '2026-09-16T17:47:07+00:00'
---

# Overview
The AAIF Brand Foundation defines visual design standards, design tokens, color ramps, and typography rules across web surfaces and Office Open XML (OOXML) estate assets (`.docx`, `.pptx`, `.xlsx`)[^evt-community-events-pr-32][^evt-community-events-pr-34].

# Architecture / Specification

## Token System & Office Document Conformance
Design tokens declared in `design/aaif-tokens.css` are projected into OOXML formats via `ooxml_style.py`, enforcing role-aware application and minimal-diff XML rewrites[^evt-community-events-pr-32]:
- **Typography Tokens**: Instrument Sans is specified for display, headings, and body copy; JetBrains Mono is designated for code, data tables, and structured status fields[^evt-community-events-pr-32][^evt-community-events-pr-34].
- **Color Palette Ramps**: Neutral inks (`--ink-1` through `--ink-4`), hairlines (`--line-1`, `--line-2`), and spectrum accents replace legacy stock office themes[^evt-community-events-pr-32].
- **Contrast & Legibility Verification**: Automated contrast resolution (`contrast.py`) evaluates effective background layers (shape fills, slide backgrounds, master layouts) to ensure accessible pairings and prevent unreadable black-on-black combinations[^evt-community-events-pr-32].

## Font Declaration vs Embedding Policy
To prevent document bloat and formatting degradation, OOXML files enforce a strict font embedding policy[^evt-community-events-pr-34]:
- **Declared, Never Embedded**: Google Fonts natively available in cloud environments (such as Instrument Sans and JetBrains Mono) are declared in `word/fontTable.xml` but stripped from embedded binary payloads (`word/fonts/`)[^evt-community-events-pr-34].
- **Metric Fallbacks**: Portable metric fallbacks (such as Manrope) are selectively embedded to preserve document layout consistency when rendered offline without primary font support[^evt-community-events-pr-34].

# References
- [AAIF Sync Badges Skill](../skills/aaif-sync-badges.md)

[^evt-community-events-pr-32]: https://github.com/aaif/community-events/pull/32
[^evt-community-events-pr-34]: https://github.com/aaif/community-events/pull/34
