---
type: guideline
title: Working Group Submission Guidelines
description: Submission workflow, evaluation criteria, voting thresholds, and tracking
  statuses for proposing new AAIF working groups.
resource: https://github.com/aaif/working-group-proposals/blob/5c17275468b2e8859b7eb261e53f7ad4d19a9ed8/README.md
tags:
- governance
- working-groups
- proposals
- technical-committee
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T09:33:44.108799+00:00'
sources:
- id: evt-working-group-proposals-file-b33563055168-33233981
  resource: https://github.com/aaif/working-group-proposals/blob/5c17275468b2e8859b7eb261e53f7ad4d19a9ed8/README.md
  author: Christina Harter
  last_modified: '2026-06-10T09:24:18-07:00'
---

# Overview
The Working Group Submission Guidelines define the formal intake, evaluation, and approval process for chartering new working groups under the Agentic AI Foundation (AAIF)[^evt-working-group-proposals-file-b33563055168-33233981]. Any prospective working group must submit a structured application to ensure alignment with foundation goals, establish an initial leadership team, and undergo technical review.

# Architecture / Specification

## Submission and Intake Process
Proposals to form a new working group are submitted via GitHub issue forms in the `aaif/working-group-proposals` repository using the standardized working group proposal template[^evt-working-group-proposals-file-b33563055168-33233981]. Submitted proposals are automatically ingested onto the public Working Group Proposals tracking board and placed in the backlog for triage[^evt-working-group-proposals-file-b33563055168-33233981].

## Evaluation and Voting Governance
Working group proposals are reviewed and voted on by the Technical Committee ([governance/technical-committee](../governance/technical-committee.md)) during scheduled meetings[^evt-working-group-proposals-file-b33563055168-33233981]:
- **Review Scheduling**: Triage places submitted proposals onto the agenda for an upcoming TC meeting.
- **Voting Threshold**: Acceptance requires a simple majority vote of all members of the Technical Committee[^evt-working-group-proposals-file-b33563055168-33233981].
- **Governing Board Ratification**: Acceptance by the Technical Committee is subject to final approval by the AAIF Governing Board[^evt-working-group-proposals-file-b33563055168-33233981].

## Proposal Status Lifecycle
Proposal progression is tracked using standard repository issue labels[^evt-working-group-proposals-file-b33563055168-33233981]:
- `New`: The proposal is newly submitted and queued in the triage backlog.
- `Waiting on Comment`: Reviewers have posted inquiries requiring submitter clarification or additional detail.
- `Too Early`: The proposal is deemed premature; guidance is provided for potential reapplication.
- `Declined`: The proposal has been declined by the TC, with explanatory feedback recorded in issue comments.
- `Approved`: The proposal has met all intake criteria and achieved requisite approvals.

# References
- [Policies: Working Group Lifecycle Policy](../policies/working-group-lifecycle-policy.md)
- [Governance: Technical Committee](../governance/technical-committee.md)

[^evt-working-group-proposals-file-b33563055168-33233981]: https://github.com/aaif/working-group-proposals/blob/5c17275468b2e8859b7eb261e53f7ad4d19a9ed8/README.md
