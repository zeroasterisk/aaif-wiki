---
type: taxonomy
title: Three-State Reconciliation
description: Evaluation model comparing an agent claim against independent observation
  resolved into agreement, contradiction, or no independent evidence.
resource: https://github.com/aaif/ws-taxonomy-landscape/issues/54
tags:
- taxonomy
- evaluation
- observability
- attestation
- audit
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:02:36.187366+00:00'
sources:
- id: evt-ws-taxonomy-landscape-issue-54
  resource: https://github.com/aaif/ws-taxonomy-landscape/issues/54
  author: narko4u
  last_modified: '2026-09-20T02:33:08+00:00'
---

# Overview
Three-state reconciliation is an evaluation model that compares an agent claim against an independent boundary observation and resolves the outcome into one of three explicit states: agreement, contradiction, or no independent evidence [^evt-ws-taxonomy-landscape-issue-54]. By designating the absence of independent evidence as an explicit third state rather than a silent failure or default pass, the model ensures that auditors can distinguish between verified consistency and unmonitored execution [^evt-ws-taxonomy-landscape-issue-54].

# Architecture / Specification
In contrast to binary reconciliation systems that collapse unobserved claims into unverified defaults, three-state reconciliation mandates explicit tri-state resolution [^evt-ws-taxonomy-landscape-issue-54]:
1. **Agreement**: The independent observation confirms the agent's asserted claim or execution outcome.
2. **Contradiction**: An independent observation exists and directly refutes or diverges from the agent claim.
3. **No Independent Evidence**: No corroborating telemetry, witness record, or boundary observation was captured for the claim [^evt-ws-taxonomy-landscape-issue-54].

This tri-state taxonomy originated in discussions around control-plane telemetry within the Observability & Traceability Working Group, where separating unchecked assertions from checked assertions was identified as a critical requirement for dispute resolution and compliance auditing [^evt-ws-taxonomy-landscape-issue-54].

# Lifecycle History
Proposed in Issue #54 of `aaif/ws-taxonomy-landscape` as part of the deferred category definitions pass, pending paired-contrast and related-term alignment with witness scope and verification-basis attributes [^evt-ws-taxonomy-landscape-issue-54].

# References
- Observability and Traceability WG: [../working-groups/observability-and-traceability.md](../working-groups/observability-and-traceability.md)
- Attestation & Evidence WG: [../working-groups/attestation-and-evidence.md](../working-groups/attestation-and-evidence.md)
- Action Record Taxonomy: [action-record.md](action-record.md)

[^evt-ws-taxonomy-landscape-issue-54]: AAIF Taxonomy & Landscape Workstream Issue #54, 'Define: three-state reconciliation', https://github.com/aaif/ws-taxonomy-landscape/issues/54
