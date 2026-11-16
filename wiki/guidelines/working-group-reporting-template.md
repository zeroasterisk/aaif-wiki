---
type: guideline
title: Working Group Reporting Template
description: Standardized cadence, structure, review timeline, and pull request workflow
  for AAIF working groups delivering monthly activity reports to the Technical Committee.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/62
tags:
- governance
- reporting
- technical-committee
- working-groups
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:34:13.154434+00:00'
sources:
- id: evt-wg-observability-and-traceability-pr-62
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/62
  author: mr-lee
  last_modified: '2026-10-12T02:55:00+00:00'
---

# Overview

The Working Group Reporting Template standardizes how Agentic AI Foundation (AAIF) working groups report operational milestones, technical deliverables, and decisions requiring [Technical Committee](../governance/technical-committee.md) review. Monthly reports ensure cross-workstream visibility, track active deliverables across working groups, and provide a historical record of consensus and governance actions.

# Architecture / Specification

Working groups publish monthly reports into their local repository trees under standardized reporting directories. To allow automated discovery and aggregation across foundation repositories, report pull requests must strictly adhere to intake guidelines [^evt-wg-observability-and-traceability-pr-62]:

- **File Naming**: Report filenames are case-sensitive and follow standardized date formatting (e.g., `YYYY-MM.md`) within the designated reports path [^evt-wg-observability-and-traceability-pr-62].
- **Pull Request Title**: Pull requests submitting monthly reports must follow the explicit format `[Report] <YYYY-MM>` rather than descriptive or working group names [^evt-wg-observability-and-traceability-pr-62].
- **Labeling**: Every report submission pull request must be tagged with the `monthly-report` label [^evt-wg-observability-and-traceability-pr-62].
- **Content Requirements**: Reports detail progress made during the reporting cycle, current roadmap milestones, meeting attendance summaries, cross-group collaborations, and explicit calls for Technical Committee decisions.

# Lifecycle History

Standardization efforts led by working groups, including the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), identified divergence between localized template instructions and the centralized Technical Committee reporting requirements [^evt-wg-observability-and-traceability-pr-62]. In response, reporting templates were updated to align pull request title conventions, label automation requirements, and case-sensitive filename constraints directly with centralized governance documentation [^evt-wg-observability-and-traceability-pr-62].

# References

- [Technical Committee Working Group Reporting Guidelines](https://github.com/aaif/technical-committee/blob/main/working-groups/reporting.md)

[^evt-wg-observability-and-traceability-pr-62]: https://github.com/aaif/wg-observability-and-traceability/pull/62
