---
type: taxonomy
title: Recoverability
description: Operational ability of an agentic system to detect failures, contain
  impact, and return to an acceptable state within bounded cost.
resource: https://github.com/aaif/ws-taxonomy-landscape/pull/106
tags:
- taxonomy
- reliability
- fault-tolerance
- failure-recovery
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:44:14.647197+00:00'
sources:
- id: evt-ws-taxonomy-landscape-pr-106
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/106
  author: jordanauge
  last_modified: '2026-11-10T10:56:34+00:00'
---

# Overview
Recoverability defines the operational ability of an agentic system to detect execution failures, contain their blast radius, and restore system state to an acceptable condition within bounded computational and financial costs [^evt-ws-taxonomy-landscape-pr-106]. Introduced as part of the [Accuracy and Reliability Working Group](../working-groups/accuracy-and-reliability.md) Deliverable 1 canonical glossary, the term formalizes recovery criteria for autonomous workflows [^evt-ws-taxonomy-landscape-pr-106].

# Architecture / Specification
The taxonomy definition establishes key boundaries distinguishing recoverability from adjacent operational concepts [^evt-ws-taxonomy-landscape-pr-106]:
- **Failure Detection and Containment**: Systems must actively identify anomalies or broken execution invariants and prevent unconstrained failure propagation.
- **Acceptable State vs. Reversibility**: Recoverability focuses on reaching a safe, well-defined acceptable state rather than requiring strict reversibility or total transaction rollback.
- **Cost Bounds**: State restoration must execute within declared resource and financial budget limits to prevent runaway recovery loops.

# References
- Taxonomy workstream PR #106 [^evt-ws-taxonomy-landscape-pr-106]

[^evt-ws-taxonomy-landscape-pr-106]: https://github.com/aaif/ws-taxonomy-landscape/pull/106
