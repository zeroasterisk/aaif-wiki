---
type: guideline
title: Reference Architecture Validation Guide
description: Standardized evaluation procedures and fit classifications for validating
  AAIF reference architectures against real-world use cases.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/35
tags:
- workflows
- reference-architectures
- guidelines
- validation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T09:55:29.329353+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-pr-35
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/35
  author: mzagar
  last_modified: '2026-09-15T20:19:55+00:00'
- id: evt-wg-workflows-and-process-integration-file-cd94574f9d34-a7acfb30
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/AGENTS.md
  author: Mario Zagar
  last_modified: '2026-09-15T16:19:55-04:00'
---

# Overview

The Reference Architecture Validation Guide defines the standardized process for evaluating an Agentic AI Foundation (AAIF) reference architecture against real-world use cases[^evt-wg-workflows-and-process-integration-pr-35]. It establishes consistent assessment categories, required evidence formats, and operational rules for AI and human contributors documenting architectural fit across production workloads[^evt-wg-workflows-and-process-integration-file-cd94574f9d34-a7acfb30].

# Architecture / Specification

### Validation Classifications
When comparing a candidate architecture against an operational use case, contributors assign one of four standardized status designations[^evt-wg-workflows-and-process-integration-pr-35]:
- **Validated**: The real-world use case demonstrably matches all core patterns, capability roles, boundaries, and exit states of the architecture.
- **Partial**: The use case shares core capability roles and pattern compositions but exhibits structural gaps, such as missing deterministic gates or divergent escalation pathways.
- **No fit**: The operational constraints, authority models, or boundary requirements fundamentally conflict with the reference architecture.
- **Candidate**: A proposed use case submitted for evaluation that has not yet completed comparative review against working group evidence standards.

### Contributor Directives
As detailed in the workstream contributor rules, validation assessments must rely strictly on verified source evidence rather than speculative interpretations[^evt-wg-workflows-and-process-integration-file-cd94574f9d34-a7acfb30]. Evaluators must avoid generating unrequested GitHub issues or pull requests during automated triage, record terminology gaps as open questions rather than novel constructs, and document domain scenarios as validation proofs rather than generic architecture definitions[^evt-wg-workflows-and-process-integration-file-cd94574f9d34-a7acfb30].

# Lifecycle History

- Authored following Workstream Sync #6 to provide a standard output mechanism for validation PRs and issue records[^evt-wg-workflows-and-process-integration-pr-35].
- Linked directly from contributor guidelines and instructions for AI contributors[^evt-wg-workflows-and-process-integration-file-cd94574f9d34-a7acfb30].

# References
- [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md)
- [Reference Architecture Template](reference-architecture-template.md)
- [Bounded Autonomous Remediation](../architectures/bounded-autonomous-remediation.md)

[^evt-wg-workflows-and-process-integration-file-cd94574f9d34-a7acfb30]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/AGENTS.md
[^evt-wg-workflows-and-process-integration-pr-35]: https://github.com/aaif/wg-workflows-and-process-integration/pull/35
