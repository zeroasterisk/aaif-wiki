---
type: policy
title: Project Proposal Process
description: Operating procedure defining the six-step intake, review, voting, legal
  formation, and onboarding workflow for prospective AAIF projects.
resource: https://github.com/aaif/technical-committee/blob/684c3d2a07da3a8d55f87647bc125b2fcd5631be/project_proposal_process.md
tags:
- governance
- intake
- technical-committee
- lifecycle
- policies
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T11:12:22.882582+00:00'
sources:
- id: evt-technical-committee-file-05a7e66403db-9c234333
  resource: https://github.com/aaif/technical-committee/blob/684c3d2a07da3a8d55f87647bc125b2fcd5631be/project_proposal_process.md
  author: Manik Surtani
  last_modified: '2026-10-15T16:14:10+11:00'
- id: evt-project-proposals-file-b33563055168-3d9290b7
  resource: https://github.com/aaif/project-proposals/blob/24210e3c136914c2df3bd643c1c717eabcb33ff5/README.md
  author: Manik Surtani
  last_modified: '2026-10-15T16:13:53+11:00'
- id: evt-project-proposals-file-6c7de919a622-15a00e3a
  resource: https://github.com/aaif/project-proposals/blob/24210e3c136914c2df3bd643c1c717eabcb33ff5/.github/ISSUE_TEMPLATE/project-proposal.yml
  author: Manik Surtani
  last_modified: '2026-10-15T16:13:53+11:00'
---

# Overview
The Project Proposal Process is the operating procedure implementing the [Project Lifecycle Policy](project-lifecycle-policy.md) for proposing, reviewing, approving, and onboarding open-source projects into the Agentic AI Foundation (AAIF).[^evt-technical-committee-file-05a7e66403db-9c234333] The procedure is structured into six sequential steps plus parallel contributor paperwork, defaulting to offline, asynchronous execution to accommodate a globally distributed Technical Committee (TC).[^evt-technical-committee-file-05a7e66403db-9c234333]

# Architecture / Specification
The intake and approval pipeline coordinates defined actor roles across six steps:[^evt-technical-committee-file-05a7e66403db-9c234333]
- **Step 1 - Initial Intake**: The CTO, assisted by an automated compliance intake agent, screens applications for completeness, performs smoke tests, and solicits input from [Technical Committee Chairs](../governance/technical-committee.md) on the proposal issue.[^evt-technical-committee-file-05a7e66403db-9c234333]
- **Step 2 - TC Q&A Window**: An asynchronous inquiry window on GitHub.[^evt-technical-committee-file-05a7e66403db-9c234333] Advancement requires meeting an explicit engagement bar consisting of active TC member participation; if unmet, the TC chairs seek an on-demand TC supporter to champion the proposal, failing which the proposal is rejected.[^evt-technical-committee-file-05a7e66403db-9c234333] Live presentations occur on demand only if requested by a TC member.[^evt-technical-committee-file-05a7e66403db-9c234333]
- **Parallel Step - Contributor Paperwork**: Contribution agreements, technical charters, and trademark assignments are prepared concurrently by LF PMO and LF Legal, and must be execution-ready before Step 4.[^evt-technical-committee-file-05a7e66403db-9c234333]
- **Step 3 - TC Vote**: The Technical Committee conducts an offline vote using LFX Vote to recommend admission and determine the initial lifecycle stage.[^evt-technical-committee-file-05a7e66403db-9c234333]
- **Step 4 - GB Vote**: The Governing Board votes offline via LFX Vote on organizational readiness and Foundation resource allocation.[^evt-technical-committee-file-05a7e66403db-9c234333]
- **Step 5 - LF Legal Formation**: LF Legal and AAIF staff execute final contribution and charter agreements via DocuSign.[^evt-technical-committee-file-05a7e66403db-9c234333]
- **Step 6 - Technical Onboarding**: Project maintainers and LF IT transfer code repositories, domains, credentials, and continuous integration infrastructure.[^evt-technical-committee-file-05a7e66403db-9c234333]

### Application Tracking Labels
Proposal issues submitted via the standardized issue form are tracked using specific workflow labels:[^evt-project-proposals-file-b33563055168-3d9290b7][^evt-project-proposals-file-6c7de919a622-15a00e3a]
- `New`: The submission is placed in the initial intake backlog.[^evt-project-proposals-file-b33563055168-3d9290b7]
- `Approved`: The application has fulfilled all approval gates and completed foundation onboarding.[^evt-project-proposals-file-b33563055168-3d9290b7]
- `Declined`: The proposal has been formally rejected with documented rationale.[^evt-project-proposals-file-b33563055168-3d9290b7]
- `Waiting on Comment`: Review is paused awaiting answers or updates from the submitter.[^evt-project-proposals-file-b33563055168-3d9290b7]
- `Too Early`: The project is not yet mature enough for hosting; guidance is provided for subsequent reapplication.[^evt-project-proposals-file-b33563055168-3d9290b7]

Foundation project hosting does not require prior AAIF corporate membership, nor does project acceptance confer corporate membership tier status or a Governing Board seat.[^evt-project-proposals-file-b33563055168-3d9290b7]

# Lifecycle History
Operating procedure v0.3 was published on August 28, 2026, codifying the engagement bar, automated intake agent responsibilities, and LFX Vote mechanics.[^evt-technical-committee-file-05a7e66403db-9c234333]

[^evt-project-proposals-file-6c7de919a622-15a00e3a]: https://github.com/aaif/project-proposals/blob/24210e3c136914c2df3bd643c1c717eabcb33ff5/.github/ISSUE_TEMPLATE/project-proposal.yml
[^evt-project-proposals-file-b33563055168-3d9290b7]: https://github.com/aaif/project-proposals/blob/24210e3c136914c2df3bd643c1c717eabcb33ff5/README.md
[^evt-technical-committee-file-05a7e66403db-9c234333]: https://github.com/aaif/technical-committee/blob/684c3d2a07da3a8d55f87647bc125b2fcd5631be/project_proposal_process.md
