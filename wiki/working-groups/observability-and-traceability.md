---
type: working-group
title: Observability and Traceability Working Group
description: Technical working group standardizing telemetry models, execution trace
  formats, agent trajectory schemas, and cross-boundary harness observability.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/42e2b81f3de6120743bf52ac31de5c63cda920a2/meeting-minutes/2026-11-11.md
tags:
- observability
- traceability
- telemetry
- opentelemetry
- working-group
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:36:12.042602+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-a09ec8b0fa09-bfbbd7a5
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/42e2b81f3de6120743bf52ac31de5c63cda920a2/meeting-minutes/2026-11-11.md
  author: Pavan Sudheendra
  last_modified: '2026-11-12T10:26:18+00:00'
---

# Overview

The Observability and Traceability Working Group establishes vendor-neutral standards, open telemetry formats, and architectural reference models for monitoring and auditing agentic AI systems.[^evt-wg-observability-and-traceability-file-a09ec8b0fa09-bfbbd7a5] Its scope spans turn-by-turn execution traces, distributed context propagation across multi-agent boundaries, payload attestation signatures, and trajectory interchange formats.[^evt-wg-observability-and-traceability-file-a09ec8b0fa09-bfbbd7a5]

# Active Deliverables and Collaborations

The working group drives several core standards and cross-foundation alignment initiatives:[^evt-wg-observability-and-traceability-file-a09ec8b0fa09-bfbbd7a5]

- **Agent Behavior Trace Model**: A standardized schema defining execution context propagation, causal execution tracing, and turn-by-turn agent state transitions, developed in active collaboration with the OpenTelemetry (OTel) GenAI Special Interest Group.[^evt-wg-observability-and-traceability-file-a09ec8b0fa09-bfbbd7a5]
- **ATIF v2 Trajectory Standardization**: Collaboration with Google, Harbor, and industry partners to standardize Agent Trajectory Interchange Format (ATIF v2) semantics, establishing mappings between OpenTelemetry traces and autonomous trajectory datasets.[^evt-wg-observability-and-traceability-file-a09ec8b0fa09-bfbbd7a5]
- **Agentic Observability White Paper**: Foundational practitioner guide distinguishing established distributed tracing practices from emerging agent-specific paradigms, targeted for review across IETF and IRTF working groups.[^evt-wg-observability-and-traceability-file-a09ec8b0fa09-bfbbd7a5]
- **Payload Attestation Signing**: Investigation into non-intrusive signature schemes that validate observation records and execution payloads without breaking trace propagation or modifying OTLP data models.[^evt-wg-observability-and-traceability-file-a09ec8b0fa09-bfbbd7a5]

# Cross-Working Group and Standards Coordination

The group coordinates closely with the [Taxonomy and Landscape Workstream](../working-groups/taxonomy-and-landscape.md) on defining foundational execution primitives such as "turn" and "step", with the emerging Attestation and Evidence working group, and with external standards bodies including the IETF, OpenTelemetry, and Cloud Security Alliance.[^evt-wg-observability-and-traceability-file-a09ec8b0fa09-bfbbd7a5]

[^evt-wg-observability-and-traceability-file-a09ec8b0fa09-bfbbd7a5]: https://github.com/aaif/wg-observability-and-traceability/blob/42e2b81f3de6120743bf52ac31de5c63cda920a2/meeting-minutes/2026-11-11.md
