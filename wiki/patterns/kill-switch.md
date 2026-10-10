---
type: pattern
title: Kill Switch
description: Architectural control plane pattern establishing an independent out-of-band
  mechanism to immediately halt agent execution, sever network access, and invalidate
  credentials.
resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/workstreams/design-patterns/README.md
tags:
- security
- containment
- control-plane
- safety
- patterns
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:13:43.764205+00:00'
sources:
- id: evt-wg-security-and-privacy-file-9d8108887b54-74938a50
  resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/workstreams/design-patterns/README.md
  author: sagardashora
  last_modified: '2026-09-30T10:16:03-04:00'
- id: evt-wg-security-and-privacy-file-d2691d0f1f64-8e9abf01
  resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/workstreams/design-patterns/DRAFT-kill_switch_pattern.md
  author: sagardashora
  last_modified: '2026-09-30T10:16:03-04:00'
- id: evt-wg-security-and-privacy-pr-26
  resource: https://github.com/aaif/wg-security-and-privacy/pull/26
  author: sagardashora
  last_modified: '2026-09-30T14:16:03+00:00'
- id: evt-wg-security-and-privacy-issue-27
  resource: https://github.com/aaif/wg-security-and-privacy/issues/27
  author: Santoshkumarpuppala
  last_modified: '2026-09-30T14:27:19+00:00'
---

# Overview

The Kill Switch pattern defines an independent, out-of-band runtime control plane that immediately halts agent execution, severs external network communications, and invalidates active session credentials [^evt-wg-security-and-privacy-file-d2691d0f1f64-8e9abf01]. By decoupling containment controls from an agent's prompt context, internal memory, and execution loops, the pattern prevents misbehaving or hijacked autonomous agents from bypassing deactivation or leaving orphaned background tasks [^evt-wg-security-and-privacy-file-d2691d0f1f64-8e9abf01].

# Architecture / Specification

Traditional process termination (`SIGKILL`) is insufficient for autonomous agent systems due to shutdown resistance, model evasion, asynchronous task orphanage (zombie processes), high execution velocity in runaway loops, and unexpired credential exposure [^evt-wg-security-and-privacy-file-d2691d0f1f64-8e9abf01]. The pattern separates declarative stopping criteria from the technical enforcement control plane across a three-stage containment loop:

1. **Detect**: External policy engines, circuit breakers, and anomaly detection services evaluate runtime telemetry outside the model's reach.
2. **Halt**: The control plane initiates immediate execution termination across the host runtime, dispatches network isolation commands to gateways, and revokes all active API tokens and ephemeral session credentials [^evt-wg-security-and-privacy-file-d2691d0f1f64-8e9abf01].
3. **Rollback**: Compensating transactions and state rollbacks reconcile modified resources to safe checkpoints.

### Relationship to Other Patterns

- [Attested Isolated Runtime](attested-isolated-runtime.md): Provides confidential hardware-isolated enforcement boundaries, hardware attestation, and scoped credential release, complementing kill-switch containment [^evt-wg-security-and-privacy-file-d2691d0f1f64-8e9abf01].
- [Approval Checkpoint](approval-checkpoint.md): Establishes verifiable pre-execution authorizations and audits prior to runtime tool calls [^evt-wg-security-and-privacy-file-9d8108887b54-74938a50].

# Lifecycle History

- Proposed and merged into the Security and Privacy Working Group design patterns catalog via PR #26 [^evt-wg-security-and-privacy-pr-26].
- Issue #27 identified an edge case where credential revocation at sidecar enforcement points could be misinterpreted as an outage by fallback handlers, emphasizing strict fail-closed behavior on HTTP 401/403 responses [^evt-wg-security-and-privacy-issue-27].

[^evt-wg-security-and-privacy-file-9d8108887b54-74938a50]: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/workstreams/design-patterns/README.md
[^evt-wg-security-and-privacy-file-d2691d0f1f64-8e9abf01]: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/workstreams/design-patterns/DRAFT-kill_switch_pattern.md
[^evt-wg-security-and-privacy-issue-27]: https://github.com/aaif/wg-security-and-privacy/issues/27
[^evt-wg-security-and-privacy-pr-26]: https://github.com/aaif/wg-security-and-privacy/pull/26
