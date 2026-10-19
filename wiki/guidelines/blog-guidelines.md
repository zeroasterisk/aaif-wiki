---
type: guideline
title: AAIF Blog Intake Guidelines
description: Editorial policies, eligibility constraints, content requirements, and
  intake workflows governing publications on aaif.io.
resource: https://github.com/aaif/foundation/blob/8df4e5b4087f2dcd5fbc77b702f68b1fc7418693/policies-guidelines/blog-guidelines.md
tags:
- aaif
- guidelines
- blog
- editorial
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T09:43:24.620104+00:00'
sources:
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
The AAIF Blog Intake Guidelines govern editorial standards, submitter eligibility, review timelines, and submission workflows for content published on aaif.io[^evt-foundation-file-d56154a3412d-c180d87c]. Owned and managed end-to-end by the Linux Foundation and AAIF communications team, the blog serves as an educational and technical outlet spotlighting open-source agentic projects, production case studies, architecture patterns, and ecosystem milestones[^evt-foundation-file-d56154a3412d-c180d87c].

# Architecture / Specification

## Contributor Eligibility and Submission Rules
Contributions are welcome across five designated community categories, subject to specific constraints[^evt-foundation-file-d56154a3412d-c180d87c]:
- **Member Companies:** Posts must remain strictly vendor-neutral. They may include at most one or two concluding sentences with a single external link (such as a company homepage, relevant repository, or open job position).
- **Project Maintainers & Contributors:** Technical updates, release notes, and engineering deep-dives covering AAIF-hosted projects such as Model Context Protocol (MCP), [../resources/goose.md](../resources/goose.md), and AGENTS.md.
- **Working Groups & Technical Committee:** Authoritative progress reports, architectural whitepapers, and specifications endorsed by working groups or the [../governance/technical-committee.md](../governance/technical-committee.md).
- **Community Contributors:** Practical tutorials, how-to guides, and thought leadership. Submissions are capped at two posts per calendar month per contributor.
- **Event Participants:** Recaps, takeaways, and lessons learned from AAIF-affiliated hackathons and community events.

## Editorial Standards and Intake Workflow
All submissions must comply with core editorial requirements prior to intake[^evt-foundation-file-d56154a3412d-c180d87c]:
- **Narrative Format:** Content must follow an educational narrative format (typically 600–1,500 words, with longer technical deep-dives permitted) rather than marketing copy or press releases.
- **Vendor Neutrality:** Articles must avoid promotional framing, unsupported superiority assertions, or language disparaging open-source alternatives.
- **Originality & Timeliness:** Submissions must be previously unpublished and represent recent work or announcements, generally within the prior two months.
- **Lead Times:** Contributors must submit finalized drafts through the official Asana intake form with a standard two-week review lead time.

Contributors can automate draft shaping, neutrality checks, and package preparation using the [../skills/aaif-blog-guidelines.md](../skills/aaif-blog-guidelines.md) modular agent skill[^evt-foundation-file-d56154a3412d-c180d87c][^evt-foundation-pr-2].

[^evt-foundation-file-d56154a3412d-c180d87c]: https://github.com/aaif/foundation/blob/8df4e5b4087f2dcd5fbc77b702f68b1fc7418693/policies-guidelines/blog-guidelines.md
[^evt-foundation-pr-2]: https://github.com/aaif/foundation/pull/2
