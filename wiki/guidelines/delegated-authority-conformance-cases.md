---
type: guideline
title: Delegated-Authority Conformance Cases
description: Eight-case evaluation framework assessing agent delegated authority designs
  against Reference Architecture invariants while mandating explicit residual disclosure.
resource: https://github.com/aaif/wg-identity-and-trust/issues/22
tags:
- identity
- delegation
- conformance
- security
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:29:37.606945+00:00'
sources:
- id: evt-wg-identity-and-trust-issue-22
  resource: https://github.com/aaif/wg-identity-and-trust/issues/22
  author: MarcMolas
  last_modified: '2026-10-31T22:24:55+00:00'
---

# Overview

The Delegated-Authority Conformance Cases define an eight-part evaluation matrix proposed for the Identity and Trust Reference Architecture to test system designs against normative delegation, attenuation, and revocation invariants.[^evt-wg-identity-and-trust-issue-22] Rather than evaluating systems via a binary pass/fail checklist that rewards unstated boundaries, the framework enforces a strict residual disclosure rule requiring every evaluated architecture to explicitly declare what it knowingly leaves uncovered and which operational trade-offs it accepts.[^evt-wg-identity-and-trust-issue-22]

# Specification

The framework maps reference invariants from the Identity and Trust Reference Architecture v1 into observable failure conditions, audit evidence requirements, and mandatory residual disclosures across eight operational cases:[^evt-wg-identity-and-trust-issue-22]

1. **Delegator Revoked After Downstream Delegation**: Tests that revocation of an upstream [principal](../taxonomy/principal.md) cascades to all downstream derived authority within declared time bounds, failing if an agent or subagent continues to be accepted.[^evt-wg-identity-and-trust-issue-22]
2. **Valid Delegation, Wrong Object or Action**: Evaluates enforcement of grant constraints (actions, counterparties, limits, validity) at the time of use (§3.5.1), failing if a grant valid for one target is accepted for another or replayed.[^evt-wg-identity-and-trust-issue-22]
3. **Acting on Stale Revocation Information**: Assesses whether relying parties establish grant status from verifiable evidence at the time of use rather than self-reported assertions, failing if decisions rely on status data exceeding max age bounds.[^evt-wg-identity-and-trust-issue-22]
4. **Escalation Authority Unavailable**: Verifies fail-closed behavior during approval timeouts or approver absence, proving that authority never widens when an escalation authority is unavailable.[^evt-wg-identity-and-trust-issue-22]
5. **Amplification Across Multi-Hop Delegation Chains**: Enforces strict attenuation (§3.5.3), requiring proof that each delegation hop only narrows constraints and never expands authority in scope or number.[^evt-wg-identity-and-trust-issue-22]
6. **Identity Valid, Authority Expired**: Proves independent lifecycle checking between identity credentials and delegated authority grants, preventing valid identity tokens from executing expired or revoked grants.[^evt-wg-identity-and-trust-issue-22]
7. **Delegation Chain Surveillance Graph**: Measures privacy protections ensuring relying parties verify that an accountable principal exists without learning the intermediate delegation chain graph or sibling agent identities.[^evt-wg-identity-and-trust-issue-22]
8. **Wrongful or Disputed Revocation**: Audits tamper-evident revocation recording (§3.6) and declared contestation or re-issuance remedies, documenting whether derived grants survive or reverse following a dispute.[^evt-wg-identity-and-trust-issue-22]

# Lifecycle History

- **2026-10**: Proposed by Sparsh Agarwal in [WG Identity and Trust](../working-groups/identity-and-trust.md) as an appendix to Reference Architecture v1 following discussion of MintID, Proofable, and Alakris reference implementations.[^evt-wg-identity-and-trust-issue-22]

[^evt-wg-identity-and-trust-issue-22]: https://github.com/aaif/wg-identity-and-trust/issues/22
