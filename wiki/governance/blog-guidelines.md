---
type: governance
title: Blog Guidelines
description: Content intake policy, contributor rules, and editorial standards for
  publishing vendor-neutral content on aaif.io.
resource: https://github.com/aaif/foundation/blob/8df4e5b4087f2dcd5fbc77b702f68b1fc7418693/policies-guidelines/blog-guidelines.md
tags:
- governance
- policy
- blog
- content
- guidelines
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:39:35.628502+00:00'
sources:
- id: evt-foundation-file-d56154a3412d-c180d87c
  resource: https://github.com/aaif/foundation/blob/8df4e5b4087f2dcd5fbc77b702f68b1fc7418693/policies-guidelines/blog-guidelines.md
  author: Angie Jones
  last_modified: '2026-05-13T11:27:17-07:00'
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

The AAIF Blog Guidelines establish the content intake process, editorial criteria, and submission workflow for publishing articles, project releases, and thought leadership on aaif.io [^evt-foundation-file-d56154a3412d-c180d87c].

The Linux Foundation team oversees the publishing pipeline to ensure all published material is educational, timely, narrative, and vendor-neutral [^evt-foundation-file-d56154a3412d-c180d87c].

# Architecture / Specification

### Contributor Eligibility and Content Rules
Submissions are accepted from member companies, project maintainers, working groups, the [Technical Committee](technical-committee.md), event participants, and community contributors [^evt-foundation-file-d56154a3412d-c180d87c]. Core requirements include:
- **Vendor Neutrality:** Content must not promote one member over others or act as sales collateral. Member companies are restricted to one or two closing sentences with a single external link [^evt-foundation-file-d56154a3412d-c180d87c].
- **Project Focus:** High-value topics include updates on AAIF-hosted projects (MCP, goose, AGENTS.md), technical tutorials, interoperability patterns, and real-world case studies [^evt-foundation-file-d56154a3412d-c180d87c].
- **Originality & Timeliness:** Posts must be original, unpublished elsewhere, and reflect work from within the last two months [^evt-foundation-file-d56154a3412d-c180d87c].
- **Frequency:** Community contributors are permitted up to two posts per month [^evt-foundation-file-d56154a3412d-c180d87c].

### Agent Skill Automation
Contributors can prepare and review blog submissions using the `aaif-blog-guidelines` [agent skill](../specification/agent-skill.md) available in [Public Agents](../initiatives/public-agents.md) [^evt-public-agents-file-2aebb9feb4df-f97f79ed][^evt-foundation-pr-2]:

```bash
npx skills add aaif/public-agents --skill aaif-blog-guidelines --global
```

[^evt-foundation-file-d56154a3412d-c180d87c]: https://github.com/aaif/foundation/blob/8df4e5b4087f2dcd5fbc77b702f68b1fc7418693/policies-guidelines/blog-guidelines.md
[^evt-foundation-pr-2]: https://github.com/aaif/foundation/pull/2
[^evt-public-agents-file-2aebb9feb4df-f97f79ed]: https://github.com/aaif/public-agents/blob/fcc3ebc4db293e01305373fc9c2f2c46845ee015/skills/aaif-blog-guidelines/SKILL.md
