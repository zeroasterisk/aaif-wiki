---
type: workstream
title: Critical Use Cases Workstream
description: A workstream within the Workflows & Process Integration Working Group
  cataloging and classifying production agentic workflows against verified production
  deployments.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/46
tags:
- workflows
- use-cases
- classification
- workstream
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T18:01:04.820609+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-pr-46
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/46
  author: jodeev
  last_modified: '2026-09-11T17:14:12+00:00'
---

# Overview
The Critical Use Cases Workstream is an initiative within the [Workflows and Process Integration Working Group](../workflows-and-process-integration.md) tasked with identifying and cataloging reusable workflow patterns from real-world, production-deployed agentic applications[^evt-wg-workflows-and-process-integration-pr-46]. Rather than serving as a subjective prioritization body, the workstream operates as an empirical classification and sourcing exercise[^evt-wg-workflows-and-process-integration-pr-46].

# Architecture / Specification
The workstream maintains two central artifacts[^evt-wg-workflows-and-process-integration-pr-46]:
- **Classification Schema (`schema-agentic-use-cases.md`)**: A structured taxonomy defining structural execution dimensions, autonomy levels, and coordination patterns (see [Agentic Use Cases Classification Schema](../../deliverable/agentic-use-cases-classification-schema.md))[^evt-wg-workflows-and-process-integration-pr-46].
- **Use Case Inventory (`use-case-inventory.md`)**: A comprehensive table mapping observed production workflows against schema dimensions[^evt-wg-workflows-and-process-integration-pr-46].

### Evidentiary Standard
The workstream mandates strict citation criteria for inventory rows[^evt-wg-workflows-and-process-integration-pr-46]:
- Every Notes entry must cite primary vendor product documentation, engineering blogs, or deployment announcements that confirm actual production usage rather than hypothetical capability[^evt-wg-workflows-and-process-integration-pr-46].
- Requires at least one verified primary citation per use case, with three target citations per row[^evt-wg-workflows-and-process-integration-pr-46].
- Dimensions lacking verified structural evidence must remain designated as `Unspecified: insufficient source detail`[^evt-wg-workflows-and-process-integration-pr-46].

# Lifecycle History
- Workstream structure, evidentiary criteria, and inventory documentation proposed via PR#46[^evt-wg-workflows-and-process-integration-pr-46].

[^evt-wg-workflows-and-process-integration-pr-46]: https://github.com/aaif/wg-workflows-and-process-integration/pull/46
