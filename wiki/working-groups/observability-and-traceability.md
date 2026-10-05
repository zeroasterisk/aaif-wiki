---
type: working-group
title: Observability and Traceability Working Group
description: AAIF working group establishing multi-layer telemetry standards, cross-boundary
  context propagation, prior-work landscape surveys, and agent observability use cases.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/working-documents/PRIOR-WORK.md
tags:
- aaif
- governance
- working-group
- observability
- telemetry
- tracing
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:47:10.524082+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/working-documents/PRIOR-WORK.md
  author: Pavan Sudheendra
  last_modified: '2026-09-26T04:52:07+01:00'
- id: evt-wg-observability-and-traceability-file-7ac80cf9ff9c-21a525e3
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/working-documents/USE-CASES.md
  author: Pavan Sudheendra
  last_modified: '2026-09-26T04:54:08+01:00'
- id: evt-wg-observability-and-traceability-pr-53
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/53
  author: narko4u
  last_modified: '2026-09-26T09:19:20+00:00'
- id: evt-wg-security-and-privacy-pr-24
  resource: https://github.com/aaif/wg-security-and-privacy/pull/24
  author: awfrazer
  last_modified: '2026-09-25T17:05:22+00:00'
---

# Overview

The Observability and Traceability Working Group is the [Agentic AI Foundation](../governance/technical-committee.md) body chartered to survey, coordinate, and standardize agent observability and tracing architectures [^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853]. Chaired by Pavan Sudheendra, the working group standardizes telemetry conventions across agent frameworks, multi-agent protocol boundaries, and infrastructure layers [^evt-wg-security-and-privacy-pr-24] [^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853].

# Core Specifications and Living Documents

- **Prior Work Landscape Survey**: Comprehensive survey tracking telemetry initiatives including OpenTelemetry GenAI Semantic Conventions, [Agent Trace](../reference-architectures/agent-trace.md), OWASP Agent Observability Standard (AOS), AGNTCY Observe, OCSF v1.9 AI Operations, and [A2A](../projects/a2a.md) traceability extensions [^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853].
- **Agent Observability Use Cases**: Standardized catalog spanning root-cause debugging, cost optimization, AI code attribution, multi-agent protocol tracing, cross-surface identity resolution (I1), and tamper-evident audit evidence (E4) [^evt-wg-observability-and-traceability-file-7ac80cf9ff9c-21a525e3] [^evt-wg-observability-and-traceability-pr-53].
- **Cross-Boundary Observability Framework**: Architecture enabling context propagation across protocol boundaries such as MCP, A2A, and agent gateway proxies [^evt-wg-security-and-privacy-pr-24] [^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853].

# Telemetry Requirements

The working group defines cross-cutting telemetry requirements requiring clear differentiation between agent self-reporting and trusted vantage points (host OS, eBPF, network, sandbox), verifiable sampling and completeness declarations, schema versioning, and causal correlation across asynchronous sessions [^evt-wg-observability-and-traceability-file-7ac80cf9ff9c-21a525e3].

[^evt-wg-observability-and-traceability-file-7ac80cf9ff9c-21a525e3]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/working-documents/USE-CASES.md
[^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/working-documents/PRIOR-WORK.md
[^evt-wg-observability-and-traceability-pr-53]: https://github.com/aaif/wg-observability-and-traceability/pull/53
[^evt-wg-security-and-privacy-pr-24]: https://github.com/aaif/wg-security-and-privacy/pull/24
