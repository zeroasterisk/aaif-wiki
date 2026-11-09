---
type: skill
title: AAIF Blog Guidelines Skill
description: Modular agent skill assisting contributors in drafting, reviewing, neutralizing,
  and packaging blog submissions against AAIF editorial standards.
resource: https://github.com/aaif/public-agents/pull/4
tags:
- editorial
- skills
- agent-skills
- linting
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:14:10.381444+00:00'
sources:
- id: evt-public-agents-pr-4
  resource: https://github.com/aaif/public-agents/pull/4
  author: steveaaif
  last_modified: '2026-10-02T13:51:20+00:00'
---

# Overview
The `aaif-blog-guidelines` skill is an automated editorial assistant that evaluates proposed blog articles against the [AAIF Blog Guidelines](../guidelines/blog-guidelines.md) [^evt-public-agents-pr-4]. Packaged as a standard [agent skill](../standards/agent-skills.md), it enforces editorial consistency, tone neutrality, and structural formatting rules prior to publication review [^evt-public-agents-pr-4].

# Architecture / Specification
The skill performs automated linting and feedback generation across contributor drafts [^evt-public-agents-pr-4]:

- **Editorial Mechanics Verification**: Evaluates text for sentence case in headings and flags non-conforming British English variants against standard US English rules [^evt-public-agents-pr-4].
- **Source Citation Auditing**: Checks assertions for primary-source links and flags unsupported categorical statements for contributor review [^evt-public-agents-pr-4].
- **Consistency Enforcement**: Verifies correct usage of official AAIF project naming and flags deviations from neutral tone [^evt-public-agents-pr-4].

# Lifecycle History
- **PR #4 (Open)**: Added sentence case heading checks, US English consistency enforcement, and primary-source attribution auditing [^evt-public-agents-pr-4].

[^evt-public-agents-pr-4]: https://github.com/aaif/public-agents/pull/4
