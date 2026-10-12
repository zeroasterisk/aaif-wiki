---
type: pattern
title: Proposal-Execution Split
description: Architectural pattern enforcing authorization and attribution at protected
  boundaries by separating proposal generation from action execution.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/53
tags:
- pattern
- governance
- authorization
- workflows
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:46:11.619660+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-pr-53
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/53
  author: zaynelt
  last_modified: '2026-10-09T18:55:43+00:00'
---

# Overview
The Proposal-Execution Split pattern prevents unauthorized or unverified agent operations by strictly decoupling the generation of an operational proposal from the mechanism authorized to execute it [^evt-wg-workflows-and-process-integration-pr-53]. By introducing an explicit governance boundary between intent synthesis and system state modification, systems can enforce policy verification, human inspection, and cryptographic attribution before point-of-effect execution [^evt-wg-workflows-and-process-integration-pr-53].

# Architecture / Specification
The pattern focuses on separation of authority rather than physical process or deployment separation [^evt-wg-workflows-and-process-integration-pr-53]. While proposal generation and execution can be hosted in distinct environments or microservices, the requirement is that the proposal-generating capability role lacks ambient privileges or execution credentials at protected interfaces [^evt-wg-workflows-and-process-integration-pr-53].

Key architectural elements include:
- **Capability Separation vs Topology**: The pattern specifies logical capability roles (proposer vs executor) rather than requiring rigid distributed deployment topologies [^evt-wg-workflows-and-process-integration-pr-53].
- **Point-of-Effect Gating**: Side effects requiring split execution are non-exhaustive and include irreversible data mutations, financial commitments, external communications, and infrastructure state changes [^evt-wg-workflows-and-process-integration-pr-53].
- **Implementation Variants**: Implementations range from harness and orchestration-level interception—such as SDK tool-use gates (e.g., `canUseTool` callbacks) that prevent tool dispatch without confirmation—to cryptographic approval checkpoints and verified execution workers [^evt-wg-workflows-and-process-integration-pr-53].

# Related Patterns
- [Single-Agent Human Approval Architecture](../architectures/single-agent-human-approval.md)
- [Human Approval Gate](../patterns/human-approval-gate.md)
- [Approval Checkpoint](../patterns/approval-checkpoint.md)

# References
- aaif/wg-workflows-and-process-integration: PR #53 (Updates based on Issue 45 TC Feedback)

[^evt-wg-workflows-and-process-integration-pr-53]: https://github.com/aaif/wg-workflows-and-process-integration/pull/53
