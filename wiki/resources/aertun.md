---
type: resource
title: Aertun
description: Open-source evidence and verification layer reconciling agent telemetry
  against gateway logs, target audit trails, and Merkle-tree audit logs.
resource: https://github.com/aaif/project-proposals/issues/71
tags:
- resource
- verification
- evidence
- attestation
- audit
- security
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:37:33.064753+00:00'
sources:
- id: evt-project-proposals-issue-71
  resource: https://github.com/aaif/project-proposals/issues/71
  author: rsh1k
  last_modified: '2026-11-22T08:47:45+00:00'
---

# Overview

Aertun is an open-source, self-hosted evidence and verification layer designed to evaluate AI agent operational accounts against external, third-party audit evidence[^evt-project-proposals-issue-71]. Implemented as a single Go binary, Aertun reconciles self-reported telemetry from an agent against intermediary gateway logs and independent target system audit trails[^evt-project-proposals-issue-71].

Verification outcomes are rendered as cryptographic in-toto Statements packaged in Dual-Signature Envelope (DSSE) envelopes, dual-signed using Ed25519 and post-quantum ML-DSA-65 keys[^evt-project-proposals-issue-71]. Each assertion produces an offline-verifiable verdict categorized as proven, refuted, or inconclusive with defined statistical bounds[^evt-project-proposals-issue-71].

# Architecture / Specification

Aertun's capabilities include:
- **Three-Way Agent Reconciliation**: Compares agent [OpenTelemetry](../resources/opentelemetry.md) traces against gateway interaction records (such as [agentgateway](../resources/agentgateway.md)) and target system access logs to detect unreported or phantom actions[^evt-project-proposals-issue-71].
- **Revocation Efficacy Proofs**: Demonstrates whether access ceased across enterprise identity providers following [kill-switch](../patterns/kill-switch.md) invocation or credential revocation[^evt-project-proposals-issue-71].
- **Log Completeness and Bitcoin Anchoring**: Generates Merkle-tree audit proofs demonstrating logs have not been truncated or forked, anchoring log roots to the Bitcoin blockchain for proof-of-existence[^evt-project-proposals-issue-71].
- **Agent Interface**: Exposes a Model Context Protocol (MCP) server supporting OAuth 2.1, DPoP-bound tokens, Shared Signals and Events (SSF), and emergency termination triggers[^evt-project-proposals-issue-71].
- **Detection Wind Tunnel**: Automates attack replay (such as prompt injection or MCP rug-pulls) alongside benign baseline workflows in CI environments to benchmark false-negative and false-positive detection rates[^evt-project-proposals-issue-71].

# Lifecycle History

- Initiated in October 2026; release v0.2.0 published in November 2026[^evt-project-proposals-issue-71].
- Proposed for AAIF Sandbox project incubation under the Technical Committee review process via issue #71[^evt-project-proposals-issue-71].

[^evt-project-proposals-issue-71]: https://github.com/aaif/project-proposals/issues/71
