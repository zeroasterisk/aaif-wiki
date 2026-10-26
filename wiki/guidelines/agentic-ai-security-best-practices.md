---
type: guideline
title: Agentic AI Security Best Practices
description: Actionable security controls, threat mitigations, and execution boundary
  standards across the autonomous agent lifecycle.
resource: https://github.com/aaif/wg-security-and-privacy/pull/42
tags:
- security
- guidelines
- threat-mitigation
- sandboxing
- confidential-computing
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T11:08:09.484639+00:00'
sources:
- id: evt-wg-security-and-privacy-pr-42
  resource: https://github.com/aaif/wg-security-and-privacy/pull/42
  author: imran-siddique
  last_modified: '2026-10-20T04:23:57+00:00'
---

# Overview

The Agentic AI Security Best Practices guideline provides defensive controls, threat mitigations, and isolation boundary rules for building and operating autonomous agent systems[^evt-wg-security-and-privacy-pr-42]. Authored by the [Security & Privacy Working Group](../working-groups/security-and-privacy.md), the document defines baseline expectations for sandboxing, credential issuance, prompt sanitization, and runtime attestation[^evt-wg-security-and-privacy-pr-42].

# Architecture / Specification

## Confidential Computing and Credential Boundaries

Hardware-enforced confidential computing environments (such as Intel TDX or AMD SEV virtual machines) isolate guest workload memory from untrusted host hypervisors and administrators[^evt-wg-security-and-privacy-pr-42]. However, security guidelines clarify the operational limits of confidential enclaves regarding credential management:
- **Guest Memory vs. Bearer Exposure**: While hardware isolation shields guest memory from external inspection, any bearer token released to software executing inside the guest environment grants full authority to whoever possesses it[^evt-wg-security-and-privacy-pr-42].
- **Token Validity and Scope**: Credential exposure within an enclave is governed by the token's configured permissions, audience restrictions, and expiration lifetime rather than the underlying hardware protection[^evt-wg-security-and-privacy-pr-42].
- **Defense-in-Depth**: Confidential computing must be paired with short-lived, down-scoped credentials, attested delegation, and hardware-bound authorization gates rather than assuming tokens are safe merely by virtue of enclave execution[^evt-wg-security-and-privacy-pr-42].

# Lifecycle History

- **Draft Revisions**: Section 2 boundary tables corrected via PR #42 to remove claims that credential exposure is inapplicable under confidential computing, aligning guidelines with standard bearer token threat models[^evt-wg-security-and-privacy-pr-42].

# References

- [AAIF Security & Privacy PR #42](https://github.com/aaif/wg-security-and-privacy/pull/42)

[^evt-wg-security-and-privacy-pr-42]: https://github.com/aaif/wg-security-and-privacy/pull/42
