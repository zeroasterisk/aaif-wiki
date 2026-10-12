---
type: guideline
title: Workflow Pattern Template
description: Standardized structure, header conventions, invariant definitions, and
  runtime mapping matrix for AAIF workflow patterns.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/TEMPLATE.md
tags:
- guidelines
- patterns
- workflows
- templates
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:09:09.431272+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-0f939e51d343-befb4054
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/TEMPLATE.md
  author: Zayne Turner
  last_modified: '2026-08-05T23:05:12-04:00'
---

# Overview
The AAIF Workflow Pattern Template standardizes the authoring of workflow patterns within the [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md) [^evt-wg-workflows-and-process-integration-file-0f939e51d343-befb4054]. Under the [Job-Oriented Architecture Model](../guidelines/job-oriented-architecture-model.md), patterns represent independently adoptable, context-free solutions to recurring workflow sub-problems, distinct from complete [reference architectures](../guidelines/reference-architecture-template.md) that compose them [^evt-wg-workflows-and-process-integration-file-0f939e51d343-befb4054].

# Architecture / Specification
Every pattern document authored for the working group must adhere to standard section conventions [^evt-wg-workflows-and-process-integration-file-0f939e51d343-befb4054]:

- **Naming Convention**: Pattern names must name the architectural fix rather than a particular use case [^evt-wg-workflows-and-process-integration-file-0f939e51d343-befb4054].
- **Header Metadata**: Required metadata lines including `Solves`, `Used in` (linking to reference architectures), `Requires capabilities` (identifying necessary capability roles), and `Related patterns` (linking to complementary patterns such as [approval-checkpoint](../patterns/approval-checkpoint.md)) [^evt-wg-workflows-and-process-integration-file-0f939e51d343-befb4054].
- **Problem & Why This Is Hard**: Formulates the recurring sub-problem recognized by practitioners and lists the competing engineering tensions that prevent naive solutions [^evt-wg-workflows-and-process-integration-file-0f939e51d343-befb4054].
- **Solution Shape**: Context-free diagram or structure restricted to 2–4 boxes without vendor, runtime, or use-case specifics; solutions requiring more boxes must be structured as reference architectures [^evt-wg-workflows-and-process-integration-file-0f939e51d343-befb4054].
- **Invariants**: Core guarantees that must hold across any implementation, expressed in product-agnostic terms [^evt-wg-workflows-and-process-integration-file-0f939e51d343-befb4054].
- **Failure Modes When Violated**: Concrete breakdowns and operational hazards corresponding directly to each violated invariant [^evt-wg-workflows-and-process-integration-file-0f939e51d343-befb4054].
- **Implementation Approaches Table**: Illustrative runtime implementations categorized along a pattern-specific differentiation axis (such as execution families or enforcement boundaries), documenting the mechanism, platform-provided capabilities, and developer-added controls [^evt-wg-workflows-and-process-integration-file-0f939e51d343-befb4054].
- **Known Uses Outside Agents**: Pre-LLM historical precedents demonstrating the pattern was discovered rather than invented, noting the conceptual delta introduced by autonomous agents [^evt-wg-workflows-and-process-integration-file-0f939e51d343-befb4054].

[^evt-wg-workflows-and-process-integration-file-0f939e51d343-befb4054]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/TEMPLATE.md
