---
type: skill
title: AAIF Blog Guidelines Agent Skill
description: Modular agent skill assisting contributors in drafting, reviewing, neutralizing,
  and packaging blog submissions according to aaif.io editorial guidelines.
resource: https://github.com/aaif/public-agents/blob/fcc3ebc4db293e01305373fc9c2f2c46845ee015/skills/aaif-blog-guidelines/SKILL.md
tags:
- aaif
- skill
- blog
- editorial
- automation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T09:43:24.620104+00:00'
sources:
- id: evt-public-agents-file-2aebb9feb4df-f97f79ed
  resource: https://github.com/aaif/public-agents/blob/fcc3ebc4db293e01305373fc9c2f2c46845ee015/skills/aaif-blog-guidelines/SKILL.md
  author: Angie Jones
  last_modified: '2026-05-13T11:19:28-07:00'
- id: evt-foundation-file-d56154a3412d-c180d87c
  resource: https://github.com/aaif/foundation/blob/8df4e5b4087f2dcd5fbc77b702f68b1fc7418693/policies-guidelines/blog-guidelines.md
  author: Angie Jones
  last_modified: '2026-05-13T11:27:17-07:00'
- id: evt-foundation-pr-2
  resource: https://github.com/aaif/foundation/pull/2
  author: angiejones
  last_modified: '2026-05-13T18:29:50+00:00'
---

# Overview
The AAIF Blog Guidelines Agent Skill (`aaif-blog-guidelines`) is an open skill specification and automated workflow packaged under [../resources/public-agent-skills.md](../resources/public-agent-skills.md) to help contributors author, revise, and package submissions for aaif.io[^evt-public-agents-file-2aebb9feb4df-f97f79ed]. Authored by Angie Jones as version 1.0, the skill automates compliance with [../guidelines/blog-guidelines.md](../guidelines/blog-guidelines.md), ensuring submissions are technically useful, vendor-neutral, and ready for Linux Foundation intake triage[^evt-public-agents-file-2aebb9feb4df-f97f79ed][^evt-foundation-file-d56154a3412d-c180d87c].

# Architecture / Specification

## Installation
The skill can be installed globally into compatible agent harnesses using the skills CLI[^evt-foundation-file-d56154a3412d-c180d87c][^evt-foundation-pr-2]:
```bash
npx skills add aaif/public-agents --skill aaif-blog-guidelines --global
```

## Execution Workflow
When assisting an author, the skill enforces a seven-stage intake pipeline[^evt-public-agents-file-2aebb9feb4df-f97f79ed]:
1. **Clarify the Story:** Establish target audience, AAIF relevance, news timeliness (within the past two months), practical takeaways, and desired publish timing.
2. **Check Eligibility:** Confirm author category (member company, project maintainer, working group member, or community contributor within monthly submission limits) and prior stakeholder approval.
3. **Shape the Post:** Enforce narrative prose structure over corporate marketing copy or press release formats.
4. **Enforce Neutrality:** Strip sales pitches, product superiority claims, and framing that advantages an individual member over others.
5. **Strengthen Utility:** Inject practical technical depth, code or configuration samples, architectural context (such as MCP or [../resources/goose.md](../resources/goose.md)), and operational lessons learned.
6. **Prepare Submission Package:** Assemble final draft text, proposed title, author biographies, headshots/logos, social amplification copy, and target publish dates.
7. **Set Expectations:** Inform the author of review lead times (minimum two weeks) and direct them to the official Asana intake form.

[^evt-foundation-file-d56154a3412d-c180d87c]: https://github.com/aaif/foundation/blob/8df4e5b4087f2dcd5fbc77b702f68b1fc7418693/policies-guidelines/blog-guidelines.md
[^evt-foundation-pr-2]: https://github.com/aaif/foundation/pull/2
[^evt-public-agents-file-2aebb9feb4df-f97f79ed]: https://github.com/aaif/public-agents/blob/fcc3ebc4db293e01305373fc9c2f2c46845ee015/skills/aaif-blog-guidelines/SKILL.md
