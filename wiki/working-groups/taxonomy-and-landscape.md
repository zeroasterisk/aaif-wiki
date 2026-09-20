---
type: working-group
title: Taxonomy & Landscape Workstream
description: Cross-working group initiative maintaining unified agentic AI taxonomy
  vocabularies, landscape maps, and shared definitions across AAIF working groups.
resource: https://github.com/aaif/ws-taxonomy-landscape/blob/09a1b58155e0789614835fbd1e75005c6c337ee3/AGENTS.md
tags:
- taxonomy
- landscape
- governance
- workstream
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T18:03:32.041820+00:00'
sources:
- id: evt-ws-taxonomy-landscape-file-a54ff182c7e8-35ff909a
  resource: https://github.com/aaif/ws-taxonomy-landscape/blob/09a1b58155e0789614835fbd1e75005c6c337ee3/AGENTS.md
  author: Julianna Langston
  last_modified: '2026-09-16T13:39:37-04:00'
- id: evt-ws-taxonomy-landscape-file-b33563055168-07a3beac
  resource: https://github.com/aaif/ws-taxonomy-landscape/blob/09a1b58155e0789614835fbd1e75005c6c337ee3/README.md
  author: Julianna Langston
  last_modified: '2026-09-16T13:39:37-04:00'
- id: evt-ws-taxonomy-landscape-file-eca12c0a30e2-333c16a8
  resource: https://github.com/aaif/ws-taxonomy-landscape/blob/09a1b58155e0789614835fbd1e75005c6c337ee3/CONTRIBUTING.md
  author: Julianna Langston
  last_modified: '2026-09-16T13:39:37-04:00'
- id: evt-ws-taxonomy-landscape-pr-61
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/61
  author: julianna-ciq
  last_modified: '2026-09-16T17:39:38+00:00'
---

# Overview
The Taxonomy & Landscape Workstream serves as the horizontal architectural bridge across all Agentic AI Foundation (AAIF) Technical Working Groups, curating an authoritative pre-competitive vocabulary and an ecosystem market map[^evt-ws-taxonomy-landscape-file-a54ff182c7e8-35ff909a] [^evt-ws-taxonomy-landscape-file-b33563055168-07a3beac]. The workstream is led by Co-Chairs Junjie Bu (Google) and Gala Malbasic (Bloomberg)[^evt-ws-taxonomy-landscape-file-b33563055168-07a3beac].

# Architecture / Specification
The workstream operates under specific architectural guardrails and governance procedures:
- **Horizontal Index vs. Domain Payload**: The workstream consolidates cross-cutting terms affecting two or more working groups into a shared index, while deep domain-specific payloads and protocols remain in vertical WG repositories[^evt-ws-taxonomy-landscape-file-a54ff182c7e8-35ff909a].
- **Taxonomy-First Contribution Scope**: Contribution is currently restricted to the Taxonomy; Landscape contributions are deferred on the future roadmap until review processes are finalized[^evt-ws-taxonomy-landscape-pr-61] [^evt-ws-taxonomy-landscape-file-eca12c0a30e2-333c16a8].
- **Curation Workflow**: Pull requests require review and consensus approval from at least two or three [Domain Editors](../taxonomy/domain-editor.md) representing different working groups before maintainers perform administrative merge[^evt-ws-taxonomy-landscape-file-eca12c0a30e2-333c16a8].
- **Epistemological Disambiguation & Anti-Erasure**: Adjacent contrasting terms require explicit boundary differentiation and associative linking (`relatedTerms` / `contrastsWith`), and terms cannot be aliased or removed without written Domain Editor sign-off[^evt-ws-taxonomy-landscape-file-a54ff182c7e8-35ff909a] [^evt-ws-taxonomy-landscape-file-eca12c0a30e2-333c16a8].

# Lifecycle History
- **PR #61 (Merged)**: Explicitly defined taxonomy-only contribution scope, deferring landscape-focused PRs until dedicated contribution processes are approved[^evt-ws-taxonomy-landscape-pr-61].

[^evt-ws-taxonomy-landscape-file-a54ff182c7e8-35ff909a]: https://github.com/aaif/ws-taxonomy-landscape/blob/09a1b58155e0789614835fbd1e75005c6c337ee3/AGENTS.md
[^evt-ws-taxonomy-landscape-file-b33563055168-07a3beac]: https://github.com/aaif/ws-taxonomy-landscape/blob/09a1b58155e0789614835fbd1e75005c6c337ee3/README.md
[^evt-ws-taxonomy-landscape-file-eca12c0a30e2-333c16a8]: https://github.com/aaif/ws-taxonomy-landscape/blob/09a1b58155e0789614835fbd1e75005c6c337ee3/CONTRIBUTING.md
[^evt-ws-taxonomy-landscape-pr-61]: https://github.com/aaif/ws-taxonomy-landscape/pull/61
