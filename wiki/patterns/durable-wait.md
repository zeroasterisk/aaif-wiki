---
type: pattern
title: Durable Wait
description: Architectural pattern converting blocking process waits into persisted,
  discoverable state records that survive host restarts and resume upon correlated
  external events.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/durable-wait.md
tags:
- patterns
- workflows
- orchestration
- persistence
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T14:59:02.868270+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/durable-wait.md
  author: Mario Zagar
  last_modified: '2026-08-25T07:58:21-07:00'
---

# Overview
The Durable Wait pattern transforms a physical, thread-blocking wait into a logical, recorded park state so that long-running workflows can outlive transient host processes[^evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7]. While parked, the workflow state record is the entire representation of the run, allowing underlying compute instances to terminate or redeploy without losing progress[^evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7].

# Architecture / Specification
When an execution reaches a wait condition (such as awaiting a human approval gate, external webhook, or timer), the execution engine records its execution state, activity position, and correlation identity before parking the run[^evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7].

Core invariants required for any compliant implementation include[^evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7]:
- **Process Survival**: A parked run survives process death, restarts, and infrastructure deployments.
- **Context Restoration**: Resume operations restore the exact activity position, inputs, and intermediate state context without requiring recomputation.
- **Idempotency**: Duplicate wake-up event deliveries result in a single, idempotent resumption.
- **Discoverability**: Parked runs remain queryable and discoverable across engine restarts.

# References
- Complements [Human Approval Gate](../patterns/human-approval-gate.md)[^evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7].
- Adheres to [Workflow Architecture Principles](../guidelines/workflow-architecture-principles.md).

[^evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/durable-wait.md
