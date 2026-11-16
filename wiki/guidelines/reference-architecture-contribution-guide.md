---
type: guideline
title: Reference Architecture Contribution Guide
description: Authoring standards, taxonomy rules, and contribution criteria distinguishing
  patterns, reference architectures, scenarios, and decision records.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/CONTRIBUTING.md
tags:
- workflows
- reference-architectures
- patterns
- guidelines
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:08:25.200780+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/CONTRIBUTING.md
  author: Mario Zagar
  last_modified: '2026-09-15T16:19:55-04:00'
---

# Overview
The Reference Architecture Contribution Guide defines the formal standards and intake criteria for authoring workflow patterns, reference architectures, and scenario evaluations within the [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md)[^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4]. It ensures vendor-neutral framing, establishes a strict distinction between atomic patterns and composed practitioner jobs, and governs the incorporation of empirical use-case validation[^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4].

# Architecture / Specification

## Contribution Taxonomy
Contributors must classify proposals into one of five structural document types based on architectural scope[^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4]:
- **Pattern**: A self-contained, context-free solution to a recurring workflow sub-problem that can be adopted independently (such as [durable waits](../patterns/durable-wait.md) or [human approval gates](../patterns/human-approval-gate.md)). Patterns define mandatory invariants and concrete failure modes[^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4].
- **Reference Architecture**: A reusable composite architecture for a complete practitioner job (answering the sentence: *"We are building a ___"*). It composes multiple patterns, capability roles, system boundaries, operational guarantees, and exit states (such as [Bounded Autonomous Remediation](../architectures/bounded-autonomous-remediation.md))[^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4].
- **Scenario**: A worked example or test case embedded in an architecture's validation sections to verify coverage against real-world systems[^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4].
- **Decision Note**: An architectural record capturing rationale, alternatives, and consequences for structural choices (using the [Reference Architecture Decision Template](../guidelines/reference-architecture-decision-template.md))[^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4].
- **Document / Research**: Background surveys, comparisons, and exploratory research informing architectures without defining normative requirements[^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4].

## Core Authoring Rules
All submissions must adhere to foundational quality and governance constraints[^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4]:
- **Vendor Neutrality**: Logical capabilities and behavioral requirements must be specified prior to referencing commercial or open-source software implementations[^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4].
- **Evidence vs. Interpretation**: Authors must separate empirical implementation facts from proposed working-group interpretations, recording genuine gaps as explicit open questions[^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4].
- **Boundary Respect**: Cross-cutting requirements owned by adjacent working groups (such as identity or telemetry standards) must be scoped out rather than redefined locally[^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4].
- **Domain Decoupling**: Generic reference architectures must not adopt domain-specific naming unless the practitioner job itself is inherently domain-locked[^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4].

# Lifecycle History
Adopted by the Workflows and Process Integration Working Group to maintain structural consistency and prevent terminology drift across reference architecture workstreams[^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4].

[^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/CONTRIBUTING.md
