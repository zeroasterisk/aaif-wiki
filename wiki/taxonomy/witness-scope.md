---
type: taxonomy
title: Witness Scope
description: Taxonomy classification designating the custody category of an entity
  holding or attesting an agent action record.
resource: https://github.com/aaif/ws-taxonomy-landscape/issues/53
tags:
- taxonomy
- evidence
- witness
- custody
- verification
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:28:04.381282+00:00'
sources:
- id: evt-ws-taxonomy-landscape-issue-53
  resource: https://github.com/aaif/ws-taxonomy-landscape/issues/53
  author: narko4u
  last_modified: '2026-09-20T02:32:57+00:00'
---

# Overview
`witness_scope` designates the custody category of a witness that holds or attests a record about an agent action [^evt-ws-taxonomy-landscape-issue-53]. It isolates the question of who retains possession of the record from whether the underlying content is technically forgeable by the subject it describes [^evt-ws-taxonomy-landscape-issue-53].

# Architecture / Specification
The taxonomy partitions witness custody across three distinct levels [^evt-ws-taxonomy-landscape-issue-53]:
- **`SELF`**: The record is held by the agent itself or its immediate local execution runtime [^evt-ws-taxonomy-landscape-issue-53].
- **`PEER`**: The record is held or attested by an immediate counterparty participating in the same shared transaction or agreement [^evt-ws-taxonomy-landscape-issue-53].
- **`EXTERNAL`**: The record is held or attested by an independent party operating outside the bilateral relationship [^evt-ws-taxonomy-landscape-issue-53].

### Separation of Custody and Forgeability
Witness scope captures record custody rather than forgeability vantage [^evt-ws-taxonomy-landscape-issue-53]. For example, an `EXTERNAL` party holding an execution record may still hold an unverifiable account if it relies on symmetric keys or self-reported data produced by the emitting agent [^evt-ws-taxonomy-landscape-issue-53]. Witness scope is formally paired with a planned companion contrast term, `verification-basis`, which addresses the substrate versus artifact vantage axis [^evt-ws-taxonomy-landscape-issue-53].

# Lifecycle History
Proposed in issue #53 within the Taxonomy and Landscape workstream following cross-organization discussions within the OWASP GenAI-Security-Project agent-control-standard milestone [^evt-ws-taxonomy-landscape-issue-53].

# References
- [Self-Reported](../taxonomy/self-reported.md)
- [Evidence Strength Labels](../taxonomy/evidence-strength-labels.md)
- [Taxonomy and Landscape Working Group](../working-groups/taxonomy-and-landscape.md)

[^evt-ws-taxonomy-landscape-issue-53]: https://github.com/aaif/ws-taxonomy-landscape/issues/53
