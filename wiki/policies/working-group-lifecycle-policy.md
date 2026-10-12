---
type: policy
title: Working Group Lifecycle Policy
description: Governance policy defining the Sandbox, Active, and Concluded stages,
  annual renewal terms, voting rules, and reporting cadences for AAIF Working Groups.
resource: https://github.com/aaif/technical-committee/blob/fe99a96791381e68eb40e8e5885690ddd08fbfb1/working-groups/lifecycle-policy.md
tags:
- governance
- policy
- working-groups
- technical-committee
- lifecycle
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
The Working Group Lifecycle Policy governs how Agentic AI Foundation (AAIF) Working Groups are proposed, chartered, operated, renewed, and concluded[^evt-technical-committee-file-6f2428968391-033df704]. Designed to sustain an active portfolio with minimal administrative overhead, the policy draws governance mechanisms from CNCF Technical Advisory Groups, OpenSSF and Kubernetes working groups, W3C time-bound charters, and the Apache Attic[^evt-technical-committee-file-6f2428968391-033df704]. It operates alongside a mandatory monthly asynchronous progress reporting mechanism that provides health signals to the Technical Committee[^evt-technical-committee-file-86b96cfaa5c4-64c967b8].

Working group governance is administered under the oversight of the [Technical Committee](../governance/technical-committee.md) and complements project intake managed through the [Project Lifecycle Policy](../policies/project-lifecycle-policy.md)[^evt-technical-committee-file-6f2428968391-033df704].

# Architecture / Specification

## Lifecycle Stages
Working Groups navigate three formal lifecycle stages following proposal approval[^evt-technical-committee-file-6f2428968391-033df704]:

1. **Sandbox**: Upon initial approval by the TC, a working group enters Sandbox for six weeks (extendable once by up to six weeks)[^evt-technical-committee-file-6f2428968391-033df704]. The group meets and drafts its operational charter. Groups that fail to produce a viable charter transition directly to Concluded[^evt-technical-committee-file-6f2428968391-033df704].
2. **Active**: Chartered groups delivering against active objectives operate under 12-month charter periods and undergo annual renewal reviews by the TC[^evt-technical-committee-file-6f2428968391-033df704].
3. **Concluded**: Groups that achieve their deliverables or cease active operations move to an open-ended archive state preserving their public records, deliverables, and meeting history[^evt-technical-committee-file-6f2428968391-033df704]. A concluded group may be revived back into Sandbox through a formal revival proposal[^evt-technical-committee-file-6f2428968391-033df704].

## Participation and Leadership Entitlements
Working group responsibilities are structured according to member tiers[^evt-technical-committee-file-6f2428968391-033df704]:
- **Participation**: Open to anyone across the broader community without membership restrictions[^evt-technical-committee-file-6f2428968391-033df704].
- **Proposals and Revivals**: May be submitted by representatives from any AAIF member organization (Platinum, Gold, Silver, or Associate)[^evt-technical-committee-file-6f2428968391-033df704]. Non-members may partner with member sponsors[^evt-technical-committee-file-6f2428968391-033df704].
- **Leadership**: Working group chairs and co-chairs must represent Platinum, Gold, or Silver member organizations, with leadership distributed across at least two distinct organizations[^evt-technical-committee-file-6f2428968391-033df704].
- **Contested Elections**: Voting in contested chair elections is restricted to participants affiliated with Platinum, Gold, or Silver member organizations[^evt-technical-committee-file-6f2428968391-033df704].

## Technical Committee Decisions and Voting
TC oversight decisions are made primarily by asynchronous lazy consensus on GitHub issues or pull requests over a 7-day objection window[^evt-technical-committee-file-6f2428968391-033df704]. Any objection forces a formal roll-call vote decided by simple majority[^evt-technical-committee-file-6f2428968391-033df704]. Three actions strictly require recorded votes[^evt-technical-committee-file-6f2428968391-033df704]:
- Approving a new Working Group (subject to subsequent Governing Board confirmation)[^evt-technical-committee-file-6f2428968391-033df704].
- Retiring a Working Group to Concluded status without the consent of its chairs[^evt-technical-committee-file-6f2428968391-033df704].
- Removing a chair, requiring a two-thirds supermajority of all TC members[^evt-technical-committee-file-6f2428968391-033df704].

## Monthly Progress Reporting
Working Groups submit a monthly report formatted as `reporting/YYYY-MM-report.md` via pull request to their respective repositories by the last business day of each month[^evt-technical-committee-file-86b96cfaa5c4-64c967b8]. Pull requests carry the `monthly-report` label and PR title `[Report] <YYYY-MM>`[^evt-technical-committee-file-86b96cfaa5c4-64c967b8]. The TC reviews asynchronously within a 7-calendar-day window[^evt-technical-committee-file-86b96cfaa5c4-64c967b8]. Missing two consecutive monthly reports triggers a mandatory live escalation check-in during the next TC sync[^evt-technical-committee-file-86b96cfaa5c4-64c967b8].

# Lifecycle History
- **2026-06-01**: Working Group Monthly Reporting framework entered into effect[^evt-technical-committee-file-86b96cfaa5c4-64c967b8].
- **2026-10-02**: Working Group Lifecycle Policy Revision 2 adopted as final by the Technical Committee[^evt-technical-committee-file-6f2428968391-033df704].

[^evt-technical-committee-file-6f2428968391-033df704]: https://github.com/aaif/technical-committee/blob/fe99a96791381e68eb40e8e5885690ddd08fbfb1/working-groups/lifecycle-policy.md
[^evt-technical-committee-file-86b96cfaa5c4-64c967b8]: https://github.com/aaif/technical-committee/blob/fe99a96791381e68eb40e8e5885690ddd08fbfb1/working-groups/reporting.md
