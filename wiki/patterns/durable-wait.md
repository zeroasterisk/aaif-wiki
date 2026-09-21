---
type: pattern
title: Durable Wait
description: Workflow pattern converting physical thread or process blocking into
  logical persisted state records surviving process restarts and deploys.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/patterns/durable-wait.md
tags:
- workflow
- pattern
- resilience
- state-management
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T10:01:49.347739+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/patterns/durable-wait.md
  author: Mario Zagar
  last_modified: '2026-08-25T07:58:21-07:00'
- id: evt-wg-workflows-and-process-integration-pr-33
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/33
  author: mzagar
  last_modified: '2026-08-25T14:58:22+00:00'
---

# Overview
The Durable Wait pattern addresses workflow runs that must pause for durations exceeding the lifespan of any hosting compute process, such as hours or days awaiting human approvals, timers, or external system events[^evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7]. Rather than blocking a thread or holding state in process memory, the pattern converts a physical wait into a logical recorded state (run parked awaiting event), allowing the workflow run to survive process termination, container restarts, and deployments[^evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7].

In alignment with the terminology standards established by the [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md), workflow execution units within durable operations are standardized as activities rather than steps[^evt-wg-workflows-and-process-integration-pr-33].

# Architecture / Specification

## Mechanism
When a durable wait is encountered:
1. **Park**: The execution engine records the current state and execution position to durable storage, marking the run as parked (`PARKED`). No active process maintains the run in memory[^evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7].
2. **Signal / Timeout**: An external event, callback, or timer triggers a resume request[^evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7].
3. **Resume**: The execution engine loads the persisted record and restores execution without loss of intermediate context[^evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7].

## Invariants
Any implementation of the Durable Wait pattern must satisfy key invariants[^evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7]:
- **Survival**: Parked runs must survive process restarts, node crashes, and rolling deployments.
- **State and Context Restoration**: Resumption restores position, context, and identity so the continuation activity runs with accumulated knowledge.
- **Idempotency**: Duplicate delivery of wake-up events must result in exactly one resumption.
- **Discoverability**: Parked runs must remain queryable and discoverable across administrative interfaces.

## Related Patterns
- [Human Approval Gate](./human-approval-gate.md): Frequently composes with Durable Wait to pause execution while awaiting human authorization.

[^evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7]: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/patterns/durable-wait.md
[^evt-wg-workflows-and-process-integration-pr-33]: https://github.com/aaif/wg-workflows-and-process-integration/pull/33
