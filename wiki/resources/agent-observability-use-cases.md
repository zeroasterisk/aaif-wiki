---
type: resource
title: Agent Observability Use Cases Catalog
description: Catalog defining multi-category agent observability use cases, cross-cutting
  telemetry requirements, and legal compliance retention boundaries.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/68
tags:
- observability
- use-cases
- compliance
- gdpr
- evidence
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:33:38.696754+00:00'
sources:
- id: evt-wg-observability-and-traceability-pr-68
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/68
  author: narko4u
  last_modified: '2026-11-02T06:27:39+00:00'
---

# Overview

The Agent Observability Use Cases Catalog is a structured reference inventory maintained by the [Observability and Traceability WG](../working-groups/observability-and-traceability.md) outlining operational, security, diagnostic, and compliance requirements for instrumented agent systems.[^evt-wg-observability-and-traceability-pr-68] It documents concrete evaluation profiles and storage invariants needed across enterprise and multi-agent deployments.

# Architecture / Specification

### Enterprise Audit and Evidence Retention (E4)

Use case E4 governs authorization tracing, approval chain provenance, and legal evidence retention for high-consequence agent actions.[^evt-wg-observability-and-traceability-pr-68] To reconcile verifiable audit trails with statutory privacy obligations, the specification deprecates unconditional write-once-read-many (WORM) storage semantics in favor of tamper-evident stores with declared retention bases:[^evt-wg-observability-and-traceability-pr-68]

- **Regulatory Conflict Resolution**: Absolute WORM semantics preclude lawful operation under GDPR Article 17(1) (Right to Erasure) and Article 5(1)(e) (Storage Limitation) when approval records contain identifiable natural persons, given that linkable hashes constitute personal data under Recital 26.[^evt-wg-observability-and-traceability-pr-68]
- **Tamper-Evident Storage with Declared Retention**: Record integrity must remain verifiable through cryptographic hash-chaining and external timestamps without requiring personal identifiers to be held indefinitely beyond their lawful basis.[^evt-wg-observability-and-traceability-pr-68]
- **Typed Tombstones**: When personal identifiers or sensitive parameters are removed under policy or data-subject requests, the record must preserve a typed tombstone. This allows downstream verifiers to differentiate between an expired record subjected to policy redaction and an invalid record that omitted mandatory fields at emission.[^evt-wg-observability-and-traceability-pr-68]
- **EU AI Act Alignment**: Reflects retention floors under EU AI Act Article 19(1) for providers and Article 26(6) for deployers, enforcing bounded retention rather than permanent identifier storage.[^evt-wg-observability-and-traceability-pr-68]

# Lifecycle History

- **October 2026**: Replaced unconditional write-once storage clause in use case E4 with tamper-evident retention with typed tombstones to ensure GDPR and EU AI Act compliance.[^evt-wg-observability-and-traceability-pr-68]

# References

- [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md)
- [Evidence Record Specification](../standards/evidence-record-spec.md)
- [Approval Checkpoint Pattern](../patterns/approval-checkpoint.md)

[^evt-wg-observability-and-traceability-pr-68]: https://github.com/aaif/wg-observability-and-traceability/pull/68
