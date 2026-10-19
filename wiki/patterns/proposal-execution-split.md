---
type: pattern
title: Proposal/Execution Split
description: Architectural governance pattern separating intent generation, authorization,
  and workflow execution into distinct roles to enforce deterministic attribution.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/proposal-execution-split.md
tags:
- workflow
- patterns
- security
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T10:16:04.076901+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/proposal-execution-split.md
  author: Mario Zagar
  last_modified: '2026-08-28T22:42:47-04:00'
---

# Overview
The Proposal/Execution Split is a workflow safety pattern that enforces authorization, attribution, and non-repudiation at protected execution boundaries when intent originates from a probabilistic AI agent[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950]. Because agent reasoning is probabilistic and non-deterministic, systems cannot accept an agent's self-contained decision as an authorized execution; instead, intent, authorization, and execution must be isolated into separate architectural roles[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950].

The pattern forms a structural prerequisite for architectures like [Single-Agent Human Approval](../architectures/single-agent-human-approval.md) and [Bounded Autonomous Remediation](../architectures/bounded-autonomous-remediation.md), working in tandem with the [Human Approval Gate](./human-approval-gate.md) and [Durable Wait](./durable-wait.md) patterns[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950].

# Architecture / Specification
The core principle requires one precept and three distinct separations: intent, authorization, and execution belong to distinct roles, and each is independently persisted in an immutable system of record[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950].

## Core Roles
- **Proposer (Agent)**: Generates proposed parameter data rather than executing direct effects. The payload is treated as immutable data representing proposed intent, not executable code or autonomous capability[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950].
- **Authorization Authority**: An accountable entity—either an authenticated human principal or an immutable, versioned policy engine—evaluating whether that exact, immutable proposal payload may proceed[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950]. If denied, timed out, or unverified, the gate fails closed into a terminal or recovery path[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950].
- **Workflow-Controlled Executor**: A deterministic system component invoked exclusively by workflow orchestrators (and inaccessible to direct agent calls) that executes the authorized payload against downstream protected resources[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950].

## Invariants and Enforcement
- **Proposal Immutability**: What is authorized must match byte-for-byte what executes; downstream mutations invalidate the approval[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950].
- **Fail-Closed Verification**: Absence, delay, or failure of an authorization signal strictly terminates execution[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950].
- **Idempotency & Non-Replayability**: Retrying an approved proposal must never result in duplicate external side effects[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950].

# References
Defined by the Workflows and Process Integration Working Group [workstream on reference architectures](../working-groups/workflows-and-process-integration.md)[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950].

[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/proposal-execution-split.md
