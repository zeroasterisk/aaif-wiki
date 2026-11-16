---
type: taxonomy
title: Robustness
description: Reliability dimension measuring an agentic system's stability under meaning-preserving
  input rephrasings, shifting environmental conditions, and underlying faults.
resource: https://github.com/aaif/ws-taxonomy-landscape/pull/103
tags:
- taxonomy
- accuracy-and-reliability
- reliability
- fault-tolerance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:46:12.863485+00:00'
sources:
- id: evt-ws-taxonomy-landscape-pr-103
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/103
  author: jordanauge
  last_modified: '2026-11-16T00:57:07+00:00'
---

# Overview
**Robustness** is the dimension of [reliability](../taxonomy/reliability.md) evaluating an agentic system's capacity to maintain correct operation in the presence of meaning-preserving input rephrasings, shifting conditions, and operational faults.[^evt-ws-taxonomy-landscape-pr-103] Established by the [Accuracy and Reliability Working Group](../working-groups/accuracy-and-reliability.md), robustness categorizes how an agent accommodates operational variance without catastrophic degradation or task failure.[^evt-ws-taxonomy-landscape-pr-103]

# Architecture / Specification
The AAIF taxonomy structures robustness across three operational sub-types and delineates strict conceptual boundaries:[^evt-ws-taxonomy-landscape-pr-103]

- **Prompt Robustness**: Resilience against syntactic rephrasing, semantic paraphrasing, irrelevant context, or formatting variance that preserves the underlying intent.[^evt-ws-taxonomy-landscape-pr-103]
- **Fault Robustness**: Ability to withstand tool execution exceptions, transient network failures, and degraded model service availability during execution.[^evt-ws-taxonomy-landscape-pr-103]
- **Environment Robustness**: Stability across external system changes, variable API latency, and shifting data schemas.[^evt-ws-taxonomy-landscape-pr-103]

### Conceptual Boundaries
Robustness is distinguished from adjacent reliability concepts:[^evt-ws-taxonomy-landscape-pr-103]
- Distinct from [recoverability](../taxonomy/recoverability.md), which focuses on detecting failures and returning the system to an acceptable state once a disruption has materialized.[^evt-ws-taxonomy-landscape-pr-103]
- Separated from active threat mitigation under the [Security and Privacy Working Group](../working-groups/security-and-privacy.md), reserving robustness specifically for non-adversarial perturbations and environmental volatility.[^evt-ws-taxonomy-landscape-pr-103]

# Lifecycle History
- **Deliverable 1 Addition**: Defined by the Accuracy and Reliability Working Group via PR #103 in `ws-taxonomy-landscape`, voted KEEP in the canonical taxonomy workstream review.[^evt-ws-taxonomy-landscape-pr-103]

[^evt-ws-taxonomy-landscape-pr-103]: https://github.com/aaif/ws-taxonomy-landscape/pull/103
