---
type: pattern
title: Human Approval Gate
description: Workflow governance pattern requiring authorized human review before
  executing sensitive agent actions, mitigated against approval fatigue via automated
  acceptance checks.
resource: https://github.com/aaif/wg-security-and-privacy/issues/35
tags:
- pattern
- governance
- hitl
- security
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T10:51:49.114172+00:00'
sources:
- id: evt-wg-security-and-privacy-issue-35
  resource: https://github.com/aaif/wg-security-and-privacy/issues/35
  author: barka-bee
  last_modified: '2026-10-05T07:57:34+00:00'
---

# Overview
The Human Approval Gate pattern establishes an explicit execution pause in an autonomous agent workflow, requiring an authorized human operator to inspect and approve a structured proposal before any irreversible or high-impact tool can execute. Designed to maintain human accountability over autonomous systems, the pattern combines cryptographic approval binding with fatigue-reduction mechanisms to prevent superficial review and rubber-stamping.

# Architecture / Specification

## Workflow Execution and Proposal Split
Operating alongside the [proposal-execution split](./proposal-execution-split.md), the agent transitions into a [durable wait](./durable-wait.md) state upon assembling a critical action. The system creates an [approval checkpoint](./approval-checkpoint.md) record containing:
- The exact serialized command and target resource.
- Contextual justifications, tool provenance, and safety classifications.
- An immutable cryptographic hash binding the reviewer's signature directly to the payload.

Execution remains blocked until an authenticated operator signs an approval token or issues a structured rejection.

## Reviewer Fatigue and Vulnerability Profiles
Working group reviews highlight that flat, high-frequency approval gates suffer severe human reliability degradation[^evt-wg-security-and-privacy-issue-35]:
- **Rubber-Stamping Baselines:** In empirical studies of interactive coding agents, operators approved 97% of permission prompts indiscriminately[^evt-wg-security-and-privacy-issue-35].
- **Interception Degradation:** Humans intercepted dangerous commands in only 13.6% of presentations, with interception success dropping to approximately 5% after 50 consecutive prompts[^evt-wg-security-and-privacy-issue-35].
- **Automated Gate Comparison:** By comparison, deterministic automated checks successfully intercepted 89% of the same hazardous operations[^evt-wg-security-and-privacy-issue-35].

## Fatigue Mitigation and Gate Calibration
To preserve defensive validity, implementations must not rely on unassisted manual review:
1. **Automated Pre-Filtering:** Precede human gates with [deterministic acceptance gates](./deterministic-acceptance-gate.md) that automatically intercept out-of-policy invocations before alerting human reviewers[^evt-wg-security-and-privacy-issue-35].
2. **Approval Velocity Limits:** Monitor prompt repetition velocity and reviewer dwell times, flagging rapid sequential approvals for secondary review.
3. **Differential Impact Highlighting:** Visually distinguish destructive, network-exfiltrating, or credential-accessing arguments from routine read operations.

# Lifecycle History
Documented as an architectural governance pattern by the [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md). Empirical failure data and rubber-stamping defenses incorporated following technical reviews with the [Security and Privacy Working Group](../working-groups/security-and-privacy.md)[^evt-wg-security-and-privacy-issue-35].

[^evt-wg-security-and-privacy-issue-35]: https://github.com/aaif/wg-security-and-privacy/issues/35
