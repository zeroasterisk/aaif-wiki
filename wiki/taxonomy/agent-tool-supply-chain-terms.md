---
type: taxonomy
title: Agent Tool Supply Chain Terms
description: Standardized security vocabulary defining tool poisoning, rug pulls,
  manifest verification, and cross-client leakage in agent tool supply chains.
resource: https://github.com/aaif/ws-taxonomy-landscape/pull/88
tags:
- taxonomy
- security
- supply-chain
- tools
- mcp
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:50:17.658922+00:00'
sources:
- id: evt-ws-taxonomy-landscape-pr-88
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/88
  author: GeeksikhSecurity
  last_modified: '2026-09-30T02:07:16+00:00'
---

# Overview
Agent tool supply chain terms define attack vectors, integrity checks, and data exposure risks specific to agent tool definitions and shared execution runtimes[^evt-ws-taxonomy-landscape-pr-88].

The taxonomy is curated across the [Security and Privacy Working Group](../working-groups/security-and-privacy.md), [Identity and Trust Working Group](../working-groups/identity-and-trust.md), and [Governance, Risk and Regulatory Alignment Working Group](../working-groups/governance-risk-and-regulatory.md)[^evt-ws-taxonomy-landscape-pr-88].

# Architecture / Specification
The supply chain terms define distinct operational and threat concepts:
- **Tool Poisoning**: A pre-deployment attack where a tool definition or implementation is maliciously crafted prior to adoption to manipulate agent reasoning or hijack executions[^evt-ws-taxonomy-landscape-pr-88].
- **Rug Pull**: A post-approval attack where a previously trusted or verified tool definition is altered after deployment to introduce malicious capabilities or alter behavior[^evt-ws-taxonomy-landscape-pr-88].
- **Tool Definition Verification**: The deterministic process of validating tool manifests, schemas, and cryptographic signatures prior to agent invocation[^evt-ws-taxonomy-landscape-pr-88].
- **Cross-Client Data Leakage**: The unauthorized exposure or sharing of state, session context, or tool output between distinct client sessions on a shared tool server[^evt-ws-taxonomy-landscape-pr-88].

# Lifecycle History
Proposed under [Taxonomy and Landscape Workstream](../workstreams/taxonomy-and-landscape.md) PR #88 in alignment with MITRE ATLAS and OWASP security classifications[^evt-ws-taxonomy-landscape-pr-88].

[^evt-ws-taxonomy-landscape-pr-88]: https://github.com/aaif/ws-taxonomy-landscape/pull/88
