---
type: taxonomy
title: Three-State Reconciliation
description: Evaluation model comparing an agent claim against independent observation
  across agreement, contradiction, and explicit absence of evidence.
resource: https://github.com/aaif/ws-taxonomy-landscape/issues/54
tags:
- taxonomy
- evaluation
- evidence
- observability
- attestation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:15:01.472995+00:00'
sources:
- id: evt-ws-taxonomy-landscape-issue-54
  resource: https://github.com/aaif/ws-taxonomy-landscape/issues/54
  author: narko4u
  last_modified: '2026-09-20T02:33:08+00:00'
---

# Overview
Three-state reconciliation is an evaluation model that compares an agent claim against an independent observation, resolving into one of three explicit states: agreement, contradiction, or no independent evidence.[^evt-ws-taxonomy-landscape-issue-54] By treating the absence of independent evidence as an explicit, first-class outcome rather than a silent default or failure, the model enables auditors to distinguish between verified consistency and unobserved claims.[^evt-ws-taxonomy-landscape-issue-54]

# Architecture / Specification
Traditional two-state reconciliation models (such as matched or mismatched) collapse unverified claims into silent defaults, creating significant blind spots for dispute resolution and compliance audits.[^evt-ws-taxonomy-landscape-issue-54] Three-state reconciliation resolves observations across three discrete outcomes:
- **Agreement**: An independent boundary observation corroborates the self-reported agent claim.
- **Contradiction**: An independent observation directly conflicts with or disproves the agent claim.
- **No Independent Evidence**: No corroborating or conflicting telemetry exists at the boundary.

The model originated in the Observability and Traceability Working Group to reconcile agent self-reported telemetry against independent control-plane observations, interacting directly with concepts like `../taxonomy/witness-scope.md` and evidence strength categorization.[^evt-ws-taxonomy-landscape-issue-54]

# Lifecycle History
Proposed in the Taxonomy and Landscape Workstream issue #54 following initial framing in Observability and Traceability WG issue #36.[^evt-ws-taxonomy-landscape-issue-54]

[^evt-ws-taxonomy-landscape-issue-54]: https://github.com/aaif/ws-taxonomy-landscape/issues/54
