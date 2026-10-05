---
type: taxonomy
title: Agent Tool Supply Chain Terms
description: Standardized vocabulary classifying agent tool supply-chain risks, definition
  verification, and multi-tenant isolation boundaries.
resource: https://github.com/aaif/ws-taxonomy-landscape/pull/88
tags:
- taxonomy
- security
- supply-chain
- mcp
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:18:07.441771+00:00'
sources:
- id: evt-ws-taxonomy-landscape-pr-88
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/88
  author: GeeksikhSecurity
  last_modified: '2026-09-30T02:07:16+00:00'
---

# Overview

Agent Tool Supply Chain Terms establish a shared, vendor-neutral vocabulary for evaluating security threats, verification procedures, and trust boundaries associated with agent tool ecosystems (such as MCP servers and external tool manifests)[^evt-ws-taxonomy-landscape-pr-88]. These terms differentiate agent-specific supply chain mechanics from general software supply chain concepts across the `../working-groups/security-and-privacy.md`, `../working-groups/governance-risk-and-regulatory.md`, and `../working-groups/identity-and-trust.md` working groups[^evt-ws-taxonomy-landscape-pr-88].

# Architecture / Specification

The taxonomy defines four core domain terms to evaluate tool provenance and runtime exposure[^evt-ws-taxonomy-landscape-pr-88]:

- **Tool Poisoning**: The deliberate manipulation or creation of a tool definition or implementation that is malicious from inception, designed to subvert agent reasoning or exfiltrate data upon invocation[^evt-ws-taxonomy-landscape-pr-88].
- **Rug Pull**: An integrity violation occurring when an initially benign and approved tool definition or implementation is subsequently altered to become malicious after passing initial verification gates[^evt-ws-taxonomy-landscape-pr-88].
- **Tool Definition Verification** (*alias: Tools Manifest Verification*): The systematic process of inspecting, validating, and cryptographically checking a tool's manifest and schema against trusted policies prior to runtime registration or execution[^evt-ws-taxonomy-landscape-pr-88].
- **Cross-Client Data Leakage**: The unauthorized exposure or bridging of state, context, or execution data across multiple distinct client sessions interacting with a shared tool runtime or server[^evt-ws-taxonomy-landscape-pr-88].

# Lifecycle History

Introduced in PR #88 of the Taxonomy and Landscape workstream (`../initiatives/taxonomy-and-landscape.md`) to provide formal terminology aligned with MITRE ATLAS and OWASP MCP security frameworks[^evt-ws-taxonomy-landscape-pr-88].

[^evt-ws-taxonomy-landscape-pr-88]: https://github.com/aaif/ws-taxonomy-landscape/pull/88
