---
type: taxonomy
title: Tool Definition Verification
description: Process of validating the authenticity, schema integrity, and behavioral
  claims of an agent tool definition or manifest prior to runtime admission.
resource: https://github.com/aaif/ws-taxonomy-landscape/pull/88
tags:
- taxonomy
- security
- verification
- tools
- identity
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:20:48.792446+00:00'
sources:
- id: evt-ws-taxonomy-landscape-pr-88
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/88
  author: GeeksikhSecurity
  last_modified: '2026-10-09T12:40:04+00:00'
---

# Overview
Tool definition verification (also referred to as tools manifest verification) is the evaluation process of checking an agent tool's schema, metadata, description, and source integrity before admitting it into an agent runtime or context window.[^evt-ws-taxonomy-landscape-pr-88] It establishes that tool capabilities conform to expected schemas, declare explicit parameter boundaries, and originate from verified publishers.[^evt-ws-taxonomy-landscape-pr-88]

In the AAIF taxonomy, tool definition verification contrasts with attestation: attestation refers to the generation of signed assertions regarding an artifact's provenance or state, whereas verification is the operational evaluation performed by an agent runtime or operator against policy constraints before use.[^evt-ws-taxonomy-landscape-pr-88]

# Architecture / Specification
Tool definition verification guards against [tool poisoning](tool-poisoning.md) and [rug pulls](rug-pull.md) through several checks:
- Verifying cryptographic signatures on tool manifests and upstream packages.[^evt-ws-taxonomy-landscape-pr-88]
- Semantic and static analysis of natural language descriptions to detect prompt injection or deceptive documentation.[^evt-ws-taxonomy-landscape-pr-88]
- Schema validation ensuring that declared input parameters and return types adhere to assigned boundary policies.[^evt-ws-taxonomy-landscape-pr-88]
- Binding immutable content hashes to prevent unauthenticated runtime endpoint drift.[^evt-ws-taxonomy-landscape-pr-88]

# Lifecycle History
Proposed in PR #88 of the [Taxonomy and Landscape Workstream](../working-groups/taxonomy-and-landscape.md) as a cross-WG taxonomy term shared between the [Security and Privacy Working Group](../working-groups/security-and-privacy.md) and [Identity and Trust Working Group](../working-groups/identity-and-trust.md).[^evt-ws-taxonomy-landscape-pr-88]

[^evt-ws-taxonomy-landscape-pr-88]: https://github.com/aaif/ws-taxonomy-landscape/pull/88
