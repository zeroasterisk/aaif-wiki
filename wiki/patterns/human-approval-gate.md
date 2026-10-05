---
type: pattern
title: Human Approval Gate
description: Runtime governance pattern subjecting privileged actions to explicit
  human review, backed by pre-execution automated filters to mitigate approval fatigue.
resource: https://github.com/aaif/wg-security-and-privacy/issues/31
tags:
- patterns
- governance
- human-in-the-loop
- approval-fatigue
- authorization
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:27:40.495878+00:00'
sources:
- id: evt-wg-security-and-privacy-issue-31
  resource: https://github.com/aaif/wg-security-and-privacy/issues/31
  author: barka-bee
  last_modified: '2026-10-05T07:57:29+00:00'
- id: evt-wg-security-and-privacy-issue-35
  resource: https://github.com/aaif/wg-security-and-privacy/issues/35
  author: barka-bee
  last_modified: '2026-10-05T07:57:34+00:00'
---

# Overview

The Human Approval Gate pattern establishes a synchronous governance boundary ensuring that high-consequence agent actions require explicit, informed review and authorization by an authenticated operator before side-effects execute. When deployed alongside deterministic rule hooks, it forms the escalation tier of runtime authorization architectures.

# Architecture / Specification

## Approval Fatigue and Failure Modes
Reliance on flat, indiscriminate approval prompts for routine tool calls induces severe reviewer fatigue [^evt-wg-security-and-privacy-issue-31] [^evt-wg-security-and-privacy-issue-35]. Empirical evaluations show human catch rates for malicious or dangerous commands degrade rapidly (from ~13.6% down to ~5% after sustained prompt exposure), while baseline user approval rates exceed 97% [^evt-wg-security-and-privacy-issue-31] [^evt-wg-security-and-privacy-issue-35].

## Multi-Stage Filtering and In-Loop Hooks
To ensure approval gates remain effective:
1. **Pre-Execution Rules**: Deterministic policy rules evaluate the specific tool name, arguments, and environmental context before invocation [^evt-wg-security-and-privacy-issue-31].
2. **Automated Blocking**: High-confidence dangerous patterns (e.g., unauthorized path traversals, credential exposure) are rejected automatically without human intervention [^evt-wg-security-and-privacy-issue-31] [^evt-wg-security-and-privacy-issue-35].
3. **Targeted Escalation**: Human intervention is reserved strictly for Tier 4 or ambiguous high-impact operations, presenting reviewers with concise contextual diffs and blast-radius summaries [^evt-wg-security-and-privacy-issue-31].

# Lifecycle History

- Baseline pattern established in foundational AAIF workflow blueprints.
- Updated with fatigue mitigation and in-loop hook requirements per `wg-security-and-privacy` issues #31 and #35.

[^evt-wg-security-and-privacy-issue-31]: https://github.com/aaif/wg-security-and-privacy/issues/31
[^evt-wg-security-and-privacy-issue-35]: https://github.com/aaif/wg-security-and-privacy/issues/35
