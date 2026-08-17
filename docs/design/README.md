# Architecture Decision Records (ADRs)

This directory contains the canonical Architecture Decision Records for the **AAIF Wiki (`aaif-wiki`)** knowledge curation engine.

> **Unofficial.** `aaif-wiki` is a personal project and is not affiliated with, endorsed by, or
> reviewed by the Agentic AI Foundation or the Linux Foundation. See
> [ADR-010](ADR-010-project-positioning-and-attribution.md).

## Index of Decisions

| ADR | Title | Status | Primary Focus |
| :--- | :--- | :--- | :--- |
| **[ADR-001](ADR-001-knowledge-representation-okf.md)** | Knowledge Representation via Open Knowledge Format (OKF v0.2) | **Accepted** | OKF profile, YAML frontmatter, relative links, `index.md`/`log.md` conventions, namespaced producer extensions |
| **[ADR-002](ADR-002-orchestration-temporal-adk.md)** | Orchestration via a Pluggable `Orchestrator` Protocol (Local Default, Temporal Optional) | **Accepted** *(supersedes the Temporal-first decision)* | Activity registry, Temporal-compatible-by-construction activities, checkpoint durability, `orchestrator: local\|temporal` |
| **[ADR-003](ADR-003-event-sourcing-ingestion.md)** | Immutable Event Sourcing, Ingest Scope & Rehydration | **Accepted** | Pointer vs. inline events, `raw/cache/` git mirrors, derived `index.db` and cursors, merged + in-flight ingest, tombstones, non-destructive replay |
| **[ADR-004](ADR-004-resilience-and-rate-limiting.md)** | Resilience, Rate Limiting & Hard Budget Ceilings | **Proposed** | Full-jitter backoff, config-owned retry policy, prose-structural payload reduction, hard USD/token/concept ceilings with partial-progress abort |
| **[ADR-005](ADR-005-horizon-agent-harness.md)** | Curator Harness as a Delta Over the Horizon Long-Horizon Harness | **Proposed** | Pinned dependency on the upstream Horizon recipe, tier content, structured `ConceptMutation` output, model pin and resolved-id provenance |
| **[ADR-006](ADR-006-tiered-context-openviking.md)** | Tiered Context Discipline (OpenViking Export Considered) | **Considered** | Binding L0/L1/L2 authoring discipline; OpenViking export recorded as viable but not built |
| **[ADR-007](ADR-007-modular-exporters-and-privacy.md)** | Pluggable Exporters & Trust Boundary | **Accepted** | Canonical bundle + exporters, generic bundle-agnostic OKF MCP server, untrusted-input fencing, outbound leak guard and link allowlist |
| **[ADR-008](ADR-008-evaluation-and-quality-gates.md)** | Evaluation, Golden Sets & Deterministic Quality Gates | **Proposed** | Blocking no-LLM validators (schema, links, provenance, orphans, OKF conformance, status, tiers) plus advisory golden-set regression |
| **[ADR-009](ADR-009-human-in-the-loop-publication.md)** | Human-in-the-Loop Publication via Pull Request | **Accepted** | No direct writes to `main`, `draft`/`stable` and `verified` lifecycle, configurable auto-merge, structured review records as an eval corpus |
| **[ADR-010](ADR-010-project-positioning-and-attribution.md)** | Project Positioning, Disclaimers & Attribution | **Accepted** | Unofficial/not-endorsed disclaimers, canonical upstream links, per-repository license detection and attribution, donation path via AAIF `project-proposals` |

## Reviews

| Document | Date | Summary |
| :--- | :--- | :--- |
| **[Architecture Review 2026-08](ARCHITECTURE-REVIEW-2026-08.md)** | 2026-08-17 | Critical review of ADR-001–007. 3 S1 findings (redundant orchestration, no review gate, untrusted input), 7 S2, 12 S3. Includes a batched question pack and a proposed ADR change list. Its open questions are now resolved: ADR-002 rewritten, ADR-003/004/005/006/007 amended, and ADR-008/009/010 added. |

## Review & Audit Guidelines
Reviewing agents should evaluate these records against:

1. **Reproducibility**: Can the knowledge graph be re-derived from raw events? (Note: re-derivation
   through an LLM is *not* bit-deterministic — inputs are fixed and recorded, outputs are
   re-derivable. See ADR-003 §8 and ARCHITECTURE-REVIEW-2026-08 §F2.)
2. **Failure Recovery**: Does every network, API, and LLM call have an explicit backoff, budget
   ceiling, and resumption strategy? (ADR-002 checkpointing, ADR-004 ceilings.)
3. **Auditability**: Can humans and autonomous agents inspect changes via standard Git diffs,
   `log.md`, and the event store — and trace any published claim back to a source event?
4. **Output Portability**: Is the *artifact* free of lock-in (plain Markdown in git, readable with
   `cat`, consumable by any OKF reader), independent of which frameworks the *pipeline* uses?
   The pipeline is not vendor-neutral and does not claim to be (ADR-005).
5. **Human Accountability**: Can a machine-generated claim be distinguished from a human-reviewed
   one, before it is published? (OKF v0.2 `status` / `verified`, gated by the pull-request flow in
   ADR-009.)
6. **Adversarial Input**: Is ingested third-party content treated as untrusted data rather than as
   instructions — and is the write path structurally bounded rather than merely instructed?
   (ADR-007.)

> **A note on verifying claims.** An earlier review pass produced a false S1 finding by asserting a
> model did not exist after a badly-scoped search (see F5). When checking whether a fast-moving
> dependency, model, or spec version exists, query the **exact string**, and treat "I could not
> find it" as *inconclusive* rather than *falsifying*.
