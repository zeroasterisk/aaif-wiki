---
type: architecture
title: Evidence Record Specification
description: Testable JSON Schema and data model encoding observation sources, verification
  vantages, integrity grades, and jurisdiction requirements.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/56
tags:
- telemetry
- observability
- evidence
- audit
- compliance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:48:39.983040+00:00'
sources:
- id: evt-wg-observability-and-traceability-pr-56
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/56
  author: narko4u
  last_modified: '2026-09-28T11:26:29+00:00'
---

# Overview

The Evidence Record Specification defines an interoperable telemetry and verifiable audit schema capturing execution evidence, agent-generated actions, and causal proof chains across agentic systems [^evt-wg-observability-and-traceability-pr-56]. Curated under [../working-groups/observability-and-traceability.md](../working-groups/observability-and-traceability.md), it establishes unambiguous structures for integrity verification, non-repudiation, and cross-boundary evidentiary exchange [^evt-wg-observability-and-traceability-pr-56].

# Architecture / Specification

The specification standardizes structured verification layers and telemetry invariants [^evt-wg-observability-and-traceability-pr-56]:
- **Evidence-Grade Ladder**: Categorizes record integrity through explicit evidence grades (such as Grade E1 through Grade E4) to avoid naming collisions with specific functional use-case identifiers [^evt-wg-observability-and-traceability-pr-56].
- **Jurisdiction and Legal Weight Separation**: Enforces a strict separation between a record's technical integrity mechanism (such as RFC 3161 cryptographic timestamping) and its legal weight [^evt-wg-observability-and-traceability-pr-56]. Where records satisfy regulatory retention or evidentiary duties (e.g., EU AI Act provider recording obligations under Article 12, or retention under Articles 19 and 26(6)), the schema mandates explicit declaration of the governing jurisdiction and legal role of the record holder rather than hardcoding a single legal system into schema enumerations [^evt-wg-observability-and-traceability-pr-56].
- **Vantage Point & Identity Attestation**: Bridges cryptographic attestation with verifiable identities (such as [../working-groups/identity-and-trust.md](../working-groups/identity-and-trust.md)) and isolated runtimes (see [../patterns/attested-isolated-runtime.md](../patterns/attested-isolated-runtime.md)).

# Lifecycle History

In working group drafts, qualifying revisions were made to clearly separate the lettered evidence grades from document use-case identifiers and to disclaim standalone legal claims from technical RFC 3161 timestamps [^evt-wg-observability-and-traceability-pr-56].

[^evt-wg-observability-and-traceability-pr-56]: https://github.com/aaif/wg-observability-and-traceability/pull/56
