---
type: taxonomy
title: Self-Reported
description: Taxonomy classification denoting observation records emitted directly
  by an artifact about itself without independent verification outside its write path.
resource: https://github.com/aaif/ws-taxonomy-landscape/issues/52
tags:
- taxonomy
- observability
- evidence
- provenance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:18:02.502024+00:00'
sources:
- id: evt-ws-taxonomy-landscape-issue-52
  resource: https://github.com/aaif/ws-taxonomy-landscape/issues/52
  author: narko4u
  last_modified: '2026-08-29T23:51:33+00:00'
---

# Overview
In the AAIF taxonomy, **self-reported** denotes a property of an observation or record that asserts the described artifact generated the telemetry or claim about itself, without independent verification from outside the artifact's own write path[^evt-ws-taxonomy-landscape-issue-52]. A record can be well-formed and schema-compliant yet remain self-reported, distinguishing it from records captured through external observation or a substrate-level vantage point[^evt-ws-taxonomy-landscape-issue-52].

# Architecture / Specification
The concept establishes the foundational boundary separating conventional application observability from tamper-evident audit evidence[^evt-ws-taxonomy-landscape-issue-52]:
- **Write Path Confinement**: Because an OpenTelemetry span is emitted directly by the runtime it describes, its contents are inherently self-reported regardless of syntax correctness[^evt-ws-taxonomy-landscape-issue-52].
- **Substrate Vantage Contrast**: External, substrate-vantage observations or hardware-attested captures operate outside the target system's execution context, providing independent corroboration[^evt-ws-taxonomy-landscape-issue-52].
- **Verifier Testing**: Originating in OWASP GenAI Security Project agent-control-standard discussions, the term defines the property under test for verifier-side security primitives and operational conformance checks[^evt-ws-taxonomy-landscape-issue-52].

Within the broader AAIF taxonomy framework, this property pairs against external observation models and informs evaluations of [evidence strength labels](../taxonomy/evidence-strength-labels.md) and [evidence records](../standards/evidence-record-spec.md).

# Lifecycle History
- **August 2026**: Proposed in [Taxonomy & Landscape](../working-groups/taxonomy-and-landscape.md) issue #52 for the cross-workgroup taxonomy definitions pass[^evt-ws-taxonomy-landscape-issue-52].

# References
- ws-taxonomy-landscape Issue #52: Define: self-reported

[^evt-ws-taxonomy-landscape-issue-52]: https://github.com/aaif/ws-taxonomy-landscape/issues/52
