---
type: guideline
title: Blog Content Intake and Editorial Guidelines
description: Editorial standards, submission workflows, contributor eligibility rules,
  and neutrality constraints governing technical publications on aaif.io.
resource: https://github.com/aaif/foundation/blob/8df4e5b4087f2dcd5fbc77b702f68b1fc7418693/policies-guidelines/blog-guidelines.md
tags:
- blog
- guidelines
- editorial
- intake
- content
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T09:29:32.892649+00:00'
sources:
- id: evt-foundation-file-d56154a3412d-c180d87c
  resource: https://github.com/aaif/foundation/blob/8df4e5b4087f2dcd5fbc77b702f68b1fc7418693/policies-guidelines/blog-guidelines.md
  author: Angie Jones
  last_modified: '2026-05-13T11:27:17-07:00'
- id: evt-foundation-pr-2
  resource: https://github.com/aaif/foundation/pull/2
  author: angiejones
  last_modified: '2026-05-13T18:29:50+00:00'
- id: evt-public-agents-file-2aebb9feb4df-f97f79ed
  resource: https://github.com/aaif/public-agents/blob/fcc3ebc4db293e01305373fc9c2f2c46845ee015/skills/aaif-blog-guidelines/SKILL.md
  author: Angie Jones
  last_modified: '2026-05-13T11:19:28-07:00'
---

# Overview
The Agentic AI Foundation Blog Guidelines establish the intake process, review workflow, and editorial quality standards for publications appearing on the official aaif.io website.[^evt-foundation-file-d56154a3412d-c180d87c] The blog acts as an educational and technical publishing platform highlighting hosted open-source projects, architectural patterns, technical guides, and community developments across the agentic AI ecosystem.[^evt-foundation-file-d56154a3412d-c180d87c]

Publishing is managed end-to-end by the Linux Foundation team, requiring all submissions to be routed through the foundation's official submission form with a standard two-week review lead time.[^evt-foundation-file-d56154a3412d-c180d87c] Contributors can also leverage the [`skills/aaif-blog-guidelines`](../skills/aaif-blog-guidelines.md) agent skill to automate drafting, quality checks, and submission packaging.[^evt-foundation-file-d56154a3412d-c180d87c] [^evt-foundation-pr-2]

# Architecture / Specification
## Contributor Eligibility and Scope
Content submissions are accepted from several contributor classes subject to clear editorial boundaries:[^evt-foundation-file-d56154a3412d-c180d87c]
- **Member Companies:** Content must remain strictly vendor-neutral, educational, and aligned with AAIF's mission; posts may include at most one or two closing sentences with a single external link (such as a company repository or open role).[^evt-foundation-file-d56154a3412d-c180d87c]
- **Project Maintainers and Contributors:** Updates, roadmaps, and deep-dives regarding AAIF-hosted technologies such as MCP, goose, and AGENTS.md.[^evt-foundation-file-d56154a3412d-c180d87c]
- **Working Groups and Technical Committee:** Official announcements and technical reports produced by AAIF working groups or the [Technical Committee](../governance/technical-committee.md).[^evt-foundation-file-d56154a3412d-c180d87c]
- **Community Contributors:** Tutorials and ecosystem experiences, limited to a maximum quota of two published posts per month per contributor.[^evt-foundation-file-d56154a3412d-c180d87c]
- **Program Participants:** Recaps, findings, and reflections stemming from AAIF hackathons and events.[^evt-foundation-file-d56154a3412d-c180d87c]

## Editorial Invariants
Submissions must adhere to strict requirements prior to intake:[^evt-foundation-file-d56154a3412d-c180d87c]
- **Readiness and Approval:** Submissions must be final, ready for publication, and pre-approved by the contributor's corporate or project stakeholders.[^evt-foundation-file-d56154a3412d-c180d87c]
- **Originality and Timeliness:** Posts must be original (not published elsewhere) and reflect activities or releases from the preceding two months.[^evt-foundation-file-d56154a3412d-c180d87c]
- **Neutrality and Non-Disparagement:** No promotional, sponsored, or comparative superiority claims benefiting one member over another; content must not criticize or discourage adoption of any open-source project.[^evt-foundation-file-d56154a3412d-c180d87c]
- **Format and Length:** Structured narrative format, typically 600–1,500 words, accompanied by titles, author bios, headshots, and social amplification copy.[^evt-public-agents-file-2aebb9feb4df-f97f79ed]

# Lifecycle History
The intake and editorial policy was published in `policies-guidelines/blog-guidelines.md` and later updated via PR#2 to integrate distribution instructions for the `aaif-blog-guidelines` agent skill via `npx skills add aaif/public-agents --skill aaif-blog-guidelines --global`.[^evt-foundation-file-d56154a3412d-c180d87c] [^evt-foundation-pr-2]

[^evt-foundation-file-d56154a3412d-c180d87c]: https://github.com/aaif/foundation/blob/8df4e5b4087f2dcd5fbc77b702f68b1fc7418693/policies-guidelines/blog-guidelines.md
[^evt-foundation-pr-2]: https://github.com/aaif/foundation/pull/2
[^evt-public-agents-file-2aebb9feb4df-f97f79ed]: https://github.com/aaif/public-agents/blob/fcc3ebc4db293e01305373fc9c2f2c46845ee015/skills/aaif-blog-guidelines/SKILL.md
