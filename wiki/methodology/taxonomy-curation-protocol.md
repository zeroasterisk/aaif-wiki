---
type: methodology
title: Taxonomy Curation and Disambiguation Protocol
description: Structured methodology defining term admission criteria, conflict resolution,
  and the Paired Contrast Disambiguation Protocol for the AAIF Taxonomy.
resource: https://github.com/aaif/ws-taxonomy-landscape/blob/09a1b58155e0789614835fbd1e75005c6c337ee3/CONTRIBUTING.md
tags:
- taxonomy
- governance
- workflow
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-flash-latest
  at: '2026-09-21T10:10:35.967237+00:00'
sources:
- id: evt-ws-taxonomy-landscape-file-eca12c0a30e2-333c16a8
  resource: https://github.com/aaif/ws-taxonomy-landscape/blob/09a1b58155e0789614835fbd1e75005c6c337ee3/CONTRIBUTING.md
  author: Julianna Langston
  last_modified: '2026-09-16T13:39:37-04:00'
- id: evt-ws-taxonomy-landscape-file-a54ff182c7e8-35ff909a
  resource: https://github.com/aaif/ws-taxonomy-landscape/blob/09a1b58155e0789614835fbd1e75005c6c337ee3/AGENTS.md
  author: Julianna Langston
  last_modified: '2026-09-16T13:39:37-04:00'
---

# Overview
The Taxonomy Curation Protocol governs the admission, definition, and relationship mapping of terms within the AAIF shared vocabulary, ensuring vendor neutrality and cross-working-group consensus [^evt-ws-taxonomy-landscape-file-eca12c0a30e2-333c16a8].

# Architecture / Specification
The protocol is guided by several core principles:

1.  **Horizontal Index Principle:** The workstream focuses on consolidating, harmonizing, and standardizing glossaries supplied by vertical Working Groups (WGs). It defines the 'Shared Index' (foundational, cross-cutting terms affecting ≥ 2 WGs) while leaving 'Domain Payload' (specialized definitions, code variables) to individual WG repositories [^evt-ws-taxonomy-landscape-file-a54ff182c7e8-35ff909a].

2.  **Paired Contrast Disambiguation Protocol:** When reviewing terms that are look-alikes or adjacent contrasts (e.g., *Tool* vs. *Skill*), explicit disambiguation is mandatory. This requires defining counterpart boundaries in the term's definition and linking the pair using `relatedTerms` or `contrastsWith` fields in the schema [^evt-ws-taxonomy-landscape-file-a54ff182c7e8-35ff909a].

3.  **Anti-Erasure Guardrails:** Concepts cannot be quietly deleted or folded into an alias without explicit written sign-off from the owning WG's Domain Editor. Look-alike terms representing distinct operational models must be preserved as separate entities [^evt-ws-taxonomy-landscape-file-a54ff182c7e8-35ff909a] [^evt-ws-taxonomy-landscape-file-eca12c0a30e2-333c16a8].

# References
See also: [../working-groups/taxonomy-and-landscape.md].

[^evt-ws-taxonomy-landscape-file-a54ff182c7e8-35ff909a]: https://github.com/aaif/ws-taxonomy-landscape/blob/09a1b58155e0789614835fbd1e75005c6c337ee3/AGENTS.md
[^evt-ws-taxonomy-landscape-file-eca12c0a30e2-333c16a8]: https://github.com/aaif/ws-taxonomy-landscape/blob/09a1b58155e0789614835fbd1e75005c6c337ee3/CONTRIBUTING.md
