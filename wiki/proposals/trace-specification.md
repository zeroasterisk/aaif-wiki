---
type: proposal
title: TRACE Specification
description: Open specification standardizing signed, verifiable trust records, hardware
  attestation, and transparency log anchoring for agent runs.
resource: https://github.com/aaif/project-proposals/issues/42
tags:
- proposals
- attestation
- evidence
- security
- transparency
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:25:43.661013+00:00'
sources:
- id: evt-project-proposals-issue-42
  resource: https://github.com/aaif/project-proposals/issues/42
  author: imran-siddique
  last_modified: '2026-10-02T02:32:06+00:00'
---

# Overview
The TRACE Specification (Trust, Runtime Attestation, and Compliance Evidence) is an open standard defining signed, vendor-neutral execution records for AI agent runs that can be appraised independently without trusting the executing operator.[^evt-project-proposals-issue-42] A standard Trust Record captures model metadata, runtime platform attestation, policy hashes, tool call transcripts, and transparency log inclusion proofs.[^evt-project-proposals-issue-42]

# Architecture / Specification
TRACE profiles existing IETF specifications, including RFC 9711 (EAT) for the envelope, RFC 9334 (RATS) for architectural roles, RFC 8785 for canonical JSON signing, and SCITT for log anchoring.[^evt-project-proposals-issue-42]

### Conformance Levels
TRACE defines three graduated conformance levels for relying-party acceptance policies:[^evt-project-proposals-issue-42]
- **Level 0 (Software-Signed):** Tamper-evident software signatures suitable for internal audit logging.
- **Level 1 (Hardware-Bound Attestation):** Cryptographically bound to trusted execution environment (TEE) hardware measurements and quotes (e.g., Intel TDX, AMD SEV-SNP, NVIDIA H100/Blackwell, AWS Nitro, Arm CCA, Google Confidential Space, TPM 2.0). Relies on independent appraisal rather than relying solely on signature verification.[^evt-project-proposals-issue-42]
- **Level 2 (Transparency-Anchored):** Level 1 evidence backed by cryptographic inclusion proofs anchored in a publicly verifiable SCITT transparency log.[^evt-project-proposals-issue-42]

# References
- Corresponds to evidence structures in [evidence-record-spec](../proposals/evidence-record-spec.md) and [attested-isolated-runtime](../patterns/attested-isolated-runtime.md).
- Proposed for AAIF adoption via [project-proposal-process](../governance/project-proposal-process.md).

[^evt-project-proposals-issue-42]: https://github.com/aaif/project-proposals/issues/42
