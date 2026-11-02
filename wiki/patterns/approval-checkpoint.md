---
type: pattern
title: Approval Checkpoint
description: Runtime governance pattern binding approval records to exact execution
  payloads and tracking decision validity across enforcement boundaries.
resource: https://github.com/aaif/wg-security-and-privacy/pull/44
tags:
- governance
- pattern
- security
- approval
- authzen
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:30:09.197993+00:00'
sources:
- id: evt-wg-security-and-privacy-pr-44
  resource: https://github.com/aaif/wg-security-and-privacy/pull/44
  author: awfrazer
  last_modified: '2026-10-28T19:18:34+00:00'
---

# Overview

The Approval Checkpoint pattern binds authorization decisions to exact action payloads, cryptographic hashes, and execution contexts before an agent is permitted to invoke tools or execute state-changing operations.[^evt-wg-security-and-privacy-pr-44] It operates as a runtime verification gate ensuring that signed approval records correspond precisely to the runtime invocation payload dispatched by the agent harness.[^evt-wg-security-and-privacy-pr-44]

# Architecture / Specification

The pattern establishes an enforcement protocol separating the policy decision point (PDP) from the policy enforcement point (PEP) embedded within the execution harness.[^evt-wg-security-and-privacy-pr-44] Implementation profiles such as the [Control Surfaces for Agentic Harnesses](../standards/control-surfaces-for-agentic-harnesses.md) define concrete reconciliation criteria for this checkpoint:

- **Digest Evaluation and Argument Minimization:** While basic checkpoint models require the enforcement point to recompute action payload digests directly from runtime arguments, privacy-preserving argument minimization protocols require PDPs to evaluate client-supplied digests against registered decision digests without full argument disclosure.[^evt-wg-security-and-privacy-pr-44]
- **Clock Skew and Validity Windows:** Verification mandates explicit clock skew tolerances between distributed policy decision points and enforcement points, preventing premature expiration or replay windows.[^evt-wg-security-and-privacy-pr-44]
- **Failure Classification:** Checkpoint implementations fold integrity mismatches, policy unavailability, and verification timeouts into deterministic fail-closed denials (`fail_closed_deny`), classifying the source of failure explicitly for audit trails.[^evt-wg-security-and-privacy-pr-44]

[^evt-wg-security-and-privacy-pr-44]: https://github.com/aaif/wg-security-and-privacy/pull/44
