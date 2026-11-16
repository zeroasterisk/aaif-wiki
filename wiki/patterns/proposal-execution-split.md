---
type: pattern
title: Proposal/Execution Split
description: Architectural governance pattern separating intent generation, authorization,
  and workflow execution into distinct roles.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/workstreams/reference-architectures/patterns/proposal-execution-split.md
tags:
- workflow
- pattern
- governance
- security
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:42:23.754300+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-832c48c2
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/workstreams/reference-architectures/patterns/proposal-execution-split.md
  author: Zayne Turner
  last_modified: '2026-11-05T08:39:07-08:00'
---

# Overview
The Proposal/Execution Split is a workflow governance pattern establishing that intent generation, authorization, and workflow execution belong to distinct, decoupled roles, each recorded independently in an audit trail.[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-832c48c2] Because probabilistic language model outputs cannot inherently guarantee regulatory or business compliance, this pattern prevents agents from executing actions directly, ensuring strict authorization and attribution at the boundary of protected side effects.[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-832c48c2]

# Architecture / Specification
The pattern partitions workflow responsibilities into three decoupled stages:[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-832c48c2]
1. **Proposer (Agent)**: Creates candidate data expressing intent. The proposal is an immutable data artifact rather than an executable capability.[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-832c48c2]
2. **Authorization Authority (Gate)**: Evaluates the exact candidate proposal against explicit policy rules or human approval. The authorization gate fails closed on missing, expired, or rejected checks.[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-832c48c2]
3. **Workflow-Controlled Executor**: A dedicated system capability invoked only after positive authorization to apply the approved change. Credentials and execution rights are held solely by the executor, never by the agent.[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-832c48c2]

Normative invariants:
- Intent, authorization, and execution remain structurally separated.[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-832c48c2]
- The authorization gate fails closed.[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-832c48c2]
- Authorization records bind cryptographically or immutably to the specific proposal version evaluated.[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-832c48c2]
- Execution cannot alter the authorized proposal payload.[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-832c48c2]

# References
- [Human Approval Gate](human-approval-gate.md)
- [Durable Wait](durable-wait.md)
- [Single-Agent Process with Human Approval](../architectures/single-agent-human-approval.md)
- [Bounded Autonomous Remediation](../architectures/bounded-autonomous-remediation.md)

[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-832c48c2]: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/workstreams/reference-architectures/patterns/proposal-execution-split.md
