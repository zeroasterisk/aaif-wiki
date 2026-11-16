---
type: pattern
title: Approval Checkpoint
description: Runtime governance pattern binding human or policy approval records to
  exact execution payloads and tracking decision, execution, and confirmed effect
  as separate audit records.
resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/workstreams/design-patterns/DRAFT-approval_checkpoint_pattern.md
tags:
- security
- runtime-governance
- authorization
- auditability
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:21:56.668978+00:00'
sources:
- id: evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5
  resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/workstreams/design-patterns/DRAFT-approval_checkpoint_pattern.md
  author: sagardashora
  last_modified: '2026-09-30T10:16:03-04:00'
- id: evt-wg-security-and-privacy-pr-26
  resource: https://github.com/aaif/wg-security-and-privacy/pull/26
  author: sagardashora
  last_modified: '2026-09-30T14:16:03+00:00'
---

# Overview
The Approval Checkpoint pattern binds an authorized human or policy decision to the exact action payload that executes, enforcing strict validity windows and maintaining three structurally decoupled audit records: decision, execution attempt, and confirmed effect.[^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5] Maintained under the [Security and Privacy Working Group](../working-groups/security-and-privacy.md) design patterns catalog, the pattern mitigates failure modes where approval flags are reused after expiration, applied to modified parameters, or conflated with confirmed downstream execution.[^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5][^evt-wg-security-and-privacy-pr-26]

# Architecture / Specification
The pattern formalizes enforcement semantics across three distinct lifecycle phases:

1. **Binding Approval to Action**: An approval record explicitly binds the action or tool identifier, target resource, arguments (either directly or as a cryptographic digest over a named canonical serialization), constraints, approver identity, validity interval, and usage limits.[^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5] For sensitive payloads, digests preserve data minimization. Where dynamic variance is legitimate (such as timestamps), allowed variance fields must be explicitly enumerated.[^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5]
2. **Execution-Point Verification**: Verification occurs strictly at the enforcement point where the action is executed. The enforcement point independently recomputes bound fields and digests directly from the candidate payload, ignoring self-reported claims from the agent.[^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5] Validity intervals are verified against the enforcement point's clock with defined skew tolerance. If an approval record fails integrity verification, it is flagged as an integrity failure rather than a mismatch; if unavailable, execution is denied.[^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5]
3. **Tripartite Record Decoupling**: Systems must record decision, execution, and effect as separate, correlated entities:
   - **Decision Record**: Captures the approval authority, validity window, and bound action digest.[^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5]
   - **Execution Record**: Tracks the execution attempt using an execution identifier assigned by the enforcement point, against which usage quotas are charged.[^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5]
   - **Effect Record**: Documents the confirmation returned by the downstream target service, correlated by a service-scoped receipt identifier. Absence of confirmation designates an unconfirmed effect, not non-occurrence.[^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5]

# Lifecycle History
Candidate specification drafted by the Security and Privacy Working Group within the [Security and Privacy Design Patterns Catalog](../resources/security-and-privacy-design-patterns-catalog.md) as pattern category Runtime Governance (SP-XXX).[^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5][^evt-wg-security-and-privacy-pr-26] Intersects with the [Kill Switch](kill-switch.md) pattern when cooling-off queues hold high-risk actions pending release.[^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5]

# References
- Catalog Draft: `workstreams/design-patterns/DRAFT-approval_checkpoint_pattern.md`[^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5]
- Implementation Guidance: [Agentic AI Security Best Practices](../guidelines/agentic-ai-security-best-practices.md)[^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5]

[^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5]: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/workstreams/design-patterns/DRAFT-approval_checkpoint_pattern.md
[^evt-wg-security-and-privacy-pr-26]: https://github.com/aaif/wg-security-and-privacy/pull/26
