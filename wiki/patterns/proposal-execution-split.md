---
type: pattern
title: Proposal/Execution Split
description: Architectural governance pattern separating intent generation, authorization,
  and workflow execution into distinct roles with independent audit records.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/proposal-execution-split.md
tags:
- architecture
- governance
- patterns
- workflows
- security
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T09:51:26.916956+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/proposal-execution-split.md
  author: Mario Zagar
  last_modified: '2026-08-28T22:42:47-04:00'
---

# Overview

The Proposal/Execution Split is an architectural governance pattern that enforces authorization and attribution at the protected-effect boundary when intent originates from a probabilistic AI agent[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950]. Because a probabilistic actor cannot provide non-repudiation or deterministic policy guarantees, the pattern mandates that intent generation, authorization, and execution must belong to distinct roles, each maintaining separate audit records[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950].

This pattern is foundational to reference architectures such as [Single-Agent Human Approval](../architectures/single-agent-human-approval.md) and [Bounded Autonomous Remediation](../architectures/bounded-autonomous-remediation.md), and coordinates directly with patterns like the [Human Approval Gate](human-approval-gate.md) and [Durable Wait](durable-wait.md)[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950].

# Architecture / Specification

The pattern establishes three distinct separations across the lifecycle of an action[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950]:

1. **Proposer (Agent)**: Generates a proposal as immutable structured data. The agent proposes data, never an executable action, and possesses no direct invocation path to downstream systems of record.
2. **Authorization Authority**: A human principal or versioned policy engine evaluates whether that exact proposal may proceed. Authorization binds strictly to the exact proposal payload.
3. **Executor (System)**: A workflow-controlled component executes the authorized proposal upon receiving explicit approval evidence. The executor is isolated from direct agent interaction.

```text
  proposer (agent)            authorization authority       executor (system)
        │                             │                            │
        ▼                             ▼                            ▼
   proposal ─────────► gate: authorize this exact ─ yes ─► workflow-controlled
   (immutable data,         proposal?                      execution of the
    not an action)            │                            authorized proposal
                              └─ no / invalid ──► terminal or     │
                                 recovery path                    ▼
                                                                effect
  ─────────────────────────────────────────────────────────────────────────
    system of record: proposal · authority + decision evidence · effect
```

### Core Invariants

Implementations must satisfy critical invariants[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950]:
- **Fail Closed**: In the absence, expiration, or failure of an authorization decision, the gate fails closed and prevents execution.
- **Payload Immutability**: What executes must match *exactly* what was authorized; mutations or drift invalidate authorization.
- **Separate Audit Logging**: Intent, authorization evidence, and execution effect are logged independently to preserve non-repudiation and clear attribution of authority.
- **Idempotency**: Retried workflow executions must avoid duplicate side effects.

# Lifecycle History

Documented as a core reference architecture pattern by the Workflows and Process Integration Working Group[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950].

[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/proposal-execution-split.md
