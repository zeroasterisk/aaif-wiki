---
type: pattern
title: Approval Checkpoint Pattern
description: Runtime governance pattern cryptographically binding authorized approvals
  to exact execution parameters and decoupling decision, execution, and effect records.
resource: https://github.com/aaif/wg-security-and-privacy/blob/e757d350133fea0858dda1deec13dbca923b3cf8/workstreams/design-patterns/DRAFT-approval_checkpoint_pattern.md
tags:
- security
- runtime-governance
- auditability
- patterns
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:18:51.650896+00:00'
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

The Approval Checkpoint Pattern binds human or policy approvals directly to the specific action that executes, enforces strict validity intervals and usage counts, and structurally separates decision records from execution records and service-reported effect receipts.[^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5] This prevents common agentic governance failures where approved actions differ from executed payloads, stale approvals are reused, or approvals are conflated with verified execution outcomes.[^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5]

# Architecture / Specification

The pattern establishes three core architectural rules:

1. **Cryptographic Action Binding**: The approval record states the tool name, target resource, arguments (directly or as a canonical digest), authorized approver, validity window, and allowed usage count.[^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5] The enforcement point independently recomputes digests from the action about to run against its own clock and tolerance skew rather than trusting client match claims.[^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5]
2. **Three-Record Architecture**:
   - **Decision Record**: Captured when approval is granted, defining authorization parameters and validity constraints.[^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5]
   - **Execution Record**: Generated when the enforcement point dispatches the action, bearing an execution identifier charged against the approval.[^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5]
   - **Effect Record**: Captured from target service response receipts, correlated to the execution ID via service-defined identifiers.[^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5]
3. **Explicit Absence and Conflict Tracking**: Missing receipts are reported as unconfirmed rather than completed or failed, and differing receipts under a single execution ID are preserved as audit conflicts.[^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5]

This pattern interfaces with the [Kill Switch Pattern](../patterns/kill-switch.md) during cooling-off dispatch queues and relies on identity standards defined by the [Identity and Trust Working Group](../working-groups/identity-and-trust.md).[^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5]

# References

- Security & Privacy Working Group Design Patterns Catalog [^evt-wg-security-and-privacy-file-9d8108887b54-74938a50]

[^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5]: https://github.com/aaif/wg-security-and-privacy/blob/e757d350133fea0858dda1deec13dbca923b3cf8/workstreams/design-patterns/DRAFT-approval_checkpoint_pattern.md
[^evt-wg-security-and-privacy-file-9d8108887b54-74938a50]: https://github.com/aaif/wg-security-and-privacy/blob/e757d350133fea0858dda1deec13dbca923b3cf8/workstreams/design-patterns/README.md
