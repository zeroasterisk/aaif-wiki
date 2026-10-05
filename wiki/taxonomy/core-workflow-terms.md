---
type: taxonomy
title: Core Workflow Terms
description: Foundational vocabulary for agentic workflows defining activities as
  primary units of execution and workflows as activity compositions.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/reporting/2026-08-report.md
tags:
- workflows
- taxonomy
- core-terms
- aaif
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:47:45.254943+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/reporting/2026-08-report.md
  author: Yaron Schneider
  last_modified: '2026-09-27T17:45:13-07:00'
- id: evt-wg-workflows-and-process-integration-pr-38
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/38
  author: yaron2
  last_modified: '2026-09-28T00:45:18+00:00'
---

# Overview

The Core Workflow Terms establish a shared, standardized vocabulary for specifying agentic AI workflows, defining the discrete units of execution, lifecycle states, and orchestration structures across AAIF reference architectures [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7]. Voted through at the August 2026 plenary by the [Workflows & Process Integration Working Group](../working-groups/workflows-and-process-integration.md), this Phase One taxonomy represents the foundation's first formalized vocabulary artifact [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7].

# Architecture / Specification

### Primary Terms
- **Activity**: The foundational unit of work within an agentic workflow, defined independently without circular references to workflows [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7]. The working group formally adopted "activity" over alternative terms like "step" or "workflow step" to decouple atomic execution units from broader orchestration topologies [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7].
- **Workflow**: A structured composition of activities executed in sequence, parallel, or cyclic iterations according to deterministic or agent-driven policies [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7].
- **Lifecycle**: The progression of state transitions managing execution, replacing prior ambiguous references to "execution engine" [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7].

### Scope Boundaries
To prevent conceptual overlap, gate, check, and evaluation terminology is explicitly scoped out of the core workflow terms and assigned to the Security & Privacy, Observability & Traceability, and Accuracy & Reliability working groups [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7].

# Lifecycle History

In August 2026, the Phase One Core Terms draft was reviewed and formally voted through by the Workflows & Process Integration Working Group [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7]. Ongoing reconciliation continues with upstream global taxonomy workstreams to align agentic AI specific terminology with baseline definitions [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7].

[^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/reporting/2026-08-report.md
