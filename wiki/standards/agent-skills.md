---
type: standard
title: Agent Skills Specification
description: Open file-based packaging format and progressive disclosure standard
  for extending AI agents with procedural skills.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/CONTRIBUTING.md
tags:
- agent-skills
- specification
- progressive-disclosure
- prompt-engineering
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T03:22:24.071069+00:00'
sources:
- id: evt-community-events-file-eca12c0a30e2-4eaff5f4
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/CONTRIBUTING.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:20:05-07:00'
---

# Overview
The Agent Skills specification defines a file-based packaging format and progressive disclosure architecture for extending autonomous agents with structured, reusable procedural skills [^evt-community-events-file-eca12c0a30e2-4eaff5f4]. It ensures that agents retrieve concise operational instructions without overwhelming context windows or diluting procedural attention.

Skills are organized into modular directories containing a primary instruction file (`SKILL.md`), optional supplementary references, and automated evaluation harnesses [^evt-community-events-file-eca12c0a30e2-4eaff5f4].

# Architecture / Specification

## Directory Layout
A skill conforms to the standard folder structure [^evt-community-events-file-eca12c0a30e2-4eaff5f4]:
```
skills/<skill-name>/
├── SKILL.md            # Primary procedural spine
├── WORKFLOW.md         # Extended multi-phase procedure (optional)
├── scripts/            # Executable helper scripts and unit tests
└── references/         # Deep contextual documentation loaded on demand
```

## Frontmatter Metadata
Each `SKILL.md` must begin with YAML frontmatter declaring identity, runtime prerequisites, and trigger descriptions [^evt-community-events-file-eca12c0a30e2-4eaff5f4]:
- `name`: Unique identifier matching the skill folder name.
- `description`: Single-line statement detailing both capability and trigger conditions ("Use when asked to...") to facilitate autonomous tool selection.
- `compatibility`: Explicit declaration of required CLI binaries, language runtimes, network access, or credentials.
- `metadata`: Client-specific invocation hints, such as argument placeholders.

## Structural and Sizing Rules
To maintain agent attention during task execution, `SKILL.md` documents adhere to strict constraints [^evt-community-events-file-eca12c0a30e2-4eaff5f4]:
1. **Size Ceilings**: The primary `SKILL.md` must remain under 500 lines and approximately 5,000 tokens. Extended procedures must be relocated to `references/` or `WORKFLOW.md`.
2. **Explicit Progressive Disclosure**: Reference documents in `references/` must begin with an explicit trigger phrase ("Load this when..."), paired with a routing table at the end of `SKILL.md`. Vague directives like "see references for details" are prohibited.
3. **Checklist Formatting**: Multi-phase actions must be formatted as markdown checklists (`- [ ] **Step** — command, then rationale`) rather than dense prose.
4. **Focused Gotchas**: Troubleshooting guidance must be limited to non-obvious failure modes ("gotchas") that agents commonly misunderstand, avoiding explanations of standard programming idioms.

# Lifecycle History
The 500-line and 5,000-token threshold was adopted as an enforceable ceiling within the AAIF community events repository following token-bloat remediation where oversized procedural documents degraded agent routing accuracy [^evt-community-events-file-eca12c0a30e2-4eaff5f4].

[^evt-community-events-file-eca12c0a30e2-4eaff5f4]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/CONTRIBUTING.md
