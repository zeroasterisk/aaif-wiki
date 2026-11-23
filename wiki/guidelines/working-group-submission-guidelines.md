---
type: guideline
title: Working Group Submission Guidelines
description: Operational intake guidelines, applicant eligibility criteria, issue
  form structure, and review lifecycle for proposing or reviving AAIF working groups.
resource: https://github.com/aaif/working-group-proposals/blob/1054856f6e1307fdfb56d51abcf9a87055ee0140/.github/ISSUE_TEMPLATE/working-group-proposal.yml
tags:
- governance
- working-groups
- proposals
- intake
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:26:12.484877+00:00'
sources:
- id: evt-working-group-proposals-file-87b3376703c5-313cc435
  resource: https://github.com/aaif/working-group-proposals/blob/1054856f6e1307fdfb56d51abcf9a87055ee0140/.github/ISSUE_TEMPLATE/working-group-proposal.yml
  author: Manik Surtani
  last_modified: '2026-10-15T16:14:24+11:00'
- id: evt-working-group-proposals-file-b33563055168-6c29ea3b
  resource: https://github.com/aaif/working-group-proposals/blob/1054856f6e1307fdfb56d51abcf9a87055ee0140/README.md
  author: Manik Surtani
  last_modified: '2026-10-15T16:14:24+11:00'
---

# Overview
The AAIF Working Group Submission Guidelines establish the operational process, intake requirements, and tracking workflow for proposing a new working group (WG) or reviving a concluded working group within the Agentic AI Foundation [^evt-working-group-proposals-file-b33563055168-6c29ea3b]. All proposals are submitted through GitHub issues using a standardized issue template and tracked publicly on the Working Group Proposals Board [^evt-working-group-proposals-file-b33563055168-6c29ea3b].

# Architecture / Specification
## Submitter and Leadership Eligibility
Proposals must be authored and submitted by a representative of an AAIF member organization [^evt-working-group-proposals-file-87b3376703c5-313cc435]. While participation in working group meetings and contributions is open to everyone across the broader open-source community, working group chairs must represent Platinum, Gold, or Silver member organizations [^evt-working-group-proposals-file-87b3376703c5-313cc435]. Non-member contributors who wish to launch a working group must find an eligible member organization to sponsor and submit the proposal on their behalf [^evt-working-group-proposals-file-b33563055168-6c29ea3b].

## Application Intake Requirements
Proposals are created via the GitHub issue form `.github/ISSUE_TEMPLATE/working-group-proposal.yml` in the `aaif/working-group-proposals` repository [^evt-working-group-proposals-file-87b3376703c5-313cc435]. The application requires:
- **Submitter Information:** Full name, business email address, organization/affiliation (validating AAIF member status), and job role or title [^evt-working-group-proposals-file-87b3376703c5-313cc435].
- **Proposal Scope:** Working group title, problem statement, charter scope, and justification for why the effort cannot be accommodated as a workstream inside an existing working group [^evt-working-group-proposals-file-87b3376703c5-313cc435].
- **Revival Specifications:** When proposing the revival of a previously Concluded working group, submitters must link directly to the former working group repository, reference the archived charter, and detail the technical or ecosystem changes justifying reinstatement [^evt-working-group-proposals-file-87b3376703c5-313cc435].

## Review Workflow and Status Taxonomy
Once submitted, AAIF staff verify completeness, and the [Technical Committee](../governance/technical-committee.md) conducts asynchronous review directly on the issue [^evt-working-group-proposals-file-b33563055168-6c29ea3b]. Proposals move through standardized tracking labels:
- `New`: The proposal has been submitted and placed into the review backlog [^evt-working-group-proposals-file-b33563055168-6c29ea3b].
- `Waiting on Comment`: Reviewers have requested supplementary information or clarification from submitters [^evt-working-group-proposals-file-b33563055168-6c29ea3b].
- `Too Early`: The proposal is deemed premature, and guidance for reapplication is provided [^evt-working-group-proposals-file-b33563055168-6c29ea3b].
- `Declined`: The proposal is rejected with rationale documented in issue comments [^evt-working-group-proposals-file-b33563055168-6c29ea3b].
- `Approved`: The proposal has obtained both Technical Committee and Governing Board approvals, enabling the group to form in the Sandbox lifecycle stage [^evt-working-group-proposals-file-b33563055168-6c29ea3b].

Approval of a proposal transitions the working group into Sandbox status to begin cadence meetings, start monthly reporting under the [Working Group Monthly Reporting Template](./working-group-reporting-template.md), and draft its formal charter under the [Working Group Lifecycle Policy](../policies/working-group-lifecycle-policy.md); it does not confer Active status, which requires subsequent Technical Committee charter approval [^evt-working-group-proposals-file-b33563055168-6c29ea3b].

[^evt-working-group-proposals-file-87b3376703c5-313cc435]: https://github.com/aaif/working-group-proposals/blob/1054856f6e1307fdfb56d51abcf9a87055ee0140/.github/ISSUE_TEMPLATE/working-group-proposal.yml
[^evt-working-group-proposals-file-b33563055168-6c29ea3b]: https://github.com/aaif/working-group-proposals/blob/1054856f6e1307fdfb56d51abcf9a87055ee0140/README.md
