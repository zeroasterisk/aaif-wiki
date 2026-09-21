---
type: working-group
title: Workflows and Process Integration Working Group
description: AAIF working group standardizing shared workflow models, execution semantics,
  state persistence, architectural principles, and human-in-the-loop integration patterns.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/principles.md
tags:
- governance
- working-group
- workflows
- process-integration
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T09:57:41.806372+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/principles.md
  author: Mario Zagar
  last_modified: '2026-08-20T06:14:14-07:00'
- id: evt-wg-workflows-and-process-integration-pr-27
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/27
  author: mzagar
  last_modified: '2026-08-20T13:14:15+00:00'
---

# Overview

The Workflows and Process Integration Working Group develops open standards, design patterns, and reference architectures for agentic workflows across enterprise business processes, durable execution engines, and multi-agent coordination systems [^evt-wg-workflows-and-process-integration-pr-27]. The working group focuses on creating vendor-neutral frameworks for state persistence, human approval gates, bounded autonomy, and deterministic execution boundaries [^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181].

# Architecture / Specification

The group's work is organized around several key specifications and deliverables:
- **[Workflow Architecture Principles](../methodology/workflow-architecture-principles.md):** Core guidelines mandating job-oriented design, bounded autonomy, explicit authority, and failure recovery [^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181].
- **[Job-Oriented Reference Architectures](../methodology/job-oriented-reference-architectures.md):** Architectural patterns organized around practitioner operational jobs rather than agent counts [^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181].
- **[Workflow Design Specification](../methodology/workflow-design-specification.md):** Formal, machine-readable specifications for defining agentic workflows and execution guarantees.
- **Integration Patterns:** Standardized design patterns such as the [Human Approval Gate](../patterns/human-approval-gate.md) ensuring critical external effects remain structurally protected [^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181].

[^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181]: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/principles.md
[^evt-wg-workflows-and-process-integration-pr-27]: https://github.com/aaif/wg-workflows-and-process-integration/pull/27
