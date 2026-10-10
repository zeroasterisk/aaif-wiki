---
type: standard
title: TRACE Specification
description: Open standard and JSON Schema for signed agent execution records supporting
  verifiable software, hardware-attested, and transparency-anchored evidence.
resource: https://github.com/aaif/project-proposals/issues/42
tags:
- trace
- attestation
- provenance
- eat
- rats
- scitt
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:18:20.208859+00:00'
sources:
- id: evt-project-proposals-issue-42
  resource: https://github.com/aaif/project-proposals/issues/42
  author: imran-siddique
  last_modified: '2026-10-02T02:32:06+00:00'
---

# Overview

The TRACE Specification (Trust, Runtime Attestation, and Compliance Evidence) is an open specification for generating signed records of AI agent runs that third parties can verify without trusting the producing operator [^evt-project-proposals-issue-42]. A TRACE Trust Record captures which model executed (`model.model_id`, `model.weights_digest`), the target execution environment (`runtime.platform`, `runtime.measurement`), policy bundles in force (`policy.bundle_hash`), data classifications, and tool transcript hashes [^evt-project-proposals-issue-42].

# Architecture / Specification

TRACE builds on existing IETF and open standards rather than defining novel cryptography [^evt-project-proposals-issue-42]:
- **RFC 9711 (EAT)**: Defines the structured claims envelope.
- **RFC 9334 (RATS)**: Defines architecture and roles for attesters, verifiers, and relying parties.
- **RFC 8785**: Canonical JSON format used prior to cryptographic signing.
- **SCITT**: Supply chain integrity transparency log anchoring.

### Conformance Levels

Records declare one of three conformance tiers [^evt-project-proposals-issue-42]:
- **Level 0 (Software-Signed)**: Cryptographically signed audit trail without hardware appraisal.
- **Level 1 (Hardware-Attested)**: Bound to hardware evidence (e.g., Intel TDX, AMD SEV-SNP, NVIDIA H100/Blackwell, AWS Nitro, Arm CCA, TPM 2.0) requiring hardware appraisal and verifier binding (see [../patterns/attested-isolated-runtime.md](../patterns/attested-isolated-runtime.md)).
- **Level 2 (Transparency-Anchored)**: Incorporates transparency log inclusion proofs based on `registry-anchor-v1` specifications.

# Lifecycle History

TRACE was initially previewed at the Confidential Computing Summit on 23 June 2026 and announced under LF Projects on 25 August 2026 before being submitted as an AAIF project proposal [^evt-project-proposals-issue-42].

[^evt-project-proposals-issue-42]: https://github.com/aaif/project-proposals/issues/42
