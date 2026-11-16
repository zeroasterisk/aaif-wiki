---
type: taxonomy
title: Safety
description: Reliability dimension ensuring an agentic system prevents prohibited,
  harmful, or unauthorized actions under prevailing governance policies.
resource: https://github.com/aaif/ws-taxonomy-landscape/pull/104
tags:
- taxonomy
- accuracy-and-reliability
- safety
- governance
- policy
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:46:12.863485+00:00'
sources:
- id: evt-ws-taxonomy-landscape-pr-104
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/104
  author: jordanauge
  last_modified: '2026-11-16T00:57:13+00:00'
---

# Overview
**Safety** is the dimension of [reliability](../taxonomy/reliability.md) concerning the prevention of prohibited, harmful, or unauthorized actions by an agentic system under the policies in force.[^evt-ws-taxonomy-landscape-pr-104] Standardized by the [Accuracy and Reliability Working Group](../working-groups/accuracy-and-reliability.md), safety focuses on negative constraints and boundary enforcement during autonomous agent execution.[^evt-ws-taxonomy-landscape-pr-104]

# Architecture / Specification
The taxonomy scope note establishes key reporting requirements and domain boundaries for safety:[^evt-ws-taxonomy-landscape-pr-104]

- **Separate Metric Reporting**: Safety evaluation must be reported independently from general correctness or [accuracy](../taxonomy/accuracy.md) aggregates, preventing high task success rates from masking critical policy violations.[^evt-ws-taxonomy-landscape-pr-104]
- **Policy Grounding**: Safety is evaluated strictly against active organizational, operational, and regulatory policies governing permitted actions and tools.[^evt-ws-taxonomy-landscape-pr-104]
- **Scope Exclusion**: Explicitly excludes the distributed-systems definition of safety (such as invariant state preservation or avoiding deadlock/race conditions), applying exclusively to harm prevention, authorization bounds, and policy compliance.[^evt-ws-taxonomy-landscape-pr-104]

# Lifecycle History
- **Deliverable 1 Addition**: Defined by the Accuracy and Reliability Working Group via PR #104 in `ws-taxonomy-landscape`, voted KEEP in the canonical taxonomy workstream review.[^evt-ws-taxonomy-landscape-pr-104]

[^evt-ws-taxonomy-landscape-pr-104]: https://github.com/aaif/ws-taxonomy-landscape/pull/104
