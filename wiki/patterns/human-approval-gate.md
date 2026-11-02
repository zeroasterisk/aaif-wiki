---
type: pattern
title: Human Approval Gate
description: Workflow governance pattern requiring authorized human review before
  executing sensitive agent actions, reinforced by automated pre-gates against approval
  fatigue.
resource: https://github.com/aaif/wg-security-and-privacy/issues/35
tags:
- pattern
- governance
- hitl
- safety
- approval-fatigue
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:15:51.752089+00:00'
sources:
- id: evt-wg-security-and-privacy-issue-35
  resource: https://github.com/aaif/wg-security-and-privacy/issues/35
  author: barka-bee
  last_modified: '2026-10-05T07:57:34+00:00'
---

# Overview

The Human Approval Gate pattern introduces a synchronous authorization checkpoint into an agent workflow, preventing the execution of sensitive or high-impact actions until an authorized operator inspects and approves the request. While standard across single-agent and multi-agent governance architectures (../architectures/single-agent-human-approval.md), unconditioned prompts are vulnerable to severe operator fatigue and habituated rubber-stamping [^evt-wg-security-and-privacy-issue-35].

# Architecture / Specification

## Approval Fatigue and Failure Dynamics
Empirical research highlights the degradation of human oversight under frequent interactive prompts [^evt-wg-security-and-privacy-issue-35]:
- **Passive Approval Rates**: In large-scale user studies, approximately 97% of interactive agent permission prompts are accepted by operators without substantive inspection [^evt-wg-security-and-privacy-issue-35].
- **Detection Decay**: Human testers caught only 13.6% of dangerous commands slipped into agent sessions, with detection efficacy falling to approximately 5% after 50 prior prompts in a single session [^evt-wg-security-and-privacy-issue-35].
- **Habituation**: Frequent binary confirmations train operators to clear modals automatically, negating the gate's efficacy against indirect prompt injections and subverted tool calls [^evt-wg-security-and-privacy-issue-35].

## Hardened Implementation Guidelines
To maintain security integrity, human approval checkpoints must be paired with automated evaluation and contextual throttling:
- **Automated Pre-Gating**: Workflows should evaluate candidate actions against deterministic policy engines (../patterns/deterministic-acceptance-gate.md) before presenting them to humans, which can catch up to 89% of hazardous actions automatically [^evt-wg-security-and-privacy-issue-35].
- **Velocity and Fatigue Tracking**: Runtimes must track prompt frequency and operator review latency, enforcing cooling-off intervals, batching routine executions, or triggering out-of-band sign-offs (../patterns/hardware-bound-human-authorization.md) when velocity indicates rubber-stamping [^evt-wg-security-and-privacy-issue-35].
- **Payload Verification**: Actions submitted for review must bind to unalterable execution artifacts via cryptographic checkpoints (../patterns/approval-checkpoint.md), ensuring the approved intent matches the executed payload [^evt-wg-security-and-privacy-issue-35].

# Lifecycle History
Originally formulated as a foundational human-in-the-loop pattern, this pattern was updated to reflect empirical human review studies submitted during Security and Privacy Working Group reviews [^evt-wg-security-and-privacy-issue-35].

[^evt-wg-security-and-privacy-issue-35]: https://github.com/aaif/wg-security-and-privacy/issues/35
