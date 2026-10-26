---
type: guideline
title: Working Group Reporting Template
description: Standardized monthly reporting template, pull request workflow, review
  timelines, and required metadata conventions for AAIF working groups.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/62
tags:
- governance
- reporting
- working-groups
- technical-committee
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T11:02:50.370350+00:00'
sources:
- id: evt-wg-observability-and-traceability-pr-62
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/62
  author: mr-lee
  last_modified: '2026-10-12T02:55:00+00:00'
---

# Overview
The Working Group Reporting Template standardizes the format, submission workflow, and metadata conventions used by Agentic AI Foundation (AAIF) working groups to report monthly progress to the Technical Committee [^evt-wg-observability-and-traceability-pr-62]. Working groups utilize this uniform template to document active deliverables, cross-working-group dependencies, decisions required from the Technical Committee, and community milestones [^evt-wg-observability-and-traceability-pr-62].

# Specification
Working group monthly reports must adhere to standardized intake and submission conventions to enable automated ingestion and cataloging by the Technical Committee [^evt-wg-observability-and-traceability-pr-62]:

- **Pull Request Title Format**: Report pull requests must strictly follow the format `[Report] <YYYY-MM>` (for example, `[Report] 2026-09`), superseding legacy formats that included working group names [^evt-wg-observability-and-traceability-pr-62].
- **Labeling Requirements**: Every report pull request must include the `monthly-report` GitHub label to support automated discovery and tracking across foundation repositories [^evt-wg-observability-and-traceability-pr-62].
- **File Naming Conventions**: Monthly report file names are case-sensitive and must conform to the directory hierarchy established by the Technical Committee [^evt-wg-observability-and-traceability-pr-62].
- **Governance Alignment**: Submission requirements align with Technical Committee operating procedures defined in `../guidelines/working-group-submission-guidelines.md` and `../governance/technical-committee.md` [^evt-wg-observability-and-traceability-pr-62].

# Lifecycle History
The reporting workflow previously permitted variant pull request title styles such as `[Report] <WG name> – <Month YYYY>`. In PR#62 of `wg-observability-and-traceability`, the instructions were aligned with Technical Committee reporting guidelines to enforce the `[Report] <YYYY-MM>` structure, mandatory `monthly-report` labeling, and case-sensitive filenames [^evt-wg-observability-and-traceability-pr-62].

[^evt-wg-observability-and-traceability-pr-62]: https://github.com/aaif/wg-observability-and-traceability/pull/62
