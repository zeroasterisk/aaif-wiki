---
type: governance
title: Technical Committee
description: Governing technical body of the AAIF managing project intake, working
  group lifecycles, cross-group consensus, and technical oversight.
resource: https://github.com/aaif/technical-committee/blob/fe99a96791381e68eb40e8e5885690ddd08fbfb1/working-groups/lifecycle-policy.md
tags:
- governance
- technical-committee
- working-groups
- voting
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T03:28:25.423120+00:00'
sources:
- id: evt-technical-committee-file-6f2428968391-033df704
  resource: https://github.com/aaif/technical-committee/blob/fe99a96791381e68eb40e8e5885690ddd08fbfb1/working-groups/lifecycle-policy.md
  author: Manik Surtani
  last_modified: '2026-10-12T10:57:40+11:00'
- id: evt-technical-committee-file-86b96cfaa5c4-64c967b8
  resource: https://github.com/aaif/technical-committee/blob/fe99a96791381e68eb40e8e5885690ddd08fbfb1/working-groups/reporting.md
  author: Manik Surtani
  last_modified: '2026-10-12T10:57:40+11:00'
---

# Overview
The Technical Committee (TC) serves as the primary technical governing body of the Agentic AI Foundation (AAIF)[^evt-technical-committee-file-6f2428968391-033df704]. The committee provides technical stewardship across Foundation initiatives, evaluating project admissions, chartering and supervising working groups, harmonizing cross-boundary architectures, and resolving technical disputes[^evt-technical-committee-file-6f2428968391-033df704].

The TC operates in coordination with the AAIF Governing Board and enforces governance standards established in the [Project Lifecycle Policy](../policies/project-lifecycle-policy.md) and the [Working Group Lifecycle Policy](../policies/working-group-lifecycle-policy.md)[^evt-technical-committee-file-6f2428968391-033df704].

# Architecture / Specification

## Decision-Making and Voting Procedures
The TC conducts business primarily through asynchronous communication on public GitHub pull requests and issue trackers[^evt-technical-committee-file-6f2428968391-033df704][^evt-technical-committee-file-86b96cfaa5c4-64c967b8]:
- **Lazy Consensus**: Routine decisions pass under lazy consensus if no TC member objects within seven calendar days of posting[^evt-technical-committee-file-6f2428968391-033df704].
- **Contested Decisions**: An objection during lazy consensus triggers a formal vote, decided by a simple majority of all TC members[^evt-technical-committee-file-6f2428968391-033df704].
- **Mandatory Roll-Call Votes**: Three specific actions cannot pass via lazy consensus and require formal recorded votes[^evt-technical-committee-file-6f2428968391-033df704]:
  1. Approving a new Working Group (subject to final Governing Board approval)[^evt-technical-committee-file-6f2428968391-033df704].
  2. Forcibly moving a Working Group to Concluded status when not requested by its chairs[^evt-technical-committee-file-6f2428968391-033df704].
  3. Removing a Working Group chair, which requires a two-thirds supermajority vote across all TC members[^evt-technical-committee-file-6f2428968391-033df704].

## Working Group Oversight
The TC evaluates proposed working groups according to the [Working Group Submission Guidelines](../guidelines/working-group-submission-guidelines.md), targeting an eight-week evaluation cycle[^evt-technical-committee-file-6f2428968391-033df704]. Approved groups undergo a Sandbox stage (six weeks, extendable once by up to six weeks) before active charter approval[^evt-technical-committee-file-6f2428968391-033df704]. Active charters run on 12-month renewal cycles[^evt-technical-committee-file-6f2428968391-033df704].

## Monthly Progress Review
Working Groups submit monthly progress reports via pull requests following the `reporting/YYYY-MM-report.md` specification[^evt-technical-committee-file-86b96cfaa5c4-64c967b8]. The TC evaluates submissions within a 7-day review window[^evt-technical-committee-file-86b96cfaa5c4-64c967b8]. While reviews are asynchronous by default, the TC schedules live synchronization meetings for substantive blockers, cross-WG dependencies, or when a group misses two consecutive monthly reporting cycles[^evt-technical-committee-file-86b96cfaa5c4-64c967b8].

# References
- Working Group Lifecycle Policy: [../policies/working-group-lifecycle-policy.md](../policies/working-group-lifecycle-policy.md)
- Working Group Submission Guidelines: [../guidelines/working-group-submission-guidelines.md](../guidelines/working-group-submission-guidelines.md)
- Project Lifecycle Policy: [../policies/project-lifecycle-policy.md](../policies/project-lifecycle-policy.md)

[^evt-technical-committee-file-6f2428968391-033df704]: https://github.com/aaif/technical-committee/blob/fe99a96791381e68eb40e8e5885690ddd08fbfb1/working-groups/lifecycle-policy.md
[^evt-technical-committee-file-86b96cfaa5c4-64c967b8]: https://github.com/aaif/technical-committee/blob/fe99a96791381e68eb40e8e5885690ddd08fbfb1/working-groups/reporting.md
