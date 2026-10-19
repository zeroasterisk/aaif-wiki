---
type: guideline
title: Working Group Proposal Submission Guidelines
description: Operating guidelines governing proposal preparation, membership eligibility,
  issue tracking, and approval workflows for AAIF working groups.
resource: https://github.com/aaif/working-group-proposals/blob/1054856f6e1307fdfb56d51abcf9a87055ee0140/submission-guidelines.md
tags:
- governance
- guidelines
- working-groups
- aaif
- proposals
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T11:13:39.958463+00:00'
sources:
- id: evt-working-group-proposals-file-67593d7c0dc3-a2eb51a2
  resource: https://github.com/aaif/working-group-proposals/blob/1054856f6e1307fdfb56d51abcf9a87055ee0140/submission-guidelines.md
  author: Manik Surtani
  last_modified: '2026-10-15T16:14:24+11:00'
- id: evt-working-group-proposals-file-87b3376703c5-313cc435
  resource: https://github.com/aaif/working-group-proposals/blob/1054856f6e1307fdfb56d51abcf9a87055ee0140/.github/ISSUE_TEMPLATE/working-group-proposal.yml
  author: Manik Surtani
  last_modified: '2026-10-15T16:14:24+11:00'
- id: evt-working-group-proposals-file-b33563055168-6c29ea3b
  resource: https://github.com/aaif/working-group-proposals/blob/1054856f6e1307fdfb56d51abcf9a87055ee0140/README.md
  author: Manik Surtani
  last_modified: '2026-10-15T16:14:24+11:00'
---

# Overview
The Working Group Proposal Submission Guidelines instruct contributors on preparing and submitting formal proposals to establish new Working Groups (WGs) or revive Concluded WGs under the Agentic AI Foundation (AAIF)[^evt-working-group-proposals-file-67593d7c0dc3-a2eb51a2][^evt-working-group-proposals-file-b33563055168-6c29ea3b]. Last updated on October 15, 2026, the guideline operationalizes the [Working Group Lifecycle Policy](../policies/working-group-lifecycle-policy.md) and standardized GitHub issue application workflows[^evt-working-group-proposals-file-67593d7c0dc3-a2eb51a2].

# Eligibility and Scope
Working groups represent enduring bodies organized around long-lived problem domains relevant to agentic AI[^evt-working-group-proposals-file-67593d7c0dc3-a2eb51a2]. Focused, short-term, or single-deliverable tasks (such as individual whitepapers, benchmarks, or specific reference architectures) must be chartered as workstreams within existing working groups rather than creating independent groups[^evt-working-group-proposals-file-67593d7c0dc3-a2eb51a2].

Eligibility constraints require[^evt-working-group-proposals-file-67593d7c0dc3-a2eb51a2]:
- **Submitters**: Proposals must originate from a representative of an AAIF member organization in good standing (Platinum, Gold, Silver, or Associate tier)[^evt-working-group-proposals-file-67593d7c0dc3-a2eb51a2]. Non-member contributors must obtain sponsorship from a member organization representative to submit on their behalf[^evt-working-group-proposals-file-67593d7c0dc3-a2eb51a2].
- **Chairs**: Designated working group chairs must belong to Platinum, Gold, or Silver member organizations[^evt-working-group-proposals-file-67593d7c0dc3-a2eb51a2].
- **Participants**: Working group meetings, discussions, and technical activities remain open to the public and all community members regardless of formal membership status[^evt-working-group-proposals-file-67593d7c0dc3-a2eb51a2].

# Proposal Structure and Review Process
Proposals are submitted through GitHub issue templates within the `aaif/working-group-proposals` repository and tracked on the public Working Group Proposals Board[^evt-working-group-proposals-file-87b3376703c5-313cc435][^evt-working-group-proposals-file-b33563055168-6c29ea3b]. Submissions require eight structured components[^evt-working-group-proposals-file-67593d7c0dc3-a2eb51a2]:
1. **Submitter Information**: Name, affiliation, role, contact info, and AAIF tier[^evt-working-group-proposals-file-67593d7c0dc3-a2eb51a2].
2. **Identity**: Proposed title and a clear, jargon-free one-sentence scope summary[^evt-working-group-proposals-file-67593d7c0dc3-a2eb51a2].
3. **Problem Statement & Purpose**: Documented industry gap, agentic relevance, alignment with foundation objectives, and justification against existing working groups[^evt-working-group-proposals-file-67593d7c0dc3-a2eb51a2].
4. **Scope & Concrete Deliverables**: In-scope and out-of-scope boundaries and tangible year-one technical deliverables (e.g., specifications, benchmarks, architectures)[^evt-working-group-proposals-file-67593d7c0dc3-a2eb51a2].
5. **First-Year Plan**: Milestone timeline and regular meeting schedules[^evt-working-group-proposals-file-67593d7c0dc3-a2eb51a2].
6. **Leadership & Committed Participants**: Proposed chairs and initial committed contributors[^evt-working-group-proposals-file-67593d7c0dc3-a2eb51a2].
7. **Overlap & Coordination**: Touchpoints with other AAIF groups and external standards bodies[^evt-working-group-proposals-file-67593d7c0dc3-a2eb51a2].
8. **Impact, Risks & Resources**: Operational requirements, infrastructure dependencies, and risk mitigation strategies[^evt-working-group-proposals-file-67593d7c0dc3-a2eb51a2].

# Review Tracking and Lifecycle Onboarding
Following intake verification by foundation staff, the [Technical Committee](../governance/technical-committee.md) reviews proposals asynchronously directly on the GitHub issue[^evt-working-group-proposals-file-b33563055168-6c29ea3b]. Review states are categorized by workflow labels[^evt-working-group-proposals-file-b33563055168-6c29ea3b]:
- `New`: Newly filed submission queued in backlog triage[^evt-working-group-proposals-file-b33563055168-6c29ea3b].
- `Waiting on Comment`: Reviewers require clarification or supplementary data from submitters[^evt-working-group-proposals-file-b33563055168-6c29ea3b].
- `Too Early`: The proposal concept lacks maturity or readiness; guidance is provided for potential reapplication[^evt-working-group-proposals-file-b33563055168-6c29ea3b].
- `Declined`: The proposal is formally declined with rationale documented in issue comments[^evt-working-group-proposals-file-b33563055168-6c29ea3b].
- `Approved`: Formal endorsement by both the TC and the Governing Board[^evt-working-group-proposals-file-b33563055168-6c29ea3b].

Upon approval, the working group launches into **Sandbox** stage, initiating regular meetings and monthly reporting while formalizing its operating charter[^evt-working-group-proposals-file-b33563055168-6c29ea3b]. Transition to **Active** status requires subsequent TC evaluation and approval of the completed charter[^evt-working-group-proposals-file-b33563055168-6c29ea3b].

[^evt-working-group-proposals-file-67593d7c0dc3-a2eb51a2]: https://github.com/aaif/working-group-proposals/blob/1054856f6e1307fdfb56d51abcf9a87055ee0140/submission-guidelines.md
[^evt-working-group-proposals-file-87b3376703c5-313cc435]: https://github.com/aaif/working-group-proposals/blob/1054856f6e1307fdfb56d51abcf9a87055ee0140/.github/ISSUE_TEMPLATE/working-group-proposal.yml
[^evt-working-group-proposals-file-b33563055168-6c29ea3b]: https://github.com/aaif/working-group-proposals/blob/1054856f6e1307fdfb56d51abcf9a87055ee0140/README.md
