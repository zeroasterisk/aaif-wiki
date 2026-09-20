---
type: deliverable
title: nono Kernel-Enforced Runtime Reference Architecture
description: A reference architecture evaluating the nono kernel-enforced runtime
  realization against observability requirements, including boundary rows for Agent
  -> Gateway/Runtime and Agent -> Human.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/52
tags:
- reference-architecture
- runtime
- observability
- security
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-flash-latest
  at: '2026-09-20T18:02:54.231316+00:00'
sources:
- id: evt-wg-observability-and-traceability-pr-52
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/52
  author: Salkimmich
  last_modified: '2026-09-16T16:22:04+00:00'
---

# Overview
This reference architecture (AAIF-REF-ARCH-NONO) evaluates the observability and traceability aspects of a kernel-enforced runtime realization, specifically nono [^evt-wg-observability-and-traceability-pr-52].
The architecture includes analysis of boundary rows for Agent → Gateway or Runtime and Agent → Human (HITL), detailing observed Security and Provenance values for Agent → Tool interactions [^evt-wg-observability-and-traceability-pr-52].

# Architecture / Specification
The work maps layers across the Observability & Traceability, Identity & Trust, and Security & Privacy working groups, focusing on the Primitives and Protocol Observability focus group within O&T [^evt-wg-observability-and-traceability-pr-52].
A finding stated in the documents is that the nono realization does not currently propagate W3C trace context into the sandbox [^evt-wg-observability-and-traceability-pr-52].

[^evt-wg-observability-and-traceability-pr-52]: https://github.com/aaif/wg-observability-and-traceability/pull/52
