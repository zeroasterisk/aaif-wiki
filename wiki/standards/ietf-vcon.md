---
type: standard
title: IETF vCon (Virtualized Conversations)
description: JSON container standardizing conversational data records, media references,
  and proposed AI agent interaction extensions.
resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/ietf-vcon.yaml
tags:
- external
- standard
- ietf
- conversations
- audit
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T01:53:06.132433+00:00'
sources:
- id: evt-ext-frmoretto-agentic-standards-map-85d122-file-c6d9d545dc25-2a247e54
  resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/ietf-vcon.yaml
  author: frmoretto
  last_modified: '2026-10-14T06:46:06+02:00'
---

# Overview
vCon is a conversational data container format stewarded by the Internet Engineering Task Force (IETF) within the Applications and Real-Time Area [^evt-ext-frmoretto-agentic-standards-map-85d122-file-c6d9d545dc25-2a247e54]. The standard specifies a JSON container structure to package and reference conversational data, including call metadata, recordings, exchanged text, transcriptions, translations, and analytical annotations [^evt-ext-frmoretto-agentic-standards-map-85d122-file-c6d9d545dc25-2a247e54]. Within agentic systems, vCon is proposed as the underlying storage format for interaction auditing under [IETF AUDIT](../standards/ietf-audit.md) [^evt-ext-frmoretto-agentic-standards-map-85d122-file-c6d9d545dc25-2a247e54].

# Architecture / Specification
- **Core Container Format**: Defined in `draft-ietf-vcon-vcon-core`, vCon encapsulates session events, participant history, and references to external files, requiring URL and content hash parameters for externally stored objects [^evt-ext-frmoretto-agentic-standards-map-85d122-file-c6d9d545dc25-2a247e54].
- **AI Agent Extension**: Proposed rechartering text incorporates an AI Agent Extension covering tool call requests and responses, foundation model metadata, token usage metrics, prompts, and reasoning traces [^evt-ext-frmoretto-agentic-standards-map-85d122-file-c6d9d545dc25-2a247e54].
- **Scope Boundaries**: Real-time streaming or updating of conversational data and the definition of a new object security model are explicitly out of scope [^evt-ext-frmoretto-agentic-standards-map-85d122-file-c6d9d545dc25-2a247e54].

# Lifecycle History
- 2026-03-18: Change of Area Director recorded in the IETF datatracker (approval date of `charter-ietf-vcon-01` not recorded in the source) [^evt-ext-frmoretto-agentic-standards-map-85d122-file-c6d9d545dc25-2a247e54].
- 2026-09-07: Publication of Standards Track draft `draft-ietf-vcon-vcon-core-04` [^evt-ext-frmoretto-agentic-standards-map-85d122-file-c6d9d545dc25-2a247e54].
- 2026-10-08: Working group interim meeting merges repository PR #37 to incorporate AI agent interaction record extensions into the draft charter text [^evt-ext-frmoretto-agentic-standards-map-85d122-file-c6d9d545dc25-2a247e54].

# References
- [ietf-wg-vcon/draft-ietf-vcon-vcon-core Repository](https://github.com/ietf-wg-vcon/draft-ietf-vcon-vcon-core)
- [PR #37: AI Agent Charter Update](https://github.com/ietf-wg-vcon/draft-ietf-vcon-vcon-core/pull/37)

[^evt-ext-frmoretto-agentic-standards-map-85d122-file-c6d9d545dc25-2a247e54]: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/ietf-vcon.yaml
