---
type: governance
title: Project Proposal Process
description: Operating procedure defining the 6-step workflow, engagement bar, automated
  intake agent, and onboarding process for AAIF project submissions.
resource: https://github.com/aaif/technical-committee/blob/35a3f31b27d682adc26f4f567bb2d0f2995ba909/project_proposal_process.md
tags:
- governance
- technical-committee
- project-intake
- lifecycle
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T10:02:45.557539+00:00'
sources:
- id: evt-technical-committee-file-05a7e66403db-81ecc37a
  resource: https://github.com/aaif/technical-committee/blob/35a3f31b27d682adc26f4f567bb2d0f2995ba909/project_proposal_process.md
  author: Manik Surtani
  last_modified: '2026-08-28T10:55:34+10:00'
- id: evt-technical-committee-pr-9
  resource: https://github.com/aaif/technical-committee/pull/9
  author: maniksurtani
  last_modified: '2026-08-28T04:07:05+00:00'
---

# Overview

The AAIF Project Proposal Process is the standard operating workflow for proposing, reviewing, approving, and onboarding open-source projects into the Agentic AI Foundation [^evt-technical-committee-file-05a7e66403db-81ecc37a]. While the [Project Lifecycle](../governance/project-lifecycle.md) establishes lifecycle stages (such as Sandbox, Growth, and Impact) and review criteria [^evt-technical-committee-pr-9], this process governs the operational intake pipeline.

The process enforces a distributed engagement model: rather than requiring a single dedicated sponsor, submissions must satisfy a minimum engagement bar across members of the [Technical Committee](../governance/technical-committee.md) during an offline Q&A window before moving to a formal vote [^evt-technical-committee-file-05a7e66403db-81ecc37a].

# Architecture / Specification

## Execution Pipeline

The operating process consists of six sequential steps, one parallel step, and an optional on-demand presentation [^evt-technical-committee-file-05a7e66403db-81ecc37a]:

1. **Initial Intake (Offline)**: The CTO screens submissions for completeness and technical fit, assisted by an automated intake agent that performs public compliance checks and private advisory reviews.
2. **TC Q&A Window (Offline)**: The Technical Committee reviews the proposal asynchronously via GitHub issues. If the minimum engagement bar is not met, TC chairs appoint an on-demand TC supporter to drive review or reject the submission.
   - *Optional Presentation (Live)*: Scheduled on demand if a TC member specifically requests a live presentation.
   - *Contributor Paperwork (Parallel)*: Submitter executes necessary contribution disclosures and legal preparation via the LF PMO.
3. **TC Vote (Offline)**: The Technical Committee votes on project admission and initial lifecycle tier using LFX Vote.
4. **Governing Board Approval (Offline)**: The Governing Board votes to confirm organizational readiness, funding, and resource allocation.
5. **Legal Formation (Offline)**: Linux Foundation Legal and AAIF staff finalize the technical charter, contribution agreement, and trademark transfers via DocuSign.
6. **Technical Onboarding (Offline)**: LF IT and the submitter complete repository migration and infrastructure integration.

# Lifecycle History

- **v0.3 (August 28, 2026)**: Defined operating procedure with 6-step sequential pipeline, engagement bar mechanics, automated intake agent role, and decoupled TC supporter on-demand trigger [^evt-technical-committee-file-05a7e66403db-81ecc37a].

[^evt-technical-committee-file-05a7e66403db-81ecc37a]: https://github.com/aaif/technical-committee/blob/35a3f31b27d682adc26f4f567bb2d0f2995ba909/project_proposal_process.md
[^evt-technical-committee-pr-9]: https://github.com/aaif/technical-committee/pull/9
