---
type: pattern
title: Kill Switch Pattern
description: An independent out-of-band runtime control plane that halts agent execution,
  revokes active credentials, and closes lateral-movement attack surfaces.
resource: https://github.com/aaif/wg-security-and-privacy/pull/26
tags:
- pattern
- security
- runtime-control
- fail-safe
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:51:02.405749+00:00'
sources:
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

The Kill Switch pattern defines an independent, out-of-band runtime control plane capable of terminating agent execution, revoking active credentials, and enforcing network and tool access denial [^evt-wg-security-and-privacy-pr-26]. Designed as a fail-safe mechanism, it guarantees deterministic containment when an agent exhibits unaligned, adversarial, or out-of-bounds behavior.

# Architecture / Specification

## Containment Actions

When activated, the kill switch executes three containment phases:
1. **Execution Halting:** Pauses or terminates active agent processes, subagents, and queued workflow tasks.
2. **Network and Tool Denial:** Disables network access and blocks tool invocation dispatch paths.
3. **Credential Revocation:** Invalidates session tokens, delegation grants, and service credentials to eliminate lateral movement surfaces [^evt-wg-security-and-privacy-issue-27].

## Residual Risks and Implementation Nuances

- **Revocation Read as an Outage:** Where the policy enforcement point runs within the agent workload (e.g., an in-process SDK or sidecar), revoking the credential it presents to its upstream policy service causes subsequent authorization requests to return HTTP 401/403 status codes [^evt-wg-security-and-privacy-issue-27]. If the enforcement point includes an availability breaker or 'fail-open' fallback, it may erroneously treat this credential rejection as a transient service outage and reopen tool dispatch [^evt-wg-security-and-privacy-issue-27]. Enforcement points must treat authentication rejections as strict policy refusals rather than availability outages [^evt-wg-security-and-privacy-issue-27].
- **Circuit Breaker Integration:** Authorization rejections must trigger halt counters within circuit breaker logic rather than triggering bypass fallbacks [^evt-wg-security-and-privacy-issue-27].

# Lifecycle History

- **2026-09-26:** Merged initial design pattern specification under the Security and Privacy Working Group [^evt-wg-security-and-privacy-pr-26].
- **2026-09-29:** Issue #27 opened proposing clarification on credential revocation failure handling in local sidecar enforcement points [^evt-wg-security-and-privacy-issue-27].

[^evt-wg-security-and-privacy-issue-27]: https://github.com/aaif/wg-security-and-privacy/issues/27
[^evt-wg-security-and-privacy-pr-26]: https://github.com/aaif/wg-security-and-privacy/pull/26
