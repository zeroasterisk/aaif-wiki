---
type: workstream
title: Reference Architectures Workstream
description: Workstream within the Workflows & Process Integration WG establishing
  a catalog of job-oriented reference architectures, patterns, and validation methods.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/CONTRIBUTING.md
tags:
- workflows
- reference-architectures
- patterns
- workstream
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T18:02:22.540545+00:00'
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
- id: evt-wg-workflows-and-process-integration-pr-35
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/35
  author: mzagar
  last_modified: '2026-09-15T20:19:55+00:00'
---

# Overview

The Reference Architectures Workstream is a core initiative within the [Workflows & Process Integration Working Group](../workflows-and-process-integration.md) tasked with authoring, formalizing, and maintaining reusable agentic workflow architectures, composable workflow patterns, and empirical validation methods [^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4]. The workstream operates under the [Job-Oriented Architecture Model](../../specification/job-oriented-architecture-model.md) to structure agentic system designs around recognizable practitioner jobs while isolating sub-problem patterns and empirical validation scenarios [^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4].

# Architecture / Specification

### Contribution Types

The workstream enforces a clear separation across four distinct contribution types [^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4]:

- **Workflow Patterns**: Independently adoptable solutions addressing a single, recurring workflow sub-problem (e.g., [durable wait](../../specification/durable-wait.md), [human approval gate](../../specification/human-approval-gate.md), or [deterministic acceptance gate](../../specification/deterministic-acceptance-gate.md)) [^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4].
- **Reference Architectures**: Reusable compositions addressing an entire practitioner job (completing the phrase *“We are building a ___”*), specifying capability roles, boundaries, guarantees, and exit states [^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4].
- **Worked Scenarios**: Real or illustrative workflow examples used to validate whether an architecture fits an empirical problem; scenarios do not constitute architectures by themselves [^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4].
- **Decision Notes**: Structured architectural decision records documenting context, trade-offs, and consequences [^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4].

### Authoring Rules and Validation

Contributions across the workstream must adhere to strict neutrality and verification guidelines [^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4], [^evt-wg-workflows-and-process-integration-file-cd94574f9d34-a7acfb30]:

- **Vendor Neutrality**: Logical capabilities and boundaries must be described before referencing specific tooling or vendor products [^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4].
- **Explicit Boundaries**: The boundary between agent execution and deterministic workflow-controlled orchestration must be explicitly delineated [^evt-wg-workflows-and-process-integration-file-cd94574f9d34-a7acfb30].
- **Evidence Grounding**: Authors must clearly distinguish verified empirical facts from proposed working group interpretations, recording unresolved questions as open questions rather than speculative assertions [^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4], [^evt-wg-workflows-and-process-integration-file-cd94574f9d34-a7acfb30].
- **Use-Case Validation**: Reference architectures are validated against real-world use cases using the [Reference Architecture Use-Case Validation Guide](../../deliverable/ra-use-case-validation-guide.md), evaluating fit and boundary alignment against empirical datasets from the [Critical Use Cases Workstream](critical-use-cases-workstream.md) [^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64], [^evt-wg-workflows-and-process-integration-pr-35].

[^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4]: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/CONTRIBUTING.md
[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64]: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/docs/ra-use-case-validation-guide.md
[^evt-wg-workflows-and-process-integration-file-cd94574f9d34-a7acfb30]: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/AGENTS.md
[^evt-wg-workflows-and-process-integration-pr-35]: https://github.com/aaif/wg-workflows-and-process-integration/pull/35
