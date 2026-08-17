# Architecture Decision Records (ADRs)

This directory contains the canonical Architecture Decision Records for the **AAIF Wiki (`aaif-wiki`)** knowledge curation engine.

## Index of Decisions

| ADR | Title | Status | Primary Focus |
| :--- | :--- | :--- | :--- |
| **[ADR-001](ADR-001-knowledge-representation-okf.md)** | Open Knowledge Format (OKF v0.2) Standard | **Accepted** | Knowledge representation, YAML frontmatter, wikilinks, `index.md`/`log.md` conventions |
| **[ADR-002](ADR-002-orchestration-temporal-adk.md)** | Durability & Orchestration with Temporal + Google ADK | **Accepted** | Workflow state machines, activity separation, deterministic checkpoints, 429 recovery |
| **[ADR-003](ADR-003-event-sourcing-ingestion.md)** | Immutable Event Sourcing & Ingestion Pipeline | **Accepted** | Multi-repo delta extraction, raw event cache, non-destructive replayability |
| **[ADR-004](ADR-004-resilience-and-rate-limiting.md)** | Resilience, Backoffs & Failure Mitigation | **Accepted** | Exponential backoff with jitter, budget guards, circuit breakers, token throttling |
| **[ADR-005](ADR-005-horizon-agent-harness.md)** | Horizon-Inspired Agent Harness & Context Management | **Accepted** | 3-tier prompt assembly, `HorizonSummarizer` compaction, guardrail plugins |
| **[ADR-006](ADR-006-tiered-context-openviking.md)** | Tiered Context & OpenViking Compatibility (P2) | **Proposed** | L0/L1/L2 hierarchical context loading, vector store compilation, external recall |
| **[ADR-007](ADR-007-modular-exporters-and-privacy.md)** | Pluggable Exporters & Privacy Boundary Guardrails | **Accepted** | Public Gist publisher, static visualizer bundle, isolation from private infrastructure |

## Review & Audit Guidelines
Reviewing agents should evaluate these records against:
1. **Determinism & Replayability**: Can the knowledge graph be reconstructed from raw events without context drift?
2. **Failure Recovery**: Does every network, API, and LLM call have an explicit backoff and recovery strategy?
3. **Auditability**: Can humans and autonomous agents inspect changes via standard Git diffs and `log.md` changelogs?
4. **Vendor Neutrality**: Does the system avoid proprietary lock-in while leveraging best-in-class orchestration tools?
