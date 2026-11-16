---
type: architecture
title: Single-Agent Process with Human Approval
description: Reference architecture enforcing human authorization before executing
  protected, irreversible, or policy-governed agent actions.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/reporting/2026-09-report.md
tags:
- workflow
- architecture
- human-in-the-loop
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:42:23.754300+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-60f28464dd94-4c7ddd9e
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/reporting/2026-09-report.md
  author: Yaron Schneider
  last_modified: '2026-11-05T08:38:51-08:00'
- id: evt-wg-workflows-and-process-integration-file-a4fea1b2d544-2fb150b7
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/workstreams/reference-architectures/architectures/single-agent-human-approval.md
  author: Zayne Turner
  last_modified: '2026-11-05T08:39:07-08:00'
---

# Overview
The Single-Agent Process with Human Approval reference architecture establishes an enforceable, human-mediated structural separation between probabilistic agent intent and protected system execution.[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-2fb150b7] Governed by the [Workflows & Process Integration Working Group](../working-groups/workflows-and-process-integration.md), this architecture standardizes the workflow pattern where an agent prepares a proposed action, a designated human approves or rejects it, and only then may a controlled executor apply the change.[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-2fb150b7] It became the working group's second formally voted deliverable in September 2026.[^evt-wg-workflows-and-process-integration-file-60f28464dd94-4c7ddd9e]

# Architecture / Specification
The architecture enforces separation of authority across discrete workflow roles:[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-2fb150b7]
- **Proposer (Agent)**: An agent investigates, computes, and formats a candidate proposal (such as a financial refund or infrastructure change) but lacks capabilities or credentials to trigger external effects directly.[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-2fb150b7]
- **Approval Gate & Durable Wait**: Persists the exact proposal payload and suspends execution via [durable wait](../patterns/durable-wait.md) across arbitrarily long human review cycles without losing state or duplicating pending operations.[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-2fb150b7]
- **Workflow-Controlled Executor**: An automated component that acts only upon explicit human approval, strictly decoupled from the agent's invocation capabilities.[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-2fb150b7]
- **System of Record**: Maintains an immutable audit trace capturing the full proposer intent, approver authorization, and execution outcome.[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-2fb150b7]

Under working group taxonomy conventions, a "business task" denotes the overall request or problem handled by the workflow, while constituent steps are designated as activities.[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-2fb150b7][^evt-wg-workflows-and-process-integration-file-60f28464dd94-4c7ddd9e]

Composed patterns include:
- [Proposal/Execution Split](../patterns/proposal-execution-split.md)
- [Human Approval Gate](../patterns/human-approval-gate.md)
- [Durable Wait](../patterns/durable-wait.md)

# Lifecycle History
- **2026-09-17**: Voted and approved unanimously at the WG Workflows & Process Integration plenary meeting.[^evt-wg-workflows-and-process-integration-file-60f28464dd94-4c7ddd9e]
- **2026-10-02**: Follow-up PR #50 merged, aligning internal terminology to "business task" and "activity".[^evt-wg-workflows-and-process-integration-file-60f28464dd94-4c7ddd9e]

# References
- [Proposal/Execution Split Pattern](../patterns/proposal-execution-split.md)
- [Human Approval Gate Pattern](../patterns/human-approval-gate.md)
- [Bounded Autonomous Remediation](bounded-autonomous-remediation.md)

[^evt-wg-workflows-and-process-integration-file-60f28464dd94-4c7ddd9e]: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/reporting/2026-09-report.md
[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-2fb150b7]: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/workstreams/reference-architectures/architectures/single-agent-human-approval.md
