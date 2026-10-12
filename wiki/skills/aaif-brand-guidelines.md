---
type: skill
title: AAIF Brand Guidelines Skill
description: Modular agent skill packaging AAIF visual, typographic, copy tone, and
  governance standards for automated asset and document generation.
resource: https://github.com/aaif/public-agents/blob/fcc3ebc4db293e01305373fc9c2f2c46845ee015/skills/aaif-brand-guidelines/SKILL.md
tags:
- skills
- branding
- guidelines
- agent-skills
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T02:35:06.639694+00:00'
sources:
- id: evt-public-agents-file-3a3a326b4277-185cd03b
  resource: https://github.com/aaif/public-agents/blob/fcc3ebc4db293e01305373fc9c2f2c46845ee015/skills/aaif-brand-guidelines/SKILL.md
  author: Angie Jones
  last_modified: '2026-05-06T19:20:16-05:00'
- id: evt-public-agents-pr-1
  resource: https://github.com/aaif/public-agents/pull/1
  author: angiejones
  last_modified: '2026-05-08T07:26:31+00:00'
- id: evt-public-agents-file-4d647326e823-2a94f808
  resource: https://github.com/aaif/public-agents/blob/fcc3ebc4db293e01305373fc9c2f2c46845ee015/skills/README.md
  author: Angie Jones
  last_modified: '2026-05-06T19:20:16-05:00'
---

# Overview

The `aaif-brand-guidelines` skill is a modular instruction package that applies Agentic AI Foundation visual, copy, and governance standards to automated agent workflows.[^evt-public-agents-file-3a3a326b4277-185cd03b] Packaged according to the open [agent skills standard](../standards/agent-skills.md), the skill instructs agents on formatting presentations, documentation, web designs, social graphics, and marketing materials without diluting foundation neutrality.[^evt-public-agents-file-3a3a326b4277-185cd03b]

Hosted within the AAIF [public agent skills catalog](../resources/public-agent-skills.md), the skill is structured for runtime discovery and dynamic loading by general-purpose agent runtimes such as [Goose](../resources/goose.md), Claude Code, Codex, and Gemini.[^evt-public-agents-file-4d647326e823-2a94f808]

# Architecture / Specification

### Packaging and Metadata

The skill resides in `skills/aaif-brand-guidelines/SKILL.md` within the `aaif/public-agents` repository and is authored by Angie Jones.[^evt-public-agents-file-3a3a326b4277-185cd03b] Frontmatter metadata identifies the package:

- `name`: `aaif-brand-guidelines`
- `organization`: `AAIF`
- `version`: `1.0`

### Core Brand Tenets

The skill enforces three foundational pillars aligning with the core [brand guidelines](../guidelines/brand-guidelines.md):[^evt-public-agents-file-3a3a326b4277-185cd03b]

1. **Neutrality**: Ensures generated designs and copy avoid implying ownership or governance by any single vendor or platform. It instructs agents to prefer balanced layouts, open standards framing, and transparent language over promotional hype.[^evt-public-agents-file-3a3a326b4277-185cd03b]
2. **Collaboration**: Directs content generation toward shared ecosystem initiatives, open standards, and cross-industry cooperation, deprecating hero-centric or siloed positioning.[^evt-public-agents-file-3a3a326b4277-185cd03b]
3. **Trustworthiness**: Leverages Linux Foundation governance credibility through clean, high-contrast visual compositions, grounded claims, and strict typography rules.[^evt-public-agents-file-3a3a326b4277-185cd03b]

### Style Rules and Execution Gates

- **Color Constraints**: Mandates a primary palette anchored by White (`#ffffff`) and Black (`#000000`) for high-contrast accessibility.[^evt-public-agents-file-3a3a326b4277-185cd03b]
- **Copy Tone**: Requires direct, factual, and ecosystem-oriented phrasing, rejecting speculative claims or aggressive marketing tactics.[^evt-public-agents-file-3a3a326b4277-185cd03b]
- **Distribution**: Distributable globally or on a per-project basis via the `skills` CLI using `npx skills add aaif/public-agents --skill aaif-brand-guidelines`.[^evt-public-agents-file-4d647326e823-2a94f808]

# References

- Skill Implementation: `skills/aaif-brand-guidelines/SKILL.md` in `aaif/public-agents` [^evt-public-agents-file-3a3a326b4277-185cd03b]
- Packaging Manifest: `skills/README.md` in `aaif/public-agents` [^evt-public-agents-file-4d647326e823-2a94f808]
- Ingestion Pull Request: PR#1 in `aaif/public-agents` [^evt-public-agents-pr-1]

[^evt-public-agents-file-3a3a326b4277-185cd03b]: https://github.com/aaif/public-agents/blob/fcc3ebc4db293e01305373fc9c2f2c46845ee015/skills/aaif-brand-guidelines/SKILL.md
[^evt-public-agents-file-4d647326e823-2a94f808]: https://github.com/aaif/public-agents/blob/fcc3ebc4db293e01305373fc9c2f2c46845ee015/skills/README.md
[^evt-public-agents-pr-1]: https://github.com/aaif/public-agents/pull/1
