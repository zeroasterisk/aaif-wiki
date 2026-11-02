---
type: taxonomy
title: Rug Pull
description: Agent tool supply-chain attack where a previously verified tool definition,
  package, or endpoint is silently replaced with malicious behavior.
resource: https://github.com/aaif/wg-security-and-privacy/pull/40
tags:
- taxonomy
- security
- supply-chain
- tools
- mitre-atlas
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:24:44.279360+00:00'
sources:
- id: evt-wg-security-and-privacy-pr-40
  resource: https://github.com/aaif/wg-security-and-privacy/pull/40
  author: barka-bee
  last_modified: '2026-10-12T12:41:45+00:00'
---

# Overview
A rug pull is an agentic supply-chain attack in which a previously verified, benign, or trusted tool definition, Model Context Protocol (MCP) package, or external API endpoint is silently modified or replaced with malicious logic post-admission.[^evt-wg-security-and-privacy-pr-40] This threat exploits static or one-time [tool definition verification](../taxonomy/tool-definition-verification.md) by altering runtime behavior while retaining established trust tokens or namespace identifiers.[^evt-wg-security-and-privacy-pr-40]

The attack is formally recognized in the [Security and Privacy Working Group](../working-groups/security-and-privacy.md) best practices guide and mapped to the MITRE ATLAS matrix under technique AML.T0109 (*AI Supply Chain Rug Pull*).[^evt-wg-security-and-privacy-pr-40]

# Architecture / Specification

## Attack Vectors and Mechanics
Rug pull attacks across agent ecosystems typically manifest across three primary surfaces:[^evt-wg-security-and-privacy-pr-40]
- **Tool Definition Hash Drift**: The registered schema or manifest of a tool changes on the remote host without incrementing version identifiers or triggering re-attestation.[^evt-wg-security-and-privacy-pr-40]
- **Silent Package Updates**: Dependencies, plugins, or MCP server packages introduce unauthorized capabilities or altered tool behaviors during downstream updates.[^evt-wg-security-and-privacy-pr-40]
- **Dynamic Endpoint Redirection**: An agent tool's underlying routing configuration is redirected to an attacker-controlled endpoint that mimics the schema but captures sensitive execution context or delivers manipulated responses.[^evt-wg-security-and-privacy-pr-40]

## Mitigations and Mapping
Mitigating rug pulls requires continuous verification of execution invariants rather than relying on one-time registration approvals:[^evt-wg-security-and-privacy-pr-40]
- **Cryptographic Hash Invariants**: Binding tool definitions to immutable cryptographic digests and rejecting runtime executions where hash drift is observed.[^evt-wg-security-and-privacy-pr-40]
- **In-Hook Policy Enforcement**: Intercepting invocations via policy decision points to verify runtime signatures and destination allowlists prior to execution.[^evt-wg-security-and-privacy-pr-40]
- **Framework Alignment**: Categorized under MITRE ATLAS v5.6.0 as technique AML.T0109 (*AI Supply Chain Rug Pull*), and classified under OWASP Top 10 for Agentic Applications (ASI) supply-chain risk categories.[^evt-wg-security-and-privacy-pr-40]

# Lifecycle History
Defined within the AAIF threat modeling and taxonomy landscape initiatives, the term was formally linked to MITRE ATLAS technique AML.T0109 during the 2026 update to the [Agentic AI Security Best Practices](../guidelines/agentic-ai-security-best-practices.md) guide.[^evt-wg-security-and-privacy-pr-40]

[^evt-wg-security-and-privacy-pr-40]: https://github.com/aaif/wg-security-and-privacy/pull/40
