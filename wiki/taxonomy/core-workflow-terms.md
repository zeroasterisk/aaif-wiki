---
type: taxonomy
title: Core Workflow Terminology
description: Standardized vocabulary and foundational execution primitives defined
  by the Workflows and Process Integration Working Group for multi-step agentic systems.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/reporting/2026-08-report.md
tags:
- taxonomy
- workflows
- process-integration
- core-terms
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:15:43.760261+00:00'
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
Core Workflow Terminology defines the standardized vocabulary and execution primitives established by the [../working-groups/workflows-and-process-integration.md](../working-groups/workflows-and-process-integration.md) to describe agentic operations, state transitions, and orchestration boundaries [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7]. It provides unambiguous conceptual building blocks for reference architectures and use-case catalogs across the AAIF ecosystem.

# Architecture / Specification
The taxonomy establishes foundational hierarchical relationships and strict boundary definitions [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7]:
- **Activity:** The foundational unit of work, defined independently without referencing workflow structures to eliminate circular dependency definitions [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7].
- **Workflow:** Defined strictly as an orchestration or composition of multiple activities [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7].
- **Lifecycle Semantics:** Adopts "lifecycle" terminology to replace vendor-specific "execution engine" references across architectural specifications [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7].
- **Scope Boundaries:** Terminology specifically for gates, checks, and evaluations is explicitly scoped out of the workflow vocabulary and reserved for the Security, Observability, and Accuracy & Reliability working groups [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7].

# Lifecycle History
The Phase One Core Terms draft was reviewed and formally voted through at the August 2026 plenary of the Workflows & Process Integration WG, becoming the first formal artifact delivered by an AAIF working group [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7]. Initial upstream alignment with the cross-working-group taxonomy workstream established agreement on six core terms while maintaining agentic-AI-specific domain definitions [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7].

[^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/reporting/2026-08-report.md
