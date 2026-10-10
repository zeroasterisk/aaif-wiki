---
type: working-group
title: Identity and Trust Working Group
description: AAIF working group advancing vendor-neutral standards, reference architectures,
  and trust models for agent identity, delegation, and attestation.
resource: https://github.com/aaif/wg-identity-and-trust/issues/12
tags:
- working-group
- identity
- attestation
- trust
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:20:12.298283+00:00'
sources:
- id: evt-wg-identity-and-trust-issue-12
  resource: https://github.com/aaif/wg-identity-and-trust/issues/12
  author: imran-siddique
  last_modified: '2026-10-05T20:10:13+00:00'
---

# Overview
The Identity and Trust Working Group establishes open specifications, reference architectures, and interoperable trust frameworks for agent identification, credential delegation, and cryptographic execution attestation.[^evt-wg-identity-and-trust-issue-12]

# Architecture / Specification
## Attestation Component Decomposition
Technical discussions in the working group decompose runtime attestation into three distinct reference architecture components to accommodate multi-platform confidential execution nuances:[^evt-wg-identity-and-trust-issue-12]

1. **Platform Evidence**: Signed hardware or firmware reports and endorsement chains (e.g., AMD SEV-SNP via `/dev/sev-guest`, Azure confidential VM paravisor claims, NVIDIA H100 GPU reports) proving the exact physical environment and launch measurements.[^evt-wg-identity-and-trust-issue-12]
2. **Identity Binding**: Signed statements binding an agent's cryptographic identity document or key to platform measurements through platform-specific fields such as `REPORT_DATA`, paravisor runtime claims `user-data`, or TPM quote `qualifyingData`.[^evt-wg-identity-and-trust-issue-12]
3. **Appraisal**: The relying party verification logic producing an authoritative trust verdict by evaluating received evidence and bindings against organizational policy rules.[^evt-wg-identity-and-trust-issue-12]

This separation interfaces with isolation patterns defined by the [Security and Privacy Working Group](../working-groups/security-and-privacy.md), such as the [Attested Isolated Runtime](../patterns/attested-isolated-runtime.md).[^evt-wg-identity-and-trust-issue-12]

# Lifecycle History
- 2026-09: Architecture proposal submitted to subdivide the unified attestation component into explicit platform evidence, identity binding, and appraisal stages across SEV-SNP, TDX, and GPU environments.[^evt-wg-identity-and-trust-issue-12]

[^evt-wg-identity-and-trust-issue-12]: https://github.com/aaif/wg-identity-and-trust/issues/12
