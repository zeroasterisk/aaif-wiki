---
type: methodology
title: Job-Oriented Workflow Reference Architectures
description: Framework organizing workflow reference architectures around practitioner
  operational jobs, reusable patterns, and validation scenarios.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/CONTRIBUTING.md
tags:
- methodology
- workflows
- reference-architectures
- patterns
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T10:09:35.963034+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/CONTRIBUTING.md
  author: Mario Zagar
  last_modified: '2026-09-15T16:19:55-04:00'
- id: evt-wg-workflows-and-process-integration-file-cd94574f9d34-a7acfb30
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/AGENTS.md
  author: Mario Zagar
  last_modified: '2026-09-15T16:19:55-04:00'
- id: evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/docs/ra-use-case-validation-guide.md
  author: Mario Zagar
  last_modified: '2026-09-15T16:19:55-04:00'
---

# Overview

The Job-Oriented Reference Architecture model is an architectural framework curated by the [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md) that organizes workflow reference architectures around concrete practitioner jobs rather than generic product categories or isolated technical mechanisms[^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4]. The methodology establishes strict differentiation between atomic patterns, multi-pattern reference architectures, validation scenarios, and decision records[^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4][^evt-wg-workflows-and-process-integration-file-cd94574f9d34-a7acfb30].

# Architecture / Specification

## Structural Taxonomy

The framework establishes explicit structural roles across three primary contribution types[^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4]:

| Contribution Type | Granularity | Scope and Purpose |
|---|---|---|
| **Pattern** | Sub-problem | Solves one recurring workflow challenge (such as [durable-wait](../patterns/durable-wait.md) or [human-approval-gate](../patterns/human-approval-gate.md)) independently of specific end-to-end jobs[^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4]. |
| **Reference Architecture** | Practitioner Job | Defines the complete logical composition, capability boundaries, execution guarantees, and exit states answering *"We are building a [Job]"*[^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4]. |
| **Scenario** | Instance/Evidence | A concrete or illustrative workflow example used in validation records to test architectural fit; scenarios do not constitute standalone architectures[^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4][^evt-wg-workflows-and-process-integration-file-cd94574f9d34-a7acfb30]. |

## Authoring and Contribution Rules

Contributors (including autonomous AI coding agents) must adhere to mandatory authoring principles[^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4][^evt-wg-workflows-and-process-integration-file-cd94574f9d34-a7acfb30]:

- **Vendor Neutrality**: Specify capabilities and required invariants at the logical role level before referencing concrete vendor products or implementations[^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4].
- **Boundary Clarity**: Explicitly delineate what is controlled by the non-deterministic agent versus deterministic workflow orchestrators and human operators[^evt-wg-workflows-and-process-integration-file-cd94574f9d34-a7acfb30].
- **Evidence vs. Interpretation**: Distinguish empirically verified facts from proposed working group interpretations, maintaining genuine gaps as explicit open questions[^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4][^evt-wg-workflows-and-process-integration-file-cd94574f9d34-a7acfb30].
- **Validation Coupling**: Every reference architecture is linked to real-world use cases using the [reference-architecture-validation methodology](../methodology/reference-architecture-validation.md)[^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4][^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].

# Lifecycle History

Adopted in the `workstreams/reference-architectures` directory of the Workflows & Process Integration Working Group as the standard structure for curating patterns, architectures, and use case validation guides[^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4][^evt-wg-workflows-and-process-integration-file-cd94574f9d34-a7acfb30].

[^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4]: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/CONTRIBUTING.md
[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64]: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/docs/ra-use-case-validation-guide.md
[^evt-wg-workflows-and-process-integration-file-cd94574f9d34-a7acfb30]: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/AGENTS.md
