---
type: architecture
title: Single-Agent Process with Human Approval
description: Reference architecture establishing an enforceable human approval gate
  and structural separation between agent proposal construction and workflow-controlled
  execution.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/architectures/single-agent-human-approval.md
tags:
- architecture
- reference-architecture
- human-approval
- workflows
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:14:40.565482+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-a4fea1b2d544-d6bb99fb
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/architectures/single-agent-human-approval.md
  author: Mario Zagar
  last_modified: '2026-10-02T11:51:25-07:00'
- id: evt-wg-workflows-and-process-integration-pr-50
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/50
  author: mzagar
  last_modified: '2026-10-02T18:51:26+00:00'
- id: evt-wg-workflows-and-process-integration-issue-45
  resource: https://github.com/aaif/wg-workflows-and-process-integration/issues/45
  author: geemus
  last_modified: '2026-10-03T00:58:32+00:00'
---

# Overview

The Single-Agent Process with Human Approval reference architecture establishes an enterprise workflow pattern where an AI agent plans and drafts a proposed action, a designated human approves or rejects the submission, and an independent workflow-controlled executor carries out the protected effect.[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-d6bb99fb] It applies when an agent's output can alter real-world environments—such as executing financial refunds, modifying production configurations, or publishing external communications—and the organization mandates enforceable authorization at the point of impact due to high reversal costs, auditability constraints, or explicit human decision ownership.[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-d6bb99fb]

Under this architecture, a high-level business task is differentiated from the discrete workflow activities executed to satisfy it.[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-d6bb99fb] [^evt-wg-workflows-and-process-integration-pr-50]

# Architecture / Specification

The architecture composes three foundational design patterns:
- [Proposal/execution split](../patterns/proposal-execution-split.md): Enforces a structural separation ensuring the reasoning agent lacks permissions to invoke the capability causing the protected effect directly.[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-d6bb99fb]
- [Human approval gate](../patterns/human-approval-gate.md): Mandates that a designated human reviewer validate the exact payload before any state change occurs.[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-d6bb99fb]
- [Durable wait](../patterns/durable-wait.md): Converts long-running human review waits into persisted state records, allowing workflows to survive crashes, restarts, or deploys without losing pending tasks.[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-d6bb99fb]

### Invariants and Guarantees
1. **Protected effect authorization**: No protected effect occurs without an explicit human approval record, and the executed payload is guaranteed to match the approved proposal rather than a modified revision.[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-d6bb99fb]
2. **Durable suspension**: Runs can pause across hours or days while awaiting sign-off; platform restarts do not drop pending reviews or duplicate executed steps.[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-d6bb99fb]
3. **Deterministic exit states**: Every execution terminates in a defined end state, maintaining an immutable chain of intent, decision, and effect (proposer, approver, executor) in the audit system of record.[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-d6bb99fb]

### Structural Capabilities
Operating this workflow requires seven capability roles: an execution engine, an agent reasoning runtime, a tool access layer, a state/context store, a human interaction surface, a workflow-controlled executor, and an audit log.[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-d6bb99fb] Working group review has highlighted open inquiries into whether the executor requires a separate host process or can execute within an isolated harness step, as well as refining selection criteria for multi-agent escalation.[^evt-wg-workflows-and-process-integration-issue-45]

[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-d6bb99fb]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/architectures/single-agent-human-approval.md
[^evt-wg-workflows-and-process-integration-issue-45]: https://github.com/aaif/wg-workflows-and-process-integration/issues/45
[^evt-wg-workflows-and-process-integration-pr-50]: https://github.com/aaif/wg-workflows-and-process-integration/pull/50
