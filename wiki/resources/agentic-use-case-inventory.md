---
type: resource
title: Agentic Use Case Inventory
description: Catalog of production agentic workflows classified by orchestration structure,
  human-in-the-loop checkpoints, failure modes, and evidentiary verification.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/critical-use-cases/use-case-inventory.md
tags:
- workflows
- use-cases
- coordination
- production-deployment
- classification
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T10:49:23.773344+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-c10bbaa87c3e-880211ae
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/critical-use-cases/use-case-inventory.md
  author: Jodee Varney
  last_modified: '2026-10-01T07:35:55-07:00'
- id: evt-wg-workflows-and-process-integration-pr-41
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/41
  author: jodeev
  last_modified: '2026-10-01T14:35:56+00:00'
---

# Overview
The Agentic Use Case Inventory is an empirical reference catalog maintained by the Critical Use Cases Workstream within the [Workflows & Process Integration Working Group](../working-groups/workflows-and-process-integration.md) that documents working, production-grade agent workflows across diverse industries [^evt-wg-workflows-and-process-integration-file-c10bbaa87c3e-880211ae]. Rather than presenting an exhaustive or speculative list of AI applications, the inventory captures concrete structural implementations—cataloging triggers, human-in-the-loop (HITL) gates, coordination mechanisms, agent counts, workflow shapes, failure modes, and operational preconditions [^evt-wg-workflows-and-process-integration-file-c10bbaa87c3e-880211ae].

The catalog aligns directly with the dimensional schema established in the [Agentic Use Case Classification](../resources/agentic-use-case-classification.md) specification, prioritizing pattern breadth across operational contexts over volume within any single vertical [^evt-wg-workflows-and-process-integration-file-c10bbaa87c3e-880211ae].

# Architecture / Specification

## Domain Coverage
The inventory categorizes agent workflows across three primary operational domains [^evt-wg-workflows-and-process-integration-file-c10bbaa87c3e-880211ae]:
1. **Cross-Industry / Horizontal**: Workflows common across corporate functions, including Sales, Marketing, Customer Support, Finance & Operations, Human Resources & Recruiting, and Research & Intelligence.
2. **Technology & Engineering**: Systems-focused implementations spanning Engineering, IT / Network Operations, Software Development Lifecycle (SDLC), and Platform Engineering.
3. **Industry-Specific**: Highly regulated or specialized operational pipelines across Healthcare, Supply Chain, Legal, Education, and Real Estate.

## Workflow Invariants and Classification Dimensions
Each cataloged row captures structural fields defined in the AAIF schema [^evt-wg-workflows-and-process-integration-file-c10bbaa87c3e-880211ae]:
- **Trigger**: The specific stimulus initializing agent activity, such as incoming messages, scheduled timers, webhooks, or system alerts.
- **HITL Pattern and Approval Gate**: Human oversight mechanisms, distinguishing between pre-execution authorization gates, asynchronous review queues, and post-execution escalations [^evt-wg-workflows-and-process-integration-pr-41].
- **Agent Count and Rationale**: Identifies single-agent versus multi-agent execution, mandating explicit rationales for workflows classified as "Better as multi-agent" or "Inherently multi-agent" [^evt-wg-workflows-and-process-integration-pr-41].
- **Coordination Mechanism**: Communication and state-passing protocols coordinating participating agents.
- **Workflow Shape and Failure Modes**: Operational topology and primary runtime risks, such as context exhaustion or boundary drift.

## Evidentiary Standards and Verification
To maintain rigor and eliminate speculative vendor claims, the inventory enforces strict citation standards [^evt-wg-workflows-and-process-integration-pr-41]:
- **Preferred Evidence**: Primary vendor announcements or product documentation referencing verified, named customer production deployments [^evt-wg-workflows-and-process-integration-pr-41].
- **Acceptable Evidence**: Vendor documentation showing robust feature capabilities operating in production at scale when customer names are proprietary [^evt-wg-workflows-and-process-integration-pr-41].
- **Prohibited Sources**: Secondary blog posts, analyst market forecasts, academic preprints, and non-authoritative implementer write-ups are excluded [^evt-wg-workflows-and-process-integration-pr-41].
- **Citation Density and Link Health**: Entries target three independent verifiable citations per row, with systematic auditing to prune link rot, acquisitions, and deprecated tooling [^evt-wg-workflows-and-process-integration-pr-41].

[^evt-wg-workflows-and-process-integration-file-c10bbaa87c3e-880211ae]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/critical-use-cases/use-case-inventory.md
[^evt-wg-workflows-and-process-integration-pr-41]: https://github.com/aaif/wg-workflows-and-process-integration/pull/41
