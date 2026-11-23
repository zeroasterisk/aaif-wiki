---
type: pattern
title: Attested Isolated Runtime
description: Architectural security pattern isolating the policy decision point and
  evidence signing within a hardware-attested environment while keeping the agent
  outside the trust boundary.
resource: https://github.com/aaif/wg-security-and-privacy/pull/11
tags:
- pattern
- security
- privacy
- confidential-computing
- attestation
- tee
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T09:47:30.288301+00:00'
sources:
- id: evt-wg-security-and-privacy-pr-11
  resource: https://github.com/aaif/wg-security-and-privacy/pull/11
  author: imran-siddique
  last_modified: '2026-08-17T19:17:48+00:00'
- id: evt-wg-security-and-privacy-file-75f22d914368-03de91f5
  resource: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/meeting-notes/2026-08-04.md
  author: Alex Frazer
  last_modified: '2026-08-13T08:00:29-04:00'
---

# Overview
The Attested Isolated Runtime is an architectural security pattern that isolates policy decision points and evidence signing within a hardware-isolated environment while leaving the AI agent outside the trust boundary[^evt-wg-security-and-privacy-pr-11]. Designed for operational deployments where infrastructure operators or hosting layers reside within the threat model, the pattern protects governance rules, tool execution authorizers, and audit proof generation from compromise by unmeasured or adversarial execution environments[^evt-wg-security-and-privacy-pr-11].

# Architecture / Specification

## Architectural Invariants
The pattern establishes four mandatory requirements to prevent governance and measurement failures[^evt-wg-security-and-privacy-pr-11]:
1. **Enforcement Isolation (Agent Outside):** The policy decision point (PDP) and enforcement logic run strictly inside an isolated runtime, while agent logic remains external[^evt-wg-security-and-privacy-pr-11]. Because agent code routinely executes untrusted and attacker-influenced input (such as prompt injections), enclosing the agent inside the trusted computing base (TCB) would expose the secure enclave to subversion[^evt-wg-security-and-privacy-pr-11].
2. **Internal Key Generation:** Signing keys must be generated inside the isolated boundary and bound directly to cryptographic attestation claims, ensuring evidence cannot be forged by host infrastructure[^evt-wg-security-and-privacy-pr-11].
3. **Measured Policy Sealing:** Policy bundles, system prompts, and tool schemas are sealed to enclave measurements and only released upon successful hardware appraisal[^evt-wg-security-and-privacy-pr-11].
4. **Independent Verifier Appraisal:** An independent external verifier appraises per-unit-of-work attestation evidence before releasing sensitive resources or executing downstream actions[^evt-wg-security-and-privacy-pr-11].

## Attestation Targets and Neutrality
The pattern is vendor-neutral and maps to multiple confidential computing architectures[^evt-wg-security-and-privacy-pr-11]:
- AMD SEV-SNP[^evt-wg-security-and-privacy-pr-11]
- Intel TDX[^evt-wg-security-and-privacy-pr-11]
- ARM CCA[^evt-wg-security-and-privacy-pr-11]
- NVIDIA GPU Confidential Computing[^evt-wg-security-and-privacy-pr-11]
- TPM 2.0 and software-only emulation modes for local testing and conformance[^evt-wg-security-and-privacy-pr-11]

## Standards Alignment and Workstream Questions
The pattern references standard attestation protocols including IETF RATS (RFC 9334), CBOR Web Token (RFC 8747), COSE (RFC 9711), IETF SCITT, and SLSA[^evt-wg-security-and-privacy-pr-11]. Key design questions under evaluation by the [Security and Privacy Working Group](../working-groups/security-and-privacy.md) include defining the exact artifact measurement set (such as prompt definitions versus dynamic memory states) and coordinating assurance vocabulary with the [Identity and Trust Working Group](../working-groups/identity-and-trust.md)[^evt-wg-security-and-privacy-pr-11][^evt-wg-security-and-privacy-file-75f22d914368-03de91f5].

[^evt-wg-security-and-privacy-file-75f22d914368-03de91f5]: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/meeting-notes/2026-08-04.md
[^evt-wg-security-and-privacy-pr-11]: https://github.com/aaif/wg-security-and-privacy/pull/11
