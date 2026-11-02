---
type: skill
title: AAIF Blog Guidelines Skill
description: Modular agent skill assisting contributors in drafting, reviewing, neutralizing,
  and packaging blog submissions for aaif.io.
resource: https://github.com/aaif/public-agents/blob/fcc3ebc4db293e01305373fc9c2f2c46845ee015/skills/aaif-blog-guidelines/SKILL.md
tags:
- skill
- blog
- editorial
- agent-skill
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T09:29:32.892649+00:00'
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
The `aaif-blog-guidelines` skill is a standardized agent skill packaged within the `aaif/public-agents` repository that guides AI agents through drafting, reviewing, neutralizing, and packaging blog content for the Agentic AI Foundation blog on aaif.io.[^evt-public-agents-file-2aebb9feb4df-f97f79ed] Authored by Angie Jones, the skill enforces the foundation's official [Blog Content Intake and Editorial Guidelines](../guidelines/blog-guidelines.md).[^evt-public-agents-file-2aebb9feb4df-f97f79ed]

It can be installed globally into compliant agent harnesses using the command `npx skills add aaif/public-agents --skill aaif-blog-guidelines --global`.[^evt-foundation-file-d56154a3412d-c180d87c]

# Architecture / Specification
## Procedural Workflow
The skill directs agents through a seven-stage assistance pipeline:[^evt-public-agents-file-2aebb9feb4df-f97f79ed]
1. **Clarify the story:** Identify core audience, AAIF relevance, timeliness, practical value, and target publishing window.[^evt-public-agents-file-2aebb9feb4df-f97f79ed]
2. **Check eligibility:** Confirm contributor category, stakeholder approval path, and original unpublished status.[^evt-public-agents-file-2aebb9feb4df-f97f79ed]
3. **Shape the post:** Structure content into an engaging narrative rather than a marketing press release or product brief.[^evt-public-agents-file-2aebb9feb4df-f97f79ed]
4. **Enforce neutrality:** Strip promotional jargon, vendor-centric framing, comparative superiority claims, and member favoritism.[^evt-public-agents-file-2aebb9feb4df-f97f79ed]
5. **Strengthen utility:** Enrich draft with implementation details, architecture diagrams, concrete examples, and ecosystem context.[^evt-public-agents-file-2aebb9feb4df-f97f79ed]
6. **Prepare submission package:** Assemble title, author names, bios, headshot/logo assets, social amplification copy, hashtags, and target release date.[^evt-public-agents-file-2aebb9feb4df-f97f79ed]
7. **Set expectations:** Communicate that publication is contingent on review and requires approximately a two-week lead time.[^evt-public-agents-file-2aebb9feb4df-f97f79ed]

## Submission Package Checklist
The skill ensures every submission bundle contains verified artifacts before routing to the official intake form: complete draft (recommended 600–1,500 words), vendor neutrality verification, stakeholder approvals, and social amplification text.[^evt-public-agents-file-2aebb9feb4df-f97f79ed]

# Lifecycle History
Version 1.0 of the skill was authored by Angie Jones in `aaif/public-agents` to provide an automated operational counterpart to the foundation's editorial policy.[^evt-public-agents-file-2aebb9feb4df-f97f79ed] The installation command was subsequently referenced directly inside the primary AAIF repository guideline documentation.[^evt-foundation-pr-2]

[^evt-foundation-file-d56154a3412d-c180d87c]: https://github.com/aaif/foundation/blob/8df4e5b4087f2dcd5fbc77b702f68b1fc7418693/policies-guidelines/blog-guidelines.md
[^evt-foundation-pr-2]: https://github.com/aaif/foundation/pull/2
[^evt-public-agents-file-2aebb9feb4df-f97f79ed]: https://github.com/aaif/public-agents/blob/fcc3ebc4db293e01305373fc9c2f2c46845ee015/skills/aaif-blog-guidelines/SKILL.md
