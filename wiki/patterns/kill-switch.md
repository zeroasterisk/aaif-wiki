---
type: pattern
title: Kill Switch
description: Architectural control plane pattern providing out-of-band execution termination,
  network isolation, credential revocation, and compensating rollback for autonomous
  agent workloads.
resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/workstreams/design-patterns/DRAFT-kill_switch_pattern.md
tags:
- security
- containment
- runtime-governance
- control-plane
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:09:49.644342+00:00'
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
The Kill Switch pattern establishes an independent, out-of-band runtime control plane capable of immediately halting an agent's execution, severing its external network communications, and invalidating its active credentials.[^evt-wg-security-and-privacy-file-d2691d0f1f64-8e9abf01] Integrated into the [Security and Privacy Design Patterns Catalog](../resources/security-and-privacy-design-patterns-catalog.md), it mitigates fundamental agent containment failures where prompt-level stop instructions are evaded or where background zombie tasks outlive orchestrator processes.[^evt-wg-security-and-privacy-file-d2691d0f1f64-8e9abf01][^evt-wg-security-and-privacy-pr-26]

# Architecture / Specification
The pattern structures agent containment into an automated loop: **detect → halt → rollback**, enforced completely outside the model's memory, prompt context, and execution loops.[^evt-wg-security-and-privacy-file-d2691d0f1f64-8e9abf01]

## Core Containment Mechanics
1. **Execution Halting**: Forcibly terminates orchestrators and background child processes or async threads, preventing task orphanage.[^evt-wg-security-and-privacy-file-d2691d0f1f64-8e9abf01]
2. **Network and Tool Denial**: Server-side proxies or runtime egress firewalls drop in-flight API requests and block tool endpoints.[^evt-wg-security-and-privacy-file-d2691d0f1f64-8e9abf01]
3. **Credential Invalidation**: Out-of-band identity provider integration revokes short-lived session tokens, signing keys, and tool permissions.[^evt-wg-security-and-privacy-file-d2691d0f1f64-8e9abf01]
4. **Circuit Breakers**: Threshold-based tripwires monitor tool error rates, loop depth, and resource consumption, triggering containment when anomalous behavior is detected.[^evt-wg-security-and-privacy-file-d2691d0f1f64-8e9abf01]
5. **Reversibility and Rollback**: Reads structured execution logs to execute compensating transactions for side effects committed prior to termination.[^evt-wg-security-and-privacy-file-d2691d0f1f64-8e9abf01]

## Unsettled Discussions and Residual Risks
Working group review has highlighted potential failure modes when enforcement points execute inside the agent's workload (e.g., sidecars or in-process SDKs). If credential revocation causes policy verification calls to return HTTP 401 or 403, misconfigured fail-open or availability fallbacks could inadvertently reopen tool dispatch, underscoring the requirement that policy rejections be strictly treated as refusal.[^evt-wg-security-and-privacy-issue-27]

## Inter-Pattern Relationships
- **[Approval Checkpoint](../patterns/approval-checkpoint.md)**: Coordinates cooling-off queue releases and provides the dual execution-service identifier mapping needed for compensating rollbacks.[^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5]
- **[Attested Isolated Runtime](../patterns/attested-isolated-runtime.md)**: Supplies an immutable, hardware-enforced boundary for credential release and policy appraisal.[^evt-wg-security-and-privacy-file-d2691d0f1f64-8e9abf01]

# Lifecycle History
- Initial draft merged into `aaif/wg-security-and-privacy` via PR #26.[^evt-wg-security-and-privacy-pr-26]
- Issue #27 opened to analyze enforcement point credential revocation and fail-open availability fallback risks.[^evt-wg-security-and-privacy-issue-27]

[^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5]: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/workstreams/design-patterns/DRAFT-approval_checkpoint_pattern.md
[^evt-wg-security-and-privacy-file-d2691d0f1f64-8e9abf01]: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/workstreams/design-patterns/DRAFT-kill_switch_pattern.md
[^evt-wg-security-and-privacy-pr-26]: https://github.com/aaif/wg-security-and-privacy/pull/26
[^evt-wg-security-and-privacy-issue-27]: https://github.com/aaif/wg-security-and-privacy/issues/27
