---
type: pattern
title: Approval Checkpoint
description: Runtime governance pattern binding policy or human approvals to exact
  action payloads and maintaining cryptographic auditability across execution boundaries.
resource: https://github.com/aaif/wg-security-and-privacy/pull/28
tags:
- patterns
- governance
- security
- authorization
- audit
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:11:44.946840+00:00'
sources:
- id: evt-wg-security-and-privacy-pr-28
  resource: https://github.com/aaif/wg-security-and-privacy/pull/28
  author: Rul1an
  last_modified: '2026-09-30T14:40:31+00:00'
---

# Overview
The Approval Checkpoint pattern establishes an enforceable runtime gate where an agent's proposed action must receive authenticated human or policy approval before execution.[^evt-wg-security-and-privacy-pr-28] By binding authorization tokens to cryptographic hashes of the specific action payload, the pattern prevents payload substitution and time-of-check to time-of-use (TOCTOU) attacks.[^evt-wg-security-and-privacy-pr-28]

# Architecture / Specification
The checkpoint operates as an intermediary control surface between agent reasoning and external tool execution:
- **Payload Binding**: Generates a deterministic hash over the candidate action, parameters, and invocation target. Authorization is strictly valid only for this exact payload.
- **Vulnerability Mitigations**: Formally addresses unauthorized payload modification (cataloged as V7), which cross-links directly with identity spoofing (V2) and tool parameter injection (V8).[^evt-wg-security-and-privacy-pr-28]
- **Kill Switch Coordination**: Integrates with the [Kill Switch](`../patterns/kill-switch.md`) pattern by maintaining an immutable record of authorized checkpoints, enabling operational response teams to know what was released prior to triggering emergency terminations.[^evt-wg-security-and-privacy-pr-28]
- **Architectural Separation**: Interlocks with [`../patterns/proposal-execution-split.md`](../patterns/proposal-execution-split.md) to decouple intent proposal from execution credentials.

# Lifecycle History
Maintained within the Security and Privacy Working Group's design pattern catalog ([`../resources/security-and-privacy-design-patterns-catalog.md`](../resources/security-and-privacy-design-patterns-catalog.md)). PR #28 restored vulnerability references to V2 and V8 in cell V7 and refined the Kill Switch coordination specification.[^evt-wg-security-and-privacy-pr-28]

[^evt-wg-security-and-privacy-pr-28]: https://github.com/aaif/wg-security-and-privacy/pull/28
