---
type: pattern
title: Human Approval Gate
description: Workflow governance pattern requiring authorized human review before
  executing sensitive agent actions.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/human-approval-gate.md
tags:
- pattern
- governance
- approval
- workflow
- human-in-the-loop
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T10:00:37.486962+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/human-approval-gate.md
  author: Zayne Turner
  last_modified: '2026-08-05T23:05:12-04:00'
---

# Overview

The Human Approval Gate pattern halts an automated agent execution workflow until a uniquely identified, accountable human principal renders an explicit decision bound to an immutable proposal version [^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428]. It establishes an enforceable barrier between speculative intent generation and side-effect execution for actions carrying significant legal, regulatory, financial, or operational risk [^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428].

# Architecture / Specification

The pattern addresses operational tensions where human response latency exceeds process lifetimes and where ambiguous approval flags fail to provide non-repudiation [^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428].

```text
immutable proposal ──► present to authorized human ──► explicit decision
                              │                           │
                              └── durable wait ─────────┘
                                          │
                          decision record: who · what · when
```

### Core Invariants
Every conformant implementation must satisfy the following rules [^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428]:
1. **Authorized Individual Principal**: The approver must be an individually authenticated human holding explicit authorization for the decision category; shared accounts are prohibited.
2. **Immutable Proposal Binding**: The presentation surface must display the exact, immutable proposal version against which the decision record binds.
3. **Explicit Decision Requirement**: Silence, timeout, channel errors, or transport failures must never default to approval.
4. **Audit Provenance**: The decision record must log the proposal version, approver identity, action, and timestamp under a unified run identity.
5. **Proposal Mutation Reset**: Any superseding proposal or modification invalidates pending state and mandates a fresh approval cycle.
6. **Defined Expiry & Escalation**: Inactive reviews must follow explicit timeout or escalation paths.
7. **Idempotency & Replay Protection**: Race conditions, late approvals, or duplicate decision submissions cannot trigger execution more than once.

# Lifecycle History

Defined by the Workflows & Process Integration Working Group as a foundational pattern within reference architectures such as Single-Agent Human Approval [^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428].

# References

- Single Agent Human Approval: `../architectures/single-agent-human-approval.md`
- Proposal Execution Split: `../patterns/proposal-execution-split.md`
- Durable Wait: `../patterns/durable-wait.md`
- Approval Checkpoint: `../patterns/approval-checkpoint.md`

[^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/human-approval-gate.md
