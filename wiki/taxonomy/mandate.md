---
type: taxonomy
title: Mandate
description: Agentic Commerce taxonomy term defining an explicit authorization and
  boundary agreement governing an agent's authority to act or transact on behalf of
  a principal.
resource: https://github.com/aaif/ws-taxonomy-landscape/pull/77
tags:
- taxonomy
- agentic-commerce
- governance
- authorization
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:22:36.598692+00:00'
sources:
- id: evt-ws-taxonomy-landscape-pr-77
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/77
  author: galesky-a
  last_modified: '2026-10-12T03:07:32+00:00'
---

# Overview

A Mandate is an Agentic Commerce taxonomy concept representing an explicit delegation of authority granted by a [principal](../taxonomy/principal.md) to an agent[^evt-ws-taxonomy-landscape-pr-77]. It defines the precise operational, financial, and contractual constraints within which an agent is legally and operationally permitted to execute tasks or financial commitments[^evt-ws-taxonomy-landscape-pr-77].

# Architecture / Specification

In agentic commerce architectures, a mandate functions as the authorization contract underpinning agent transactions, including [agent-in-the-loop transactions](../taxonomy/agent-in-the-loop-transaction.md) and [agent-initiated transactions](../taxonomy/agent-initiated-transaction.md)[^evt-ws-taxonomy-landscape-pr-77]. 

A mandate typically articulates:
- **Scope of Representation**: Permitted counterparty domains, merchant registries, or catalog surfaces.
- **Transaction Boundaries**: Per-transaction or aggregate monetary thresholds and expiration timelines.
- **Execution Constraints**: Required checkpoints, such as invoking a [human-approval-gate](../patterns/human-approval-gate.md) or [delegated-payment](../taxonomy/delegated-payment.md) execution mechanism when transactions exceed authorized boundaries.

[^evt-ws-taxonomy-landscape-pr-77]: https://github.com/aaif/ws-taxonomy-landscape/pull/77
