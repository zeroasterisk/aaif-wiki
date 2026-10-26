---
type: guideline
title: Brand Guidelines
description: Visual identity rules, typography tokens, dual surface palettes, OOXML
  asset mappings, and contrast constraints governing AAIF community and technical
  materials.
resource: https://github.com/aaif/community-events/pull/32
tags:
- design
- brand
- typography
- tokens
- ooxml
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T10:30:20.733533+00:00'
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

The AAIF Brand Guidelines define the typographic standards, color palette tokens, legibility constraints, and asset formatting rules across digital, printable, and office productivity materials.

The guidelines specify concrete mapping rules for OpenXML (OOXML) documents, ensuring templates and reports rendered in Google Docs or Microsoft Office faithfully implement AAIF design tokens without generating file bloat or legibility failures [^evt-community-events-pr-32] [^evt-community-events-pr-34].

# Architecture / Specification

### Typographic Tokens and Font Embedding Rules

- **Display and Theme Typography**: Instrument Sans serves as the universal display and theme font across slides, documents, and headings [^evt-community-events-pr-32].
- **Monospace Typography**: JetBrains Mono is designated for field labels, table headers, dates, statuses, and code identifiers [^evt-community-events-pr-32] [^evt-community-events-pr-34].
- **Metric Fallback**: Manrope is retained as the sole embedded metric fallback in document packages for external or offline environments lacking local font availability [^evt-community-events-pr-34].
- **Font Embedding Policy (`ox.NEVER_EMBED`)**: For cloud-first formats destined for Google Docs, fonts available natively in the service (Instrument Sans and JetBrains Mono) must be declared in `word/fontTable.xml` but stripped from embedded font payloads (`word/fonts/`). Embedding these fonts imposes ~210KB of unnecessary bloat per document [^evt-community-events-pr-34].

### Palette Remapping in Office Formats

OOXML documents must map legacy Office palettes (`4472C4`, `ED7D31`) to AAIF neutral and spectrum tokens [^evt-community-events-pr-32]:
- **Neutrals**: Map greys and borders to `--line-2`, `--ink-4`, and `--ink-3`.
- **Black Plate**: High-emphasis table headers and slide titles use dark fills with crisp hairline borders.
- **Spectrum Accents**: Highlights and map pins map to spectrum tokens such as `--spec-3`.
- **Role-Aware Application**: Color replacement must distinguish structural context—for example, treating a hex color as a filled background plate in a table header versus a hairline border on table cells [^evt-community-events-pr-32].

### Multi-Layer Contrast Resolution

Token conformance alone cannot guarantee legibility: pairing two valid tokens (e.g., light ink on light backgrounds, or dark ink on black plates) produces unreadable artifacts [^evt-community-events-pr-32]. Automated checks must evaluate effective contrast by traversing drawing layers:
1. Direct shape fill.
2. Slide background property (`<p:bg>`).
3. Slide layout background.
4. Slide master background.
5. Default canvas white.

Text rendering must ensure sufficient luminosity delta against the resolved background before artifacts pass compliance gates [^evt-community-events-pr-32].

# Lifecycle History

- **PR #32**: Defined token remapping, SpreadsheetML ARGB styling, Word font table pruning, and dynamic slide contrast verification for the OOXML estate [^evt-community-events-pr-32].
- **PR #34**: Established the `ox.NEVER_EMBED` rule for cloud-hosted Google Docs environments, declaring monospace typefaces while omitting binary font embeds [^evt-community-events-pr-34].

[^evt-community-events-pr-32]: https://github.com/aaif/community-events/pull/32
[^evt-community-events-pr-34]: https://github.com/aaif/community-events/pull/34
