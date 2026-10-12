---
type: guideline
title: Agentic AI Security Best Practices Guide
description: Operational security guidelines, threat taxonomy mappings, and runtime
  defense architectures defining security baselines for agent deployments.
resource: https://github.com/aaif/wg-security-and-privacy/issues/30
tags:
- security
- best-practices
- threat-modeling
- runtime-protection
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T03:16:55.654115+00:00'
sources:
- id: evt-wg-security-and-privacy-issue-30
  resource: https://github.com/aaif/wg-security-and-privacy/issues/30
  author: barka-bee
  last_modified: '2026-10-05T13:51:53+00:00'
- id: evt-wg-security-and-privacy-issue-32
  resource: https://github.com/aaif/wg-security-and-privacy/issues/32
  author: barka-bee
  last_modified: '2026-10-05T13:57:03+00:00'
- id: evt-wg-security-and-privacy-issue-34
  resource: https://github.com/aaif/wg-security-and-privacy/issues/34
  author: barka-bee
  last_modified: '2026-10-05T17:42:01+00:00'
- id: evt-wg-security-and-privacy-issue-37
  resource: https://github.com/aaif/wg-security-and-privacy/issues/37
  author: imran-siddique
  last_modified: '2026-10-05T15:26:00+00:00'
---

# Overview
The Agentic AI Security Best Practices Guide establishes architectural controls, runtime invariants, and defense-in-depth requirements for securing autonomous agents and tool-use environments. Developed under the [Security and Privacy Working Group](../working-groups/security-and-privacy.md), the guide specifies defensive baselines spanning credential management, tool sandboxing, gateway routing, and in-loop execution governance.

# Architecture / Specification

## In-Loop Hooks vs. Gateway Enforcement
While centralized network checkpoints (such as Model Context Protocol gateways) facilitate payload capture and remote authentication, active working group discussions emphasize that comprehensive policy enforcement belongs at an in-loop hook within the agent execution loop [^evt-wg-security-and-privacy-issue-30]. Network gateways only observe remote traffic; they miss local stdio transport servers, framework-level connectors, direct SDK calls, and shell commands, and lack the user prompt context needed to evaluate policy [^evt-wg-security-and-privacy-issue-30]. Under this model, runtime policy-as-code must be evaluated at the in-loop hook, with network gateways functioning as telemetry relays and perimeter authentication checkpoints rather than the primary enforcement layer [^evt-wg-security-and-privacy-issue-30].

## Sandbox Blast Radius and Containment Limits
Execution sandboxing for agent tools restricts filesystem access to working-directory scope, but working group reviews emphasize that it does not inherently eliminate blast radius [^evt-wg-security-and-privacy-issue-34]. Sandboxed agents can bypass egress blocks by invoking high-level network utilities (such as Python urllib) or write poisoned files into shared project workspaces that unsandboxed host tools subsequently execute [^evt-wg-security-and-privacy-issue-34]. Comprehensive isolation requires addressing host trust handoffs and egress controls alongside filesystem restrictions [^evt-wg-security-and-privacy-issue-34].

## Confidential Computing and Credential Lifecycles
Within [Attested Isolated Runtimes](../patterns/attested-isolated-runtime.md), hardware enclaves isolate guest memory from host and hypervisor inspection [^evt-wg-security-and-privacy-issue-37]. However, hardware isolation does not truncate credential exposure windows if guest software leaks a bearer token [^evt-wg-security-and-privacy-issue-37]. Confidential computing deployments must therefore combine hardware isolation with short-lived, minimally scoped tokens and strict controls on which guest components may access them [^evt-wg-security-and-privacy-issue-37].

## Threat Taxonomy Alignment
The guide maps defensive requirements against standard industry taxonomies, including MITRE ATLAS (v5.6.0) and the OWASP Top 10 for Agentic Applications (ASI) [^evt-wg-security-and-privacy-issue-32]:
- **Tool Poisoning and Supply Chain**: AI Agent Tool Poisoning (AML.T0110) and Indirect Prompt Injection (AML.T0051.001) map to ASI02 and ASI04 [^evt-wg-security-and-privacy-issue-32].
- **Credential Access**: Unsecured Credentials (AML.T0055) and Agent Configuration Harvesting (AML.T0083) map to ASI03 [^evt-wg-security-and-privacy-issue-32].
- **Exfiltration and Context Poisoning**: Tool Invocation Exfiltration (AML.T0086) and Context/Memory Poisoning (AML.T0080.000) map to ASI01, ASI06, and ASI10 [^evt-wg-security-and-privacy-issue-32].

# Lifecycle History
The guide was developed by the Security and Privacy Working Group. Ongoing issues #30, #32, #34, and #37 track open refinements addressing in-loop enforcement hooks, sandbox containment limits, confidential computing exposure models, and formal ATLAS/ASI threat taxonomy tagging.

[^evt-wg-security-and-privacy-issue-30]: https://github.com/aaif/wg-security-and-privacy/issues/30
[^evt-wg-security-and-privacy-issue-32]: https://github.com/aaif/wg-security-and-privacy/issues/32
[^evt-wg-security-and-privacy-issue-34]: https://github.com/aaif/wg-security-and-privacy/issues/34
[^evt-wg-security-and-privacy-issue-37]: https://github.com/aaif/wg-security-and-privacy/issues/37
