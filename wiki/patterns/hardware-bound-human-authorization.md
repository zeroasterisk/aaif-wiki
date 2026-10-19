---
type: pattern
title: Hardware-Bound Human Authorization
description: Architectural pattern binding human approval to hardware-protected keys,
  witnessed actions, and explicit freshness appraisal.
resource: https://github.com/aaif/wg-identity-and-trust/issues/19
tags:
- identity
- authorization
- hardware-security
- witness
- verification
- rats
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T11:12:22.882582+00:00'
sources:
- id: evt-wg-identity-and-trust-issue-19
  resource: https://github.com/aaif/wg-identity-and-trust/issues/19
  author: michaelkuan-create
  last_modified: '2026-10-15T01:51:52+00:00'
---

# Overview
Hardware-Bound Human Authorization is an architectural security pattern establishing cryptographic verifiable accountability for agent actions by binding explicit human approvals to hardware-protected signing keys, correlated with independent execution witnesses and freshness appraisals.[^evt-wg-identity-and-trust-issue-19] Conforming to the separation of evidence, appraisal, and reliance defined in the IETF Remote ATtestation procedureS (RATS) architecture (RFC 9334), the pattern ensures that a verifier distinguishes between cryptographic key possession and actual user authorization intent.[^evt-wg-identity-and-trust-issue-19]

# Architecture / Specification
The pattern structures verifier appraisal across five orthogonal dimensions:[^evt-wg-identity-and-trust-issue-19]
- **Source Evaluation**: Evaluates who asserted each claim, how the source was authenticated, and its relative independence from both the agent and operator.[^evt-wg-identity-and-trust-issue-19] Hardware protection alone does not confer source independence.[^evt-wg-identity-and-trust-issue-19]
- **Construction Integrity**: Verifies the strict binding among human approval, agent identity, delegated scopes, and execution constraints (such as destination, amount, and expiry) recorded in an [action record](../taxonomy/action-record.md) or [approval checkpoint](approval-checkpoint.md).[^evt-wg-identity-and-trust-issue-19]
- **Hardware Assurance**: Validates cryptographic evidence of key protection, provenance, and platform measurements where supported; unverified hardware claims remain explicitly unestablished.[^evt-wg-identity-and-trust-issue-19]
- **Freshness, Expiry, and Revocation**: Checks challenge freshness, execution timestamps, credential validity, and status evidence age, keeping revocation checks and temporal age separate.[^evt-wg-identity-and-trust-issue-19]
- **Observation Scope and Witnessing**: Correlates separate witness records across request submission, execution context, and final outcome.[^evt-wg-identity-and-trust-issue-19] Unavailable evidence is explicitly differentiated from contradictory evidence.[^evt-wg-identity-and-trust-issue-19]

### Hardware-to-Cloud Boundary
Edge hardware devices provide strong evidence regarding local key operations and user approvals within their demonstrated local capture scope.[^evt-wg-identity-and-trust-issue-19] However, local hardware protection does not establish what occurred inside a remote agent model or service, which requires independent execution evidence bound to the relevant request and outcome.[^evt-wg-identity-and-trust-issue-19]

# Lifecycle History
Proposed in the [Identity & Trust Working Group](../working-groups/identity-and-trust.md) via Issue #19 as a worked example contribution to the AAIF Patterns deliverable.[^evt-wg-identity-and-trust-issue-19]

[^evt-wg-identity-and-trust-issue-19]: https://github.com/aaif/wg-identity-and-trust/issues/19
