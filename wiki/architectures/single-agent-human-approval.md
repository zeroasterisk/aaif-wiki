---
type: architecture
title: Single Agent Human Approval
description: Reference architecture enforcing explicit human authorization gates before
  an agent executes protected, irreversible operations.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/53
tags:
- architecture
- reference-architecture
- governance
- approval
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:21:12.283283+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-pr-53
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/53
  author: zaynelt
  last_modified: '2026-10-09T18:55:43+00:00'
---

# Overview
Single Agent Human Approval is an Agentic AI Foundation reference architecture for workflows where a single autonomous agent plans and proposes actions, but requires an explicit, authenticated human authorization decision before executing protected operations[^evt-wg-workflows-and-process-integration-pr-53]. The architecture implements the [`patterns/proposal-execution-split`](../patterns/proposal-execution-split.md) pattern, ensuring that autonomous reasoning cannot trigger sensitive side effects without passing through an external authorization checkpoint.

The architecture emphasizes separation of authority versus process rather than a requirement for separate deployment topologies, defining capability roles rather than physical node layouts[^evt-wg-workflows-and-process-integration-pr-53].

# Architecture / Specification
The Single Agent Human Approval workflow coordinates three primary functional components:

- **Agent Runtime**: Ingests prompts and tools to generate proposed action payloads. The agent does not possess ambient credentials to execute sensitive actions directly[^evt-wg-workflows-and-process-integration-pr-53].
- **Human Approval Gate**: Intercepts proposed actions that trigger defined risk thresholds. It surfaces the action payload, provenance, and rationale to an authorized reviewer ([`patterns/human-approval-gate`](../patterns/human-approval-gate.md)).
- **Execution Engine**: Executes the action only upon receipt of a validated approval token or record ([`patterns/approval-checkpoint`](../patterns/approval-checkpoint.md)).

## Applicability Criteria
Practitioners evaluate workflow fit using a standard checklist:

1. **Single Proposer**: Exactly one agent produces the proposal that the human evaluates, excluding architectures with peer agent critiques or consensus swarms[^evt-wg-workflows-and-process-integration-pr-53].
2. **Irreversible Side Effects**: The operation produces non-exhaustive side effects—such as external communication, financial transactions, database mutations, or code deployments—that cannot be safely rolled back automatically[^evt-wg-workflows-and-process-integration-pr-53].
3. **Human Discretion Required**: Approval cannot be fully delegated to deterministic automated policies due to contextual ambiguity or regulatory governance constraints.

[^evt-wg-workflows-and-process-integration-pr-53]: https://github.com/aaif/wg-workflows-and-process-integration/pull/53
