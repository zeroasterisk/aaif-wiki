---
type: skill
title: AAIF Blog Guidelines Skill
description: Modular agent skill assisting contributors in drafting, reviewing, neutralizing,
  and validating blog submissions against AAIF editorial standards.
resource: https://github.com/aaif/public-agents/pull/4
tags:
- skills
- editorial
- blog
- agents
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:25:05.357203+00:00'
sources:
- id: evt-public-agents-pr-4
  resource: https://github.com/aaif/public-agents/pull/4
  author: steveaaif
  last_modified: '2026-10-02T13:51:20+00:00'
---

# Overview
The `aaif-blog-guidelines` skill is an automated editorial assistant for authors preparing content for the Agentic AI Foundation blog.[^evt-public-agents-pr-4] It evaluates draft text against the standards documented in [Blog Guidelines](../guidelines/blog-guidelines.md), checking language conventions, source citations, and neutrality rules.

# Architecture / Specification
The skill packages verification heuristics and automated linting routines:

- **Stylistic Audits**: Verifies sentence case in titles and headings and enforces US English orthography across draft text.[^evt-public-agents-pr-4]
- **Source Guidance**: Flags unsupported assertions and guides contributors to supply primary-source links for technical claims.[^evt-public-agents-pr-4]
- **Terminology Consistency**: Validates official project and foundation naming conventions, cross-referencing approved foundation entities.[^evt-public-agents-pr-4]
- **Neutrality and Claims Check**: Flags promotional bias or vendor favoritism in accordance with AAIF publishing policies.[^evt-public-agents-pr-4]

# Lifecycle History
- **PR #4 (Open)**: Expanded skill routines to evaluate sentence case, US English conventions, source verification checks, and editorial consistency.[^evt-public-agents-pr-4]

[^evt-public-agents-pr-4]: https://github.com/aaif/public-agents/pull/4
