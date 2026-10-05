---
type: pattern
title: Attested Isolated Runtime
description: Hardware-isolated policy enforcement and evidence signing pattern gating
  agent data release on independent verifier appraisal.
resource: https://github.com/aaif/wg-security-and-privacy/pull/11
tags:
- security
- patterns
- confidential-computing
- tee
- attestation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T09:57:19.945291+00:00'
sources:
- id: evt-wg-security-and-privacy-pr-11
  resource: https://github.com/aaif/wg-security-and-privacy/pull/11
  author: imran-siddique
  last_modified: '2026-08-17T19:17:48+00:00'
---

# Overview
The Attested Isolated Runtime is a design pattern developed within the [Security and Privacy Working Group](../working-groups/security-and-privacy.md) for agentic AI deployments where the infrastructure operator is considered part of the threat model[^evt-wg-security-and-privacy-pr-11]. It isolates the Policy Decision Point (PDP) and evidence signer inside a hardware-isolated environment (such as a Trusted Execution Environment or TEE) while keeping agent workload execution outside the boundary to avoid enlarging the Trusted Computing Base (TCB)[^evt-wg-security-and-privacy-pr-11].

# Architecture / Specification
The pattern defines four mandatory elements necessary to maintain policy integrity and verifiable execution[^evt-wg-security-and-privacy-pr-11]:
1. **Isolated Enforcement Point**: Isolate policy evaluation and decision logic within a hardware boundary while keeping agent code outside, mitigating the risk of untrusted prompt inputs compromising the TCB[^evt-wg-security-and-privacy-pr-11].
2. **Internal Key Generation**: Generate cryptographic evidence-signing keys inside the hardware boundary and bind all generated execution evidence to those keys[^evt-wg-security-and-privacy-pr-11].
3. **Measurement-Sealed Policy**: Cryptographically seal the active policy bundle to the runtime's measured state, releasing decryption capabilities only after successful attestation appraisal[^evt-wg-security-and-privacy-pr-11].
4. **Per-Unit-of-Work Appraisal**: Gate data release and execution steps on verification of per-unit-of-work evidence by an independent appraisal service[^evt-wg-security-and-privacy-pr-11].

The specification supports multiple hardware mechanisms—including AMD SEV-SNP, Intel TDX, ARM CCA, NVIDIA GPU confidential computing, and TPM 2.0—and aligns with RFC 9334 (RATS Architecture), RFC 9711 (COSE), RFC 8747, IETF SCITT, and SLSA[^evt-wg-security-and-privacy-pr-11]. It also specifies a software-only operational mode for testing and development in environments without confidential computing hardware[^evt-wg-security-and-privacy-pr-11].

# Lifecycle History
- **2026-08 (PR #11)**: Introduced as an initial draft pattern in the `wg-security-and-privacy` design-patterns workstream[^evt-wg-security-and-privacy-pr-11].

[^evt-wg-security-and-privacy-pr-11]: https://github.com/aaif/wg-security-and-privacy/pull/11
