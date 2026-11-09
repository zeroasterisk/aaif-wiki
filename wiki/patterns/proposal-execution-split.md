---
type: pattern
title: Proposal/Execution Split
description: Architectural governance pattern separating probabilistic agent intent
  generation, policy or human authorization, and workflow-controlled execution into
  distinct, auditable roles.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/workstreams/reference-architectures/patterns/proposal-execution-split.md
tags:
- pattern
- governance
- security
- workflows
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:33:12.467454+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-832c48c2
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/workstreams/reference-architectures/patterns/proposal-execution-split.md
  author: Zayne Turner
  last_modified: '2026-11-05T08:39:07-08:00'
---

# Overview
The Proposal/Execution Split is an architectural governance pattern that enforces authorization and attribution boundaries when intent originates from a probabilistic AI agent[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-832c48c2]. Probabilistic models cannot provide non-repudiable audit guarantees or hold organizational accountability. The pattern enforces a fundamental precept: intent, authorization, and execution belong to distinct roles, each recorded separately in the system of record[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-832c48c2].

# Architecture / Specification
The pattern divides the execution pipeline into three strictly separated roles:
1. **Proposer (Agent)**: Generates an immutable proposal containing structured intent data, but lacks capability or authorization to execute real-world actions[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-832c48c2].
2. **Authorization Authority**: An explicit human principal or deterministic policy engine that evaluates the exact proposal payload and emits an authorization decision[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-832c48c2].
3. **Executor (System)**: A workflow-controlled, non-probabilistic component holding the credentials required to invoke the external protected effect, acting only upon receiving valid authorization evidence[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-832c48c2].

### Invariants
Any compliant implementation must maintain the following invariants:
- **Proposals are data, not actions**: The artifact crossing from the proposer to the gate is inert state[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-832c48c2].
- **Fail-closed authorization**: An absent, expired, or invalid authorization decision routes strictly to terminal or recovery pathways; permission is never inferred by default[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-832c48c2].
- **Exact payload binding**: The executor only executes the exact payload authorized by the authority; any modification invalidates authorization[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-832c48c2].
- **Separate audit attribution**: Proposer identity, authorization decision evidence, and execution outcomes must be logged as distinct records in the audit trail[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-832c48c2].

### Related Architectures and Patterns
This pattern serves as a foundational building block for:
- [Single-Agent Process with Human Approval](../architectures/single-agent-human-approval.md)[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-832c48c2]
- [Bounded Autonomous Remediation](../architectures/bounded-autonomous-remediation.md)[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-832c48c2]
- [Human Approval Gate](human-approval-gate.md)[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-832c48c2]
- [Durable Wait](durable-wait.md)[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-832c48c2]

[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-832c48c2]: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/workstreams/reference-architectures/patterns/proposal-execution-split.md
