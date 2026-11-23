---
type: policy
title: Project Proposal Process
description: Six-step operating procedure and review workflow defining offline-first
  evaluation, engagement bars, voting gates, and onboarding for AAIF project candidates.
resource: https://github.com/aaif/technical-committee/blob/684c3d2a07da3a8d55f87647bc125b2fcd5631be/project_proposal_process.md
tags:
- governance
- process
- onboarding
- lifecycle
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:25:27.486713+00:00'
sources:
- id: evt-technical-committee-file-05a7e66403db-9c234333
  resource: https://github.com/aaif/technical-committee/blob/684c3d2a07da3a8d55f87647bc125b2fcd5631be/project_proposal_process.md
  author: Manik Surtani
  last_modified: '2026-10-15T16:14:10+11:00'
- id: evt-project-proposals-file-6c7de919a622-15a00e3a
  resource: https://github.com/aaif/project-proposals/blob/24210e3c136914c2df3bd643c1c717eabcb33ff5/.github/ISSUE_TEMPLATE/project-proposal.yml
  author: Manik Surtani
  last_modified: '2026-10-15T16:13:53+11:00'
- id: evt-project-proposals-file-b33563055168-3d9290b7
  resource: https://github.com/aaif/project-proposals/blob/24210e3c136914c2df3bd643c1c717eabcb33ff5/README.md
  author: Manik Surtani
  last_modified: '2026-10-15T16:13:53+11:00'
---

# Overview
The Project Proposal Process is the authoritative operating procedure for submitting, reviewing, voting on, and onboarding open-source technical projects into the Agentic AI Foundation (AAIF)[^evt-technical-committee-file-05a7e66403db-9c234333]. Implemented by the [Technical Committee](../governance/technical-committee.md), the Governing Board, and Linux Foundation operational teams, it guides project candidates through formal admission into foundation hosting[^evt-project-proposals-file-b33563055168-3d9290b7].

# Process Specification
Candidates file a project proposal issue in the `aaif/project-proposals` repository using the standardized issue template[^evt-project-proposals-file-6c7de919a622-15a00e3a][^evt-project-proposals-file-b33563055168-3d9290b7]. The evaluation workflow defaults to asynchronous, offline execution across six sequential steps[^evt-technical-committee-file-05a7e66403db-9c234333]:

1. **Initial Intake**: The AAIF CTO, assisted by an automated intake agent, performs completeness and compliance checks, smoke tests the submission, and alerts Technical Committee (TC) chairs[^evt-technical-committee-file-05a7e66403db-9c234333].
2. **TC Q&A Window**: The Technical Committee reviews the proposal and poses questions asynchronously on the GitHub issue. Rather than requiring an individual champion, the process guarantees a collective engagement bar ensuring a minimum breadth of TC scrutiny[^evt-technical-committee-file-05a7e66403db-9c234333]. If the bar is unmet, TC chairs may assign an on-demand TC supporter to restart review, failing which the proposal is rejected[^evt-technical-committee-file-05a7e66403db-9c234333]. Live presentations are scheduled only on demand[^evt-technical-committee-file-05a7e66403db-9c234333].
3. **TC Vote**: The TC conducts an offline vote via LFX Vote on technical admission and recommended initial stage[^evt-technical-committee-file-05a7e66403db-9c234333].
4. **Governing Board (GB) Vote**: The Governing Board votes via LFX Vote to confirm organizational readiness and resource allocation[^evt-technical-committee-file-05a7e66403db-9c234333].
5. **Legal Formation**: In parallel with votes, contributor paperwork is prepared; Linux Foundation Legal coordinates final contribution agreements, technical charters, and trademark transfers[^evt-technical-committee-file-05a7e66403db-9c234333].
6. **Technical Onboarding**: Linux Foundation IT and project maintainers execute repository transfers and infrastructure setup[^evt-technical-committee-file-05a7e66403db-9c234333].

Application states are tracked publicly using issue labels: `New`, `Waiting on Comment`, `Too Early`, `Approved`, and `Declined`[^evt-project-proposals-file-b33563055168-3d9290b7].

# Governance and Membership Rules
Project admission is detached from commercial foundation membership: submitting organizations are not required to be AAIF members, and accepted project contributors do not automatically receive member tier status or Governing Board seats[^evt-project-proposals-file-b33563055168-3d9290b7]. Stage selection and graduation criteria adhere to the [Project Lifecycle Policy](./project-lifecycle-policy.md)[^evt-technical-committee-file-8f732085cd4f-04c1d0b2].

[^evt-project-proposals-file-6c7de919a622-15a00e3a]: https://github.com/aaif/project-proposals/blob/24210e3c136914c2df3bd643c1c717eabcb33ff5/.github/ISSUE_TEMPLATE/project-proposal.yml
[^evt-project-proposals-file-b33563055168-3d9290b7]: https://github.com/aaif/project-proposals/blob/24210e3c136914c2df3bd643c1c717eabcb33ff5/README.md
[^evt-technical-committee-file-05a7e66403db-9c234333]: https://github.com/aaif/technical-committee/blob/684c3d2a07da3a8d55f87647bc125b2fcd5631be/project_proposal_process.md
