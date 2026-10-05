---
type: pattern
title: Kill Switch Pattern
description: Architectural control plane pattern establishing out-of-band execution
  termination, credential invalidation, and network/tool denial for rogue agent workloads.
resource: https://github.com/aaif/wg-security-and-privacy/pull/26
tags:
- pattern
- security
- containment
- runtime
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:19:26.401683+00:00'
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
The Kill Switch pattern provides an out-of-band control plane mechanism to immediately halt autonomous agent execution, revoke credentials, and isolate compromised workloads [^evt-wg-security-and-privacy-pr-26]. Designed as a foundational defense pattern within the Security and Privacy Working Group catalog, it mitigates runaway iteration, data exfiltration, and unauthorized actions by severing an agent's lateral movement and tool dispatch capabilities [^evt-wg-security-and-privacy-pr-26].

# Architecture / Specification
The kill switch pattern executes containment actions across sequential enforcement steps [^evt-wg-security-and-privacy-issue-27]:
1. **Execution Termination**: Signaling local runtimes or container harnesses to halt active agent loop processes.
2. **Network and Tool Denial**: Dynamically rejecting tool invocations and network access at the enforcement proxy or gateway boundary.
3. **Credential Revocation**: Invalidating session tokens, IAM roles, and API keys issued to the agent to permanently close lateral movement surfaces [^evt-wg-security-and-privacy-issue-27].
4. **Circuit Breakers**: Tracking error rates and halting dispatch when threshold counters or kill triggers trip [^evt-wg-security-and-privacy-issue-27].

## Revocation and Outage Handling
A critical edge case occurs when the enforcement point runs within the agent workload (e.g., an in-process SDK or sidecar) and authenticates to a central policy service using credentials invalidated during containment [^evt-wg-security-and-privacy-issue-27]. If the policy service responds with HTTP 401 or 403, downstream availability breakers or "fail-open" allow-fallbacks must not interpret this authentication failure as a transient network outage [^evt-wg-security-and-privacy-issue-27]. Treating a 401/403 rejection as an outage could mistakenly reopen tool dispatch; instead, the enforcement point must treat credential invalidation as an explicit refusal and fail-closed [^evt-wg-security-and-privacy-issue-27].

# Lifecycle History
Drafted within the [../working-groups/security-and-privacy.md](../working-groups/security-and-privacy.md) design patterns catalog via PR #26 [^evt-wg-security-and-privacy-pr-26], with active discussion on residual failure modes when handling policy endpoint credential invalidation [^evt-wg-security-and-privacy-issue-27].

[^evt-wg-security-and-privacy-issue-27]: https://github.com/aaif/wg-security-and-privacy/issues/27
[^evt-wg-security-and-privacy-pr-26]: https://github.com/aaif/wg-security-and-privacy/pull/26
