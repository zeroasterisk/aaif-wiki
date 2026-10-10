---
type: pattern
title: Proposal-Execution Split Pattern
description: Architectural pattern enforcing authorization and attribution at protected
  boundaries by separating untrusted proposal generation from privileged execution.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/53
tags:
- patterns
- authorization
- governance
- security
- workflows
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:24:22.444967+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-pr-53
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/53
  author: zaynelt
  last_modified: '2026-10-09T18:55:43+00:00'
---

# Overview

The Proposal-Execution Split pattern isolates the generation of candidate agent actions from their eventual execution at protected operational boundaries [^evt-wg-workflows-and-process-integration-pr-53]. By ensuring that an agent cannot autonomously invoke side-effecting operations without passing through an external authorization or evaluation checkpoint, systems mitigate prompt injection, privilege escalation, and unintended state mutation [^evt-wg-workflows-and-process-integration-pr-53].

# Architecture / Specification

### Separation of Authority vs. Process Boundary

The pattern fundamentally mandates a separation of **authority** rather than prescribing physical process or network isolation [^evt-wg-workflows-and-process-integration-pr-53]:
- **Authority Boundary**: The proposer entity lacks intrinsic privileges or credentials to mutate state directly. The executor entity possesses execution authority but does not formulate intent autonomously [^evt-wg-workflows-and-process-integration-pr-53].
- **Deployment Topology Flexibility**: The separation may be realized at multiple architectural tiers:
  - *Harness / Orchestrator Level*: In-process execution gates (such as the `canUseTool` interception hook in the Claude Agent SDK) intercepting proposed tool payloads before invocation [^evt-wg-workflows-and-process-integration-pr-53].
  - *Proxy / Gateway Level*: Network-level proxies (e.g., [Prismor](../resources/prismor.md) or [Context Forge](../resources/context-forge.md)) validating signed action proposals against policy-as-code engines.
  - *External Human-in-the-Loop Gate*: Asynchronous review workflows matching the [Single Agent Human Approval](../architectures/single-agent-human-approval.md) reference architecture.

### Protected Side-Effect Domains

Proposal validation is required whenever actions cross into external domains, including but not limited to [^evt-wg-workflows-and-process-integration-pr-53]:
- Financial transactions, checkout commitments, or credit allocations.
- Infrastructure mutations, database writes, or secret disclosures.
- External communication dispatch (email, customer notifications, public repository commits).

# Lifecycle History

- Architectural boundaries clarified in PR #53 following Technical Committee review feedback [^evt-wg-workflows-and-process-integration-pr-53].

[^evt-wg-workflows-and-process-integration-pr-53]: https://github.com/aaif/wg-workflows-and-process-integration/pull/53
