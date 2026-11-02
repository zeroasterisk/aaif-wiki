---
type: resource
title: Agentic Use Case Inventory
description: Verified production workflow catalog categorizing real-world agent deployments
  across horizontal business functions and vertical industries under strict evidentiary
  standards.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/critical-use-cases/use-case-inventory.md
tags:
- workflows
- use-cases
- production
- taxonomy
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:13:51.697874+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-c10bbaa87c3e-880211ae
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/critical-use-cases/use-case-inventory.md
  author: Jodee Varney
  last_modified: '2026-10-01T07:35:55-07:00'
- id: evt-wg-workflows-and-process-integration-pr-41
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/41
  author: jodeev
  last_modified: '2026-10-01T14:35:56+00:00'
---

# Overview
The Agentic Use Case Inventory is a community-maintained catalog of verified real-world agentic workflows developed by the Workflows & Process Integration Working Group's Critical Use Cases Workstream [^evt-wg-workflows-and-process-integration-file-c10bbaa87c3e-880211ae]. Classified against the multi-dimensional schema defined in `../resources/agentic-use-case-classification.md`, the inventory documents working deployments across horizontal business functions and vertical industries to identify recurring workflow shapes, coordination mechanisms, and failure patterns [^evt-wg-workflows-and-process-integration-file-c10bbaa87c3e-880211ae].

The catalog emphasizes pattern diversity over exhaustive coverage, serving as an empirical reference for working group deliverables rather than a ranked list or normative endorsement [^evt-wg-workflows-and-process-integration-file-c10bbaa87c3e-880211ae].

# Architecture / Specification

## Catalog Structure and Coverage
Workflows are cataloged across structured dimensions including trigger types, human-in-the-loop (HITL) patterns, agent counts, coordination mechanisms, workflow patterns, failure modes, and operational preconditions [^evt-wg-workflows-and-process-integration-file-c10bbaa87c3e-880211ae]. Coverage spans:
- **Cross-Industry / Horizontal**: Sales, marketing, customer support, finance & operations, HR & recruiting, and research & intelligence [^evt-wg-workflows-and-process-integration-file-c10bbaa87c3e-880211ae].
- **Technology & Engineering**: Software engineering, IT / network operations, software development lifecycle (SDLC), and platform engineering [^evt-wg-workflows-and-process-integration-file-c10bbaa87c3e-880211ae].
- **Industry-Specific**: Healthcare, supply chain, legal, education, and real estate [^evt-wg-workflows-and-process-integration-file-c10bbaa87c3e-880211ae].

## Sourcing and Evidentiary Standards
The inventory enforces strict evidentiary tiers for entries to eliminate speculative or unverified claims [^evt-wg-workflows-and-process-integration-pr-41]:
- **Preferred Evidence**: Vendor product documentation or primary announcements citing a named customer production deployment [^evt-wg-workflows-and-process-integration-pr-41].
- **Acceptable Evidence**: Primary vendor product documentation demonstrating strong feature evidence of production deployment at scale when customer names are proprietary [^evt-wg-workflows-and-process-integration-pr-41].
- **Unacceptable Sources**: Secondary blog posts, analyst commentary, academic preprints, market projection statistics, or unsubstantiated individual implementer write-ups [^evt-wg-workflows-and-process-integration-pr-41].

Each entry targets three primary citations, explicitly recording the source date and handling vendor renames or acquisitions to guard against link rot and reference decay [^evt-wg-workflows-and-process-integration-pr-41]. Entries classified as multi-agent require explicit architectural rationale detailing why the problem is inherently or preferentially suited for multi-agent coordination [^evt-wg-workflows-and-process-integration-pr-41].

# Lifecycle History
- **Initial Inventory**: Established by the Critical Use Cases Workstream to ground workflow pattern specifications [^evt-wg-workflows-and-process-integration-file-c10bbaa87c3e-880211ae].
- **Source Verification & Cleanup**: In PR #41, secondary and speculative citations were excised, approval gate terminology harmonized, multi-agent rationales added, and strict primary-source evidentiary standards instituted [^evt-wg-workflows-and-process-integration-pr-41].

[^evt-wg-workflows-and-process-integration-file-c10bbaa87c3e-880211ae]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/critical-use-cases/use-case-inventory.md
[^evt-wg-workflows-and-process-integration-pr-41]: https://github.com/aaif/wg-workflows-and-process-integration/pull/41
