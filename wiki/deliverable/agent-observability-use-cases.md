---
type: deliverable
title: Agent Observability Use Cases Catalog
description: A catalog of practitioner use cases and cross-cutting telemetry requirements
  across debugging, cost, safety, compliance, and tamper-evident auditability.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/30
tags:
- observability
- telemetry
- compliance
- auditability
- use-cases
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:56:17.597216+00:00'
sources:
- id: evt-wg-observability-and-traceability-pr-30
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/30
  author: narko4u
  last_modified: '2026-08-23T09:50:09+00:00'
---

# Overview

The Agent Observability Use Cases Catalog outlines real-world operational and governance scenarios that shape telemetry protocols and tracing models for agentic AI systems [^evt-wg-observability-and-traceability-pr-30]. The document catalogs cross-cutting telemetry requirements spanning developer debugging, cost governance, safety enforcement, and legal compliance.

# Architecture / Specification

### Safety and Compliance Use Cases

In addition to operational and performance debugging, the catalog classifies compliance and safety requirements into standardized clusters:

- **E1–E3 Compliance Cluster**: Telemetry tracks safety guardrails, policy adherence, and cross-system interaction boundaries.
- **Use Case E4 (Tamper-Evident Evidence for Audit and Dispute Resolution)**: Defines technical requirements for regulated entities to definitively prove an agent's runtime actions to auditors, regulators, or courts [^evt-wg-observability-and-traceability-pr-30].

#### Requirements for Tamper-Evident Evidence (E4)
- **Merkle-Chained Records**: Event records must be cryptographically signed and chained into Merkle structures to prevent retroactive modification [^evt-wg-observability-and-traceability-pr-30].
- **Write-Once-Read-Many (WORM) Storage & RFC 3161 Timestamps**: Enforces immutable event persistence with certified external time stamping [^evt-wg-observability-and-traceability-pr-30].
- **Approval Chain Tracking**: Captures explicit links between human approval decisions and subsequent agent actions [^evt-wg-observability-and-traceability-pr-30].
- **Declared-vs-Observed Verification**: Correlates declared plans against actual runtime tool and kernel interactions [^evt-wg-observability-and-traceability-pr-30].
- **Evidence-Grade Ladder**: References frameworks such as WitnessOS (spanning E0 Declared to E4 Anchored) and EU AI Act compliance grading models to assess evidentiary strength [^evt-wg-observability-and-traceability-pr-30].

# Lifecycle History

- **PR #30**: Introduced Use Case E4 alongside priority matrix contributions emphasizing evidence-grade trace integrity [^evt-wg-observability-and-traceability-pr-30].

[^evt-wg-observability-and-traceability-pr-30]: https://github.com/aaif/wg-observability-and-traceability/pull/30
