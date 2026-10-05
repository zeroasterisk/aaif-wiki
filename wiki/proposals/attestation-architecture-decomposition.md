---
type: proposal
title: Attestation Architecture Decomposition
description: Architectural decomposition splitting agent attestation into platform
  evidence, identity binding, and appraisal layers across confidential runtimes.
resource: https://github.com/aaif/wg-identity-and-trust/issues/12
tags:
- attestation
- confidential-computing
- identity-binding
- reference-architecture
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:25:24.695424+00:00'
sources:
- id: evt-wg-identity-and-trust-issue-12
  resource: https://github.com/aaif/wg-identity-and-trust/issues/12
  author: imran-siddique
  last_modified: '2026-10-01T21:05:02+00:00'
---

# Overview
The Attestation Architecture Decomposition proposal addresses platform integration failures in confidential execution environments by restructuring the monolithic attestation box in agent reference architectures into three distinct functional layers [^evt-wg-identity-and-trust-issue-12]. This prevents reliance on brittle assumptions regarding how agent identities bind to hardware reports across diverse platforms [^evt-wg-identity-and-trust-issue-12].

# Architecture / Specification
The proposed model splits attestation into three discrete structural components [^evt-wg-identity-and-trust-issue-12]:
1. **Platform Evidence**: Signed hardware or firmware reports and endorsement chains that attest to the execution environment measurements and hardware root of trust [^evt-wg-identity-and-trust-issue-12].
2. **Identity Binding**: Signed statements cryptographically binding an agent's identifier, key, or configuration to platform evidence (e.g., via AMD SEV-SNP `REPORT_DATA`, Azure paravisor Runtime Claims `user-data`, or TPM quote `qualifyingData`), explicitly defining trust boundary boundaries [^evt-wg-identity-and-trust-issue-12].
3. **Appraisal**: The relying party's policy execution layer that evaluates composite evidence to produce an appraisal verdict [^evt-wg-identity-and-trust-issue-12].

# Lifecycle History
Submitted in Issue #12 of the Identity & Trust Working Group following validation across GCP N2D SEV-SNP, Azure Confidential VMs, and NVIDIA H100 GPU environments [^evt-wg-identity-and-trust-issue-12].

# References
- Cross-references: [Identity and Trust Working Group](../working-groups/identity-and-trust.md), [Attested Isolated Runtime](../patterns/attested-isolated-runtime.md), [Evidence-Strength Labels](evidence-strength-labels.md).

[^evt-wg-identity-and-trust-issue-12]: https://github.com/aaif/wg-identity-and-trust/issues/12
