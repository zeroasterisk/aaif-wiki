---
type: resource
title: Agentic AI Landscape
description: Interactive ecosystem catalog and market map tracking open-source and
  commercial technologies across agent frameworks, protocols, runtimes, and governance
  tooling.
resource: https://github.com/aaif/ws-taxonomy-landscape/pull/27
tags:
- landscape
- catalog
- taxonomy
- ecosystem
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:34:13.154434+00:00'
sources:
- id: evt-ws-taxonomy-landscape-pr-27
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/27
  author: thc1006
  last_modified: '2026-10-12T03:30:56+00:00'
- id: evt-ws-taxonomy-landscape-pr-28
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/28
  author: thc1006
  last_modified: '2026-10-12T03:30:59+00:00'
---

# Overview

The Agentic AI Landscape is an interactive ecosystem catalog and market map managed by the [Taxonomy and Landscape Workstream](../working-groups/taxonomy-and-landscape.md). It provides an authoritative, structured directory of open-source frameworks, commercial platforms, infrastructure services, and emerging standards across the agentic artificial intelligence ecosystem [^evt-ws-taxonomy-landscape-pr-27].

# Architecture / Specification

The landscape data model and publishing pipeline rely on declarative YAML configuration coupled with automated validation and client-side rendering [^evt-ws-taxonomy-landscape-pr-28]:

- **Data Schema (`landscape.yml`)**: Entries are grouped hierarchically into categories and subcategories. Each item defines mandatory fields (`name`, `homepage_url`, `description`, `project`) and optional repository locations (`repo_url`) conforming to foundation schema specifications [^evt-ws-taxonomy-landscape-pr-27].
- **CI Validation Engine (`validate-landscape.mjs`)**: Automated pull request testing parses catalog files using the same `js-yaml` version and `FAILSAFE_SCHEMA` options as the browser client, enforcing strict type consistency and preventing unquoted string mismatches [^evt-ws-taxonomy-landscape-pr-28].
- **Denial-of-Service and Boundary Limits**: The validator enforces strict defense-in-depth resource bounds, including a 512 KB file size cap, a 500-item maximum, a 5,000-object/array graph limit, and a 20,000-reference traversal budget [^evt-ws-taxonomy-landscape-pr-28]. It prohibits YAML merge keys, cyclic object aliases, and control characters [^evt-ws-taxonomy-landscape-pr-28].
- **Symlink Prevention**: An automated pre- and post-assembly check (`check-no-symlinks.sh`) prevents committed symbolic links from exposing runner-local files during artifact packing and deployment via GitHub Pages [^evt-ws-taxonomy-landscape-pr-28].
- **Browser Client Search**: The client application (`app.js`) executes search highlighting using bounded regular expression walks with Unicode case folding, preventing input injection and avoiding unconstrained string allocations [^evt-ws-taxonomy-landscape-pr-28].

# Lifecycle History

Originally deployed to map the emerging AI agent tooling ecosystem, the landscape expanded following the creation of the AAIF. Foundational projects donated at launch—including [Goose](../resources/goose.md) and Model Context Protocol—were integrated into member project categories such as Autonomous Agent Frameworks [^evt-ws-taxonomy-landscape-pr-27]. Continued growth prompted hardening of the intake pipeline, introducing strict static validation, parsing limits, and symlink protection to ensure repository integrity and rendering safety [^evt-ws-taxonomy-landscape-pr-28].

# References

- [Taxonomy and Landscape Repository](https://github.com/aaif/ws-taxonomy-landscape)

[^evt-ws-taxonomy-landscape-pr-27]: https://github.com/aaif/ws-taxonomy-landscape/pull/27
[^evt-ws-taxonomy-landscape-pr-28]: https://github.com/aaif/ws-taxonomy-landscape/pull/28
