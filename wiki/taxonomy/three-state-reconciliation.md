---
type: taxonomy
title: Three-State Reconciliation
description: Evaluation model comparing an agent claim against independent observation
  across agreement, contradiction, and absence of evidence.
resource: https://github.com/aaif/ws-taxonomy-landscape/issues/54
tags:
- taxonomy
- evaluation
- reconciliation
- evidence
- observability
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T10:34:34.894779+00:00'
sources:
- id: evt-ws-taxonomy-landscape-issue-54
  resource: https://github.com/aaif/ws-taxonomy-landscape/issues/54
  author: narko4u
  last_modified: '2026-09-20T02:33:08+00:00'
---

# Overview

Three-state reconciliation is an evaluation framework comparing an agent claim against independent observations, resolving into one of three explicit states: agreement, contradiction, or no independent evidence [^evt-ws-taxonomy-landscape-issue-54].

A two-state model (matched vs. mismatched) implicitly collapses instances where no independent observation exists into a silent default. Three-state reconciliation treats the absence of independent evidence as an explicit, first-class state so an auditor or verification system can distinguish between "verified consistent" and "nothing checked it" [^evt-ws-taxonomy-landscape-issue-54].

# Architecture / Specification

The taxonomy term formalizes reconciliation outcomes for evidence and dispute workflows, originating in discussion within the Observability & Traceability Working Group around control-plane telemetry as an evidence source [^evt-ws-taxonomy-landscape-issue-54].

Related taxonomy concepts under elaboration include witness custody categories and verification basis axes, such as `../taxonomy/witness-scope.md` and `../taxonomy/evidence-strength-labels.md` [^evt-ws-taxonomy-landscape-issue-54].

[^evt-ws-taxonomy-landscape-issue-54]: https://github.com/aaif/ws-taxonomy-landscape/issues/54
