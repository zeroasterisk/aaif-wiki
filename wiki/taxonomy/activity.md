---
type: taxonomy
title: Activity
description: A single, bounded task with defined inputs and outputs that can be tracked
  to completion within an agent workflow.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/reporting/2026-08-report.md
tags:
- taxonomy
- workflows
- execution
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:09:51.859299+00:00'
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
An activity is a single, bounded task with defined inputs and outputs that can be tracked to completion.[^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7] Within the [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md) vocabulary, an activity represents the fundamental atomic unit of agent execution, serving as the building block from which larger agentic workflows are composed.[^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7]

# Architecture / Specification
In the AAIF workflow taxonomy, activity was explicitly selected over alternative terms such as "step" or "workflow step" to prevent circular semantic definitions:[^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7]
- **Decoupled Definition:** The term is defined independently without circular references to a containing workflow structure.[^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7]
- **Compositional Hierarchy:** A workflow is subsequently modeled as an orchestration or composition of one or more activities.[^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7]
- **Scope Boundaries:** Gate, check, and evaluation semantics are explicitly scoped out of the activity primitive, remaining under the custody of security, observability, and accuracy working groups.[^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7]

# Lifecycle History
Adopted as part of the Phase One Core Terms draft by WG Workflows & Process Integration and formally voted through at the August 2026 plenary meeting, making it part of the first official deliverable shipped across the Agentic AI Foundation.[^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7]

[^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/reporting/2026-08-report.md
