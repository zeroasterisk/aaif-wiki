---
type: taxonomy
title: Emission Conformant
description: Taxonomy classification designating an artifact claim asserting structural
  schema validity at the emission boundary without operational behavioral guarantees.
resource: https://github.com/aaif/ws-taxonomy-landscape/issues/50
tags:
- taxonomy
- conformance
- schema
- validation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:28:04.381282+00:00'
sources:
- id: evt-ws-taxonomy-landscape-issue-50
  resource: https://github.com/aaif/ws-taxonomy-landscape/issues/50
  author: narko4u
  last_modified: '2026-09-20T02:33:00+00:00'
---

# Overview
`emission-conformant` defines an artifact claim asserting compliance exclusively at the boundary serialization layer, confirming that an emitted record matches a canonical schema without validating execution behavior or factual authenticity [^evt-ws-taxonomy-landscape-issue-50].

# Architecture / Specification
An emission-conformant classification establishes minimal contract adherence for agent records [^evt-ws-taxonomy-landscape-issue-50]:
- **Syntactic Conformance**: The payload parses successfully and adheres to field, type, and serialization rules defined by the target schema [^evt-ws-taxonomy-landscape-issue-50].
- **No Operational Guarantee**: The claim makes no representation regarding runtime invariants, policy compliance, or proper agent state transitions [^evt-ws-taxonomy-landscape-issue-50].
- **No Truth Assertion**: The classification does not verify whether the claims contained within the payload represent an accurate account of physical or logical execution [^evt-ws-taxonomy-landscape-issue-50].

This distinction prevents unqualified claims of system conformance from obscuring unverified agent operations [^evt-ws-taxonomy-landscape-issue-50]. It serves as a precursor to the contrast term `operationally conformant` [^evt-ws-taxonomy-landscape-issue-50].

# Lifecycle History
Proposed in issue #50 of the Taxonomy and Landscape workstream, emerging from claim-scope classifications introduced in the OWASP GenAI-Security-Project agent-control-standard discussions [^evt-ws-taxonomy-landscape-issue-50].

# References
- [Witness Scope](../taxonomy/witness-scope.md)
- [Taxonomy and Landscape Working Group](../working-groups/taxonomy-and-landscape.md)

[^evt-ws-taxonomy-landscape-issue-50]: https://github.com/aaif/ws-taxonomy-landscape/issues/50
