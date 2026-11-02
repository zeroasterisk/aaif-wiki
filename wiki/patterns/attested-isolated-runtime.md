---
type: pattern
title: Attested Isolated Runtime
description: Architectural security pattern isolating policy evaluation and evidence
  signing inside hardware-attested environments while leaving agent execution outside
  the trust boundary.
resource: https://github.com/aaif/wg-security-and-privacy/pull/11
tags:
- pattern
- security
- confidential-computing
- tee
- attestation
- privacy
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T09:45:14.530544+00:00'
sources:
- id: evt-wg-security-and-privacy-pr-11
  resource: https://github.com/aaif/wg-security-and-privacy/pull/11
  author: imran-siddique
  last_modified: '2026-08-17T19:17:48+00:00'
- id: evt-wg-security-and-privacy-file-d7a6875f36a3-18be1974
  resource: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/meeting-notes/README.md
  author: Alex Frazer
  last_modified: '2026-08-13T08:00:29-04:00'
---

# Overview
Attested Isolated Runtime is an architectural security pattern designed for agentic deployments where the host infrastructure operator is situated inside the threat model [^evt-wg-security-and-privacy-pr-11]. The pattern isolates policy evaluation and evidence signing within a hardware-enforced Trusted Execution Environment (TEE), gating data release and sensitive actions on an independent verifier's appraisal while purposefully leaving the agent execution itself outside the trust boundary [^evt-wg-security-and-privacy-pr-11].

By maintaining the agent outside the isolated boundary, the pattern prevents attacker-manipulated prompt or context flows from expanding the trusted computing base (TCB) [^evt-wg-security-and-privacy-pr-11].

# Architecture / Specification
The pattern specifies four mandatory architectural elements, each paired with a distinct failure mode if omitted [^evt-wg-security-and-privacy-pr-11]:

1. **External Agent Boundary**: The policy decision point (PDP) is isolated within the hardware boundary, leaving the agent runtime outside to avoid exposing the TCB to untrusted model inputs [^evt-wg-security-and-privacy-pr-11].
2. **Internal Key Generation**: Cryptographic signing keys are generated strictly inside the hardware-isolated boundary and bound to tamper-evident action evidence [^evt-wg-security-and-privacy-pr-11].
3. **Measurement-Sealed Policy**: Operational policy bundles and system configurations are sealed to initial platform measurements and unsealed solely upon successful appraisal [^evt-wg-security-and-privacy-pr-11].
4. **Independent Verifier Appraisal**: An external verifier appraises per-unit-of-work attestation evidence before releasing sensitive data or authorization tokens [^evt-wg-security-and-privacy-pr-11].

### Implementation and Neutrality
The pattern maintains vendor neutrality by supporting diverse hardware attestation environments—including AMD SEV-SNP, Intel TDX, ARM CCA, NVIDIA GPU confidential computing, and TPM 2.0—alongside an explicit software-only fallback mode for testing and non-TEE environments [^evt-wg-security-and-privacy-pr-11]. Standards alignment includes RFC 9334 (RATS architecture), RFC 9711, RFC 8747, IETF SCITT, and SLSA [^evt-wg-security-and-privacy-pr-11].

# Lifecycle History
Authored by Opaque Systems, the initial draft of the Attested Isolated Runtime pattern was introduced to the [Security and Privacy Working Group](../working-groups/security-and-privacy.md) in July/August 2026 under PR#11 to establish reference architectures for privacy-preserving execution [^evt-wg-security-and-privacy-pr-11][^evt-wg-security-and-privacy-file-d7a6875f36a3-18be1974].

[^evt-wg-security-and-privacy-file-d7a6875f36a3-18be1974]: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/meeting-notes/README.md
[^evt-wg-security-and-privacy-pr-11]: https://github.com/aaif/wg-security-and-privacy/pull/11
