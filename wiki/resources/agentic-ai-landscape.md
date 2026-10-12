---
type: resource
title: Agentic AI Landscape
description: Interactive catalog, schema specification, and CI validation engine mapping
  open-source agentic AI projects, runtimes, and protocols.
resource: https://github.com/aaif/ws-taxonomy-landscape/pull/27
tags:
- landscape
- catalog
- schema
- validation
- taxonomy
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:52:34.061085+00:00'
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
The Agentic AI Landscape is an interactive directory and structured schema that maps open-source agentic AI runtimes, frameworks, protocols, and developer tooling across the Agentic AI Foundation (AAIF) ecosystem [^evt-ws-taxonomy-landscape-pr-27]. Maintained by the Taxonomy and Landscape workstream, the landscape classifies foundation projects—such as the Model Context Protocol (MCP) and Goose—alongside member and community software into defined categories including Autonomous Agent Frameworks [^evt-ws-taxonomy-landscape-pr-27].

# Architecture / Specification
Data integrity and parser security for the underlying `landscape/landscape.yml` registry are enforced through automated schema validation and strict parser bounds [^evt-ws-taxonomy-landscape-pr-28].

## Schema and Validation Invariants
The CI validation suite (`scripts/validate-landscape.mjs`) implements constraints to ensure browser and CLI parser parity and defend against untrusted input expansion [^evt-ws-taxonomy-landscape-pr-28]:
- **Parser Alignment**: Both the Node.js validation runner and client-side application (`app.js`) parse YAML using `js-yaml` configured with `FAILSAFE_SCHEMA` and explicit `maxDepth` limits [^evt-ws-taxonomy-landscape-pr-28]. This prevents numeric type coercion (such as string values coercing into numbers) from triggering client runtime exceptions.
- **Work Budgets**: File size is capped at 512 KB via filesystem `statSync` checks before parsing. Structural limits cap the landscape to 500 items, while traversal is limited to an object graph budget of 5,000 objects/arrays and 20,000 references [^evt-ws-taxonomy-landscape-pr-28].
- **Disallowed Constructs**: Reused object/array nodes (YAML anchors and cyclic aliases), merge keys, and unescaped control/format characters are rejected; only bounded scalar aliases are permitted [^evt-ws-taxonomy-landscape-pr-28].
- **Field Validation**: Items require `name`, `homepage_url`, `description`, and a valid `project` enum value (`member`, `graduated`, or `incubating`), with optional `repo_url` [^evt-ws-taxonomy-landscape-pr-27, ^evt-ws-taxonomy-landscape-pr-28]. All URLs must use HTTPS without user credentials, and item names must be unique under Unicode normalization [^evt-ws-taxonomy-landscape-pr-28].
- **Symlink Protection**: A deployment guard (`scripts/check-no-symlinks.sh`) verifies that no symbolic links exist in sources or build artifacts before packaging with `tar --dereference`, mitigating arbitrary file publication risks [^evt-ws-taxonomy-landscape-pr-28].
- **Search Execution**: The web client performs Unicode-aware regex matching (`u` flag) using a single compiled regular expression and shared match budget across fields to avoid client-side CPU exhaustion [^evt-ws-taxonomy-landscape-pr-28].

# Lifecycle History
The landscape tracks foundation-hosted projects donated at launch, such as Goose and MCP, while coordinating taxonomy classifications for emerging entries like `agentgateway` and `AGENTS.md` [^evt-ws-taxonomy-landscape-pr-27]. Validation automation was introduced to prevent rendering discrepancies and harden data intake against algorithmic complexity vulnerabilities [^evt-ws-taxonomy-landscape-pr-28].

[^evt-ws-taxonomy-landscape-pr-27]: https://github.com/aaif/ws-taxonomy-landscape/pull/27
[^evt-ws-taxonomy-landscape-pr-28]: https://github.com/aaif/ws-taxonomy-landscape/pull/28
