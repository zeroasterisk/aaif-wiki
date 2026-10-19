---
type: standard
title: IETF AUDIT (Agent Use of Delegation and Interaction Traceability)
description: Proposed IETF auditing and interaction record framework for observable
  agent behaviors and delegated execution.
resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/ietf-audit.yaml
tags:
- external
- ietf
- audit
- vcon
- traceability
- expected-records
- standards
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T01:39:51.865388+00:00'
sources:
- id: evt-ext-frmoretto-agentic-standards-map-85d122-file-0f3c7fb1c947-80cfabe5
  resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/ietf-audit.yaml
  author: frmoretto
  last_modified: '2026-10-14T06:46:06+02:00'
---

# Overview

AUDIT (Agent Use of Delegation and Interaction Traceability) is a proposed IETF working group charter under BoF preparation (not a chartered IETF working group)[^evt-ext-frmoretto-agentic-standards-map-85d122-file-0f3c7fb1c947-80cfabe5]. It targets the standardization of verifiable audit records documenting observable agent actions, delegated authorities, and tool interactions when agents act on behalf of users or systems[^evt-ext-frmoretto-agentic-standards-map-85d122-file-0f3c7fb1c947-80cfabe5].

Related work includes the signed execution schema in [Trace](../standards/trace.md) and the verifiable claims in [Evidence Record Spec](../standards/evidence-record-spec.md).

# Architecture / Specification

The AUDIT initiative addresses cross-domain traceability for delegated agentic tasks[^evt-ext-frmoretto-agentic-standards-map-85d122-file-0f3c7fb1c947-80cfabe5]:
- **Scope of Auditing**: Focuses on the observable runtime behavior of agents, including user intent declarations, tool invocations, accepted or declined actions, and exchanged inter-agent messages[^evt-ext-frmoretto-agentic-standards-map-85d122-file-0f3c7fb1c947-80cfabe5].
- **Record Container Alignment**: Proposes leveraging the IETF vCon conversation format as an interaction record structure, with extensions for AI-specific interaction primitives[^evt-ext-frmoretto-agentic-standards-map-85d122-file-0f3c7fb1c947-80cfabe5].
- **Expected Records Framework**: Evaluates expected record declarations where each participating domain commits to produce specific evidence; audits distinguish true absence from incomplete observation, ineligible holders, or actions refused prior to execution[^evt-ext-frmoretto-agentic-standards-map-85d122-file-0f3c7fb1c947-80cfabe5].
- **Explicit Scope Boundaries**: Auditing the internal parameters, training datasets, or inference logic of underlying AI models is explicitly excluded, as is the introduction of novel identity primitives[^evt-ext-frmoretto-agentic-standards-map-85d122-file-0f3c7fb1c947-80cfabe5].

# Lifecycle History

- **2026-09-18**: BoF preparation repository updated the proposed session agenda to include e-commerce and multi-agent financial transaction use cases[^evt-ext-frmoretto-agentic-standards-map-85d122-file-0f3c7fb1c947-80cfabe5].

# References

- [IETF AUDIT in Agentic Standards Map](https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/ietf-audit.yaml)[^evt-ext-frmoretto-agentic-standards-map-85d122-file-0f3c7fb1c947-80cfabe5]

[^evt-ext-frmoretto-agentic-standards-map-85d122-file-0f3c7fb1c947-80cfabe5]: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/ietf-audit.yaml
