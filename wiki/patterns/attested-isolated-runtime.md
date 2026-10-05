---
type: pattern
title: Attested Isolated Runtime
description: Hardware-isolated execution pattern placing policy decision points and
  evidence signers in a confidential environment while keeping the agent outside the
  trust boundary.
resource: https://github.com/aaif/wg-security-and-privacy/pull/11
tags:
- security
- privacy
- confidential-computing
- tee
- attestation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:30:48.656779+00:00'
sources:
- id: evt-wg-security-and-privacy-pr-11
  resource: https://github.com/aaif/wg-security-and-privacy/pull/11
  author: imran-siddique
  last_modified: '2026-08-17T19:17:48+00:00'
---

# Overview

The Attested Isolated Runtime is a security design pattern for deployments where the infrastructure operator is inside the threat model[^evt-wg-security-and-privacy-pr-11]. Developed within the [Security and Privacy Working Group](../working-groups/security-and-privacy.md), it isolates the policy enforcement point and evidence signing keys inside a hardware confidential computing boundary while leaving the AI agent outside.

# Architecture / Specification

The pattern defines four core requirements for confidential agent policy enforcement[^evt-wg-security-and-privacy-pr-11]:

1. **Isolate the Enforcement Point, Exclude the Agent:** The policy decision point and evidence signer run in a hardware-isolated environment (such as AMD SEV-SNP, Intel TDX, ARM CCA, NVIDIA GPU confidential computing, or TPM 2.0). The agent execution engine itself remains outside the trusted computing base (TCB) because agent code processes untrusted, attacker-influenced input as normal operation[^evt-wg-security-and-privacy-pr-11].
2. **Internal Key Generation:** Cryptographic signing keys are generated inside the isolated boundary and bound to hardware measurements.
3. **Policy Sealing:** Policy bundles, system prompts, tool schemas, and model weight digests are sealed to cryptographic measurements and released only upon successful appraisal[^evt-wg-security-and-privacy-pr-11].
4. **Independent Verifier Appraisal:** An external, independent verifier appraises per-unit-of-work attestation evidence before sensitive data release (aligned with RFC 9334, RFC 9711, RFC 8747, IETF SCITT, and SLSA)[^evt-wg-security-and-privacy-pr-11].

A software-only emulation mode is specified as a valid deployment for testing, development, and non-confidential hardware environments[^evt-wg-security-and-privacy-pr-11].

# Open Questions

The working group is reviewing three open architectural questions[^evt-wg-security-and-privacy-pr-11]:

- Whether the agent should strictly remain outside the trust boundary or if specialized agent modules belong inside the TCB.
- The exact scope of measured artifacts, specifically how dynamic state like retrieved context and working memory should be managed.
- Establishing a shared assurance vocabulary (signed, attested, transparency-anchored) coordinated with the [Identity and Trust Working Group](../working-groups/identity-and-trust.md).

[^evt-wg-security-and-privacy-pr-11]: https://github.com/aaif/wg-security-and-privacy/pull/11
