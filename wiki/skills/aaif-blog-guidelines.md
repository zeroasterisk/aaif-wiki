---
type: skill
title: AAIF Blog Guidelines Skill
description: Modular agent skill assisting contributors in drafting, reviewing, neutralizing,
  and styling AAIF blog publications.
resource: https://github.com/aaif/public-agents/pull/4
tags:
- skills
- editorial
- blog
- style-guide
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T10:48:03.610328+00:00'
sources:
- id: evt-public-agents-pr-4
  resource: https://github.com/aaif/public-agents/pull/4
  author: steveaaif
  last_modified: '2026-10-02T13:51:20+00:00'
---

# Overview
The AAIF Blog Guidelines Skill is an automated agent skill providing editorial validation and drafting assistance for community blog posts published under the Agentic AI Foundation. It operationalizes editorial standards, tone neutralization, attribution rules, and publication checklists established by Foundation governance.

# Architecture / Specification
The skill enforces formatting and style rules during blog drafting and pull request reviews:
- **Style and Tone Verification**: Validates US English spelling and sentence case conventions across headings and document sections.[^evt-public-agents-pr-4]
- **Neutrality and Claims Guidance**: Verifies factual attributions and neutral phrasing, ensuring claims are backed by verifiable sources rather than subjective vendor positioning.[^evt-public-agents-pr-4]
- **Editorial Consistency Checks**: Programmatically scans markdown frontmatter, author metadata, and document structure to ensure compliance with the foundational [Blog Guidelines](../guidelines/blog-guidelines.md).[^evt-public-agents-pr-4]

# Lifecycle History
Iteratively maintained within the public agent skills repository (`aaif/public-agents`), incorporating updated copy standards and automated consistency checks for contributor workflows.[^evt-public-agents-pr-4]

[^evt-public-agents-pr-4]: https://github.com/aaif/public-agents/pull/4
