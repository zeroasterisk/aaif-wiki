---
type: skill
title: AAIF Blog Guidelines Skill
description: Modular agent skill assisting contributors in drafting, validating, and
  packaging vendor-neutral blog posts according to AAIF editorial standards.
resource: https://github.com/aaif/public-agents/pull/4
tags:
- skill
- editorial
- guidelines
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T03:15:15.871817+00:00'
sources:
- id: evt-public-agents-pr-4
  resource: https://github.com/aaif/public-agents/pull/4
  author: steveaaif
  last_modified: '2026-10-02T13:51:20+00:00'
---

# Overview
The AAIF Blog Guidelines skill is a modular agent skill designed to guide technical contributors through authoring, linting, and submitting articles for publication on the Agentic AI Foundation blog.[^evt-public-agents-pr-4] It encodes organizational publication guidelines into automated drafting assistants and validation checks.[^evt-public-agents-pr-4]

The skill enforces alignment with Foundation editorial standards defined in the [Blog Guidelines](../guidelines/blog-guidelines.md).[^evt-public-agents-pr-4]

# Architecture / Specification
The skill automates pre-submission validation and editorial guidance across several key quality dimensions:[^evt-public-agents-pr-4]

- **Casing and Grammar**: Enforces standardized sentence-case capitalization across headings and titles, alongside American English (US English) spelling and stylistic conventions.[^evt-public-agents-pr-4]
- **Source Verification Guidance**: Guides authors on properly citing external specifications, foundation repositories, and factual references while filtering unsupported assertions.[^evt-public-agents-pr-4]
- **Editorial Consistency**: Executes automated checks for vendor neutrality, tone, markdown formatting hygiene, and metadata frontmatter correctness prior to pull request intake.[^evt-public-agents-pr-4]

# References
- [Blog Guidelines](../guidelines/blog-guidelines.md)
- [Public Agent Skills Repository](https://github.com/aaif/public-agents)

[^evt-public-agents-pr-4]: https://github.com/aaif/public-agents/pull/4
