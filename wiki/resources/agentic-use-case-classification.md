---
type: resource
title: Agentic Use Case Classification Schema
description: Classification schema defining structural workflow dimensions and evidentiary
  standards for cataloging production agent deployments.
resource: https://github.com/aaif/wg-workflows-and-process-integration/issues/58
tags:
- use-cases
- classification
- workflows
- schema
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:29:37.606945+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-issue-58
  resource: https://github.com/aaif/wg-workflows-and-process-integration/issues/58
  author: jodeev
  last_modified: '2026-10-29T15:37:04+00:00'
- id: evt-wg-workflows-and-process-integration-issue-59
  resource: https://github.com/aaif/wg-workflows-and-process-integration/issues/59
  author: jodeev
  last_modified: '2026-10-29T15:34:57+00:00'
---

# Overview

The Agentic Use Case Classification Schema establishes a structured categorization framework for analyzing real-world agent deployments within the [Agentic Use Case Inventory](../resources/agentic-use-case-inventory.md).[^evt-wg-workflows-and-process-integration-issue-59] Maintained by the [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md), the schema provides dimensional metadata to classify autonomy bounds, orchestration topologies, and human-in-the-loop oversight mechanisms.[^evt-wg-workflows-and-process-integration-issue-58]

# Specification

The classification schema structures each documented production use case across key organizational and technical dimensions:[^evt-wg-workflows-and-process-integration-issue-58][^evt-wg-workflows-and-process-integration-issue-59]

- **Workflow Topology and Shape**: Categorizes execution structures (e.g., single-agent loops, parallel fan-out, hierarchical delegation); actively proposed to transition nomenclature from "Workflow Pattern" to "Workflow Shape" to avoid conflation with foundational Reference Architecture patterns and primitives.[^evt-wg-workflows-and-process-integration-issue-58]
- **HITL Oversight**: Defines interaction boundaries and approval checkpoints; actively proposed to transition from "HITL Pattern" to "HITL Shape".[^evt-wg-workflows-and-process-integration-issue-58]
- **Evidentiary Citation Standard**: Mandates that every cataloged deployment cite verifiable, publicly accessible primary sources (vendor announcements or production case studies) with publication or retrieval dates.[^evt-wg-workflows-and-process-integration-issue-59]
- **Link Hygiene and Rot Remediation**: Implements automated link extraction and validation workflows to monitor citation status (200, redirect, 404, or blocked) and flag stale evidence without corrupting evidentiary compliance.[^evt-wg-workflows-and-process-integration-issue-59]

# Lifecycle History

- **2026-10**: Issue #58 proposed renaming schema pattern dimensions to "shapes" to disambiguate use case metadata from reference architecture patterns.[^evt-wg-workflows-and-process-integration-issue-58]
- **2026-10**: Issue #59 initiated scheduled CI automation to extract and verify external citation links against link rot.[^evt-wg-workflows-and-process-integration-issue-59]

[^evt-wg-workflows-and-process-integration-issue-58]: https://github.com/aaif/wg-workflows-and-process-integration/issues/58
[^evt-wg-workflows-and-process-integration-issue-59]: https://github.com/aaif/wg-workflows-and-process-integration/issues/59
