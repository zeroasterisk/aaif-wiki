---
type: standard
title: Control Surfaces for Agentic Harnesses
description: Standardized specification defining administrative harness lifecycle
  events, external authorization checkpoints, policy decision and enforcement points,
  and verifiable containment hooks.
resource: https://github.com/aaif/wg-security-and-privacy/blob/9fdce8acf3b6640e31a08498bcfaa66f53c9c53b/meeting-notes/2026-11-10.md
tags:
- security
- harness
- pdp-pep
- standard
- runtime-governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:36:12.042602+00:00'
sources:
- id: evt-wg-security-and-privacy-file-6623dd4920c0-d9c3520f
  resource: https://github.com/aaif/wg-security-and-privacy/blob/9fdce8acf3b6640e31a08498bcfaa66f53c9c53b/meeting-notes/2026-11-10.md
  author: Alex Frazer
  last_modified: '2026-11-16T11:50:26-05:00'
---

# Overview

Control Surfaces for Agentic Harnesses is a standard specification initiated within the [Security and Privacy Working Group](../working-groups/security-and-privacy.md) to define predictable, standardized interfaces for execution control and policy interception in agent harnesses such as Claude Code and Cursor.[^evt-wg-security-and-privacy-file-6623dd4920c0-d9c3520f] Because diverse harness implementations currently expose ad hoc hooks, this standard provides common contract expectations for operators and tool builders.[^evt-wg-security-and-privacy-file-6623dd4920c0-d9c3520f]

# Architecture / Specification

The specification standardizes how an external Policy Enforcement Point (PEP) and Policy Decision Point (PDP) integrate across agent execution environments.[^evt-wg-security-and-privacy-file-6623dd4920c0-d9c3520f] It defines lifecycle interception hooks across four primary operational surfaces:[^evt-wg-security-and-privacy-file-6623dd4920c0-d9c3520f]

1. **Agent Harness Environment**: Pre-execution, turn-level, and tool-dispatch interception hooks controlling the local agent loop.[^evt-wg-security-and-privacy-file-6623dd4920c0-d9c3520f]
2. **Gateway Interceptors**: Ingress and egress traffic policy enforcement handling protocol mediation (such as Model Context Protocol calls).[^evt-wg-security-and-privacy-file-6623dd4920c0-d9c3520f]
3. **Identity and Access Layer**: Authorization context validation and token delegation checkpoints (aligned with AuthZEN and related standards).[^evt-wg-security-and-privacy-file-6623dd4920c0-d9c3520f]
4. **Execution Sandboxes**: Kernel-level or containerized isolation boundaries enforcing system resource and capability boundaries.[^evt-wg-security-and-privacy-file-6623dd4920c0-d9c3520f]

### Verifiable Conformance

The specification targets machine-verifiable compliance testing, allowing conforming harnesses to validate hook contracts and earn standardized trust badges demonstrating compatibility with external policy engines.[^evt-wg-security-and-privacy-file-6623dd4920c0-d9c3520f]

# Lifecycle History

- **2026-11**: Introduced by Alex Frazer in the Security and Privacy Working Group under PR #45, synthesizing threat modeling, design pattern deliverables, and runtime policy requirements.[^evt-wg-security-and-privacy-file-6623dd4920c0-d9c3520f]

[^evt-wg-security-and-privacy-file-6623dd4920c0-d9c3520f]: https://github.com/aaif/wg-security-and-privacy/blob/9fdce8acf3b6640e31a08498bcfaa66f53c9c53b/meeting-notes/2026-11-10.md
