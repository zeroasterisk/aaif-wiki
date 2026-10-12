---
type: guideline
title: Reference Architecture Validation Methodology
description: Four-outcome evaluation methodology validating workflow reference architectures
  against real-world use cases by verifying architectural boundary fit.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/reporting/2026-08-report.md
tags:
- guideline
- validation
- reference-architecture
- workflows
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:33:54.765261+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/reporting/2026-08-report.md
  author: Yaron Schneider
  last_modified: '2026-09-27T17:45:13-07:00'
---

# Overview

The Reference Architecture Validation Methodology defines the criteria and evaluation framework used by the [Workflows & Process Integration Working Group](../working-groups/workflows-and-process-integration.md) to validate whether reference architectures accurately represent real-world use cases.[^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7] The methodology focuses exclusively on architectural fit—verifying that an architecture addresses the same operational job and respects identical structural boundaries—without imposing runtime implementation requirements.[^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7]

# Architecture / Specification

Validation evaluations assign each candidate architecture-to-use-case relationship into one of four standard outcomes:[^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7]

- **Validated**: The reference architecture precisely matches the operational role, boundary transitions, and safety constraints of the production use case from which it was abstracted or against which it was tested.[^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7]
- **Partial**: The reference architecture captures core interactions but omits structural variants or topological nuances (e.g., parallel remediation branches or alternative subagent structures).[^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7]
- **Candidate**: The architecture is theoretically aligned with a class of use cases but awaits formal verification against multiple inventory entries.[^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7]
- **No Fit**: The operational problem exhibits fundamentally mismatched control planes, approval mechanics, or security boundaries, requiring a distinct architectural archetype.[^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7]

# Lifecycle History

Formulated in August 2026 during the finalization of the charter deliverables for the Reference Architectures workstream.[^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7] The model was initially applied to classify the [Bounded Autonomous Remediation](../architectures/bounded-autonomous-remediation.md) architecture as validated against its source case, and the [Single-Agent Human Approval](../architectures/single-agent-human-approval.md) architecture as candidate pending broader multi-case inventory verification.[^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7]

[^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/reporting/2026-08-report.md
