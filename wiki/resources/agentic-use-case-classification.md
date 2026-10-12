---
type: resource
title: Agentic Use Case Classification and Inventory
description: Empirical inventory and classification schema mapping production agentic
  workflows against multi-dimensional properties and strict deployment evidentiary
  standards.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/critical-use-cases/README.md
tags:
- workflows
- use-cases
- classification
- methodology
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:38:13.383580+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-5028db4c24a1-b054a303
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/critical-use-cases/README.md
  author: Jodee Varney
  last_modified: '2026-10-01T07:36:14-07:00'
- id: evt-wg-workflows-and-process-integration-pr-46
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/46
  author: jodeev
  last_modified: '2026-10-01T14:36:15+00:00'
---

# Overview
The Agentic Use Case Classification and Inventory is an empirical catalog maintained by the [Workflows & Process Integration Working Group](../working-groups/workflows-and-process-integration.md) to document recurring agentic workflow shapes from real-world production deployments [^evt-wg-workflows-and-process-integration-file-5028db4c24a1-b054a303]. The initiative provides an explicit, evidence-backed inventory of named workflows rather than hypothetical architectures, enabling practitioners to identify patterns across multiple industries [^evt-wg-workflows-and-process-integration-pr-46].

# Architecture / Specification
The workstream repository is organized into distinct documentation components [^evt-wg-workflows-and-process-integration-file-5028db4c24a1-b054a303]:
- `schema-agentic-use-cases.md`: Defines column schemas, valid categorical property values, and open taxonomy questions for workflow classification.
- `use-case-inventory.md`: The central matrix recording deployed workflows, associated runtime properties, and verified production references.

## Evidentiary Standard
To ensure reliable taxonomy derivation, the workstream enforces an evidentiary threshold for all inventory entries [^evt-wg-workflows-and-process-integration-file-5028db4c24a1-b054a303]:
- **Citation Minimums**: Each use case requires at least one publicly accessible, independently verifiable citation of confirmed production deployment, with a target of three independent citations [^evt-wg-workflows-and-process-integration-file-5028db4c24a1-b054a303].
- **Preferred Evidence**: Primary announcements or vendor product documentation demonstrating a named customer deployment (such as Cohere Health with BSIM or PagerDuty with Chicago Trading Company) [^evt-wg-workflows-and-process-integration-file-5028db4c24a1-b054a303].
- **Acceptable Evidence**: Vendor documentation showing strong technical evidence of production usage at scale, even without an identified customer [^evt-wg-workflows-and-process-integration-file-5028db4c24a1-b054a303].
- **Unacceptable Sources**: Secondary blog posts, market analyst commentary, academic publications, market projections, or unverifiable implementer claims [^evt-wg-workflows-and-process-integration-file-5028db4c24a1-b054a303].

# Lifecycle History
The classification schema, category groupings, and evidentiary criteria were codified for working group vote in PR#46 [^evt-wg-workflows-and-process-integration-pr-46], moving row-level verification into an active multi-contributor phase.

[^evt-wg-workflows-and-process-integration-file-5028db4c24a1-b054a303]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/critical-use-cases/README.md
[^evt-wg-workflows-and-process-integration-pr-46]: https://github.com/aaif/wg-workflows-and-process-integration/pull/46
