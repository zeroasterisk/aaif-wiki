---
type: working-group
title: Identity and Trust Working Group
description: AAIF working group establishing vendor-neutral standards for AI agent
  identity, verifiable delegation, and appraisal-driven evidence strength.
resource: https://github.com/aaif/wg-identity-and-trust/issues/5
tags:
- identity
- trust
- attestation
- delegation
- working-group
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:59:46.074542+00:00'
sources:
- id: evt-wg-identity-and-trust-issue-5
  resource: https://github.com/aaif/wg-identity-and-trust/issues/5
  author: narko4u
  last_modified: '2026-10-01T17:45:41+00:00'
- id: evt-wg-identity-and-trust-issue-12
  resource: https://github.com/aaif/wg-identity-and-trust/issues/12
  author: imran-siddique
  last_modified: '2026-10-01T21:05:02+00:00'
---

# Overview
The Identity and Trust Working Group establishes vendor-neutral standards, reference architectures, and vocabularies for AI agent identity, verifiable delegation, provenance, and cross-organizational trust evaluation [^evt-wg-identity-and-trust-issue-5]. The group focuses on how agents authenticate their operational context, prove authorization chains, and provide verifiable evidence of user approval [^evt-wg-identity-and-trust-issue-5].

# Architecture / Specification
Key technical models under development include:

### Evidence-Strength Vocabulary
The group defines evidence-strength labels as outputs of relying-party appraisal rather than self-asserted credential fields [^evt-wg-identity-and-trust-issue-5]:
- **Axis A (Who Asserts)**: Evaluates assertion independence across *Declared* (self-asserted), *Platform-attested* (runtime environment), and *Corroborated* (independent third-party confirmation) [^evt-wg-identity-and-trust-issue-5].
- **Axis B (Chain Construction)**: Evaluates delegation binding across *Composed* (multi-hop chains governed by the weakest-hop rule) and *Anchored* (terminating in an independently verifiable trust root) [^evt-wg-identity-and-trust-issue-5].
- **Freshness and Revocation**: A distinct appraisal dimension tracking real-time status against revocation stores rather than treating freshness as a static rank [^evt-wg-identity-and-trust-issue-5].

### Attestation Component Architecture
The reference architecture decomposes agent attestation into three distinct layers [^evt-wg-identity-and-trust-issue-12]:
1. **Platform Evidence**: Signed hardware or firmware measurement reports (e.g., AMD SEV-SNP, Intel TDX, NVIDIA H100 reports) [^evt-wg-identity-and-trust-issue-12].
2. **Identity Binding**: Signed statements explicitly linking the agent's key or identity payload to platform measurement registers (e.g., via `REPORT_DATA`, paravisor runtime claims JSON, or TPM qualifying data) [^evt-wg-identity-and-trust-issue-12].
3. **Appraisal**: Verifier evaluation against local policy to produce attestation verdicts [^evt-wg-identity-and-trust-issue-12].

[^evt-wg-identity-and-trust-issue-12]: https://github.com/aaif/wg-identity-and-trust/issues/12
[^evt-wg-identity-and-trust-issue-5]: https://github.com/aaif/wg-identity-and-trust/issues/5
