---
type: skill
title: Taxonomy Contributions Workflow and Skill
description: Automated agent skill and contributor workflow enforcing SKOS-Lite schemas,
  validation checklists, and maintainer-gated CI testing for taxonomy assets.
resource: https://github.com/aaif/ws-taxonomy-landscape/blob/6ac90f517a064054d4113b3331c8c06e380258b8/.github/workflows/validate-taxonomy.yml
tags:
- taxonomy
- workflow
- validation
- ci-cd
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T10:28:57.202119+00:00'
sources:
- id: evt-ws-taxonomy-landscape-file-eda84dd4e776-0e9c3434
  resource: https://github.com/aaif/ws-taxonomy-landscape/blob/6ac90f517a064054d4113b3331c8c06e380258b8/.github/workflows/validate-taxonomy.yml
  author: Matthew Khouzam
  last_modified: '2026-09-21T16:36:37-04:00'
---

# Overview
The Taxonomy Contributions skill and validation harness support contributors in authoring, verifying, and submitting terminology additions to the AAIF taxonomy landscape[^evt-ws-taxonomy-landscape-file-eda84dd4e776-0e9c3434]. It enforces syntactic validity and schema compliance on `taxonomy/taxonomy-data.js` to ensure that malformed metadata (such as unescaped strings) cannot break downstream web viewers and client applications[^evt-ws-taxonomy-landscape-file-eda84dd4e776-0e9c3434].

# Architecture / Specification

## Maintainer-Gated CI Pipeline
To guard against compute abuse while maintaining push protection on target branches, automated taxonomy testing is isolated behind explicit human maintainer actions[^evt-ws-taxonomy-landscape-file-eda84dd4e776-0e9c3434]:
- **Trigger Conditions**: The GitHub Actions workflow (`validate-taxonomy.yml`) runs exclusively upon `pull_request_review` submission or edits by maintainers, as well as on manual `workflow_dispatch`[^evt-ws-taxonomy-landscape-file-eda84dd4e776-0e9c3434]. Unreviewed external contributor pushes do not trigger CI automatically[^evt-ws-taxonomy-landscape-file-eda84dd4e776-0e9c3434].
- **Target Head Checkout**: Review-triggered runs explicitly check out the proposed head commit (`github.event.pull_request.head.sha`) rather than the base branch[^evt-ws-taxonomy-landscape-file-eda84dd4e776-0e9c3434].
- **Resource Boundaries**: Jobs enforce a 5-minute timeout, cancel superseded in-progress runs via concurrency groups, and reject oversized data payloads prior to parsing[^evt-ws-taxonomy-landscape-file-eda84dd4e776-0e9c3434].

[^evt-ws-taxonomy-landscape-file-eda84dd4e776-0e9c3434]: https://github.com/aaif/ws-taxonomy-landscape/blob/6ac90f517a064054d4113b3331c8c06e380258b8/.github/workflows/validate-taxonomy.yml
