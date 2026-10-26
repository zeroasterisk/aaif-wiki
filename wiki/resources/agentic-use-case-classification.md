---
type: resource
title: Agentic Use Case Classification Schema
description: Twelve-column taxonomy separating structural design choices into five
  classification dimensions from seven supporting execution and evidence fields.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/critical-use-cases/schema-agentic-use-cases.md
tags:
- workflows
- classification
- schema
- use-cases
- architecture
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T10:45:03.901065+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-6cdd0fb97084-5ba45ebc
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/critical-use-cases/schema-agentic-use-cases.md
  author: Jodee Varney
  last_modified: '2026-10-01T07:35:55-07:00'
- id: evt-wg-workflows-and-process-integration-pr-46
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/46
  author: jodeev
  last_modified: '2026-10-01T14:36:15+00:00'
---

# Overview

The Agentic AI Foundation Workflows & Process Integration Working Group defines a standardized twelve-column classification schema for describing and comparing agentic workflows across production deployments [^evt-wg-workflows-and-process-integration-file-6cdd0fb97084-5ba45ebc]. Developed by the Critical Use Cases Workstream, the schema establishes a common framework to classify implementations in the companion use case inventory [^evt-wg-workflows-and-process-integration-pr-46].

The schema explicitly distinguishes between five core structural dimensions that reflect deliberate architectural choices and seven supporting fields that provide row identification, runtime observations, and empirical deployment evidence [^evt-wg-workflows-and-process-integration-file-6cdd0fb97084-5ba45ebc]. Workflows are classified against their specific cited implementations rather than abstract use case names, accommodating variations across systems sharing similar functional titles.

# Architecture / Specification

### Classification Dimensions

A classification dimension represents a structural fork in workflow design. The schema standardizes five discrete dimensions [^evt-wg-workflows-and-process-integration-file-6cdd0fb97084-5ba45ebc]:

1. **Trigger**: The invocation mechanism initiating workflow execution (external system events, scheduled cron routines, or direct human prompting).
2. **HITL Pattern**: The human-in-the-loop governance structure determining where, if anywhere, human intervention is mandatory before proceeding (e.g., [human approval gates](../patterns/human-approval-gate.md) or checkpoints).
3. **Agent Count**: The number of distinct reasoning agents deployed, driven by task decomposition, model specialization, or isolated tool privilege boundaries.
4. **Coordination**: The control mechanism orchestrating multi-agent or multi-step execution, categorized as fixed deterministic code or dynamic runtime model reasoning.
5. **Workflow Pattern**: The operational execution topology, distinguishing sequential straight-line executions, concurrent branch-and-merge pipelines, or iterative loops retrying against validation gates (such as [bounded convergence loops](../patterns/bounded-convergence-loop.md)).

### Supporting Fields

The remaining seven columns record non-dimensional metadata, observed metrics, and evidentiary rationale [^evt-wg-workflows-and-process-integration-file-6cdd0fb97084-5ba45ebc]:

- **Duration**: Empirical agent processing time, strictly excluding human approval queue waits and external downstream latency.
- **Use Case & Description**: Standardized names and descriptive summaries.
- **Tools & Systems**: Connected external interfaces and host environments.
- **Key Failure Mode**: Principal breakdown scenarios observed or mitigated.
- **Preconditions**: Required system states, tokens, or environment baselines.
- **Notes**: Rationale and verifiable deployment citations.

# Lifecycle History

The classification schema was developed within the Critical Use Cases Workstream and merged in pull request #46 [^evt-wg-workflows-and-process-integration-pr-46]. As of late 2026, the schema definitions and category groupings are positioned for Working Group review, with formal alignment underway with the Reference Architecture Workstream [^evt-wg-workflows-and-process-integration-file-6cdd0fb97084-5ba45ebc].

# References

- Companion catalog: [Agentic Use Case Inventory](../resources/agentic-use-case-inventory.md)
- Working group: [Workflows & Process Integration Working Group](../working-groups/workflows-and-process-integration.md)
- Architecture guidelines: [Workflow Pattern Template](../guidelines/workflow-pattern-template.md)

[^evt-wg-workflows-and-process-integration-file-6cdd0fb97084-5ba45ebc]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/critical-use-cases/schema-agentic-use-cases.md
[^evt-wg-workflows-and-process-integration-pr-46]: https://github.com/aaif/wg-workflows-and-process-integration/pull/46
