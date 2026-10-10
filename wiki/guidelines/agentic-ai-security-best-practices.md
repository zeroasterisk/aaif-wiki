---
type: guideline
title: Agentic AI Security Best Practices
description: Technical guidance consolidating practical security controls across secrets
  elimination, in-loop policy enforcement, and pre-execution interception hooks for
  AI agents.
resource: https://github.com/aaif/wg-security-and-privacy/issues/31
tags:
- security
- best-practices
- guardrails
- authorization
- hooks
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:24:45.883098+00:00'
sources:
- id: evt-wg-security-and-privacy-issue-31
  resource: https://github.com/aaif/wg-security-and-privacy/issues/31
  author: barka-bee
  last_modified: '2026-10-10T01:10:12+00:00'
---

# Overview

The Agentic AI Security Best Practices guide establishes actionable defensive patterns and guardrails for deploying autonomous agents in production environments [^evt-wg-security-and-privacy-issue-31]. It outlines controls to prevent unauthorized resource access, eliminate direct tool-level secret exposure, and enforce deterministic policy boundaries around model operations.

The guidance is curated by the [Security and Privacy Working Group](../working-groups/security-and-privacy.md) to provide practical security architectures for enterprise agent integration.

# Architecture / Specification

### Pre-Execution Interception Hooks and Authorization Tiers

To prevent authorization bypasses and mitigate human approval fatigue, authorization controls should be structured around pre-execution hooks rather than purely static design-time categories [^evt-wg-security-and-privacy-issue-31]:
- **Pre-Execution Interception**: Every agent tool invocation is intercepted by deterministic code before execution. The policy engine evaluates the request to produce an explicit outcome: `allow`, `deny`, `modify`, or `ask` [^evt-wg-security-and-privacy-issue-31].
- **Context and Argument-Aware Classification**: Tier assignments are dynamically evaluated using the concrete tool call, runtime arguments, and operational context (e.g., distinguishing read queries from destructive SQL updates) [^evt-wg-security-and-privacy-issue-31].
- **Layered Decision Escalation**: Deterministic rule sets evaluate invocations first, handing off to LLM judges only when rules do not resolve, and reserving human-in-the-loop approval workflows specifically for the `ask` pathway [^evt-wg-security-and-privacy-issue-31].

### Core Security Controls

1. **Credential Isolation**: Elimination of plaintext credentials from agent context windows via secure vaults and proxy brokers.
2. **Runtime Policy Enforcement**: Enforcing boundaries via sandboxed environments and strict network allowlists [^evt-wg-security-and-privacy-issue-31].
3. **Auditability and Attribution**: Generating tamper-evident logs for all tool dispatches and authorization decisions.

# Lifecycle History

- Proposals introduced to refine Section 4 authorization controls into pre-execution interception hooks keyed on runtime arguments and context [^evt-wg-security-and-privacy-issue-31].

[^evt-wg-security-and-privacy-issue-31]: https://github.com/aaif/wg-security-and-privacy/issues/31
