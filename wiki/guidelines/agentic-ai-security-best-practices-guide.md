---
type: guideline
title: Agentic AI Security Best Practices Guide
description: Comprehensive security baseline establishing in-loop hook controls, context
  redaction, sandbox boundary limits, and MITRE ATLAS/OWASP ASI threat alignments.
resource: https://github.com/aaif/wg-security-and-privacy/issues/30
tags:
- security
- best-practices
- authorization
- mitre-atlas
- owasp-asi
- sandboxing
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:27:40.495878+00:00'
sources:
- id: evt-wg-security-and-privacy-issue-30
  resource: https://github.com/aaif/wg-security-and-privacy/issues/30
  author: barka-bee
  last_modified: '2026-10-05T07:57:28+00:00'
- id: evt-wg-security-and-privacy-issue-31
  resource: https://github.com/aaif/wg-security-and-privacy/issues/31
  author: barka-bee
  last_modified: '2026-10-05T07:57:29+00:00'
- id: evt-wg-security-and-privacy-issue-32
  resource: https://github.com/aaif/wg-security-and-privacy/issues/32
  author: barka-bee
  last_modified: '2026-10-05T07:57:31+00:00'
- id: evt-wg-security-and-privacy-issue-33
  resource: https://github.com/aaif/wg-security-and-privacy/issues/33
  author: barka-bee
  last_modified: '2026-10-05T07:57:32+00:00'
- id: evt-wg-security-and-privacy-issue-34
  resource: https://github.com/aaif/wg-security-and-privacy/issues/34
  author: barka-bee
  last_modified: '2026-10-05T07:57:33+00:00'
- id: evt-wg-security-and-privacy-issue-35
  resource: https://github.com/aaif/wg-security-and-privacy/issues/35
  author: barka-bee
  last_modified: '2026-10-05T07:57:34+00:00'
---

# Overview

The Agentic AI Security Best Practices Guide establishes architectural controls and operational baselines for securing agentic systems across the agent execution lifecycle. Developed by the [Security and Privacy Working Group](../working-groups/security-and-privacy.md), the guide provides practical controls covering credential management, tool execution interception, sandboxing boundaries, tiered human authorization, and threat model mapping.

# Architecture / Specification

## In-Loop Enforcement and Pre-Execution Hooks
While network gateways serve as ingress/egress checkpoints and payload logging hubs for remote MCP servers, authoritative tool enforcement operates via pre-execution hooks directly within the agent loop [^evt-wg-security-and-privacy-issue-30]. In-loop hooks intercept all tool executions regardless of transport—including stdio MCP servers, direct shell executions, SDK invocations, and framework connectors—evaluating context-aware policies against full prompt context before execution [^evt-wg-security-and-privacy-issue-30].

## Tiered Authorization and Approval Fatigue Controls
Authorization tiers evaluate concrete execution calls (tool, arguments, and execution context) rather than broad static operation types [^evt-wg-security-and-privacy-issue-31]. To counter approval fatigue—where repetitive human prompts yield rubber-stamping approval rates above 90%—authorization workflows enforce automated deterministic rules first, hand off to secondary judges where applicable, and reserve the [Human Approval Gate](../patterns/human-approval-gate.md) solely for escalated high-risk requests [^evt-wg-security-and-privacy-issue-31] [^evt-wg-security-and-privacy-issue-35].

## Secret Management and Context Redaction
Secret protection spans agent configuration files (e.g., committed `.mcp.json` environment blocks and skill packages), host environment credentials (such as SSH keys and cloud tokens vulnerable to sandbox escapes), and runtime context flows [^evt-wg-security-and-privacy-issue-33]. Systems must redact sensitive tokens from tool outputs before re-entering agent context, memory stores, and telemetry streams to avoid memory-based privilege retention [^evt-wg-security-and-privacy-issue-33].

## Sandboxing Scope and Egress Containment
Filesystem sandboxing reduces local file alteration scope to designated working directories but does not eliminate network egress risks or indirect execution via unverified host artifacts [^evt-wg-security-and-privacy-issue-34]. Sandboxing controls must be paired with hook-level path denials, short-lived credentials, and strict network egress policies [^evt-wg-security-and-privacy-issue-33] [^evt-wg-security-and-privacy-issue-34].

## Threat Mapping Alignment
Controls map directly to MITRE ATLAS v5.6.0 techniques (including AML.T0110 Tool Poisoning, AML.T0086 Exfiltration, and AML.T0055 Unsecured Credentials) and OWASP Top 10 for Agentic Applications 2026 classifications (ASI01 through ASI10) [^evt-wg-security-and-privacy-issue-32].

# Lifecycle History

- Deliverable initiated under PR #9 in `aaif/wg-security-and-privacy`.
- Refined via WG issues #30 through #35 addressing in-loop enforcement, authorization hook architectures, secret redaction, and threat classification alignments.

[^evt-wg-security-and-privacy-issue-30]: https://github.com/aaif/wg-security-and-privacy/issues/30
[^evt-wg-security-and-privacy-issue-31]: https://github.com/aaif/wg-security-and-privacy/issues/31
[^evt-wg-security-and-privacy-issue-32]: https://github.com/aaif/wg-security-and-privacy/issues/32
[^evt-wg-security-and-privacy-issue-33]: https://github.com/aaif/wg-security-and-privacy/issues/33
[^evt-wg-security-and-privacy-issue-34]: https://github.com/aaif/wg-security-and-privacy/issues/34
[^evt-wg-security-and-privacy-issue-35]: https://github.com/aaif/wg-security-and-privacy/issues/35
