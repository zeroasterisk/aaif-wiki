---
type: guideline
title: Agentic AI Security Best Practices
description: Operational security guidelines structuring runtime sandbox boundaries,
  tool egress controls, pre-execution hook policy enforcement, and multi-tier authorization
  gates.
resource: https://github.com/aaif/wg-security-and-privacy/pull/38
tags:
- security
- best-practices
- sandboxing
- policy-decision-point
- mitre-atlas
- owasp-asi
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T11:10:42.748405+00:00'
sources:
- id: evt-wg-security-and-privacy-pr-38
  resource: https://github.com/aaif/wg-security-and-privacy/pull/38
  author: barka-bee
  last_modified: '2026-10-12T11:44:58+00:00'
- id: evt-wg-security-and-privacy-pr-39
  resource: https://github.com/aaif/wg-security-and-privacy/pull/39
  author: barka-bee
  last_modified: '2026-10-12T12:30:29+00:00'
- id: evt-wg-security-and-privacy-pr-40
  resource: https://github.com/aaif/wg-security-and-privacy/pull/40
  author: barka-bee
  last_modified: '2026-10-12T12:41:45+00:00'
- id: evt-wg-security-and-privacy-pr-41
  resource: https://github.com/aaif/wg-security-and-privacy/pull/41
  author: barka-bee
  last_modified: '2026-10-12T12:51:05+00:00'
---

# Overview
The Agentic AI Security Best Practices guideline defines defensive design criteria, execution containment models, and authorization standards for deploying autonomous agents safely across development and enterprise environments. It provides operational principles for sandboxing, pre-execution runtime hooks, traffic checkpointing, and taxonomy-mapped threat mitigations.

# Architecture / Specification
The guideline establishes layered controls across runtime execution, authorization, network boundaries, and threat taxonomies:

## Hook-Based Policy Decision Point
Runtime policy enforcement intercepts execution via lifecycle hooks where the agent host suspends pending calls and submits the tool name, arguments, and full session context to an external Policy Decision Point (PDP).[^evt-wg-security-and-privacy-pr-38] Decisions follow three sequential stages:[^evt-wg-security-and-privacy-pr-39]
1. **Deterministic Rules Engine**: Imposes non-negotiable static constraints and baseline invariants before any secondary model evaluation.
2. **Contextual Evaluation**: Routes non-trivial calls handed off by the deterministic rules to secondary classifiers, specialized evaluators, or isolated policy agents.
3. **Human Review Gate**: Escalates strictly when an `ask` verdict is rendered, directly counteracting human approval fatigue observed in production environments where passive oversight leads to approving routine actions without scrutiny.[^evt-wg-security-and-privacy-pr-39]

The executing agent has no structural mechanism to influence or bypass any stage of the policy pipeline.[^evt-wg-security-and-privacy-pr-39]

## Gateway Checkpoints and Traffic Controls
Complementing local hook controls, Model Context Protocol (MCP) gateways such as [AgentGateway](../resources/agentgateway.md) operate as network-path checkpoints.[^evt-wg-security-and-privacy-pr-38] Gateways aggregate connections to remote MCP servers, handle OAuth authentication, enforce per-tool network permissions, and log tamper-evident payload events for downstream auditing.[^evt-wg-security-and-privacy-pr-38]

## Sandbox Confinement and Egress Limitations
Execution sandboxing is categorized as narrowing the blast radius from the full user account to the working directory rather than achieving total operational containment.[^evt-wg-security-and-privacy-pr-41] Unless backed by kernel-level isolation (including namespaces, filesystem confinement, and system call filtering), sandboxes do not inherently block outbound network egress or prevent handoff attacks executed via host components.[^evt-wg-security-and-privacy-pr-41] Proxy allowlists must govern outbound connectivity, and artifact verification remains mandatory even within sandboxed environments.[^evt-wg-security-and-privacy-pr-41]

## External Threat Harmonization
Defensive clauses across the guideline are mapped to MITRE ATLAS v5.6.0 techniques (including AML.T0109 for supply chain rug pulls, AML.T0110, and AML.T0051.001) and OWASP Top 10 for Agentic Applications categories (such as ASI02 and ASI04).[^evt-wg-security-and-privacy-pr-40]

# References
- Deliverable updates in aaif/wg-security-and-privacy: https://github.com/aaif/wg-security-and-privacy/pull/38 [^evt-wg-security-and-privacy-pr-38]
- Policy decision point specification: https://github.com/aaif/wg-security-and-privacy/pull/39 [^evt-wg-security-and-privacy-pr-39]
- ATLAS v5.6.0 and OWASP ASI cross-referencing: https://github.com/aaif/wg-security-and-privacy/pull/40 [^evt-wg-security-and-privacy-pr-40]
- Sandbox boundary definitions: https://github.com/aaif/wg-security-and-privacy/pull/41 [^evt-wg-security-and-privacy-pr-41]

[^evt-wg-security-and-privacy-pr-38]: https://github.com/aaif/wg-security-and-privacy/pull/38
[^evt-wg-security-and-privacy-pr-39]: https://github.com/aaif/wg-security-and-privacy/pull/39
[^evt-wg-security-and-privacy-pr-40]: https://github.com/aaif/wg-security-and-privacy/pull/40
[^evt-wg-security-and-privacy-pr-41]: https://github.com/aaif/wg-security-and-privacy/pull/41
