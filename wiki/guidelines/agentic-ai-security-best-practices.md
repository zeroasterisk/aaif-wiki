---
type: guideline
title: Agentic AI Security Best Practices
description: Practical builder guidance covering pre-execution interception hooks,
  gateway checkpoints, sandbox boundaries, and cryptographic skill provenance.
resource: https://github.com/aaif/wg-security-and-privacy/pull/49
tags:
- aaif
- security
- best-practices
- c2pa
- provenance
- skills
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:35:22.654393+00:00'
sources:
- id: evt-wg-security-and-privacy-pr-49
  resource: https://github.com/aaif/wg-security-and-privacy/pull/49
  author: mrappard
  last_modified: '2026-11-08T18:42:20+00:00'
---

# Overview
The Agentic AI Security Best Practices guide provides practical defensive controls, architectural hardening patterns, and supply-chain verification standards for engineering teams deploying autonomous agents [^evt-wg-security-and-privacy-pr-49]. Developed within the [Security & Privacy Working Group](../working-groups/security-and-privacy.md), the guideline outlines multi-tier verification baselines for runtime sandboxes, model gateway policy checkpoints, and extension packages such as Model Context Protocol servers and [Agent Skills](../standards/agent-skills.md) [^evt-wg-security-and-privacy-pr-49].

# Architecture / Specification

## Multi-Tier Supply-Chain Provenance
The framework establishes tiered controls for package ingestion and tool verification:
- **Build-Linked Artifact Provenance**: Requires MCP server packages to provide cryptographic attestations via npm provenance, PyPI attestations, or cosign signatures linking artifacts to immutable build pipelines [^evt-wg-security-and-privacy-pr-49].
- **Cryptographic Skill Provenance (Tier 3 Proposal)**: An experimental tier proposes verifying skill publisher authenticity through C2PA Content Credentials [^evt-wg-security-and-privacy-pr-49]. The mechanism binds the `SKILL.md` manifest to a validated publisher certificate via frontmatter manifest references and incorporates a digest of subsidiary assets in `metadata` to protect executable scripts [^evt-wg-security-and-privacy-pr-49].

## Security Boundaries and Cryptographic Limitations
The proposal notes critical threat boundary limitations regarding content credentials [^evt-wg-security-and-privacy-pr-49]:
- **Identity vs. Safety**: Cryptographic signatures validate publisher identity and manifest integrity; they do not attest to runtime behavioral safety or absence of malicious logic [^evt-wg-security-and-privacy-pr-49].
- **Stripped Credential Detection**: Because stripped C2PA credentials appear unsigned, registry catalogs must record expected signing identities alongside hash pins to prevent downgrade attacks [^evt-wg-security-and-privacy-pr-49].
- **Validation Scope**: Standard C2PA validators inspect only the primary manifest (`SKILL.md`), necessitating extended validation routines across the skill package directory structure [^evt-wg-security-and-privacy-pr-49].

[^evt-wg-security-and-privacy-pr-49]: https://github.com/aaif/wg-security-and-privacy/pull/49
