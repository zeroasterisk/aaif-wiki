---
type: working-group
title: Workflows and Process Integration Working Group
description: AAIF technical working group establishing shared workflow execution models,
  reference architectures, boundary patterns, and activity-based composition taxonomies.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/reporting/2026-08-report.md
tags:
- working-group
- workflows
- architecture
- taxonomy
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:07:11.194936+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/reporting/2026-08-report.md
  author: Yaron Schneider
  last_modified: '2026-09-27T17:45:13-07:00'
- id: evt-wg-workflows-and-process-integration-pr-38
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/38
  author: yaron2
  last_modified: '2026-09-28T00:45:18+00:00'
---

# Overview
The Workflows and Process Integration Working Group (WG Workflows & Process Integration) develops vendor-neutral architectural patterns, execution primitives, and reference architectures for agentic workflows [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7]. Chaired by Yaron Schneider and Adam Seligman, the group standardizes how agentic systems structure activities, enforce execution boundaries, and coordinate human and automated actors across enterprise environments [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7].

# Architecture / Specification
The working group organizes its technical outputs across three primary workstreams [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7]:
- **Reference Architectures**: Standardizes formal architectural blueprints, including [Single-Agent Human Approval](../architectures/single-agent-human-approval.md) ("human-approved operation") and [Bounded Autonomous Remediation](../architectures/bounded-autonomous-remediation.md) [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7]. Architectures are validated using a four-outcome classification model: validated, partial, candidate, or no fit [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7].
- **Taxonomy**: Curates core execution vocabulary, establishing "activity" as an atomic unit and defining workflows as compositions of activities to eliminate circular definitions [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7]. Evaluation and gate terminology are scoped out to security, observability, and reliability groups [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7].
- **Critical Use Cases**: Evaluates production agent workflows and aligns real-world operational sequences with standardized primitives and taxonomy [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7].

The working group enforces a standing contribution policy capping pull requests at approximately ten files to preserve reviewability [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7].

# Lifecycle History
In August 2026, the working group delivered its Phase One Core Terms draft, becoming the first AAIF working group to ship an approved asset [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7]. During the same period, architecture principles and the first reference architecture were merged, and pull request size limits were instituted to manage complex topologies [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7].

[^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/reporting/2026-08-report.md
