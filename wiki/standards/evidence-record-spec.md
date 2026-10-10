---
type: standard
title: Evidence Record Specification
description: Testable JSON Schema and interchange data model encoding agent observation
  sources, verification vantages, E0-E4 integrity grades, and claim reconciliation.
resource: https://github.com/aaif/wg-observability-and-traceability/issues/37
tags:
- observability
- evidence
- traceability
- validation
- integrity
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:23:01.422207+00:00'
sources:
- id: evt-wg-observability-and-traceability-issue-37
  resource: https://github.com/aaif/wg-observability-and-traceability/issues/37
  author: narko4u
  last_modified: '2026-10-09T09:17:37+00:00'
---

# Overview

The Evidence Record Specification is a testable data model and interchange format addressing the tamper-evident agent evidence gap (identified as use case E4 within the [Observability & Traceability Working Group](../working-groups/observability-and-traceability.md)) [^evt-wg-observability-and-traceability-issue-37]. Rather than defining a single vendor-dependent mechanism, the specification establishes an implementation-neutral schema for asserting, grading, and validating claims about agent operations [^evt-wg-observability-and-traceability-issue-37].

# Architecture / Specification

The specification structures agent evidence records around four explicit dimensions [^evt-wg-observability-and-traceability-issue-37]:

- **Observation**: Records the observation source (ranging from agent self-reporting to external authorities) and relationship (direct, corroborating, contradictory, or derived).
- **Verification**: Formulates verification basis across vantage (substrate versus artifact) and capture method (intercepted versus reconstructed).
- **Grade Ladder**: Defines an integrity ladder spanning E0 to E4 (Declared, Observed, Enforced, Corroborated, Anchored) coupled with strict grade-to-integrity floor requirements.
- **Claims and Reconciliation**: Captures emission-conformant and operationally-conformant claims, resolving discrepancies through a three-state reconciliation model (agreement, contradiction, or no independent evidence).

Validation rules require strict closed-vocabulary checking, semantic derivation consistency, and mandatory provenance trails for derived records [^evt-wg-observability-and-traceability-issue-37].

[^evt-wg-observability-and-traceability-issue-37]: https://github.com/aaif/wg-observability-and-traceability/issues/37
