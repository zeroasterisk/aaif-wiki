---
type: reference-architecture
title: Single-Agent Human Approval Reference Architecture
description: Reference architecture ensuring protected actions only execute following
  explicit human review and authorization of immutable proposals.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/36
tags:
- reference-architecture
- human-in-the-loop
- workflows
- approval
- patterns
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T10:05:42.946415+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-pr-36
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/36
  author: itafra
  last_modified: '2026-09-03T15:22:48+00:00'
---

# Overview

The Single-Agent Human Approval Reference Architecture defines patterns and execution boundaries where an autonomous agent proposes actions or content modifications, but protected execution or publication only occurs after explicit human authorization[^evt-wg-workflows-and-process-integration-pr-36].

# Architecture / Specification

The architecture establishes three distinct operational boundaries[^evt-wg-workflows-and-process-integration-pr-36]:

1. **Proposal Generation**: The agent operates autonomously within its tools and context to assemble candidate changes or artifacts (such as draft documentation or copy), emitted as an immutable proposal.
2. **Human Approval Gate**: The proposal is held in a durable waiting state, presented to an authorized human principal via an explicit approval interface.
3. **Publication / Execution Boundary**: Upon verified authorization by the human reviewer, a deterministic execution engine applies or publishes the changes.

## Validated Scenarios

The Workflows and Process Integration WG validates this architecture against standard content operational use cases[^evt-wg-workflows-and-process-integration-pr-36]:
- **FAQ and Knowledge Base Updates**: Drafting and validating edits to internal and public knowledge repositories before publication.
- **Release Notes Generation**: Synthesizing software changelogs and pull request histories into customer-facing release notes.
- **Listing and Catalog Descriptions**: Generating and updating marketplace listing metadata subject to editorial review.

# References

- Cross-references: [../patterns/human-approval-gate.md](../patterns/human-approval-gate.md), [../patterns/proposal-execution-split.md](../patterns/proposal-execution-split.md), [../working-groups/workflows-and-process-integration.md](../working-groups/workflows-and-process-integration.md).

[^evt-wg-workflows-and-process-integration-pr-36]: https://github.com/aaif/wg-workflows-and-process-integration/pull/36
