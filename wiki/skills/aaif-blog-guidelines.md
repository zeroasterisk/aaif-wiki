---
type: skill
title: AAIF Blog Guidelines Skill
description: Procedural agent skill packaging AAIF editorial guidelines, story evaluation
  workflows, neutrality enforcement, and submission packaging.
resource: https://github.com/aaif/public-agents/blob/fcc3ebc4db293e01305373fc9c2f2c46845ee015/skills/aaif-blog-guidelines/SKILL.md
tags:
- skill
- editorial
- agent-skill
- publishing
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T09:31:11.191932+00:00'
sources:
- id: evt-public-agents-file-2aebb9feb4df-f97f79ed
  resource: https://github.com/aaif/public-agents/blob/fcc3ebc4db293e01305373fc9c2f2c46845ee015/skills/aaif-blog-guidelines/SKILL.md
  author: Angie Jones
  last_modified: '2026-05-13T11:19:28-07:00'
- id: evt-foundation-pr-2
  resource: https://github.com/aaif/foundation/pull/2
  author: angiejones
  last_modified: '2026-05-13T18:29:50+00:00'
---

# Overview

The `aaif-blog-guidelines` skill is an automated agent skill maintained under the AAIF public agents registry to assist contributors in drafting, reviewing, neutralizing, and packaging blog content for aaif.io [^evt-public-agents-file-2aebb9feb4df-f97f79ed]. Distributed for global execution via npx, the skill operationalizes the foundation's content intake policy and ensures compliance with editorial constraints prior to human submission [^evt-public-agents-file-2aebb9feb4df-f97f79ed][^evt-foundation-pr-2].

# Architecture / Specification

## Skill Definition and Metadata

Configured as version 1.0 authored by Angie Jones, the skill references `../guidelines/blog-guidelines.md` as its normative foundation [^evt-public-agents-file-2aebb9feb4df-f97f79ed]. It provides prompt instructions and validation criteria covering release posts for hosted projects like MCP, `../resources/goose.md`, and AGENTS.md, as well as community tutorials and case studies [^evt-public-agents-file-2aebb9feb4df-f97f79ed].

## Agent Execution Workflow

The skill guides agents through a seven-step procedure [^evt-public-agents-file-2aebb9feb4df-f97f79ed]:

1. **Clarify the story:** Identify target audience, news value, and publication timeline.
2. **Check eligibility:** Verify contributor class, pre-existing internal approvals, and draft originality.
3. **Shape the post:** Structure content around narrative progression (recommended 600–1,500 words) instead of promotional summaries.
4. **Enforce neutrality:** Strip promotional prose, vendor bias, and comparative superiority claims.
5. **Strengthen utility:** Embed concrete technical examples and lessons learned.
6. **Package submission:** Compile author bios, headshots, metadata, social amplification copy, and submission links.
7. **Set expectations:** Communicate review timelines (standard two-week lead time) to contributors.

# Lifecycle History

Version 1.0 released in `aaif/public-agents` and cross-referenced in foundation repository guidelines [^evt-public-agents-file-2aebb9feb4df-f97f79ed][^evt-foundation-pr-2].

[^evt-foundation-pr-2]: https://github.com/aaif/foundation/pull/2
[^evt-public-agents-file-2aebb9feb4df-f97f79ed]: https://github.com/aaif/public-agents/blob/fcc3ebc4db293e01305373fc9c2f2c46845ee015/skills/aaif-blog-guidelines/SKILL.md
