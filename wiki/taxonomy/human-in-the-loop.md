---
type: taxonomy
title: Human in the Loop (HITL)
description: Taxonomy standard defining synchronous human intervention checkpoints
  required before an agent executes protected actions.
resource: https://github.com/aaif/ws-taxonomy-landscape/pull/40
tags:
- taxonomy
- governance
- hitl
- safety
- control
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T10:08:50.194494+00:00'
sources:
- id: evt-ws-taxonomy-landscape-pr-40
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/40
  author: julianna-ciq
  last_modified: '2026-09-15T03:36:58+00:00'
---

# Overview
Human in the Loop (HITL) is an accepted Agentic AI Foundation taxonomy term specifying an operational architecture and control requirement where an agent workflow halts at defined checkpoints, requiring active human authorization or review before proceeding [^evt-ws-taxonomy-landscape-pr-40].

# Architecture / Specification

## Scope and Semantic Boundaries
Within the AAIF Taxonomy framework, Human in the Loop is delineated from related control patterns [^evt-ws-taxonomy-landscape-pr-40]:
- **Human in the Loop (HITL)**: Requires synchronous human intervention and explicit review at an enforcement barrier prior to task completion or sensitive state transitions [^evt-ws-taxonomy-landscape-pr-40]. See [Human Approval Gate](../patterns/human-approval-gate.md).
- **Human on the Loop (HOTL)**: Involves asynchronous monitoring and supervisory control where the human oversees autonomous agent execution and intervenes only for exceptions or policy deviations [^evt-ws-taxonomy-landscape-pr-40].
- **Handoff**: Represents an operational transfer of execution control where the agent permanently or conditionally yields the active task execution context to a human operator or secondary agent system [^evt-ws-taxonomy-landscape-pr-40].

# References
- [Taxonomy and Landscape Workstream](../working-groups/taxonomy-and-landscape.md)
- [Single-Agent Human Approval Reference Architecture](../reference-architectures/single-agent-human-approval.md)
- [Core Workflow Terms](../taxonomy/core-workflow-terms.md)

[^evt-ws-taxonomy-landscape-pr-40]: https://github.com/aaif/ws-taxonomy-landscape/pull/40
