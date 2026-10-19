---
type: working-group
title: Workflows and Process Integration Working Group
description: AAIF technical working group establishing shared workflow execution models,
  state persistence patterns, human intervention boundaries, and reference architectures.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/reporting/2026-07-report.md
tags:
- working-group
- workflows
- orchestration
- process-integration
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T10:41:41.215948+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-fa4050a9f626-89594a26
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/reporting/2026-07-report.md
  author: Yaron Schneider
  last_modified: '2026-09-28T06:29:14-07:00'
- id: evt-wg-workflows-and-process-integration-pr-24
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/24
  author: yaron2
  last_modified: '2026-09-28T13:29:14+00:00'
---

# Overview

The Workflows and Process Integration Working Group (WG Workflows & Process Integration) develops standard execution models, state persistence patterns, human intervention boundaries, and reference architectures for agentic workflows across the Agentic AI Foundation (AAIF)[^evt-wg-workflows-and-process-integration-file-fa4050a9f626-89594a26]. Co-chaired by Yaron Schneider (Diagrid) and Adam Seligman (Workato), the working group coordinates cross-vendor alignment on orchestrating AI agents across deterministic and autonomous business processes[^evt-wg-workflows-and-process-integration-file-fa4050a9f626-89594a26].

# Architecture / Specification

The working group organizes its technical deliverables into three collaborative workstreams[^evt-wg-workflows-and-process-integration-file-fa4050a9f626-89594a26]:

- **Reference Architectures**: Led by Mario and Zayne, this stream defines seven execution profiles ranging from Profile 1 (fully deterministic) to Profile 7 (fully agentic), applying a proposed "least agentic default" principle[^evt-wg-workflows-and-process-integration-file-fa4050a9f626-89594a26]. It formulates six charter-derived archetypes (including bounded automation and gated operation) and maintains a specification-driven design flow that transforms structured YAML use-case definitions into documentation and diagrams[^evt-wg-workflows-and-process-integration-file-fa4050a9f626-89594a26].
- **Critical Use Cases**: Led by Kevin Ng (Telus) and Jodee Varney (Cisco), with contributions from Rocky Zhang (SAP), this stream categorized 89 production use cases against execution primitives including triggers, human-in-the-loop patterns, agent count, coordination models, and workflow patterns[^evt-wg-workflows-and-process-integration-file-fa4050a9f626-89594a26]. The workflows align against a consolidated catalog of under 10 reusable patterns, including the [bounded convergence loop](../patterns/bounded-convergence-loop.md)[^evt-wg-workflows-and-process-integration-file-fa4050a9f626-89594a26].
- **Taxonomy**: Led by Gala, this stream aligns workflow terminology with the Foundation-wide glossary in collaboration with the [Taxonomy and Landscape Working Group](../working-groups/taxonomy-and-landscape.md), preventing cross-working-group vocabulary divergence and reconciling execution profile parameters against common terms[^evt-wg-workflows-and-process-integration-file-fa4050a9f626-89594a26].

# Lifecycle History

In July 2026, the working group submitted its monthly status report to the [Technical Committee](../governance/technical-committee.md)[^evt-wg-workflows-and-process-integration-pr-24][^evt-wg-workflows-and-process-integration-file-fa4050a9f626-89594a26]. The group reported bi-weekly plenary meetings averaging 25 members alongside active workstream syncs. Target publication schedules for taxonomy and reference architecture deliverables shifted to August 2026 to permit thorough cross-validation of execution profiles, archetypes, and primitives prior to formal TC votes[^evt-wg-workflows-and-process-integration-file-fa4050a9f626-89594a26].

[^evt-wg-workflows-and-process-integration-file-fa4050a9f626-89594a26]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/reporting/2026-07-report.md
[^evt-wg-workflows-and-process-integration-pr-24]: https://github.com/aaif/wg-workflows-and-process-integration/pull/24
