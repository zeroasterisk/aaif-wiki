---
type: deliverable
title: Attested Isolated Runtime
description: A security design pattern isolating policy enforcement and evidence signing
  in confidential computing environments while keeping agent execution outside the
  trust boundary.
resource: https://github.com/aaif/wg-security-and-privacy/pull/11
tags:
- security
- privacy
- confidential-computing
- tee
- attestation
- design-patterns
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:50:21.114223+00:00'
sources:
- id: evt-wg-security-and-privacy-pr-11
  resource: https://github.com/aaif/wg-security-and-privacy/pull/11
  author: imran-siddique
  last_modified: '2026-08-17T19:17:48+00:00'
---

# Overview

The Attested Isolated Runtime is a design pattern developed by the [Security and Privacy Working Group](../working-groups/security-and-privacy.md) addressing threat models where the infrastructure operator sits within the untrusted boundary[^evt-wg-security-and-privacy-pr-11]. The pattern moves the policy decision point and evidence signer into a hardware-isolated environment (such as a Trusted Execution Environment / TEE) and gates data release upon appraisal by an independent verifier.

# Architecture / Specification

## Core Invariants

The pattern requires four foundational elements[^evt-wg-security-and-privacy-pr-11]:

1. **External Agent Execution**: The core agent logic remains outside the hardware-isolated trust boundary, preventing attacker-influenced inputs from expanding the Trusted Computing Base (TCB).
2. **Internal Key Generation**: Cryptographic signing keys are generated strictly inside the isolated runtime boundary and bound to evidence artifacts.
3. **Policy Measurement Sealing**: Operational policies are sealed to specific environmental measurements and released only upon valid appraisal.
4. **Per-Unit-of-Work Verifier Appraisal**: An independent verifier appraises cryptographically signed evidence for each discrete unit of execution.

## Hardware and Standards Alignment

The specification supports vendor-neutral implementation across AMD SEV-SNP, Intel TDX, ARM CCA, NVIDIA GPU confidential computing, and TPM 2.0 architectures, alongside a software-only evaluation mode[^evt-wg-security-and-privacy-pr-11]. It maps to RFC 9334 (RATS), RFC 9711 (COSE), RFC 8747, IETF SCITT, and SLSA provenance standards.

[^evt-wg-security-and-privacy-pr-11]: https://github.com/aaif/wg-security-and-privacy/pull/11
