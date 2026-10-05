---
type: pattern
title: Approval Checkpoint Pattern
description: Runtime governance pattern binding approvals to exact executed actions
  and separately maintaining decision, execution, and confirmed service effect records.
resource: https://github.com/aaif/wg-security-and-privacy/blob/e757d350133fea0858dda1deec13dbca923b3cf8/workstreams/design-patterns/DRAFT-approval_checkpoint_pattern.md
tags:
- runtime-governance
- approval
- integrity
- accountability
- auditability
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:50:41.603890+00:00'
sources:
- id: evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5
  resource: https://github.com/aaif/wg-security-and-privacy/blob/e757d350133fea0858dda1deec13dbca923b3cf8/workstreams/design-patterns/DRAFT-approval_checkpoint_pattern.md
  author: sagardashora
  last_modified: '2026-09-30T10:16:03-04:00'
- id: evt-wg-security-and-privacy-file-9d8108887b54-74938a50
  resource: https://github.com/aaif/wg-security-and-privacy/blob/e757d350133fea0858dda1deec13dbca923b3cf8/workstreams/design-patterns/README.md
  author: sagardashora
  last_modified: '2026-09-30T10:16:03-04:00'
---

# Overview

The Approval Checkpoint pattern binds a human or policy approval directly to the exact action that executes, constraining its validity interval and usage count while strictly separating the approval decision from execution attempts and confirmed target effects [^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5]. This prevents common failure modes such as approval reuse, action alteration post-approval, and treating unverified approvals as proof of execution [^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5].

# Architecture / Specification

The pattern structures runtime action governance around cryptographic binding and three-tier record keeping [^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5]:

- **Action Binding:** The approval record explicitly identifies the target action, arguments or artifact digest (computed over a defined canonical form), validity window, permitted variations, and usage limits [^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5].
- **Enforcement Point Verification:** The policy enforcement point recomputes argument bindings from the action about to run and checks them against its local clock, rejecting expired, exhausted, or mismatched approvals without granting new authority [^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5].
- **Three-Tier Record Model:** Decouples the *decision* (approval record), the *execution attempt* (bearing an enforcement execution ID), and the *confirmed effect* (target service receipt/identifier) [^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5].
- **Explicit Absence and Conflict Tracking:** Unconfirmed actions are recorded as unconfirmed rather than non-occurrences, and disagreeing service receipts for retried execution identifiers remain visible as audit conflicts [^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5].

# References

- Developed under the [Security & Privacy Working Group](../working-groups/security-and-privacy.md) Design Patterns Catalog [^evt-wg-security-and-privacy-file-9d8108887b54-74938a50].
- Related to [Human Approval Gate](../patterns/human-approval-gate.md) and [Proposal Execution Split](../patterns/proposal-execution-split.md) [^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5].

[^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5]: https://github.com/aaif/wg-security-and-privacy/blob/e757d350133fea0858dda1deec13dbca923b3cf8/workstreams/design-patterns/DRAFT-approval_checkpoint_pattern.md
[^evt-wg-security-and-privacy-file-9d8108887b54-74938a50]: https://github.com/aaif/wg-security-and-privacy/blob/e757d350133fea0858dda1deec13dbca923b3cf8/workstreams/design-patterns/README.md
