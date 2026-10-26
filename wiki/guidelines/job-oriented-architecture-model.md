---
type: guideline
title: Job-Oriented Architecture Model
description: Architectural framework structuring agent workflows around recognizable
  practitioner jobs rather than structural agent counts.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/decisions/job-oriented-architecture-model.md
tags:
- workflows
- reference-architecture
- design-patterns
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T10:02:14.815405+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-f035520d0488-6fefbf62
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/decisions/job-oriented-architecture-model.md
  author: Zayne Turner
  last_modified: '2026-08-05T23:05:12-04:00'
---

# Overview

The Job-Oriented Architecture Model organizes Agentic AI Foundation workflow reference architectures around recognizable practitioner jobs rather than structural agent counts.[^evt-wg-workflows-and-process-integration-file-f035520d0488-6fefbf62]

Practitioners typically approach workflow design with a concrete operational objective—such as required human approval, durable state execution, bounded convergence, or coordinated handoff—before deciding how many agents are needed to fulfill it.[^evt-wg-workflows-and-process-integration-file-f035520d0488-6fefbf62] Structuring the architecture catalog around agent count creates ambiguous categories containing workflows with materially different guarantees, failure modes, and security topologies.[^evt-wg-workflows-and-process-integration-file-f035520d0488-6fefbf62]

# Architecture / Specification

Under this decision model, reference architectures and reusable workflow patterns maintain an explicit structural relationship:

- **Reference Architecture**: A complete composition of reusable patterns, required capabilities, system boundaries, operational guarantees, and exit states tailored to a discrete, named practitioner job.[^evt-wg-workflows-and-process-integration-file-f035520d0488-6fefbf62]
- **Workflow Pattern**: An independently adoptable technical solution to one recurring workflow problem (such as `../patterns/human-approval-gate.md` or `../patterns/durable-wait.md`). Architectures compose patterns, while patterns retain their own invariants, failure modes, and implementation examples.[^evt-wg-workflows-and-process-integration-file-f035520d0488-6fefbf62]
- **Structural Characteristics**: Topologies such as single-agent or multi-agent are treated as internal structural characteristics rather than top-level architectural categories.[^evt-wg-workflows-and-process-integration-file-f035520d0488-6fefbf62]
- **Validation via Use Cases**: Practical scenarios and use cases validate whether a reference architecture provides appropriate coverage. Unmatched scenarios signal a missing pattern or a distinct job requiring a separate architecture.[^evt-wg-workflows-and-process-integration-file-f035520d0488-6fefbf62]

# Lifecycle History

Proposed on 2026-07-20 within the Workflows and Process Integration Working Group (`../working-groups/workflows-and-process-integration.md`) to replace generic agent count scaffolding with job-centric compositions.[^evt-wg-workflows-and-process-integration-file-f035520d0488-6fefbf62]

# References

- Working group decision note: `workstreams/reference-architectures/decisions/job-oriented-architecture-model.md`.[^evt-wg-workflows-and-process-integration-file-f035520d0488-6fefbf62]

[^evt-wg-workflows-and-process-integration-file-f035520d0488-6fefbf62]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/decisions/job-oriented-architecture-model.md
