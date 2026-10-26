---
type: pattern
title: Proposal-Execution Split
description: Architectural governance pattern separating intent generation, authorization,
  and workflow execution into decoupled authority roles.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/53
tags:
- pattern
- governance
- security
- workflows
- authorization
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
The Proposal-Execution Split pattern isolates the generation of an intended action from its authorization and runtime execution, ensuring that an agent cannot enact side effects solely on its own authority [^evt-wg-workflows-and-process-integration-pr-53]. This architectural split guarantees that candidate operations must transition through an explicit governance checkpoint before accessing sensitive tools or committing side effects [^evt-wg-workflows-and-process-integration-pr-53].

The separation focuses fundamentally on authority and capability boundaries rather than physical process boundaries [^evt-wg-workflows-and-process-integration-pr-53]. As a result, the pattern can be realized both across distributed multi-tier services and within unified harness-level execution runtimes [^evt-wg-workflows-and-process-integration-pr-53].

# Architecture / Specification
The pattern defines an authority barrier separating proposal generation from action execution:
- **Intent Formulation**: The model produces an unauthenticated action manifest or tool call proposal describing intended effects [^evt-wg-workflows-and-process-integration-pr-53].
- **Policy and Authorization Gate**: An independent evaluation plane assesses the proposal against deterministic policies, organizational rules, or human approval gates [^evt-wg-workflows-and-process-integration-pr-53].
- **Effect Execution**: An execution engine receives validated approval evidence and executes the target operation [^evt-wg-workflows-and-process-integration-pr-53].

At the implementation layer, this pattern can be instantiated via orchestration- and harness-level controls, such as the `canUseTool` capability gate in agent SDKs (e.g., Anthropic Claude Agent SDK), or through distributed protocol proxies and sidecars [^evt-wg-workflows-and-process-integration-pr-53]. The pattern mitigates risks including unconstrained autonomous state corruption, unauthorized financial outlays, unintended message broadcast, and credential leakage [^evt-wg-workflows-and-process-integration-pr-53].

# Lifecycle History
Authored within the Workflows and Process Integration Working Group (../working-groups/workflows-and-process-integration.md). Updated in PR #53 based on Technical Committee review to clarify authority separation versus process isolation and document harness-level implementation mechanisms [^evt-wg-workflows-and-process-integration-pr-53].

# References
- [WG Workflows PR #53](https://github.com/aaif/wg-workflows-and-process-integration/pull/53)
- [Single-Agent Human Approval Reference Architecture](../architectures/single-agent-human-approval.md)
- [Approval Checkpoint](../patterns/approval-checkpoint.md)

[^evt-wg-workflows-and-process-integration-pr-53]: https://github.com/aaif/wg-workflows-and-process-integration/pull/53
