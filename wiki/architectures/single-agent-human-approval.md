---
type: architecture
title: Single-Agent Process with Human Approval
description: Reference architecture establishing an enforceable human approval gate
  and structural break between agent proposal generation and protected execution.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/architectures/single-agent-human-approval.md
tags:
- architecture
- human-in-the-loop
- governance
- workflows
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T03:15:53.446387+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-a4fea1b2d544-d6bb99fb
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/architectures/single-agent-human-approval.md
  author: Mario Zagar
  last_modified: '2026-10-02T11:51:25-07:00'
- id: evt-wg-workflows-and-process-integration-pr-50
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/50
  author: mzagar
  last_modified: '2026-10-02T18:51:26+00:00'
---

# Overview

The Single-Agent Process with Human Approval reference architecture defines an operational model where an autonomous agent prepares a candidate action, an authorized human reviews and decides on the proposal, and a decoupled executor enacts the effect only after recording explicit approval [^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-d6bb99fb]. It enforces behavioral boundaries whenever an agent's reasoning may alter external systems—such as disbursing refunds, updating production configurations, or publishing public communications—requiring non-repudiable human ownership and strict regulatory defensibility.

The architecture establishes a strict conceptual distinction between the overarching business task (the client request or incident being managed) and the discrete workflow activities executed to satisfy it [^evt-wg-workflows-and-process-integration-pr-50]. By default, workflows route through a single reasoning agent unless concrete constraints—such as mandatory separation of duties, independent concurrent reasoning streams, or cross-organizational domain boundaries—compel multi-agent topologies [^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-d6bb99fb].

# Architecture / Specification

```
+--------------------------------------------------------------------------+
|                             Workflow Engine                              |
|                                                                          |
|  [Business Task]                                                         |
|         |                                                                |
|         v                                                                |
|   +-----------+      Proposal       +-------------------+                |
|   |   Agent   | ------------------> |   Human Approval  |                |
|   | Activity  |   (Payload Hash)    |        Gate       |                |
|   +-----------+                     +-------------------+                |
|         |                                     |                          |
|         | Read-only / Sandbox                 | Approved Verdict         |
|         v                                     v                          |
|   +-----------+                     +-------------------+   Side-Effect  |
|   | Context & |                     | Workflow Executor | -------------> |
|   |   Tools   |                     |     Activity      |                |
|   +-----------+                     +-------------------+                |
|                                               |                          |
|                                               v                          |
|                                        +--------------+                  |
|                                        |  Audit Log   |                  |
|                                        +--------------+                  |
+--------------------------------------------------------------------------+
```

### Pattern Composition

The architecture composes three core workflow patterns [^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-d6bb99fb]:
1. `../patterns/proposal-execution-split.md`: The agent investigates context, synthesizes arguments, and formats the proposal payload, but lacks direct access to external mutation capabilities.
2. `../patterns/human-approval-gate.md`: A designated individual inspects the immutable proposal, evaluating its rationale and execution parameters before emitting a cryptographic or non-repudiable verdict.
3. `../patterns/durable-wait.md`: Because human evaluations introduce asynchronous delays ranging from minutes to days, workflow state persists durably across system restarts, process crashes, or infrastructure deployments.

### Architectural Invariants

- **Zero Protected Effects Without Human Approval**: The workflow-controlled executor will not fire absent an authenticated approval token bound to the exact payload hash [^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-d6bb99fb].
- **Resilience Across Wait States**: Process interruption or orchestrator redeployment during approval wait states retains pending proposal integrity without triggering orphaned or duplicate actions [^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-d6bb99fb].
- **Deterministic Audit Binding**: Every run concludes in a verifiable state recording the full lineage chain—proposer agent identity, human decision authority, and executor confirmation—into the system of record [^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-d6bb99fb].

# References

- Composed pattern specifications: `../patterns/proposal-execution-split.md`, `../patterns/human-approval-gate.md`, `../patterns/durable-wait.md`
- Taxonomy primitives: `../taxonomy/workflow-primitives.md`

[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-d6bb99fb]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/architectures/single-agent-human-approval.md
[^evt-wg-workflows-and-process-integration-pr-50]: https://github.com/aaif/wg-workflows-and-process-integration/pull/50
