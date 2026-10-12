---
type: policy
title: Project Proposal Process
description: Operating procedure defining the six-stage intake, automated compliance
  review, TC engagement bar, and LFX voting process for AAIF project proposals.
resource: https://github.com/aaif/technical-committee/blob/fe99a96791381e68eb40e8e5885690ddd08fbfb1/project_proposal_process.md
tags:
- governance
- intake
- technical-committee
- lifecycle
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T02:53:46.880870+00:00'
sources:
- id: evt-technical-committee-file-05a7e66403db-81ecc37a
  resource: https://github.com/aaif/technical-committee/blob/fe99a96791381e68eb40e8e5885690ddd08fbfb1/project_proposal_process.md
  author: Manik Surtani
  last_modified: '2026-08-28T10:55:34+10:00'
---

# Overview
The AAIF Project Proposal Process is the operational workflow through which software projects, libraries, and specifications are submitted, evaluated, approved, and onboarded into the Agentic AI Foundation[^evt-technical-committee-file-05a7e66403db-81ecc37a]. Governed by the Technical Committee in coordination with the Governing Board, the process implements the entry rules set out in the [Project Lifecycle Policy](../policies/project-lifecycle-policy.md) through an asynchronous, offline-first intake pipeline[^evt-technical-committee-file-05a7e66403db-81ecc37a].

The procedure is designed around an engagement bar rather than requiring dedicated single champions, ensuring broad Technical Committee consensus and early risk identification before advancing to a formal admission vote[^evt-technical-committee-file-05a7e66403db-81ecc37a].

# Architecture / Specification

## Roles and Responsibilities
The process assigns responsibilities across key governance actors[^evt-technical-committee-file-05a7e66403db-81ecc37a]:
- **Project Submitter**: Files the proposal, addresses technical inquiries on the GitHub tracking issue, conducts optional presentations, and completes contributor agreements.
- **CTO**: Oversees Step 1 intake triage, runs initial smoke tests alongside the intake agent, prepares committee briefs, and handles Q&A extension requests.
- **Intake Agent**: Automated bot executing public technical compliance checks on the proposal issue and delivering advisory compliance reviews to private Technical Committee channels.
- **TC Chairs**: Provide oversight during triage and recruit an on-demand TC Supporter if the proposal stalls at the engagement bar.
- **TC Supporter (On-Demand)**: A [Technical Committee](../governance/technical-committee.md) member assigned only when baseline committee engagement is unmet, responsible for championing the proposal through a reset Q&A window.
- **Technical Committee**: Evaluates proposal architecture, asks questions during the public Q&A window, and casts votes on technical merit and initial lifecycle stage.
- **Governing Board**: Votes on budget allocation, legal exposure, and organizational alignment.
- **LF PMO, Legal, and IT**: Manage asynchronous paperwork, contribution agreements, charter drafting, and technical repository onboarding.

## Six-Stage Intake Workflow
The intake pipeline operates primarily offline and asynchronously across six sequential steps and one parallel track[^evt-technical-committee-file-05a7e66403db-81ecc37a]:
1. **Initial Intake**: The project proposal is submitted via GitHub. The Intake Agent performs static compliance and licensing checks, alerting the CTO and TC Chairs. The CTO verifies completeness and strategic fit.
2. **TC Q&A Window**: A time-boxed asynchronous review window on GitHub where TC members review the proposal. The proposal must satisfy the engagement bar (a mandatory quorum of distinct TC member interactions) to advance. An optional live presentation may be scheduled upon TC request. If the engagement bar is unmet, TC Chairs appoint an on-demand supporter or reject the proposal.
- **Contributor Paperwork (Parallel Track)**: Concurrently with Step 2, submitters complete Linux Foundation contributor documentation via LF PMO.
3. **TC Vote**: The Technical Committee votes asynchronously via LFX Vote to approve project admission and assign its initial lifecycle stage.
4. **GB Approval**: The Governing Board votes via LFX Vote to authorize organizational resource commitments and legal acceptance.
5. **LF Legal Formation**: LF Legal coordinates signing of technical charters, IP transfers, and contribution agreements via DocuSign.
6. **Technical Onboarding**: LF IT transfers repositories, configures access controls, and provisions foundation CI/CD infrastructure.

# Lifecycle History
Version 0.3 of the operating procedure took effect on August 28, 2026, codifying intake agent automation, replacing single-champion requirements with the engagement bar, and formalizing LFX Vote tooling[^evt-technical-committee-file-05a7e66403db-81ecc37a].

[^evt-technical-committee-file-05a7e66403db-81ecc37a]: https://github.com/aaif/technical-committee/blob/fe99a96791381e68eb40e8e5885690ddd08fbfb1/project_proposal_process.md
