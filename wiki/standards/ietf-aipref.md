---
type: standard
title: IETF AI Preferences
description: IETF protocol specifications defining vocabularies and attachment mechanisms
  for expressing content processing preferences for AI models.
resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/ietf-aipref.yaml
tags:
- external
- standard
- ietf
- preferences
- policy
- vocabulary
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T01:45:26.365731+00:00'
sources:
- id: evt-ext-frmoretto-agentic-standards-map-85d122-file-6c3b5927dfe6-b05dc83d
  resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/ietf-aipref.yaml
  author: frmoretto
  last_modified: '2026-10-14T06:28:09+02:00'
---

# Overview
IETF AI Preferences is a standardization initiative stewarded by the Internet Engineering Task Force (IETF) within the aipref Working Group[^evt-ext-frmoretto-agentic-standards-map-85d122-file-6c3b5927dfe6-b05dc83d]. Cataloged by independent researcher Francesco Marinoni Moretto, the working group develops building blocks enabling publishers and content owners to express machine-readable preferences regarding how their content is collected, indexed, and processed for AI model development, fine-tuning, and inference[^evt-ext-frmoretto-agentic-standards-map-85d122-file-6c3b5927dfe6-b05dc83d].

# Architecture / Specification
The standardization track is split across two core documents:
1. **Vocabulary Draft (`draft-ietf-aipref-vocab`)**: Defines terms and consent categories governing AI data collection and usage, including specific clauses for scenarios where assets are not directly provided by end users[^evt-ext-frmoretto-agentic-standards-map-85d122-file-6c3b5927dfe6-b05dc83d].
2. **Attach Draft (`draft-ietf-aipref-attach`)**: Specifies protocol binding mechanisms to attach preference assertions to web resources and HTTP response headers[^evt-ext-frmoretto-agentic-standards-map-85d122-file-6c3b5927dfe6-b05dc83d].

The specification boundary explicitly treats caching, proxying, and embedding implementations as implementation details outside the normative document scope[^evt-ext-frmoretto-agentic-standards-map-85d122-file-6c3b5927dfe6-b05dc83d]. The working group maintains coordination touchpoints with parallel browser efforts in the W3C[^evt-ext-frmoretto-agentic-standards-map-85d122-file-6c3b5927dfe6-b05dc83d].

# Lifecycle History
- **2026-08-19**: Publication of `draft-ietf-aipref-attach-05` specifying attachment protocols[^evt-ext-frmoretto-agentic-standards-map-85d122-file-6c3b5927dfe6-b05dc83d].
- **2026-08-26**: Participant proposal submitted to introduce an explicit `ai-embed` category for embeddings and index copies[^evt-ext-frmoretto-agentic-standards-map-85d122-file-6c3b5927dfe6-b05dc83d].
- **2026-09-14**: Publication of `draft-ietf-aipref-vocab-08` updating normative preference terms[^evt-ext-frmoretto-agentic-standards-map-85d122-file-6c3b5927dfe6-b05dc83d].

# References
- [Francesco Marinoni Moretto: IETF AIPREF Entry](https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/ietf-aipref.yaml)

[^evt-ext-frmoretto-agentic-standards-map-85d122-file-6c3b5927dfe6-b05dc83d]: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/ietf-aipref.yaml
