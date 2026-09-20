---
type: taxonomy-term
title: Human in the Loop
description: An execution pattern requiring an explicit human approval or decision
  checkpoint before an agent action can proceed.
resource: https://github.com/aaif/ws-taxonomy-landscape/pull/40
tags:
- taxonomy
- governance
- interaction-models
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T18:01:40.280027+00:00'
sources:
- id: evt-ws-taxonomy-landscape-pr-40
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/40
  author: julianna-ciq
  last_modified: '2026-09-15T03:36:58+00:00'
---

# Overview
Human in the loop (HITL) is an interaction and oversight pattern in which an AI agent cannot proceed beyond specific execution checkpoints without explicit human authorization, review, or input [^evt-ws-taxonomy-landscape-pr-40].

# Architecture / Specification
HITL establishes synchronous verification boundaries within agent workflows, contrasting with autonomous execution or human-on-the-loop oversight where monitoring occurs post-action or asynchronously [^evt-ws-taxonomy-landscape-pr-40]. In practice, it interfaces directly with approval mechanisms such as [human approval gates](../specification/human-approval-gate.md) and agent handoff protocols [^evt-ws-taxonomy-landscape-pr-40].

[^evt-ws-taxonomy-landscape-pr-40]: https://github.com/aaif/ws-taxonomy-landscape/pull/40
