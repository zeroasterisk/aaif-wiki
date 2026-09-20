# ADR-012: Autonomous resolution ladder and durable exceptions

- Status: Proposed
- Date: 2026-09-19

## Context

The wiki is a maintained data source for future inquiry and reporting, not a
human-operated approval tool. It must continue for one or two months without a
maintainer. The previous design had no semantic conflict type or queue. It
applied curator mutations, then relied on a generic PR review gate when
`auto_merge` was false. The current repository contains no committed review
records, which explains why there is no history of resolved conflicts.

## Decision

1. Jev enriches typed proposals with kind, target, confidence, provenance and
   priority. It is optional and off by default; failure never blocks.
2. An ordered resolution ladder runs after enrichment. The first layer records
   deterministic context such as duplicate creates and stable claims from open
   sources. Model-backed layers are pluggable and run at increasing fidelity on
   the existing Vertex path (`vertex-fast`, then `vertex-deep`).
3. Every layer emits `ResolutionEvidence`: layer, outcome, confidence,
   rationale and flags. Evidence is stored with the proposal.
4. Deterministic invariant violations and unresolved conflicts are withheld from
   the canonical bundle, preventing automated runs from corrupting `main`.
5. Withheld mutations and unresolved cases are appended to
   `raw/exceptions/YYYY/MM/DD/*.json` alongside the full proposed concept. Clean
   mutations proceed to bundle application and auto-merge. The queue never pauses
   ingestion.
6. A later human resolution updates the exception with actor/time and a
   structured `training_signal` pair. This is refinement data for prompts,
   golden cases and future resolvers.
7. Publication may auto-merge draft/unverified machine output. Consumers use
   provenance and evidence metadata to decide trust. Human review remains a
   last-resort audit and training path, not a prerequisite for progress.

## Neglect tolerance

The queue is append-only, partitioned by date and independent of a running
workflow. Resolver failures are captured as records and the run continues.
Budget and retry ceilings remain bounded. A monthly absence grows a queryable
backlog rather than parking or failing the pipeline.
