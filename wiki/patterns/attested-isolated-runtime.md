---
type: pattern
title: Attested Isolated Runtime
description: Security design pattern isolating policy enforcement and evidence signing
  inside a hardware TEE while keeping dynamic agent execution outside the trust boundary.
resource: https://github.com/aaif/wg-security-and-privacy/pull/11
tags:
- security
- privacy
- tee
- attestation
- patterns
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T09:53:13.218027+00:00'
sources:
- id: evt-wg-security-and-privacy-pr-11
  resource: https://github.com/aaif/wg-security-and-privacy/pull/11
  author: imran-siddique
  last_modified: '2026-08-17T19:17:48+00:00'
---

# Overview

The Attested Isolated Runtime is a security design pattern for agentic deployments where infrastructure operators sit within the threat model [^evt-wg-security-and-privacy-pr-11]. The pattern separates policy enforcement and cryptographic evidence generation from dynamic agent execution by placing the Policy Decision Point (PDP) and evidence signer inside a hardware-isolated Trusted Execution Environment (TEE), while keeping agent runtime code outside the trusted computing base [^evt-wg-security-and-privacy-pr-11].

By ensuring that data release and tool execution are gated on independent verifier appraisal of cryptographic measurements, the pattern restricts unauthorized infrastructure manipulation without expanding the trusted boundary to untrusted agent inputs [^evt-wg-security-and-privacy-pr-11].

# Architecture / Specification

## Core Requirements

The pattern defines four structural elements [^evt-wg-security-and-privacy-pr-11]:
1. **External Agent Placement**: The agent engine remains outside the hardware-isolated boundary because agent code executes attacker-influenced inputs, avoiding unnecessary expansion of the trusted computing base.
2. **Internal Key Generation**: The evidence-signing key is generated strictly inside the isolated boundary and bound directly to runtime measurements.
3. **Policy Sealing**: Policy bundles, tool schemas, model weight digests, and system prompts are sealed to the hardware measurement and unlocked only upon verified appraisal.
4. **Independent Verifier Appraisal**: Evidence per unit of work is appraised by an independent relying-party verifier (aligned with RFC 9334 RATS architecture).

## Implementation Spectrum and Limits

- **Hardware & Standards Neutrality**: Designed to work across AMD SEV-SNP, Intel TDX, ARM CCA, NVIDIA GPU confidential computing, and TPM 2.0 architectures, alongside RFC 9334, RFC 9711, RFC 8747, and IETF SCITT standards [^evt-wg-security-and-privacy-pr-11].
- **Software-Only Emulation**: Supports software-only execution modes for local development, continuous integration, and non-confidential environments [^evt-wg-security-and-privacy-pr-11].
- **Explicit Limitations**: The pattern does not prevent prompt injection, algorithmic bias, or side-channel leakage; it isolates enforcement and verification mechanics from operator compromise [^evt-wg-security-and-privacy-pr-11].

# References

- [Security and Privacy Working Group](../working-groups/security-and-privacy.md)
- [SP Design Patterns Workstream](../working-groups/sp-design-patterns.md)
- [Identity and Trust Working Group](../working-groups/identity-and-trust.md)

[^evt-wg-security-and-privacy-pr-11]: https://github.com/aaif/wg-security-and-privacy/pull/11
