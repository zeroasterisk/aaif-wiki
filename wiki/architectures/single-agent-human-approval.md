---
type: architecture
title: Single-Agent Human Approval Reference Architecture
description: Reference architecture establishing an enforceable human approval gate
  and structural break between agent proposal and execution.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/53
tags:
- architecture
- human-in-the-loop
- workflows
- approval
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:46:11.619660+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-pr-53
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/53
  author: zaynelt
  last_modified: '2026-10-09T18:55:43+00:00'
---

# Overview
The Single-Agent Human Approval reference architecture defines an operational model where an autonomous agent formulates actions or remediation plans, but cannot execute them without explicit human sign-off [^evt-wg-workflows-and-process-integration-pr-53]. The architecture enforces a structural boundary ensuring that the proposal phase produces an immutable candidate execution payload while execution authority remains reserved for authorized humans or execution delegates [^evt-wg-workflows-and-process-integration-pr-53].

# Architecture / Specification
The reference architecture is structured around capability roles rather than strict deployment boundaries [^evt-wg-workflows-and-process-integration-pr-53]:
- **Separation of Authority**: The separation between proposing and executing focuses on authority, credentials, and point-of-effect boundaries rather than requiring isolated processes or distinct physical servers [^evt-wg-workflows-and-process-integration-pr-53].
- **Applicability Scope**: The architecture applies when a single agent produces the candidate proposal that an authorized operator must evaluate, distinguishing it from multi-agent critique isolation or swarm topologies [^evt-wg-workflows-and-process-integration-pr-53].
- **Protected Side Effects**: Point-of-effect protection covers non-exhaustive operational actions, including production database writes, cloud provisioning, security policy changes, and outbound messages [^evt-wg-workflows-and-process-integration-pr-53].

# Related Patterns
- [Proposal-Execution Split](../patterns/proposal-execution-split.md)
- [Human Approval Gate](../patterns/human-approval-gate.md)
- [Approval Checkpoint](../patterns/approval-checkpoint.md)

# References
- aaif/wg-workflows-and-process-integration: PR #53 (Updates based on Issue 45 TC Feedback)

[^evt-wg-workflows-and-process-integration-pr-53]: https://github.com/aaif/wg-workflows-and-process-integration/pull/53
