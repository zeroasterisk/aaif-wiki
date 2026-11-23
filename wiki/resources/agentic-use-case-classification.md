---
type: resource
title: Agentic Use Case Classification Schema
description: Classification schema defining structural workflow dimensions and active
  proposals for cross-boundary interaction categorizations.
resource: https://github.com/aaif/wg-workflows-and-process-integration/issues/60
tags:
- classification
- taxonomy
- use-cases
- workflows
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:30:36.677870+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-issue-60
  resource: https://github.com/aaif/wg-workflows-and-process-integration/issues/60
  author: mluciano-sbai
  last_modified: '2026-10-30T20:12:06+00:00'
---

# Overview
The Agentic Use Case Classification Schema establishes a structured taxonomy for cataloging and analyzing enterprise and horizontal agentic workflows [^evt-wg-workflows-and-process-integration-issue-60]. Developed under the [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md), the schema provides structural dimensions to describe agent initiation, autonomy gates, coordination models, and execution linearity.

# Architecture / Specification
## Established Classification Dimensions
The core schema organizes agent workflows across five foundational architectural dimensions [^evt-wg-workflows-and-process-integration-issue-60]:
1. **Trigger / Initiation**: Event-driven versus schedule- or human-initiated workflows.
2. **Governance Gate**: Autonomy level and presence of human checkpoints (e.g., approval gates).
3. **Agent Topology**: Single-agent sufficient versus multi-agent coordination models.
4. **Execution Flexibility**: Fixed or scripted logic versus dynamic path selection.
5. **Orchestration Pattern**: Sequential pipelines, parallel fan-outs, or iterative convergence loops.

## Proposed Boundary Dimension
An open proposal within the working group introduces an organizational boundary dimension to distinguish workflows based on data and approval demarcation [^evt-wg-workflows-and-process-integration-issue-60]:
- **Same team**: Workflow outputs and operational scopes remain within a single internal team (e.g., automated resume screening).
- **Across teams**: Workflows cross organizational boundaries requiring external handoffs and inter-department approvals (e.g., access request fulfillment or legal hold notifications).
- **Across companies**: Workflows negotiate or execute interactions across independent commercial entities (e.g., autonomous inventory reordering).

This proposed dimension addresses routing, verification, and boundary-crossing constraints that alter workflow governance across entries in the [Agentic Use Case Inventory](./agentic-use-case-inventory.md) [^evt-wg-workflows-and-process-integration-issue-60].

# References
- [WG Workflows and Process Integration Issue #60](https://github.com/aaif/wg-workflows-and-process-integration/issues/60) [^evt-wg-workflows-and-process-integration-issue-60]

[^evt-wg-workflows-and-process-integration-issue-60]: https://github.com/aaif/wg-workflows-and-process-integration/issues/60
