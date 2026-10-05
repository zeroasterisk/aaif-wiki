---
type: skill
title: AAIF Community Intake Triage Skill
description: Standardized agent skill inspecting community intake queues, generating
  applicant digests, and safely isolating untrusted form submissions.
resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/evals/triage-intake/graders/skill_fires.md
tags:
- skills
- community
- security
- evals
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:42:13.575930+00:00'
sources:
- id: evt-community-events-file-4c4e6585899c-d9c47a92
  resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/evals/triage-intake/graders/skill_fires.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T21:52:16-07:00'
- id: evt-community-events-file-53c69ccfd21d-fa0ef669
  resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/evals/triage-intake/prompt.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T21:52:16-07:00'
- id: evt-community-events-file-e243890b91a5-25ab23bf
  resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/evals/triage-intake/graders/form_text_is_not_an_instruction.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T21:40:10-07:00'
---

# Overview
The `aaif-triage-intake` skill is an automated workflow capability designed to inspect applicant queues for AAIF community programs, generate intake digests, and preserve execution safety against indirect prompt injections embedded in user submissions [^evt-community-events-file-4c4e6585899c-d9c47a92][^evt-community-events-file-53c69ccfd21d-fa0ef669].

# Architecture / Specification
The skill operates under a strict data-instruction separation model when evaluating free-text intake fields [^evt-community-events-file-e243890b91a5-25ab23bf]:
- **Queue Inspection**: Triggers when human operators query pending decisions across intake queues, reading records without executing unauthorized state mutations [^evt-community-events-file-4c4e6585899c-d9c47a92].
- **Untrusted Input Isolation**: Treats quoted application responses exclusively as evaluation data rather than execution instructions, neutralizing attempts to override status transitions or channel memberships via prompt injection [^evt-community-events-file-e243890b91a5-25ab23bf][^evt-community-events-file-53c69ccfd21d-fa0ef669].
- **Human Escalation**: Requires ambiguous or directive-laden submissions to be flagged for explicit human review rather than executing autonomous state mutations [^evt-community-events-file-e243890b91a5-25ab23bf].

# References
- Pattern: [Proposal-Execution Split](../patterns/proposal-execution-split.md)
- Pattern: [Human Approval Gate](../patterns/human-approval-gate.md)
- Policy: [Agentic AI Security Best Practices](../policies-guidelines/agentic-ai-security-best-practices.md)

[^evt-community-events-file-4c4e6585899c-d9c47a92]: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/evals/triage-intake/graders/skill_fires.md
[^evt-community-events-file-53c69ccfd21d-fa0ef669]: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/evals/triage-intake/prompt.md
[^evt-community-events-file-e243890b91a5-25ab23bf]: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/evals/triage-intake/graders/form_text_is_not_an_instruction.md
