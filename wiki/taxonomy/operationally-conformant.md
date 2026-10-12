---
type: taxonomy
title: Operationally Conformant
description: Taxonomy classification designating a claim asserting that runtime system
  or agent behavior satisfies specification requirements regardless of record schema
  validation.
resource: https://github.com/aaif/ws-taxonomy-landscape/issues/51
tags:
- taxonomy
- compliance
- verification
- specifications
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:28:37.295086+00:00'
sources:
- id: evt-ws-taxonomy-landscape-issue-51
  resource: https://github.com/aaif/ws-taxonomy-landscape/issues/51
  author: narko4u
  last_modified: '2026-09-20T02:33:03+00:00'
---

# Overview
`Operationally conformant` is a taxonomy term defining an assertion that a system or agent behaves in accordance with standard runtime requirements, without asserting whether emitted observation or telemetry records strictly validate against a canonical schema[^evt-ws-taxonomy-landscape-issue-51].

It serves as the paired contrast to [emission-conformant](./emission-conformant.md), which designates the inverse: structural schema validity of emitted records without guaranteeing behavioral adherence[^evt-ws-taxonomy-landscape-issue-51]. Together, the pair decomposes unqualified "conformant" labels to prevent conflating runtime behavior with data formatting.

# Architecture / Specification
The classification emerged from claim-scope vocabularies developed in the OWASP GenAI-Security-Project agent-control-standard discussions regarding witness scope splits[^evt-ws-taxonomy-landscape-issue-51].

- **Assertion target**: Runtime execution dynamics, policy enforcement, and operational behavior.
- **Excluded guarantees**: Syntactic or structural validity of serialization formats or trace records.
- **Relationship**: Paired with [emission-conformant](./emission-conformant.md) to decompose audit claims into independent data and execution dimensions[^evt-ws-taxonomy-landscape-issue-51].

# Lifecycle History
Proposed in `aaif/ws-taxonomy-landscape` issue #51 by the Taxonomy and Landscape Working Group as part of the paired-contrast definitions pass[^evt-ws-taxonomy-landscape-issue-51].

[^evt-ws-taxonomy-landscape-issue-51]: https://github.com/aaif/ws-taxonomy-landscape/issues/51
