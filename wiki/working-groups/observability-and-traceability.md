---
type: working-group
title: Observability and Traceability Working Group
description: AAIF technical working group establishing vendor-neutral agent telemetry
  standards, cross-boundary trace context, and execution verification architectures.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/f10288d27f769a4ff90184490100a0f7fdbc4d4e/meeting-minutes/2026-10-14.md
tags:
- working-group
- observability
- telemetry
- tracing
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T11:06:49.409332+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-7c02d5e673bb-b7cb2b21
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/f10288d27f769a4ff90184490100a0f7fdbc4d4e/meeting-minutes/2026-10-14.md
  author: Pavan Sudheendra
  last_modified: '2026-10-19T15:06:04+01:00'
- id: evt-wg-observability-and-traceability-issue-64
  resource: https://github.com/aaif/wg-observability-and-traceability/issues/64
  author: jmaionchi
  last_modified: '2026-10-18T18:27:15+00:00'
- id: evt-wg-observability-and-traceability-issue-65
  resource: https://github.com/aaif/wg-observability-and-traceability/issues/65
  author: jmaionchi
  last_modified: '2026-10-18T18:41:21+00:00'
---

# Overview
The Observability and Traceability Working Group establishes vendor-neutral telemetry standards, distributed tracing conventions, and execution audit architectures for autonomous agent systems [^evt-wg-observability-and-traceability-file-7c02d5e673bb-b7cb2b21]. The group focuses on capturing causal execution chains across LLM primitives, tool invocations, and multi-agent protocols [^evt-wg-observability-and-traceability-file-7c02d5e673bb-b7cb2b21].

# Initiatives and Active Workstreams
The working group coordinates several specifications and industry alignments:
- **Telemetry Seams and OTel/OCSF Mapping**: Collaborating with the OpenTelemetry (OTel) GenAI SIG and the Open Cybersecurity Schema Framework (OCSF) to define standard extension points and nine identified integration seams for coding agents, agent SDKs, and AI gateways [^evt-wg-observability-and-traceability-file-7c02d5e673bb-b7cb2b21].
- **Agentic Resource Discovery (ARD) Observability**: Defining telemetry requirements and an observability specification section for the decentralized [Agentic Resource Discovery](../standards/agentic-resource-discovery.md) standard [^evt-wg-observability-and-traceability-file-7c02d5e673bb-b7cb2b21].
- **Context Engines and Verifiable Replay**: Assessing cryptographic audit structures, provable execution replay, and zero-knowledge boundary protocols such as CIGAR (Context Intelligence Graph Agentic Runtime) and Agent Action Capsule (AAC) specifications [^evt-wg-observability-and-traceability-file-7c02d5e673bb-b7cb2b21].
- **Cross-Boundary Security Coordination**: Partnering with the [Security and Privacy Working Group](../working-groups/security-and-privacy.md) to integrate attestation evidence and policy enforcement boundaries into trace contexts [^evt-wg-observability-and-traceability-file-7c02d5e673bb-b7cb2b21].
- **Taxonomy Definitions**: Reviewing operational telemetry classifications, such as [Operationally Conformant](../taxonomy/operationally-conformant.md) and universal reasoning terms, in coordination with the [Taxonomy and Landscape Working Group](../working-groups/taxonomy-and-landscape.md) [^evt-wg-observability-and-traceability-issue-64], [^evt-wg-observability-and-traceability-issue-65].

[^evt-wg-observability-and-traceability-file-7c02d5e673bb-b7cb2b21]: https://github.com/aaif/wg-observability-and-traceability/blob/f10288d27f769a4ff90184490100a0f7fdbc4d4e/meeting-minutes/2026-10-14.md
[^evt-wg-observability-and-traceability-issue-64]: https://github.com/aaif/wg-observability-and-traceability/issues/64
[^evt-wg-observability-and-traceability-issue-65]: https://github.com/aaif/wg-observability-and-traceability/issues/65
