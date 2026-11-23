---
type: working-group
title: Workflows and Process Integration Working Group
description: AAIF technical working group defining shared workflow models, common
  execution semantics, and reference architectures for agent orchestration.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/reporting/2026-07-report.md
tags:
- workflows
- orchestration
- architecture
- working-group
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:10:57.892768+00:00'
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
The Workflows & Process Integration Working Group (WG Workflows & Process Integration) is an Agentic AI Foundation technical body establishing reusable agentic workflow models, execution primitives, and reference architectures [^evt-wg-workflows-and-process-integration-file-fa4050a9f626-89594a26]. The working group is co-chaired by Yaron Schneider (Diagrid) and Adam Seligman (Workato) [^evt-wg-workflows-and-process-integration-file-fa4050a9f626-89594a26].

# Architecture / Specification
The working group structures its deliverables across three coordinated workstreams [^evt-wg-workflows-and-process-integration-file-fa4050a9f626-89594a26]:

- **Reference Architectures**: Led by Mario and Zayne, developing architectural archetypes, structural design principles, and a specification-driven design flow that transforms machine-readable YAML specs into documentation and execution diagrams [^evt-wg-workflows-and-process-integration-file-fa4050a9f626-89594a26]. The workstream established seven execution profiles ranging from 1 (fully deterministic) to 7 (fully agentic), operating under a proposed "least agentic default" architectural principle [^evt-wg-workflows-and-process-integration-file-fa4050a9f626-89594a26].
- **Critical Use Cases**: Led by Kevin Ng (Telus) and Jodee Varney (Cisco) with contributor Rocky Zhang (SAP), cataloging 89 production use cases categorized against structural primitives—including trigger types, human-in-the-loop patterns, agent count, coordination models, and workflow patterns [^evt-wg-workflows-and-process-integration-file-fa4050a9f626-89594a26]. The workstream converged on a shortlist of under 10 reusable patterns, including the [bounded convergence loop](../patterns/bounded-convergence-loop.md) [^evt-wg-workflows-and-process-integration-file-fa4050a9f626-89594a26].
- **Taxonomy Alignment**: Led by Gala, coordinating universal workflow terms and primitive definitions in direct collaboration with the [Taxonomy and Landscape Workstream](../working-groups/taxonomy-and-landscape.md) to prevent cross-group terminology drift [^evt-wg-workflows-and-process-integration-file-fa4050a9f626-89594a26].

# Lifecycle History
In July 2026, the working group validated its specification-driven design pipeline against invoice processing and autonomous maintenance use cases across both default and elevated autonomy profiles [^evt-wg-workflows-and-process-integration-file-fa4050a9f626-89594a26]. Workstream syncs were established bi-weekly alongside the regular plenary to finalize foundation PRs and reconcile primitive vocabularies prior to formal membership votes [^evt-wg-workflows-and-process-integration-file-fa4050a9f626-89594a26].

[^evt-wg-workflows-and-process-integration-file-fa4050a9f626-89594a26]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/reporting/2026-07-report.md
