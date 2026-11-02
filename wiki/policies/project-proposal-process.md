---
type: policy
title: AAIF Project Proposal Process
description: Six-step operating procedure and review gate governing project proposal
  intake, engagement thresholds, voting, and onboarding into the Agentic AI Foundation.
resource: https://github.com/aaif/technical-committee/blob/684c3d2a07da3a8d55f87647bc125b2fcd5631be/project_proposal_process.md
tags:
- governance
- projects
- proposals
- technical-committee
- onboarding
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:25:30.692233+00:00'
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

The AAIF Project Proposal Process defines the operating procedure for submitting, reviewing, voting on, and onboarding open technical projects into the Agentic AI Foundation [^evt-technical-committee-file-05a7e66403db-9c234333]. Governed by the [Technical Committee](../governance/technical-committee.md) in coordination with the Governing Board, the process operationalizes the admission criteria defined in the [Project Lifecycle Policy](project-lifecycle-policy.md) [^evt-technical-committee-file-05a7e66403db-9c234333].

Submissions are managed publicly via issue forms in the `aaif/project-proposals` repository, which acts as the official application and tracking ledger [^evt-project-proposals-file-b33563055168-3d9290b7]. Foundation membership is explicitly decoupled from project admission; non-member organizations may submit projects, and project acceptance confers neither commercial membership tiers nor Governing Board seats [^evt-project-proposals-file-b33563055168-3d9290b7].

# Architecture / Specification

## Sequential Operating Steps

The evaluation lifecycle prioritizes asynchronous, offline review across six sequential stages plus parallel legal drafting [^evt-technical-committee-file-05a7e66403db-9c234333]:

1. **Initial Intake (Step 1)**: The AAIF CTO, supported by an automated intake agent executing technical smoke tests, screens new submissions for scope, OSI-compliant permissive licensing, and completeness before alerting the Technical Committee chairs [^evt-technical-committee-file-05a7e66403db-9c234333].
2. **TC Q&A Window (Step 2)**: An offline review window conducted via comments on the GitHub issue. To advance, proposals must satisfy an *engagement bar* requiring substantive interaction from multiple TC members rather than relying on a single project sponsor [^evt-technical-committee-file-05a7e66403db-9c234333]. If the bar is unmet, TC chairs may appoint an on-demand TC supporter to champion the proposal; lack of engagement results in decline [^evt-technical-committee-file-05a7e66403db-9c234333]. An optional live presentation may be scheduled upon request [^evt-technical-committee-file-05a7e66403db-9c234333].
3. **Parallel Contributor Paperwork**: Linux Foundation PMO and Legal coordinate technical charters, contribution agreements, and trademark assignments in parallel with technical evaluations [^evt-technical-committee-file-05a7e66403db-9c234333].
4. **TC Vote (Step 3)**: The Technical Committee evaluates admission and recommends an initial lifecycle stage (Sandbox, Growth, or Impact) via LFX Vote [^evt-technical-committee-file-05a7e66403db-9c234333][^evt-project-proposals-file-6c7de919a622-15a00e3a].
5. **Governing Board Vote (Step 4)**: The Governing Board votes via LFX Vote to confirm organizational readiness, resource allocation, and stage entry [^evt-technical-committee-file-05a7e66403db-9c234333].
6. **LF Legal Formation (Step 5)**: Final execution of contribution agreements, trademark transfers, and technical charters via DocuSign [^evt-technical-committee-file-05a7e66403db-9c234333].
7. **Technical Onboarding (Step 6)**: LF IT and PMO transfer repository ownership, configure CI/CD credentials, and establish project infrastructure [^evt-technical-committee-file-05a7e66403db-9c234333].

## Repository Tracking Labels

Issue tracking in `aaif/project-proposals` reflects candidate status via five canonical labels: `New`, `Approved`, `Declined`, `Waiting on Comment`, and `Too Early` [^evt-project-proposals-file-b33563055168-3d9290b7]. Projects must satisfy all legal and governance criteria before publicly representing themselves as accepted or foundation-hosted [^evt-project-proposals-file-6c7de919a622-15a00e3a].

# Lifecycle History

- **2026-08-28**: Operating procedure version v0.3 enacted, formalizing the offline engagement bar and automated intake mechanics [^evt-technical-committee-file-05a7e66403db-9c234333].

[^evt-project-proposals-file-6c7de919a622-15a00e3a]: https://github.com/aaif/project-proposals/blob/24210e3c136914c2df3bd643c1c717eabcb33ff5/.github/ISSUE_TEMPLATE/project-proposal.yml
[^evt-project-proposals-file-b33563055168-3d9290b7]: https://github.com/aaif/project-proposals/blob/24210e3c136914c2df3bd643c1c717eabcb33ff5/README.md
[^evt-technical-committee-file-05a7e66403db-9c234333]: https://github.com/aaif/technical-committee/blob/684c3d2a07da3a8d55f87647bc125b2fcd5631be/project_proposal_process.md
