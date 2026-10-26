---
type: architecture
title: Single-Agent Human Approval Reference Architecture
description: Reference architecture establishing an enforceable human approval gate
  and structural separation of authority between proposal generation and execution
  in single-agent workflows.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/53
tags:
- architecture
- human-in-the-loop
- workflows
- governance
- security
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T10:53:12.499283+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-pr-53
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/53
  author: zaynelt
  last_modified: '2026-10-09T18:55:43+00:00'
---

# Overview
The Single-Agent Human Approval Reference Architecture defines an enforceable structural break between an agent's proposal generation and the downstream execution of side effects, requiring verified human authorization prior to runtime enactment [^evt-wg-workflows-and-process-integration-pr-53]. This architecture structures workflows around distinct capability roles rather than specific physical deployment topologies, ensuring that authority boundaries remain invariant whether components run across distributed microservices or inside a single orchestration harness [^evt-wg-workflows-and-process-integration-pr-53].

By decoupling proposal drafting from execution privileges, the pattern ensures that autonomous agents cannot directly invoke high-impact side effects without traversing an immutable approval gate [^evt-wg-workflows-and-process-integration-pr-53].

# Architecture / Specification
The architecture organizes system capabilities into three logical roles:
1. **Proposal Generator**: An AI agent that inspects task context, formulates proposed actions or tool calls, and submits structured execution candidates without holding the authority or credentials to enact them directly [^evt-wg-workflows-and-process-integration-pr-53].
2. **Approval Gate**: An external boundary checkpoint where designated human operators review, inspect, and approve or reject proposed actions against governance policy [^evt-wg-workflows-and-process-integration-pr-53].
3. **Executor**: A secured execution runtime possessing point-of-effect credentials that only executes validated payloads upon presentation of a verified approval grant [^evt-wg-workflows-and-process-integration-pr-53].

Separation in this architecture focuses on authority and access privilege rather than process isolation [^evt-wg-workflows-and-process-integration-pr-53]. Side effects governed by the gate include non-exhaustive operations such as production database mutations, external message publication, financial transactions, and credential issuance [^evt-wg-workflows-and-process-integration-pr-53]. Qualification for this reference architecture requires verifying that a single agent produces the candidate proposal subject to human approval, regardless of whether internal critique or generation sub-steps are employed [^evt-wg-workflows-and-process-integration-pr-53].

# Lifecycle History
Developed under the Workflows and Process Integration Working Group (../working-groups/workflows-and-process-integration.md). Refined in PR #53 following Technical Committee feedback to clarify authority boundaries versus physical deployment topology and broaden side-effect definitions [^evt-wg-workflows-and-process-integration-pr-53].

# References
- Proposed under [WG Workflows PR #53](https://github.com/aaif/wg-workflows-and-process-integration/pull/53)
- Derived from [Proposal-Execution Split](../patterns/proposal-execution-split.md)
- Related to [Human Approval Gate](../patterns/human-approval-gate.md)

[^evt-wg-workflows-and-process-integration-pr-53]: https://github.com/aaif/wg-workflows-and-process-integration/pull/53
