---
type: working-group
title: Identity and Trust Working Group
description: AAIF technical working group standardizing decentralized agent identity,
  hardware attestation layering, cryptographic delegation, and authorization boundaries.
resource: https://github.com/aaif/wg-identity-and-trust/issues/12
tags:
- identity
- attestation
- trust
- working-group
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:40:05.907782+00:00'
sources:
- id: evt-wg-identity-and-trust-issue-12
  resource: https://github.com/aaif/wg-identity-and-trust/issues/12
  author: imran-siddique
  last_modified: '2026-10-05T20:10:13+00:00'
---

# Overview
The Identity and Trust Working Group standardizes identity frameworks, cryptographic attestation mechanisms, authentication protocols, and delegation boundaries across autonomous agent systems[^evt-wg-identity-and-trust-issue-12]. Operating under the technical governance of the Agentic AI Foundation, the working group establishes reference architectures and interoperability baselines allowing relying parties to verify agent execution integrity and authorized delegation.

# Architecture / Specification
To address architectural divergence across hardware environments, the group is restructuring attestation specifications into a three-part model[^evt-wg-identity-and-trust-issue-12]:
- **Platform Evidence**: Signed hardware or firmware reports and endorsement chains (such as AMD SEV-SNP, Intel TDX, or GPU attestation) certifying the underlying execution environment and boot state[^evt-wg-identity-and-trust-issue-12].
- **Identity Binding**: Cryptographic statements binding an agent key or identifier to hardware measurements using transport structures such as guest report data, paravisor runtime claims, or TPM qualifying data[^evt-wg-identity-and-trust-issue-12].
- **Appraisal**: Verification logic and policy verdicts executed by relying parties to confirm evidence satisfies security and compliance thresholds[^evt-wg-identity-and-trust-issue-12].

This structural division resolves cross-platform inconsistencies between direct guest attestation, hypervisor-managed paravisor runtime structures, and multi-accelerator environments[^evt-wg-identity-and-trust-issue-12].

# Lifecycle History
Following charter establishment, reference architecture discussions in Issue #12 identified gaps in monolithic attestation representations, leading to proposals decomposing attestation into platform evidence, identity binding, and appraisal layers[^evt-wg-identity-and-trust-issue-12].

[^evt-wg-identity-and-trust-issue-12]: https://github.com/aaif/wg-identity-and-trust/issues/12
