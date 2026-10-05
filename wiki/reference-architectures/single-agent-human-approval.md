---
type: reference-architecture
title: Single Agent Human Approval Reference Architecture
description: Job-oriented reference architecture separating probabilistic agent proposal
  generation from human approval and privileged execution across authority roles.
resource: https://github.com/aaif/wg-workflows-and-process-integration/issues/45
tags:
- reference-architectures
- workflows
- human-in-the-loop
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:27:17.138242+00:00'
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
The Single Agent Human Approval reference architecture specifies a structured lifecycle where a single autonomous agent formulates an action proposal, suspends execution at an immutable approval gate, and hands off the signed proposal for human authorization prior to execution [^evt-wg-workflows-and-process-integration-issue-45] [^evt-wg-workflows-and-process-integration-pr-53].

# Architecture / Specification
The reference architecture is structured around capability roles rather than rigid deployment topologies [^evt-wg-workflows-and-process-integration-pr-53]:

- **Proposer Agent**: A single AI agent formulates execution plans and tool arguments without possessing execution privileges. Where multi-agent critique or reasoning isolation is required, sessions are split explicitly [^evt-wg-workflows-and-process-integration-issue-45].
- **Authority Gate**: Intercepts the proposal and halts execution, persisting intent during human review using durable wait mechanics [^evt-wg-workflows-and-process-integration-issue-45].
- **Human Reviewer**: An authorized individual inspects the immutable proposal, parameters, and justification, granting or rejecting execution authority.
- **Executor**: Executes the approved action against target systems. While execution may occur within the same harness or a separate dedicated process, separation of authority is strictly enforced [^evt-wg-workflows-and-process-integration-pr-53].

## Architecture Checklist
Practitioners evaluate architecture fit against specific criteria:
- Is a single agent producing the proposal that a human must review and approve? [^evt-wg-workflows-and-process-integration-pr-53]
- Does the target operation carry potential side effects requiring enforceable behavior at the point of effect? [^evt-wg-workflows-and-process-integration-pr-53]
- Are wait times asynchronous or state persistence requirements decoupled from agent process lifetimes? [^evt-wg-workflows-and-process-integration-issue-45]

# Lifecycle History
Originated in the Workflows and Process Integration Working Group to define standardized human-in-the-loop patterns, updated via TC feedback in PR #53 to clarify authority roles versus deployment processes [^evt-wg-workflows-and-process-integration-pr-53].

# References
- [../patterns/proposal-execution-split.md](../patterns/proposal-execution-split.md)
- [../patterns/human-approval-gate.md](../patterns/human-approval-gate.md)
- [../patterns/durable-wait.md](../patterns/durable-wait.md)
- [../working-groups/workflows-and-process-integration.md](../working-groups/workflows-and-process-integration.md)

[^evt-wg-workflows-and-process-integration-issue-45]: https://github.com/aaif/wg-workflows-and-process-integration/issues/45
[^evt-wg-workflows-and-process-integration-pr-53]: https://github.com/aaif/wg-workflows-and-process-integration/pull/53
