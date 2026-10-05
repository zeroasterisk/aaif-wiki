---
type: policy
title: Project Lifecycle Policy
description: Governance policy establishing proposal intake workflows, review criteria,
  stage transitions (Growth, Impact, Emeritus), and voting requirements for hosted
  projects.
resource: https://github.com/aaif/project-proposals/blob/f95b796d901b553de20e37213c63f81f40a627a2/README.md
tags:
- governance
- policy
- project-lifecycle
- intake
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T09:48:43.703258+00:00'
sources:
- id: evt-project-proposals-file-b33563055168-aa8532b6
  resource: https://github.com/aaif/project-proposals/blob/f95b796d901b553de20e37213c63f81f40a627a2/README.md
  author: Angie Jones
  last_modified: '2026-06-07T19:02:00-05:00'
- id: evt-project-proposals-pr-35
  resource: https://github.com/aaif/project-proposals/pull/35
  author: angiejones
  last_modified: '2026-06-07T23:57:58+00:00'
---

# Overview
The Project Lifecycle Policy defines the stages, eligibility criteria, intake procedures, and review standards for open source projects hosted by the Agentic AI Foundation[^evt-project-proposals-file-b33563055168-aa8532b6]. It establishes a transparent path for external and member-contributed software to progress through foundation-hosted stages under the technical supervision of the [Technical Committee](../governance/technical-committee.md)[^evt-project-proposals-file-b33563055168-aa8532b6].

# Architecture / Specification

## Intake and Submission Process
Prospective projects submit a standardized proposal issue within the `aaif/project-proposals` intake repository[^evt-project-proposals-file-b33563055168-aa8532b6][^evt-project-proposals-pr-35]. Submitted applications follow structured lifecycle stages:
1. **Triage & Backlog:** Proposals receive initial triage and are scheduled for technical review.
2. **Review Presentation:** Project maintainers deliver a presentation to the Technical Committee with AAIF staff assistance[^evt-project-proposals-file-b33563055168-aa8532b6].
3. **Evaluation & Voting:** The Technical Committee reviews the application for alignment as either a Growth or Impact project. Acceptance requires an absolute majority vote (>50%) of all Technical Committee members, followed by ratification from the Governing Board[^evt-project-proposals-file-b33563055168-aa8532b6].

## Proposal Status Labels
Applications are tracked on the public project board with explicit status states[^evt-project-proposals-file-b33563055168-aa8532b6]:
- `New`: Newly submitted application placed in the intake backlog.
- `Approved`: Accepted into the foundation hosting structure.
- `Declined`: Application declined with documented feedback.
- `Waiting on Comment`: Review pending maintainer clarifications.
- `Too Early`: Project not yet mature enough for stage requirements.

## Reapplication and Membership Conditions
- **Reapplication Window:** Declined projects may reapply after addressing reviewer feedback, with a mandatory 3-month cooldown period showing tangible progress[^evt-project-proposals-file-b33563055168-aa8532b6].
- **Membership Neutrality:** Submitting or hosting a project does not require AAIF corporate membership, nor does project hosting confer governing board representation or corporate membership tier status[^evt-project-proposals-file-b33563055168-aa8532b6].

[^evt-project-proposals-file-b33563055168-aa8532b6]: https://github.com/aaif/project-proposals/blob/f95b796d901b553de20e37213c63f81f40a627a2/README.md
[^evt-project-proposals-pr-35]: https://github.com/aaif/project-proposals/pull/35
