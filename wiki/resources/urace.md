---
type: resource
title: URACE (Unified Runtime for Autonomous Collaborative Evolution)
description: Open-source P2P-first lifecycle control plane and execution runtime governing
  autonomous AI-assisted software improvements.
resource: https://github.com/aaif/project-proposals/issues/67
tags:
- runtime
- control-plane
- p2p
- governance
- cryptography
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:32:44.481487+00:00'
sources:
- id: evt-project-proposals-issue-67
  resource: https://github.com/aaif/project-proposals/issues/67
  author: joaoalbertocsjunior
  last_modified: '2026-11-02T05:25:01+00:00'
---

# Overview
URACE (Unified Runtime for Autonomous Collaborative Evolution) is an open-source, peer-to-peer (P2P) lifecycle control plane and execution runtime designed to govern autonomous AI-assisted software evolution.[^evt-project-proposals-issue-67] Proposed for the AAIF Growth lifecycle stage under the Apache 2.0 license, URACE enables AI executors to discover, propose, qualify, and distribute verified code improvements across decentralized networks without central coordination.[^evt-project-proposals-issue-67]

# Architecture / Specification
URACE provides a governed runtime architecture bridging agent model outputs with production codebases:

- **Governed Improvement Loop**: Enforces an operational pipeline transitioning objectives to executor plans, qualification gate evaluation, accepted operations, and an immutable HMAC-chained ledger.[^evt-project-proposals-issue-67] AI executors are prevented by schema enforcement from modifying governance rules, authority boundaries, or qualification criteria.[^evt-project-proposals-issue-67]
- **Decentralized P2P Feature Marketplace**: Facilitates tokenized exchange and borrowing of verified code improvements between network peers using a physics-calibrated token economy with Sybil-resistant reputation scoring based on the Wilson lower-bound algorithm.[^evt-project-proposals-issue-67]
- **Cryptographic Security**: Employs hybrid post-quantum cryptography combining ML-KEM-768 with classical TLS, alongside self-signed certificates and tamper-evident audit trails.[^evt-project-proposals-issue-67]
- **Composability**: Exposes an `AGENTS.md` machine-readable onboarding API surface, allowing integration with external agent frameworks as gated executors while generating compatible software provenance records.[^evt-project-proposals-issue-67]

# Lifecycle History
Originally developed as an independent research and production codebase with 280 source files and 2,677 tests, URACE was submitted to the AAIF Technical Committee in Issue #67 as a candidate for Growth stage adoption under the [Project Lifecycle Policy](../policies/project-lifecycle-policy.md).[^evt-project-proposals-issue-67]

[^evt-project-proposals-issue-67]: https://github.com/aaif/project-proposals/issues/67
