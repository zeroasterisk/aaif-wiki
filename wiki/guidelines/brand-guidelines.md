---
type: guidelines
title: AAIF Brand Guidelines
description: Design system specifications, typography rules, color tokens, and asset
  usage policies for AAIF visual identity across web and OOXML office documents.
resource: https://github.com/aaif/community-events/pull/32
tags:
- branding
- design-system
- tokens
- typography
- ooxml
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T10:11:27.774715+00:00'
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

The AAIF Brand Guidelines establish the visual identity, typography, color tokens, and layout standards for all official Agentic AI Foundation materials[^evt-community-events-pr-32]. These rules apply across digital properties, marketing collateral, presentation decks (`.pptx`), documents (`.docx`), and spreadsheets (`.xlsx`)[^evt-community-events-pr-32].

# Architecture / Specification

### Typography & Font Embedding
- **Display & Body Face**: Instrument Sans is the primary typeface across both prose and presentation decks[^evt-community-events-pr-32].
- **Monospace Face**: JetBrains Mono is designated for code runs, table headers, labels, and structured metadata[^evt-community-events-pr-32][^evt-community-events-pr-34].
- **Metric Fallback**: Manrope serves as the embedded metric fallback for environments lacking native Instrument Sans support[^evt-community-events-pr-34].
- **OOXML Font Policy (`ox.NEVER_EMBED`)**: To avoid document bloat, web-native Google Fonts like Instrument Sans and JetBrains Mono are declared in OOXML font tables but **never embedded**, saving ~210KB per document while rendering correctly in cloud editors[^evt-community-events-pr-34].

### Palette Tokens & Semantic Color Roles
- **Palette**: Colors derive directly from `design/aaif-tokens.css` neutrals and spectrum tokens (`--line-2`, `--ink-4`, `--ink-3`, `--spec-3`), replacing default stock office palettes[^evt-community-events-pr-32].
- **Context-Aware Role Mapping**: Dark neutral fills (e.g., black plate `#1e2761` mapping) are used for table headers, paired with hairline borders rather than raw fill replacements[^evt-community-events-pr-32].
- **Legibility Verification**: Automated contrast analysis verifies that foreground ink tokens and background container fills meet strict readability thresholds across all slide layouts and document tables[^evt-community-events-pr-32].

# Lifecycle History

PR #32 conformed the entire OOXML document estate to the AAIF design tokens[^evt-community-events-pr-32], and PR #34 codified the `ox.NEVER_EMBED` rule for monospace typefaces[^evt-community-events-pr-34].

[^evt-community-events-pr-32]: https://github.com/aaif/community-events/pull/32
[^evt-community-events-pr-34]: https://github.com/aaif/community-events/pull/34
