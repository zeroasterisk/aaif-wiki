---
type: guideline
title: Job-Oriented Architecture Model
description: Architectural framework structuring agent workflow reference architectures
  around recognizable practitioner jobs, patterns, and scenarios.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/CONTRIBUTING.md
tags:
- architecture
- guidelines
- patterns
- workflows
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T09:55:05.974401+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/CONTRIBUTING.md
  author: Mario Zagar
  last_modified: '2026-09-15T16:19:55-04:00'
---

# Overview

The Job-Oriented Architecture Model provides the organizing framework for the [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md) reference architecture workstream, delineating the responsibilities of patterns, reference architectures, scenarios, and decision records [^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4]. It ensures architectural specifications represent cohesive practitioner roles rather than fragmented implementation recipes [^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4].

# Contribution Taxonomy

The framework establishes strict boundaries for authoring workflow assets [^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4]:

- **Patterns**: Address a single recurring workflow sub-problem with an independently adoptable solution and testable invariants (e.g., [Durable Wait](../patterns/durable-wait.md), [Human Approval Gate](../patterns/human-approval-gate.md)) [^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4].
- **Reference Architectures**: The reusable whole addressing a recognizable practitioner job, answering the statement "We are building a ___" [^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4]. Architectures compose multiple capability roles, boundary controls, pattern invariants, and exit states (e.g., [Bounded Autonomous Remediation](../architectures/bounded-autonomous-remediation.md)) [^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4]. Domain-specific examples do not serve as architecture titles unless the practitioner job itself is inherently domain-specific.
- **Scenarios**: Concrete or illustrative workflow examples documented in an architecture's worked scenarios and validation records to verify architectural fit without forming standalone architectures [^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4].
- **Decision Notes**: Formal records capturing structural rationale, evaluated alternatives, and consequences [^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4].

# Authoring Principles

Contributions across all tiers must maintain vendor neutrality, define logical capability requirements prior to naming tools, separate empirical evidence from working group interpretations, explicitly cite cross-cutting concerns owned by other working groups as out of scope, and document genuine gaps as open questions [^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4].

[^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/CONTRIBUTING.md
