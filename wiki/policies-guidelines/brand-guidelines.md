---
type: guideline
title: Brand Guidelines
description: Visual design, typography, surface tokens, and OOXML asset styling standards
  defining the AAIF brand design system.
resource: https://github.com/aaif/community-events/pull/32
tags:
- branding
- design-tokens
- typography
- guidelines
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:41:45.800159+00:00'
sources:
- id: evt-community-events-pr-32
  resource: https://github.com/aaif/community-events/pull/32
  author: rparundekar
  last_modified: '2026-09-16T17:47:15+00:00'
---

# Overview
The AAIF Brand Guidelines define the visual design language, typographic hierarchy, surface palettes, and asset formatting standards across web, PDF, and office document surfaces [^evt-community-events-pr-32]. The system emphasizes a neutral, minimal, flat design aesthetic with distinct ink ramps and spectrum accents.

# Architecture / Specification
The brand system enforces tokenized styling across HTML, PDF, and OOXML documents (`.pptx`, `.docx`, `.xlsx`) to eliminate manual hex and ad-hoc font drift [^evt-community-events-pr-32].

## Typography
- **Primary / Display / Theme Face**: Instrument Sans serves as the canonical face across presentation decks, word processing documents, and tracking sheets [^evt-community-events-pr-32].
- **Code / Monospace**: Monospace fonts are restricted to structured data and code blocks rather than body copy [^evt-community-events-pr-32].

## Palette and Design Tokens
- **Neutrals**: AAIF ink and line ramp tokens (`--line-2`, `--ink-4`, `--ink-3`) govern borders, metadata text, and secondary copy [^evt-community-events-pr-32].
- **Headers & Plates**: Table and tracker headers utilize black plates with hairline borders rather than arbitrary dark navy fills [^evt-community-events-pr-32].
- **Spectrum Accents**: Status and geographic indicators use tokenized spectrum accents such as `--spec-3` for map markers [^evt-community-events-pr-32].

## Contrast and Legibility Validation
Color applications must undergo automated background-to-foreground contrast resolution checking (shape fill -> slide background -> layout -> master -> white) to prevent illegible token pairings [^evt-community-events-pr-32].

# Lifecycle History
The OOXML estate was conformed to `design/aaif-tokens.css` standards to reconcile office documents and chapter slide decks with web token standards [^evt-community-events-pr-32].

[^evt-community-events-pr-32]: https://github.com/aaif/community-events/pull/32
