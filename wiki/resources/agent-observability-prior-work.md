---
type: resource
title: Prior Work in Agent Observability
description: Comparative landscape survey analyzing open specifications, industry
  standards, protocols, and platforms across agent observability and telemetry.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/working-documents/PRIOR-WORK.md
tags:
- observability
- telemetry
- prior-work
- landscape
- opentelemetry
- standards
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:08:29.691110+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/working-documents/PRIOR-WORK.md
  author: Pavan Sudheendra
  last_modified: '2026-09-26T04:52:07+01:00'
---

# Overview

Prior Work in Agent Observability is a living landscape survey maintained by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md)[^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853]. It surveys existing specifications, data formats, open-source platforms, and academic research relevant to agentic telemetry, providing a common foundation for AAIF standards like the [Agent Behavior Trace Model](../standards/agent-behavior-trace-model.md)[^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853].

# Architecture / Specification

### Landscape Refresh Highlights (June–August 2026)

The landscape reflects significant specification maturation and protocol consolidation across industry bodies[^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853]:

- **OpenTelemetry GenAI Standards Repository**: OpenTelemetry established a dedicated repository (`open-telemetry/semantic-conventions-genai`) for GenAI semantic conventions, standardizing explicit spans for `create-agent`, `invoke-agent`, `invoke-workflow`, `execute-tool`, and `plan`[^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853].
- **Open Cybersecurity Schema Framework (OCSF)**: OCSF Schema 1.9 introduced an agent-specific profile defining AI Operation, AI Agent, Delegation, and Record Integrity classes, enabling normalized security event logging for agent actions and delegated authority[^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853].
- **OWASP Agent Observability Standard (AOS)**: AOS separated its specification surface into distinct Instrument, Trace, and Inspect specifications, establishing mappings for OpenTelemetry, OCSF, and AgBOM software supply-chain standards (CycloneDX/SPDX/SWID)[^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853].
- **AGNTCY Observe**: The AGNTCY Observe SDK (`v1.0.43`) provides protocol-level telemetry interception across A2A, SLIM, and MCP with distributed trace recomposition over multi-agent boundaries[^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853].
- **Agent-to-Agent (A2A) Protocol**: Following its accession to AAIF in August 2026, A2A v1.0 standardizes signed agent cards, cross-vendor task delegation, and nested step trace extensions[^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853].
- **Environment-Derived Instrumentation**: OTel eBPF instrumentation (including OBI) provides kernel-level, unforgeable network and execution signals that complement framework-emitted telemetry[^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853].
- **Focused Attribution Formats**: Specialized formats like Cursor Agent Trace (v0.1.0) remain focused on narrow AI code attribution within developer tools[^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853].

### Comparative Matrix

| Initiative | Scope | Maturity | Format / License | Primary Focus |
|---|---|---|---|---|
| **OTel GenAI SemConv** | LLM, agent, workflow, tool, MCP spans/events | Active Development | Open (Apache 2.0) | Broad multi-vendor runtime telemetry |
| **OWASP AOS** | Security, auditing, AgBOM mapping | Draft / Active | Open | Compliance, guardrail violation auditing |
| **OCSF (v1.9)** | AI agent identity, delegation, integrity | Production Schema | Open | Security incident and audit evidence |
| **AGNTCY Observe** | Multi-agent context propagation | SDK v1.0.43 | Open (Apache 2.0) | Cross-agent protocol boundary reconstruction |
| **Agent Trace (Cursor)** | Source code attribution | RFC v0.1.0 | Open (CC BY 4.0) | Line-level IDE code generation provenance |
| **Monocle (LF AI & Data)**| GenAI framework auto-instrumentation | v0.8.4 | Open (Apache 2.0) | Non-intrusive trace wrapper generation |

# Lifecycle History

- **2026-03-15**: Initial landscape survey drafted by the AAIF Observability Working Group[^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853].
- **2026-08-13**: Comprehensive refresh capturing dedicated OTel GenAI repository separation, OCSF 1.9 AI Agent profile, A2A AAIF accession, and AOS multi-part specifications[^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853].

# References

- [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md)
- [Agent Behavior Trace Model](../standards/agent-behavior-trace-model.md)
- [Agent-MCP Server Boundary](../resources/agent-mcp-server-boundary.md)
- [Agntcy](../resources/agntcy.md)

[^evt-wg-observability-and-traceability-file-dcf5c1ecc194-085a2853]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/working-documents/PRIOR-WORK.md
