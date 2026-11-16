---
type: pattern
title: Kill Switch
description: Architectural control plane pattern establishing an independent, out-of-band
  containment loop to halt agent execution, sever network communication, invalidate
  credentials, and roll back state.
resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/workstreams/design-patterns/DRAFT-kill_switch_pattern.md
tags:
- security
- containment
- control-plane
- fault-tolerance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:21:56.668978+00:00'
sources:
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
The Kill Switch pattern establishes an independent, out-of-band runtime control plane capable of immediately halting an agent's execution, severing its external network communications, revoking active session credentials, and initiating state rollback outside the agent's internal reasoning loop.[^evt-wg-security-and-privacy-file-d2691d0f1f64-8e9abf01] Designed for systems architects and safety engineers, the pattern addresses fundamental agentic failure modes where naive OS-level process termination (`SIGKILL`) fails due to model evasion, shutdown resistance, machine-speed runaway feedback loops, credential leakage, or orphaned asynchronous background tasks.[^evt-wg-security-and-privacy-file-d2691d0f1f64-8e9abf01]

# Architecture / Specification
The pattern separates declarative trigger criteria (policies defining when to stop) from technical enforcement architecture, organizing runtime containment into a coordinated three-phase loop: **detect → halt → rollback**.[^evt-wg-security-and-privacy-file-d2691d0f1f64-8e9abf01]

- **Containment Execution**: Execution termination is managed entirely server-side, isolated from the agent's prompt context and memory to prevent model subversion.[^evt-wg-security-and-privacy-file-d2691d0f1f64-8e9abf01]
- **Network and Tool Denial**: Immediately blocks tool dispatch interfaces, agent-to-agent gateways, and outbound network traffic to prevent lateral movement.[^evt-wg-security-and-privacy-file-d2691d0f1f64-8e9abf01]
- **Credential Revocation**: Automatically invalidates ephemeral tokens, API keys, and session delegations across all distributed components to decommission background scripts and child tasks.[^evt-wg-security-and-privacy-file-d2691d0f1f64-8e9abf01]
- **Reversibility and Rollback**: Reads the in-flight execution log (such as the execution records structured under [Approval Checkpoint](approval-checkpoint.md)) to trigger compensating transactions against external services using both execution and service identifiers.[^evt-wg-security-and-privacy-file-d2691d0f1f64-8e9abf01]

Working group discussions track an open implementation risk where in-process sidecars or SDK enforcement points receive HTTP 401/403 errors upon policy credential revocation; systems must ensure such rejections are treated as hard refusals and circuit-breaker events rather than failing open as transient network outages.[^evt-wg-security-and-privacy-issue-27]

# Lifecycle History
Merged into the [Security and Privacy Design Patterns Catalog](../resources/security-and-privacy-design-patterns-catalog.md) as a foundational containment pattern.[^evt-wg-security-and-privacy-file-d2691d0f1f64-8e9abf01][^evt-wg-security-and-privacy-pr-26] Complements [Attested Isolated Runtime](attested-isolated-runtime.md) for hardened enforcement boundaries and protected credential release.[^evt-wg-security-and-privacy-file-d2691d0f1f64-8e9abf01]

# References
- Catalog Draft: `workstreams/design-patterns/DRAFT-kill_switch_pattern.md`[^evt-wg-security-and-privacy-file-d2691d0f1f64-8e9abf01]
- Working Group Discussion: Issue #27 on credential revocation interaction with circuit breakers[^evt-wg-security-and-privacy-issue-27]

[^evt-wg-security-and-privacy-file-d2691d0f1f64-8e9abf01]: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/workstreams/design-patterns/DRAFT-kill_switch_pattern.md
[^evt-wg-security-and-privacy-issue-27]: https://github.com/aaif/wg-security-and-privacy/issues/27
[^evt-wg-security-and-privacy-pr-26]: https://github.com/aaif/wg-security-and-privacy/pull/26
