---
type: taxonomy
title: Three-State Reconciliation
description: Taxonomy classification designating the comparison of an agent claim
  against independent observation into agreement, contradiction, or absent evidence.
resource: https://github.com/aaif/ws-taxonomy-landscape/issues/54
tags:
- taxonomy
- observability
- verification
- audit
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:28:37.295086+00:00'
sources:
- id: evt-ws-taxonomy-landscape-issue-54
  resource: https://github.com/aaif/ws-taxonomy-landscape/issues/54
  author: narko4u
  last_modified: '2026-09-20T02:33:08+00:00'
---

# Overview
`Three-state reconciliation` is a taxonomy term defining an evidence evaluation model where an agent claim is compared against independent observations and classified into one of three distinct states: agreement, contradiction, or no independent evidence[^evt-ws-taxonomy-landscape-issue-54].

The framework prevents silent defaults by elevating missing independent telemetry to an explicit evaluative state rather than treating it as verification failure or implicit confirmation[^evt-ws-taxonomy-landscape-issue-54].

# Architecture / Specification
Formulated within the Observability & Traceability Working Group in discussion around control-plane telemetry as an evidence source[^evt-ws-taxonomy-landscape-issue-54], three-state reconciliation prevents conflating checked claims with unchecked ones:

1. **Agreement**: The independent observation directly corroborates the agent's asserted action or state.
2. **Contradiction**: Independent boundary observations refute or diverge from the agent's asserted claim.
3. **No Independent Evidence**: No external observation exists to assess the claim, exposing an audit visibility gap rather than asserting fault.

This pattern operates in conjunction with [witness-scope](./witness-scope.md) evaluations and verification-basis frameworks[^evt-ws-taxonomy-landscape-issue-54].

# Lifecycle History
Proposed in `aaif/ws-taxonomy-landscape` issue #54 following initial framing in Observability & Traceability Working Group issue #36[^evt-ws-taxonomy-landscape-issue-54].

[^evt-ws-taxonomy-landscape-issue-54]: https://github.com/aaif/ws-taxonomy-landscape/issues/54
