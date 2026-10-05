---
type: pattern
title: Proposal-Execution Split
description: Workflow design pattern strictly separating probabilistic intent generation
  from privileged side-effect execution across authority boundaries.
resource: https://github.com/aaif/wg-workflows-and-process-integration/issues/45
tags:
- workflows
- patterns
- governance
- security
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
The Proposal-Execution Split pattern decouples the probabilistic generation of action plans, tool invocations, or data mutations by an AI agent from the deterministic execution of those actions against downstream systems [^evt-wg-workflows-and-process-integration-pr-53]. Rather than granting an agent direct execution credentials, the agent emits an immutable candidate proposal that is validated, authorized, or executed across an authority boundary [^evt-wg-workflows-and-process-integration-issue-45].

# Architecture / Specification
The core separation in the Proposal-Execution Split focuses on authority boundaries rather than requiring physical process isolation, though distinct process or container boundaries may also be employed [^evt-wg-workflows-and-process-integration-pr-53]:

- **Proposal Phase**: The agent produces a structured, declarative proposal detailing intent, parameters, and rationale. The agent operates under least privilege with no direct write or mutating capabilities.
- **Enforcement and Execution Boundary**: The candidate proposal is intercepted by an authorization checkpoint or execution harness before reaching the point of effect.
- **Side Effect Drivers**: Point-of-effect enforcement is motivated by non-exhaustive risk drivers, including high financial impact, data exfiltration risks, irreversible database mutations, or regulatory compliance mandates [^evt-wg-workflows-and-process-integration-pr-53].

## Implementation Approaches
Implementations vary across orchestration layers and execution topologies:
- **Harness/SDK Level**: Middleware or SDK hooks (such as Anthropic Claude Agent SDK `canUseTool` callbacks) intercept proposed tool calls within the runtime before invocation occurs [^evt-wg-workflows-and-process-integration-pr-53].
- **Gateway/Proxy Level**: Out-of-band proxy services or Model Context Protocol (MCP) gateways validate signatures and policies before relaying calls to external services.
- **Isolated Executor**: Dedicated worker processes execute verified proposals after asynchronous approvals, decoupling runtime state and mitigating cold-cache issues across durable waits [^evt-wg-workflows-and-process-integration-issue-45].

# Lifecycle History
Derived from foundational workflow patterns established by the Workflows and Process Integration Working Group [^evt-wg-workflows-and-process-integration-issue-45], with refinements on authority separation and SDK-level interception introduced in PR #53 [^evt-wg-workflows-and-process-integration-pr-53].

# References
- [../reference-architectures/single-agent-human-approval.md](../reference-architectures/single-agent-human-approval.md)
- [../patterns/human-approval-gate.md](../patterns/human-approval-gate.md)
- [../patterns/approval-checkpoint.md](../patterns/approval-checkpoint.md)
- [../working-groups/workflows-and-process-integration.md](../working-groups/workflows-and-process-integration.md)

[^evt-wg-workflows-and-process-integration-issue-45]: https://github.com/aaif/wg-workflows-and-process-integration/issues/45
[^evt-wg-workflows-and-process-integration-pr-53]: https://github.com/aaif/wg-workflows-and-process-integration/pull/53
