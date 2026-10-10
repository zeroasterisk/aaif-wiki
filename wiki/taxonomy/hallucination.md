---
type: taxonomy
title: Hallucination
description: Universal taxonomy term defining a facially plausible detail or assertion
  in AI output that lacks evidential support or ground-truth basis.
resource: https://github.com/aaif/ws-taxonomy-landscape/pull/85
tags:
- taxonomy
- reliability
- evaluation
- safety
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:23:19.617877+00:00'
sources:
- id: evt-ws-taxonomy-landscape-pr-85
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/85
  author: julianna-ciq
  last_modified: '2026-10-09T13:00:42+00:00'
---

# Overview

In the Agentic AI Foundation vocabulary, Hallucination is defined as a facially plausible detail or position in artificial intelligence output that lacks any available support or basis in provided context or ground-truth data [^evt-ws-taxonomy-landscape-pr-85]. In agentic execution environments, hallucinations present critical failure modes when unverified outputs trigger unauthorized tool calls or compromise decision boundaries.

# Vocabulary and Scope

Addressing hallucination risks within autonomous agent workflows requires deterministic guardrails and verification architectures. Architectural mitigations commonly include [deterministic acceptance gates](../patterns/deterministic-acceptance-gate.md) and structured evidence capture governed by the [Evidence Record Spec](../standards/evidence-record-spec.md) to validate that generated positions and tool parameters are empirically grounded before state mutations occur [^evt-ws-taxonomy-landscape-pr-85].

[^evt-ws-taxonomy-landscape-pr-85]: https://github.com/aaif/ws-taxonomy-landscape/pull/85
