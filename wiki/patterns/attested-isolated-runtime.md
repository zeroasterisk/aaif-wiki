---
type: pattern
title: Attested Isolated Runtime Pattern
description: Architectural pattern isolating policy enforcement and evidence signing
  within hardware-attested boundaries while keeping untrusted agent execution external.
resource: https://github.com/aaif/wg-security-and-privacy/pull/11
tags:
- security
- confidential-computing
- tee
- attestation
- patterns
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T14:53:42.300444+00:00'
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

The Attested Isolated Runtime pattern defines an architectural model for deploying agentic systems where the infrastructure operator sits inside the threat model [^evt-wg-security-and-privacy-pr-11]. It places policy decision enforcement and evidence signing within a hardware-isolated environment (such as a Trusted Execution Environment or TEE) while explicitly keeping untrusted agent runtime code outside the isolated boundary [^evt-wg-security-and-privacy-pr-11].

# Architecture / Specification

The pattern requires four foundational elements to secure agent execution and data gating [^evt-wg-security-and-privacy-pr-11]:

1. **External Agent Placement**: The agent runtime executes outside the trusted computing base (TCB) because agent code processes attacker-influenced inputs as normal operation [^evt-wg-security-and-privacy-pr-11].
2. **Internal Key Generation**: Cryptographic signing keys are generated inside the isolation boundary and bound directly to verifiable attestation evidence [^evt-wg-security-and-privacy-pr-11].
3. **Measurement Sealing**: Enforcement policies are sealed to the hardware measurement of the boundary and released only upon valid appraisal [^evt-wg-security-and-privacy-pr-11].
4. **Independent Appraisal**: An independent verifier appraises per-unit-of-work evidence before data release or downstream tool invocations are permitted [^evt-wg-security-and-privacy-pr-11].

The pattern supports multiple confidential computing hardware stacks—including AMD SEV-SNP, Intel TDX, ARM CCA, NVIDIA GPU confidential computing, and TPM 2.0—while also specifying a software-only mode for development and testing [^evt-wg-security-and-privacy-pr-11].

# Lifecycle History

Proposed within the [Security and Privacy Working Group](../working-groups/security-and-privacy.md) design patterns workstream [^evt-wg-security-and-privacy-pr-11][^evt-wg-security-and-privacy-file-d7a6875f36a3-18be1974].

[^evt-wg-security-and-privacy-file-d7a6875f36a3-18be1974]: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/meeting-notes/README.md
[^evt-wg-security-and-privacy-pr-11]: https://github.com/aaif/wg-security-and-privacy/pull/11
