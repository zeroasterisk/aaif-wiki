---
type: guideline
title: Agentic AI Security Best Practices Guide
description: Implementation guide establishing architectural controls for secrets
  management, workload identity, secure tool invocation, and MCP threat mitigation.
resource: https://github.com/aaif/wg-security-and-privacy/blob/f9fc39165fb5d8eb088f9efec10912f30a5672c9/deliverables/DRAFT-agentic-ai-security-best-practices-guide.md
tags:
- security
- guidelines
- mcp
- secrets-management
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:33:45.576359+00:00'
sources:
- id: evt-wg-security-and-privacy-file-b8b8567533b6-eaf41d99
  resource: https://github.com/aaif/wg-security-and-privacy/blob/f9fc39165fb5d8eb088f9efec10912f30a5672c9/deliverables/DRAFT-agentic-ai-security-best-practices-guide.md
  author: Imran Siddique
  last_modified: '2026-11-07T16:48:53+05:30'
- id: evt-wg-security-and-privacy-pr-49
  resource: https://github.com/aaif/wg-security-and-privacy/pull/49
  author: mrappard
  last_modified: '2026-11-08T18:42:20+00:00'
---

# Overview

The Agentic AI Security Best Practices Guide, curated by the Security and Privacy Working Group, defines operational and architectural controls for production agent deployments [^evt-wg-security-and-privacy-file-b8b8567533b6-eaf41d99]. It addresses five core functional areas: secrets management, secure tool invocation, guardrails, evaluation frameworks, and post-incident forensics [^evt-wg-security-and-privacy-file-b8b8567533b6-eaf41d99]. Delegated identity architectures (such as SPIFFE/SVID and UCANs) are coordinated with the Identity and Trust Working Group and surfaced via the [Cross-WG Security and Privacy Review Checklist](../guidelines/cross-wg-security-review-checklist.md) [^evt-wg-security-and-privacy-file-b8b8567533b6-eaf41d99].

# Architecture / Specification

### Secrets Management

Static and long-lived credentials in agent environments present persistent extraction vectors via prompt injection or deserialization exploits (e.g., CVE-2025-68664) [^evt-wg-security-and-privacy-file-b8b8567533b6-eaf41d99]. The guide mandates transitioning from stored static assets to ephemeral attestations across a hierarchy of patterns [^evt-wg-security-and-privacy-file-b8b8567533b6-eaf41d99]:

1. **Workload Identity:** Primary baseline utilizing cloud OIDC attestation (IRSA, GCP Workload Identity, Azure Managed Identity) to supply 1-hour credentials [^evt-wg-security-and-privacy-file-b8b8567533b6-eaf41d99].
2. **Dynamic Secrets:** On-demand short-lived credentials via tools like HashiCorp Vault for third-party databases and APIs [^evt-wg-security-and-privacy-file-b8b8567533b6-eaf41d99].
3. **Network-Layer Injection:** Sidecar proxies handling credential attachment out-of-band for legacy systems [^evt-wg-security-and-privacy-file-b8b8567533b6-eaf41d99].
4. **Confidential Computing:** Hardware memory encryption (Intel TDX, AMD SEV-SNP) for high-sensitivity regulatory or multi-tenant agent workloads, bound to short-lived token lifetimes [^evt-wg-security-and-privacy-file-b8b8567533b6-eaf41d99].
5. **OAuth Token Exchange (RFC 8693):** Downstream token scope narrowing per delegation hop [^evt-wg-security-and-privacy-file-b8b8567533b6-eaf41d99].

### Secure Tool Invocation and MCP Security

The guide highlights vulnerability patterns in Model Context Protocol (MCP) ecosystems, including tool description poisoning (Unicode tag injection), server rug pulls, cross-server shadowing, and sampling abuse [^evt-wg-security-and-privacy-file-b8b8567533b6-eaf41d99]. Mitigations include mandatory pre-deployment static scanning, public advisory cross-referencing, enforcement of OAuth 2.1 with PKCE and RFC 8707 audience binding on HTTP transports, and sandboxing local stdio executions [^evt-wg-security-and-privacy-file-b8b8567533b6-eaf41d99]. Proposals also investigate C2PA Content Credentials to verify publisher provenance across agent skills [^evt-wg-security-and-privacy-pr-49].

[^evt-wg-security-and-privacy-file-b8b8567533b6-eaf41d99]: https://github.com/aaif/wg-security-and-privacy/blob/f9fc39165fb5d8eb088f9efec10912f30a5672c9/deliverables/DRAFT-agentic-ai-security-best-practices-guide.md
[^evt-wg-security-and-privacy-pr-49]: https://github.com/aaif/wg-security-and-privacy/pull/49
