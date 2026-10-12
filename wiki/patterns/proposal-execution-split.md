---
type: pattern
title: Proposal/Execution Split
description: Architectural pattern enforcing authorization and attribution at protected
  boundaries by separating probabilistic agent proposal from workflow-controlled execution.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/proposal-execution-split.md
tags:
- workflow
- security
- pattern
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T02:54:39.529684+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/proposal-execution-split.md
  author: Mario Zagar
  last_modified: '2026-08-28T22:42:47-04:00'
---

# Overview

The Proposal/Execution Split is an architectural pattern that enforces authorization and attribution at protected-effect boundaries by isolating probabilistic agent proposal from deterministic execution.[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950] In production enterprise environments, agent actions carry risk exposure, audit exposure, and regulatory accountability requirements that cannot be fulfilled if a probabilistic model both decides and acts directly.[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950]

# Architecture / Specification

The pattern establishes three distinct roles and separate systems of record across the execution lifecycle:[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950]

1. **Proposer (Agent)**: Generates candidate intent as immutable structured data, not an executable side-effect.
2. **Authorization Authority (Gate)**: Evaluates whether the exact proposed payload may proceed against policy or human oversight.
3. **Executor (System)**: A workflow-controlled component that executes the authorized payload without allowing the agent to trigger the action directly.

### Invariants

- The proposal is immutable data; the agent cannot directly invoke the executor.[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950]
- The authorization decision attaches strictly to the exact proposal payload (typically verified by content hash).[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950]
- Authorization gates must fail closed on expiration, timeout, or policy evaluation error.[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950]
- Workflow execution must be idempotent to prevent duplicate side-effects on retry.[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950]

# Related Patterns

This pattern is foundational to [Single-Agent Process with Human Approval](../architectures/single-agent-human-approval.md) and [Bounded Autonomous Remediation](../architectures/bounded-autonomous-remediation.md), and coordinates directly with [Human Approval Gate](./human-approval-gate.md) and [Durable Wait](./durable-wait.md).[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950]

[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/proposal-execution-split.md
