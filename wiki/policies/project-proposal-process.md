---
type: policy
title: Project Proposal Process
description: Operating procedure defining intake criteria, contribution agreements,
  triage roles, and joint TC and Governing Board review gates for AAIF projects.
resource: https://github.com/aaif/project-proposals/blob/f95b796d901b553de20e37213c63f81f40a627a2/.github/ISSUE_TEMPLATE/project-proposal.yml
tags:
- governance
- policy
- project-intake
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:19:24.664549+00:00'
sources:
- id: evt-project-proposals-file-6c7de919a622-a1bc6ba1
  resource: https://github.com/aaif/project-proposals/blob/f95b796d901b553de20e37213c63f81f40a627a2/.github/ISSUE_TEMPLATE/project-proposal.yml
  author: Manik Surtani
  last_modified: '2026-09-06T17:37:26+08:00'
---

# Overview

The Project Proposal Process defines the intake workflow and review gates for open-source projects applying to become official AAIF Hosted Projects across the Sandbox, Growth, and Impact maturity tiers [^evt-project-proposals-file-6c7de919a622-a1bc6ba1]. The process requires formal alignment analysis, an executed legal Contribution Agreement, and affirmative approval votes from both the Technical Committee (TC) and the Governing Board (GB) [^evt-project-proposals-file-6c7de919a622-a1bc6ba1].

# Architecture / Specification

## Intake and Triage

Applications are submitted via the structured GitHub issue template in the `aaif/project-proposals` repository labeled `New` [^evt-project-proposals-file-6c7de919a622-a1bc6ba1]. Applicants must detail:

- Project origins, capabilities, and technical maturity [^evt-project-proposals-file-6c7de919a622-a1bc6ba1].
- Alignment with the AAIF mission and ecosystem [^evt-project-proposals-file-6c7de919a622-a1bc6ba1].
- Architectural relationship to existing AAIF hosted projects and specifications [^evt-project-proposals-file-6c7de919a622-a1bc6ba1].

## Contribution Agreement and Dual Approval Gates

1. **Contribution Agreement**: A legal Contribution Agreement is sent to designated project contacts based on submission information. This agreement must be signed before the Governing Board can conduct a formal acceptance vote [^evt-project-proposals-file-6c7de919a622-a1bc6ba1].
2. **TC and GB Approval**: Official acceptance requires affirmative votes by both the Technical Committee (see [../governance/technical-committee.md](../governance/technical-committee.md)) and the Governing Board [^evt-project-proposals-file-6c7de919a622-a1bc6ba1].
3. **Linux Foundation Countersignature**: The Linux Foundation countersigns the Contribution Agreement only after a successful Governing Board vote [^evt-project-proposals-file-6c7de919a622-a1bc6ba1].
4. **Representation Restrictions**: Maintainers cannot represent their project as "donated" or "contributed" until both voting gates succeed and the Contribution Agreement is countersigned [^evt-project-proposals-file-6c7de919a622-a1bc6ba1].

[^evt-project-proposals-file-6c7de919a622-a1bc6ba1]: https://github.com/aaif/project-proposals/blob/f95b796d901b553de20e37213c63f81f40a627a2/.github/ISSUE_TEMPLATE/project-proposal.yml
