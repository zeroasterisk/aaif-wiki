---
type: guideline
title: Reference Architecture Validation Guide
description: Evaluation methodology and classification criteria validating AAIF reference
  architectures against empirical use cases using structured fit ratings.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/35
tags:
- guidelines
- reference-architectures
- validation
- use-cases
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T10:22:02.383460+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-pr-35
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/35
  author: mzagar
  last_modified: '2026-09-15T20:19:55+00:00'
---

# Overview

The Reference Architecture Validation Guide defines the standardized evaluation framework for testing AAIF workflow reference architectures against real-world use cases[^evt-wg-workflows-and-process-integration-pr-35]. It establishes repeatable scoring categories and structured artifact formats for validation records submitted via GitHub issues and pull requests[^evt-wg-workflows-and-process-integration-pr-35].

# Architecture / Specification

### Architectural Fit Classifications

Validation assessments classify the architectural compatibility of a candidate use case into four standard ratings[^evt-wg-workflows-and-process-integration-pr-35]:

- **Validated:** The use case fully matches the reference architecture's structural boundaries, pattern composition, and execution guarantees without requiring architectural exceptions.
- **Partial:** The use case conforms to the core execution model but diverges in specific boundary controls, tooling requirements, or peripheral capabilities.
- **No Fit:** The use case violates core architectural assumptions (e.g., attempting bounded autonomy without independent acceptance gates, or omitting human checkpoints where required).
- **Candidate:** The use case has been proposed and documented as an illustrative scenario but lacks empirical execution data or an authoritative Use Case Inventory backing[^evt-wg-workflows-and-process-integration-pr-35].

### Contribution and Lifecycle

Validation records are linked directly to architecture specifications—such as [Bounded Autonomous Remediation](../architectures/bounded-autonomous-remediation.md)—and indexed in working group documentation to prevent theoretical drift[^evt-wg-workflows-and-process-integration-pr-35].

[^evt-wg-workflows-and-process-integration-pr-35]: https://github.com/aaif/wg-workflows-and-process-integration/pull/35
