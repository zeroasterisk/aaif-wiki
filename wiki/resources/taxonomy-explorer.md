---
type: resource
title: Taxonomy Explorer and Term Wizard
description: Zero-backend browser application and wizard for browsing AAIF taxonomy
  terms and authoring schema-compliant pull requests.
resource: https://github.com/aaif/ws-taxonomy-landscape/blob/719905a88f11ab6846080313dfe4b8c423411235/taxonomy/README.md
tags:
- taxonomy
- tooling
- open-source
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:38:51.049663+00:00'
sources:
- id: evt-ws-taxonomy-landscape-file-62f724d00262-cc94b3ad
  resource: https://github.com/aaif/ws-taxonomy-landscape/blob/719905a88f11ab6846080313dfe4b8c423411235/taxonomy/README.md
  author: Matthew Khouzam
  last_modified: '2026-10-28T16:19:04-04:00'
---

# Overview

The Taxonomy Explorer and Term Wizard is a zero-backend, single-page web application hosted within the [Taxonomy and Landscape Workstream](../working-groups/taxonomy-and-landscape.md) repository that enables contributors to browse terms and submit standardized pull requests without local development tooling[^evt-ws-taxonomy-landscape-file-62f724d00262-cc94b3ad]. Served entirely from static files (`index.html` and `taxonomy-data.js`), the tool bundles catalog search, relational mindmaps, AI-assisted authoring, and token-free GitHub PR submission workflows[^evt-ws-taxonomy-landscape-file-62f724d00262-cc94b3ad].

# Architecture / Specification

The utility is structured around client-side execution, offline accessibility, and strict validation checks to maintain taxonomy integrity according to the [taxonomy-contribution-guide](../guidelines/taxonomy-contribution-guide.md)[^evt-ws-taxonomy-landscape-file-62f724d00262-cc94b3ad].

### Data Storage and Execution
Taxonomy definitions are assigned directly to `window.AAIF_TAXONOMY` within `taxonomy-data.js`[^evt-ws-taxonomy-landscape-file-62f724d00262-cc94b3ad]. Loading the script directly avoids server-side rendering, cross-origin resource sharing (CORS) limits, and raw repository API quotas[^evt-ws-taxonomy-landscape-file-62f724d00262-cc94b3ad].

### Exploration and Term Visualization
The browsing component surfaces terms through search queries, categorical filters, responsive grid card layouts, detailed split-pane inspectors, and interactive visual mindmaps reflecting ontological connections[^evt-ws-taxonomy-landscape-file-62f724d00262-cc94b3ad].

### AI-Assisted Proposal Drafting
The wizard includes an optional generation capability backed by the key-less Puter SDK[^evt-ws-taxonomy-landscape-file-62f724d00262-cc94b3ad]:
- **Model Agnosticism**: Provides access to all models made available by the SDK without privileging or defaulting to a single commercial vendor[^evt-ws-taxonomy-landscape-file-62f724d00262-cc94b3ad].
- **Constrained Outputs**: Cross-references and working group associations suggested by LLMs are constrained against existing vocabulary entries; ungrounded suggestions are rejected by validation passes[^evt-ws-taxonomy-landscape-file-62f724d00262-cc94b3ad].
- **Provenance Tracking**: Measures character-level and list-overlap edit distance between the model draft and the contributor's final submission, recording the AI contribution ratio and model tag directly in commit metadata and pull request templates[^evt-ws-taxonomy-landscape-file-62f724d00262-cc94b3ad].
- **Mandatory Review**: Imposes explicit confirmation prompts when an entry is submitted without human modification to prevent silent automated merges[^evt-ws-taxonomy-landscape-file-62f724d00262-cc94b3ad].

### Validation Rules and Ingestion
Before generating a change payload, the wizard enforces strict integrity guardrails[^evt-ws-taxonomy-landscape-file-62f724d00262-cc94b3ad]:
- **Alias Non-Collision**: Prevents an alias from colliding with any primary term slug[^evt-ws-taxonomy-landscape-file-62f724d00262-cc94b3ad].
- **Referential Integrity**: Requires all related or contrasting terms to resolve against pre-existing taxonomy entities[^evt-ws-taxonomy-landscape-file-62f724d00262-cc94b3ad].

Submissions are dispatched either via a token-less in-browser GitHub commit flow targeting the contributor's fork or via an automated shell script (`create-pr.sh`)[^evt-ws-taxonomy-landscape-file-62f724d00262-cc94b3ad].

[^evt-ws-taxonomy-landscape-file-62f724d00262-cc94b3ad]: https://github.com/aaif/ws-taxonomy-landscape/blob/719905a88f11ab6846080313dfe4b8c423411235/taxonomy/README.md
