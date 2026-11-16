---
type: guideline
title: Agentic AI Security Best Practices
description: Practical builder guidance covering secrets management, context redaction,
  host sandboxing, and runtime tool invocation controls for agentic deployments.
resource: https://github.com/aaif/wg-security-and-privacy/blob/f9fc39165fb5d8eb088f9efec10912f30a5672c9/deliverables/DRAFT-agentic-ai-security-best-practices-guide.md
tags:
- security
- best-practices
- secrets-management
- mcp
- confidential-computing
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:43:19.607440+00:00'
sources:
- id: evt-wg-security-and-privacy-file-b8b8567533b6-eaf41d99
  resource: https://github.com/aaif/wg-security-and-privacy/blob/f9fc39165fb5d8eb088f9efec10912f30a5672c9/deliverables/DRAFT-agentic-ai-security-best-practices-guide.md
  author: Imran Siddique
  last_modified: '2026-11-07T16:48:53+05:30'
---

# Overview
The Agentic AI Security Best Practices Guide establishes implementable controls for builders deploying production agentic systems across secrets management, secure tool invocation, guardrails, evaluation frameworks, and post-incident forensics.[^evt-wg-security-and-privacy-file-b8b8567533b6-eaf41d99] The guideline focuses on blast-radius minimization and operational hardening, while delegating comprehensive identity delegation and SPIFFE/SVID workload attestation architectures to the [Identity and Trust Working Group](../working-groups/identity-and-trust.md).[^evt-wg-security-and-privacy-file-b8b8567533b6-eaf41d99]

# Architecture / Specification

## Secrets Management: Ephemeral Attestation Hierarchy
Static, long-lived credentials and environment-variable secrets present durable attack surfaces vulnerable to prompt injection, deserialization leaks, and lateral movement.[^evt-wg-security-and-privacy-file-b8b8567533b6-eaf41d99] The guide establishes five progressive secrets management patterns in adoption priority order:[^evt-wg-security-and-privacy-file-b8b8567533b6-eaf41d99]
1. **Workload Identity:** Native platform attestation (AWS IRSA, GCP Workload Identity, Azure Managed Identity) exchanging cluster OIDC tokens for short-lived credentials without storing ambient secrets in container environments.[^evt-wg-security-and-privacy-file-b8b8567533b6-eaf41d99]
2. **Dynamic Secrets:** Ephemeral credentials issued on demand by secrets management engines (e.g., HashiCorp Vault) with granular time-to-live expiration.[^evt-wg-security-and-privacy-file-b8b8567533b6-eaf41d99]
3. **Network-Layer Injection:** Sidecars or proxy gateways attaching credentials to upstream calls out-of-band so agent processes never observe or serialize secret material.[^evt-wg-security-and-privacy-file-b8b8567533b6-eaf41d99]
4. **Confidential Computing:** Hardware enclaves (Intel TDX, AMD SEV-SNP) providing VM-level isolation for high-sensitivity multi-tenant contexts, which must still be combined with short token lifetimes because guest software remains inside the trusted computing base.[^evt-wg-security-and-privacy-file-b8b8567533b6-eaf41d99]
5. **OAuth Token Exchange (RFC 8693):** Cryptographic scope narrowing applied across each hop of multi-agent delegation chains.[^evt-wg-security-and-privacy-file-b8b8567533b6-eaf41d99]

## Secure Tool Invocation and MCP Hardening
Model Context Protocol (MCP) deployments face structural security risks because OAuth 2.1 authentication is optional in the specification and stdio transport is exempt by default, creating exposure to tool poisoning, rug pulls, and cross-server shadowing.[^evt-wg-security-and-privacy-file-b8b8567533b6-eaf41d99] Essential controls include:
- **Pre-Deployment Static Scanning:** Auditing source activity, checking public vulnerability registries, and executing static analysis before establishing server connections.[^evt-wg-security-and-privacy-file-b8b8567533b6-eaf41d99]
- **Transport Isolation:** Treating third-party stdio servers as untrusted local binaries executing with full user privileges, while requiring OAuth 2.1 with PKCE and RFC 8707 audience-bound resource indicators across remote HTTP transports.[^evt-wg-security-and-privacy-file-b8b8567533b6-eaf41d99]

# References
- Security & Privacy Working Group: Deliverable 4 (Agentic AI Security Best Practices Guide).[^evt-wg-security-and-privacy-file-b8b8567533b6-eaf41d99]

[^evt-wg-security-and-privacy-file-b8b8567533b6-eaf41d99]: https://github.com/aaif/wg-security-and-privacy/blob/f9fc39165fb5d8eb088f9efec10912f30a5672c9/deliverables/DRAFT-agentic-ai-security-best-practices-guide.md
