---
type: pattern
title: Proposal-Execution Split Pattern
description: Workflow pattern separating probabilistic agent intent generation, deterministic
  authorization, and external side-effect execution.
resource: https://github.com/aaif/wg-workflows-and-process-integration/issues/45
tags:
- workflow
- patterns
- governance
- security
- execution
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T06:02:04.084757+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-issue-45
  resource: https://github.com/aaif/wg-workflows-and-process-integration/issues/45
  author: geemus
  last_modified: '2026-10-03T00:58:32+00:00'
- id: evt-wg-workflows-and-process-integration-pr-53
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/53
  author: zaynelt
  last_modified: '2026-10-04T18:06:45+00:00'
---

# Overview

The Proposal-Execution Split pattern partitions an agentic workflow into distinct phases: generating proposed actions, deterministically validating them, and executing approved operations [^evt-wg-workflows-and-process-integration-pr-53]. This separation guarantees that non-deterministic model outputs cannot trigger external side effects without traversing an authoritative boundary [^evt-wg-workflows-and-process-integration-issue-45].

# Architecture / Specification

### Authority vs Process Topology
- **Authority Separation**: The core requirement is structural decoupling of authority rather than physical deployment isolation [^evt-wg-workflows-and-process-integration-pr-53]. Capability roles define the boundary between probabilistic reasoning and deterministic execution.
- **Harness-Level Hooks**: Implementation can occur within a single execution harness via deterministic interception mechanisms, such as tool authorization gates (e.g., `canUseTool` hooks in agent SDKs) before dispatch [^evt-wg-workflows-and-process-integration-pr-53].
- **Side-Effect Enforceability**: Point-of-effect gates are required for non-exhaustive side-effect categories including financial transactions, credential mutations, privileged infrastructure modifications, and irreversible data destruction [^evt-wg-workflows-and-process-integration-issue-45] [^evt-wg-workflows-and-process-integration-pr-53].

# References
- [`../reference-architectures/single-agent-human-approval.md`](../reference-architectures/single-agent-human-approval.md)
- [`../patterns/approval-checkpoint.md`](../patterns/approval-checkpoint.md)
- [`../patterns/human-approval-gate.md`](../patterns/human-approval-gate.md)

[^evt-wg-workflows-and-process-integration-issue-45]: https://github.com/aaif/wg-workflows-and-process-integration/issues/45
[^evt-wg-workflows-and-process-integration-pr-53]: https://github.com/aaif/wg-workflows-and-process-integration/pull/53
