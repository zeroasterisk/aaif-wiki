---
type: pattern
title: Approval Checkpoint
description: Runtime governance pattern binding approval records to exact execution
  payloads and tracking decision, execution, and confirmation states independently.
resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/workstreams/design-patterns/DRAFT-approval_checkpoint_pattern.md
tags:
- security
- runtime-governance
- pattern
- access-control
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:13:19.023330+00:00'
sources:
- id: evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5
  resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/workstreams/design-patterns/DRAFT-approval_checkpoint_pattern.md
  author: sagardashora
  last_modified: '2026-09-30T10:16:03-04:00'
- id: evt-wg-security-and-privacy-file-3bbe1dee7e1d-99b84ed8
  resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/workstreams/design-patterns/DRAFT-design_patterns_catalog.md
  author: sagardashora
  last_modified: '2026-09-30T10:16:03-04:00'
---

# Overview
The Approval Checkpoint pattern binds human or automated policy approvals directly to specific action payloads and validity constraints, ensuring executed actions cannot silently deviate from what was authorized[^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5]. It decouples authorization decisions from execution attempts and downstream effect receipts to maintain clear provenance across asynchronous or retried operations[^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5].

# Architecture / Specification
Runtime policy enforcement points validate that incoming agent actions match bound parameters, target identifiers, and digest values computed over canonical representations prior to dispatch[^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5]. The pattern segregates state tracking across three distinct records:
1. **Decision Record**: Captures the approval authority, validity interval, scope, constraints, and canonical payload digest.
2. **Execution Record**: Tracks execution attempts and assigns unique enforcement point identifiers, charging against approval quota limits.
3. **Effect Record**: Logs verified target service confirmation responses, treating missing confirmations as unconfirmed rather than absent.

This pattern complements [Proposal-Execution Split](../patterns/proposal-execution-split.md) and [Deterministic Acceptance Gate](../patterns/deterministic-acceptance-gate.md) by providing cryptographically bound verification at runtime execution boundaries[^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5].

[^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5]: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/workstreams/design-patterns/DRAFT-approval_checkpoint_pattern.md
