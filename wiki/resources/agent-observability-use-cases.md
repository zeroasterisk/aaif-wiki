---
type: resource
title: Agent Observability Use Cases Catalog
description: Structured catalog detailing operational agent observability use cases,
  cross-cutting telemetry requirements, and regulatory audit criteria.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/68
tags:
- observability
- telemetry
- use-cases
- traceability
- compliance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:32:44.481487+00:00'
sources:
- id: evt-wg-observability-and-traceability-pr-68
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/68
  author: narko4u
  last_modified: '2026-11-02T06:27:39+00:00'
---

# Overview
The Agent Observability Use Cases Catalog documents structural, operational, and regulatory observability scenarios across autonomous agents, multi-agent frameworks, and external tools.[^evt-wg-observability-and-traceability-pr-68] Developed by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), the catalog establishes standardized telemetry requirements across runtime environments.

# Architecture / Specification
Use cases within the catalog define granular functional requirements across evaluation, debugging, auditability, and compliance:

- **E4 Compliance and Auditability Requirement**: Requires tamper-evident storage with a declared retention basis rather than immutable write-once-read-many (WORM) storage.[^evt-wg-observability-and-traceability-pr-68] Record integrity must remain cryptographically verifiable through hash chaining and external timestamping without requiring personal identifiers to be preserved beyond the lifespan permitted under GDPR (e.g., Art. 17 right to erasure, Art. 5(1)(e) storage limitation) and EU AI Act retention mandates (Art. 19(1) for providers and Art. 26(6) for deployers).[^evt-wg-observability-and-traceability-pr-68]
- **Typed Tombstones**: When personal identifiers or authorization records are excised under policy or data-subject erasure requests, the evidence record must retain a typed tombstone.[^evt-wg-observability-and-traceability-pr-68] This mechanism permits verifiers to distinguish legitimately expired attributes from unpopulated or tampered fields.[^evt-wg-observability-and-traceability-pr-68]

# Lifecycle History
In October 2026, the working group updated use case E4 via PR #68 to eliminate strict write-once storage constraints in favor of declared retention periods and typed tombstone markers to reconcile cryptographic auditability with European data protection regulations.[^evt-wg-observability-and-traceability-pr-68]

[^evt-wg-observability-and-traceability-pr-68]: https://github.com/aaif/wg-observability-and-traceability/pull/68
