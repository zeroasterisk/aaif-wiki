---
type: resource
title: URACE (Unified Runtime for Autonomous Collaborative Evolution)
description: Open-source P2P lifecycle control plane and governed runtime for autonomous
  software evolution, qualification gates, and post-quantum audited code distribution.
resource: https://github.com/aaif/project-proposals/issues/67
tags:
- runtime
- p2p
- governance
- qualification-gate
- cryptography
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:33:38.696754+00:00'
sources:
- id: evt-project-proposals-issue-67
  resource: https://github.com/aaif/project-proposals/issues/67
  author: joaoalbertocsjunior
  last_modified: '2026-11-02T05:25:01+00:00'
---

# Overview

URACE (Unified Runtime for Autonomous Collaborative Evolution) is an open-source, peer-to-peer lifecycle control plane designed to govern autonomous, AI-driven software development and distribution across decentralized networks without central authorities.[^evt-project-proposals-issue-67] It bridges the gap between raw AI code generation and production repositories by enforcing qualification gates, post-quantum cryptographic identity, and tamper-evident audit ledgers.[^evt-project-proposals-issue-67]

# Architecture / Specification

### Governed Improvement Loop

URACE coordinates autonomous executors (LLMs or automated agents) through an immutable execution cycle:[^evt-project-proposals-issue-67]

1. **Objective Ingestion**: Practitioners define declarative targets (e.g., latency reduction, test coverage).
2. **Executor Planning**: AI executors draft structured execution plans and code modifications.
3. **Qualification Gate**: An automated evaluation harness executes trial tests, safety predicates, and schema constraints. Executors are strictly prohibited from altering governance rules, authority configurations, or evaluation criteria.
4. **Accepted Operations**: Changes meeting acceptance thresholds are committed to the codebase.
5. **Immutable Audit Trail**: All decisions, trial evidence, and operations are recorded in an HMAC-chained, cryptographically verifiable ledger.

### P2P Feature Marketplace and Token Economy

Verified improvements can be tokenized, exchanged, or borrowed between peers across a decentralized network using a physics-calibrated token model.[^evt-project-proposals-issue-67] Peer reputation is calculated via Wilson lower-bound scoring based on verified delivery history rather than subjective assertions, providing defense against Sybil attacks and cartel manipulation.[^evt-project-proposals-issue-67]

### Cryptographic Architecture

URACE implements hybrid post-quantum cryptography combining ML-KEM-768 with classical TLS transport, alongside self-signed cryptographic identity certificates and machine-readable `AGENTS.md` interface manifests for zero-configuration executor onboarding.[^evt-project-proposals-issue-67]

# Lifecycle History

- **October 2026**: Submitted to the Agentic AI Foundation as a Growth stage project proposal under the Apache 2.0 license.[^evt-project-proposals-issue-67]

# References

- [Deterministic Acceptance Gate](../patterns/deterministic-acceptance-gate.md)
- [Project Proposal Process](../policies/project-proposal-process.md)
- [Project Lifecycle Policy](../policies/project-lifecycle-policy.md)

[^evt-project-proposals-issue-67]: https://github.com/aaif/project-proposals/issues/67
