---
type: architecture
title: Single-Agent Human Approval Reference Architecture
description: Job-oriented reference architecture enforcing a structural separation
  between probabilistic agent proposals, human authorization, and deterministic execution.
resource: https://github.com/aaif/wg-workflows-and-process-integration/issues/45
tags:
- reference-architecture
- human-in-the-loop
- workflows
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T06:02:04.084757+00:00'
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

The Single-Agent Human Approval reference architecture provides a standardized blueprint for workflows where an autonomous agent formulates action proposals that must receive explicit human authorization before execution [^evt-wg-workflows-and-process-integration-pr-53]. It enforces authority boundaries across capability roles to ensure that side effects are strictly bounded and auditable [^evt-wg-workflows-and-process-integration-issue-45].

# Architecture / Specification

### Capability Roles and Boundary Separation
- **Capability Roles vs Topology**: The separation between proposal generation, approval checkpoints, and action execution defines logical capability boundaries and authority contracts rather than mandating multi-process deployment topologies [^evt-wg-workflows-and-process-integration-pr-53].
- **Proposal Authority**: A single agent produces the candidate proposal subject to human evaluation, distinct from multi-agent critique or collaborative consensus pipelines [^evt-wg-workflows-and-process-integration-issue-45] [^evt-wg-workflows-and-process-integration-pr-53].
- **Point-of-Effect Governance**: External actions with non-reversible side effects (such as payments, data deletions, access grants, or environment modifications) must pass through an immutable gate validating the human authorization token [^evt-wg-workflows-and-process-integration-pr-53].

# References
- [`../patterns/proposal-execution-split.md`](../patterns/proposal-execution-split.md)
- [`../patterns/human-approval-gate.md`](../patterns/human-approval-gate.md)
- [`../patterns/durable-wait.md`](../patterns/durable-wait.md)
- [`../policies-guidelines/single-agent-workflow-blueprint.md`](../policies-guidelines/single-agent-workflow-blueprint.md)

[^evt-wg-workflows-and-process-integration-issue-45]: https://github.com/aaif/wg-workflows-and-process-integration/issues/45
[^evt-wg-workflows-and-process-integration-pr-53]: https://github.com/aaif/wg-workflows-and-process-integration/pull/53
