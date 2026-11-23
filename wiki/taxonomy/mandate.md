---
type: taxonomy
title: Mandate
description: Agentic Commerce taxonomy term defining an explicit authorization and
  parameter boundary granted by a principal permitting an agent to initiate transactions.
resource: https://github.com/aaif/ws-taxonomy-landscape/pull/77
tags:
- taxonomy
- commerce
- authorization
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:23:39.129324+00:00'
sources:
- id: evt-ws-taxonomy-landscape-pr-77
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/77
  author: galesky-a
  last_modified: '2026-10-12T03:07:32+00:00'
---

# Overview
A **mandate** in the Agentic Commerce taxonomy is an explicit authorization granted by a [principal](../taxonomy/principal.md) that establishes the valid constraints, financial thresholds, and operational scope under which an agent may initiate or mediate commercial transactions [^evt-ws-taxonomy-landscape-pr-77].

# Architecture / Specification
Within agentic commerce workflows, mandates define the legal and runtime permissions for transaction execution [^evt-ws-taxonomy-landscape-pr-77]:
- **Pre-authorized Execution**: Serves as the policy boundary allowing [agent-initiated transactions](../taxonomy/agent-initiated-transaction.md) and [delegated payments](../taxonomy/delegated-payment.md) to proceed autonomously without per-action synchronous approval, provided operational parameters remain within declared constraints [^evt-ws-taxonomy-landscape-pr-77].
- **Constraint Boundaries**: Encapsulates specific financial ceilings, frequency limits, counterparty conditions, and validity timeframes established during [agentic checkout](../taxonomy/agentic-checkout.md) or onboarding.
- **Lifecycle and Revocation**: Subject to revocation, renewal, and attestation by the authorizing principal or governing institution under [Agentic Commerce Working Group](../working-groups/agentic-commerce.md) frameworks.

[^evt-ws-taxonomy-landscape-pr-77]: https://github.com/aaif/ws-taxonomy-landscape/pull/77
