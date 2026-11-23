---
type: guideline
title: Reference Architecture Validation Guide
description: Operational framework and evaluation taxonomy classifying reference architecture
  candidate fit into Validated, Partial, No fit, and Candidate statuses.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/35
tags:
- guideline
- workflows
- reference-architectures
- validation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T09:57:30.857051+00:00'
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
The Reference Architecture Validation Guide provides contributors and working group members with a standardized process to evaluate candidate reference architectures against concrete enterprise use cases [^evt-wg-workflows-and-process-integration-pr-35]. Governed by the [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md), this framework prevents speculative architectures by requiring documented evidence from real-world practitioner deployments [^evt-wg-workflows-and-process-integration-file-cd94574f9d34-a7acfb30].

# Architecture / Specification
### Classification Tiers
Validation evaluations assign one of four structured status labels to a reference architecture against a specific use case [^evt-wg-workflows-and-process-integration-pr-35]:
- **Validated**: The reference architecture completely satisfies the operational, boundary, and capability requirements of the use case without architectural modification.
- **Partial**: The architecture satisfies substantial portions of the job but exhibits minor gaps, unmodeled steps, or auxiliary constraints.
- **No fit**: Fundamental mismatches exist in the authority model, autonomy boundary, or effect reversibility (e.g., applying autonomous loops to irreversible high-impact actions).
- **Candidate**: A promising deployment scenario proposed for review that is still awaiting complete operational evidence or inventory verification.

### Contribution Rules
In accordance with contributor instructions and working group guidelines [^evt-wg-workflows-and-process-integration-file-cd94574f9d34-a7acfb30]:
- Scenarios validate architectures; domain-specific examples must not be mistaken for the generic architecture name.
- Evaluations must rely strictly on supplied empirical evidence rather than hypothetical agent capabilities.
- Validation records are submitted as structured pull requests or issues adhering to standard templates.

# Lifecycle History
- Formulated during RA Workstream Sync #6 and adopted via PR #35 in the Workflows and Process Integration Working Group [^evt-wg-workflows-and-process-integration-pr-35].

[^evt-wg-workflows-and-process-integration-file-cd94574f9d34-a7acfb30]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/AGENTS.md
[^evt-wg-workflows-and-process-integration-pr-35]: https://github.com/aaif/wg-workflows-and-process-integration/pull/35
