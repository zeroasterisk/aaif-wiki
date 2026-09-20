---
type: specification
title: Human Approval Gate
description: A workflow pattern ensuring a named human must explicitly approve or
  reject an immutable proposal before a protected effect can occur.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/patterns/human-approval-gate.md
tags:
- pattern
- workflow
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-flash-latest
  at: '2026-09-20T17:48:22.618496+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/patterns/human-approval-gate.md
  author: Zayne Turner
  last_modified: '2026-08-05T23:05:12-04:00'
- id: evt-wg-workflows-and-process-integration-pr-20
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/20
  author: zaynelt
  last_modified: '2026-08-06T03:05:13+00:00'
---

# Overview

The Human Approval Gate pattern addresses the need for human judgment and accountability before a workflow executes an action with high risk, audit obligations, or ownership requirements [^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428]. It is used in architectures such as the single-agent process with human approval.

# Architecture / Specification

The pattern requires presenting an immutable proposal to a uniquely identified, authorized human principal. The workflow enters a durable wait state until an explicit decision (approve or reject) is recorded, bound to that specific proposal version. Timeout and escalation paths must be explicit outcomes, never resulting in implicit approval [^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428].

## Invariants

Key invariants that must hold in any implementation include:

*   The approver must be a uniquely identified human principal authorized for the decision class; shared approval identities are prohibited.
*   The interaction surface must display the exact, immutable proposal version.
*   Approval and rejection must be explicit decisions; silence, timeout, or system error never constitute approval.
*   The decision record must capture the proposal version, approver identity, decision, and timestamp under the same run identity.
*   A changed proposal requires a new approval decision.
*   Pending approval has a deadline and a defined expiry or escalation path.
*   Duplicate, late, or conflicting decision events cannot resume or execute the run more than once [^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428].

## Related Patterns

This pattern is related to the Proposal/Execution Split and Durable Wait patterns [^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428].

[^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428]: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/patterns/human-approval-gate.md
