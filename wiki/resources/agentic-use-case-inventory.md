---
type: resource
title: Agentic Use Case Inventory
description: Curated catalog of production agent deployments cross-referenced by architectural
  shape, human-in-the-loop model, and verifiable primary source citations.
resource: https://github.com/aaif/wg-workflows-and-process-integration/issues/58
tags:
- use-cases
- workflows
- catalog
- production
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:39:42.950330+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-issue-58
  resource: https://github.com/aaif/wg-workflows-and-process-integration/issues/58
  author: jodeev
  last_modified: '2026-10-29T15:37:04+00:00'
- id: evt-wg-workflows-and-process-integration-issue-59
  resource: https://github.com/aaif/wg-workflows-and-process-integration/issues/59
  author: jodeev
  last_modified: '2026-10-29T15:34:57+00:00'
---

# Overview

The Agentic Use Case Inventory is an evidence-backed repository cataloging verified, real-world AI agent deployments across enterprises and open-source ecosystems [^evt-wg-workflows-and-process-integration-issue-59]. Governed by the Workflows and Process Integration Working Group, every entry maps a deployment against standardized classification dimensions and links to primary source citations demonstrating genuine production usage [^evt-wg-workflows-and-process-integration-issue-59].

# Architecture / Specification

The inventory enforces strict evidentiary standards to ensure catalog integrity:

- **Classification Dimensions**: Each entry records deployment parameters using `../resources/agentic-use-case-classification.md`, categorizing entries by autonomy level, Workflow Shape, and HITL Shape [^evt-wg-workflows-and-process-integration-issue-58].
- **Primary Evidence Rule**: Rows must provide at least one publicly verifiable citation (vendor product documentation, technical whitepaper, or deployment announcement) accompanied by publication or retrieval dates [^evt-wg-workflows-and-process-integration-issue-59].
- **Automated Link Rot Monitoring**: To address citation decay and vendor restructuring, automated recurring workflows inspect URLs in the Notes column [^evt-wg-workflows-and-process-integration-issue-59]. The automation extracts targets, categorizes responses (resolves, redirects, 404, timeouts, or bot-blocked 403s), and generates triage issues when evidence is broken [^evt-wg-workflows-and-process-integration-issue-59].
- **Content Integrity Checks**: Secondary validation evaluates whether surviving endpoints still substantiate original claims via content hash checks or targeted text inspection [^evt-wg-workflows-and-process-integration-issue-59].

# Lifecycle History

Maintained by the Critical Use Cases workstream in `../working-groups/workflows-and-process-integration.md`. Ongoing governance updates focused on automated citation hygiene to sustain evidentiary validity [^evt-wg-workflows-and-process-integration-issue-59] and aligning column terminology with reference architecture guidelines [^evt-wg-workflows-and-process-integration-issue-58].

[^evt-wg-workflows-and-process-integration-issue-58]: https://github.com/aaif/wg-workflows-and-process-integration/issues/58
[^evt-wg-workflows-and-process-integration-issue-59]: https://github.com/aaif/wg-workflows-and-process-integration/issues/59
