# ADR-011: Optional Jev mutation assessment

- Status: Proposed
- Date: 2026-09-19

## Context

The GitHub pipeline and OKF gate are deterministic. The curator already emits a
typed mutation before any filesystem write, deterministic validation runs on
every proposal, and a human review is the only path to stable/human-reviewed.
Jev can add useful classification and prioritization, but making it required
would turn CI into a network- and vendor-dependent gate.

## Decision

Jev is an advisory component after typed mutation generation and before the
existing deterministic apply/validate steps.

- `jev.enabled: false` is the default.
- `JEV_ENABLED` can enable or disable it for one run.
- `JEV_API_KEY` is read only at runtime and is never stored in config or review records.
- Disabled, missing-key, timeout, rate-limit, and service-error paths return the
  original mutations unchanged.
- Low-confidence results are recorded as `abstain`; they do not block the run.
- Jev never writes content, changes OKF validation, promotes a concept, or merges a PR.
- Review records preserve the assessment next to the machine proposal. Reviewers
  can add a `human_label` to create a committed evaluation example.
- `aaif-wiki eval-jev` computes agreement and coverage from those records without
  a network call.

The questions are typed: mutation kind (`new_concept`, `update`, `relation`,
`conflict`, `no_op`), target node, provenance score, and review priority. The
minimum confidence across answers controls pass versus abstain.

## Consequences

The default pipeline remains exactly deterministic and credential-free. An
enabled run gets extra review metadata and measurable performance at the cost of
one external evaluation request per proposed mutation. Jev results are advice,
not authority.
