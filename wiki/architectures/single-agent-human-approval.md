---
type: architecture
title: Single-Agent Process with Human Approval
description: Reference architecture establishing an enforceable human approval gate
  and structural break between agent proposal generation and protected system execution.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/architectures/single-agent-human-approval.md
tags:
- architecture
- human-in-the-loop
- approval-gate
- workflow-engine
- safety
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T10:50:37.814965+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-a4fea1b2d544-d6bb99fb
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/architectures/single-agent-human-approval.md
  author: Mario Zagar
  last_modified: '2026-10-02T11:51:25-07:00'
- id: evt-wg-workflows-and-process-integration-pr-50
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/50
  author: mzagar
  last_modified: '2026-10-02T18:51:26+00:00'
- id: evt-wg-workflows-and-process-integration-issue-45
  resource: https://github.com/aaif/wg-workflows-and-process-integration/issues/45
  author: geemus
  last_modified: '2026-10-03T00:58:32+00:00'
---

# Overview
The Single-Agent Process with Human Approval reference architecture governs workflows where an autonomous agent prepares an action, a designated human approves or rejects it, and an independent workflow-controlled executor applies the protected effect only upon recorded approval[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-d6bb99fb]. It establishes a strict structural separation between reasoning and execution, preventing generative models from directly invoking irreversible or high-consequence system capabilities[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-d6bb99fb].

The architecture addresses common enterprise operations—such as issuing financial refunds, modifying production configurations, or dispatching external communications—where audit compliance mandates non-repudiation of authorization or where error reversal costs are high[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-d6bb99fb]. Core architectural guarantees require that no protected effect occurs without prior approval, the exact approved payload cannot be modified prior to dispatch, execution state survives long-duration waits, and complete provenance records link the proposer, approver, and executor[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-d6bb99fb].

# Architecture / Specification

## Pattern Composition
The reference architecture is composed of three core runtime patterns:
- [Proposal/Execution Split](../patterns/proposal-execution-split.md): Isolates the agent's exploratory and reasoning activities from the execution interface, restricting the agent to emitting structured action proposals[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-d6bb99fb].
- [Human Approval Gate](../patterns/human-approval-gate.md): Mandates explicit, non-bypassable sign-off from an authenticated human reviewer on the immutable candidate proposal[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-d6bb99fb].
- [Durable Wait](../patterns/durable-wait.md): Converts human review delays into persisted, queryable suspension states, ensuring process runs survive restarts, infrastructure deployments, or multi-day wait times without dropping state or re-executing completed steps[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-d6bb99fb].

## Required Capabilities
Executing this architecture requires seven coordinated capabilities across the runtime environment[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-d6bb99fb]:
1. **Execution Engine**: Orchestrates step sequencing, state transitions, timers, and durable pauses.
2. **Agent Runtime**: Hosts the reasoning model, manages context windows, and synthesizes candidate plans.
3. **Tool Access Layer**: Restricts agent tools to read-only or sandbox queries, strictly excluding protected mutation endpoints.
4. **State and Context Store**: Persists run progress, agent inputs, intermediate evidence, and serialized proposals.
5. **Human Interaction Surface**: Presents the candidate proposal, context, and decision controls to authorized approvers.
6. **Workflow-Controlled Executor**: Executes approved actions against target systems strictly based on recorded authorization.
7. **Audit Log**: Immutably records the proposer identity, proposed payload, approver identity, approval verdict, and dispatch status.

## Task and Activity Boundaries
The architecture distinguishes between overarching business tasks and execution activities:
- **Business Task**: The end-to-end operational problem or request managed by the workflow (for example, a disputed transaction resolution)[^evt-wg-workflows-and-process-integration-pr-50].
- **Activities**: The discrete, scheduled units of work executed by either deterministic logic or model-driven agents to resolve that business task[^evt-wg-workflows-and-process-integration-pr-50].

## Execution Separation and Review Feedback
Working group feedback highlights operational trade-offs concerning whether the executor must be isolated as an independent process or can run within an existing harness[^evt-wg-workflows-and-process-integration-issue-45]. An independent executor avoids stale in-memory context and security vulnerabilities following multi-day durable waits, while requiring fresh context loading at execution time[^evt-wg-workflows-and-process-integration-issue-45]. Reviewers also noted that decision criteria for introducing multi-agent configurations—such as separating reasoning sessions for independent critique—are illustrative design patterns rather than an exhaustive boundary[^evt-wg-workflows-and-process-integration-issue-45].

# Lifecycle History
- **Draft Reference Architecture**: Initial drafting codified pattern invariants, refund walkthroughs, and crash-recovery procedures[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-d6bb99fb].
- **Clarification of Task and Activity Terminology**: PR #50 updated terminology to explicitly distinguish business tasks from [workflow primitives](../taxonomy/workflow-primitives.md) and activities[^evt-wg-workflows-and-process-integration-pr-50].
- **Runtime Discussion**: Issue #45 introduced community feedback on executor isolation trade-offs and multi-agent routing criteria[^evt-wg-workflows-and-process-integration-issue-45].

[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-d6bb99fb]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/architectures/single-agent-human-approval.md
[^evt-wg-workflows-and-process-integration-issue-45]: https://github.com/aaif/wg-workflows-and-process-integration/issues/45
[^evt-wg-workflows-and-process-integration-pr-50]: https://github.com/aaif/wg-workflows-and-process-integration/pull/50
