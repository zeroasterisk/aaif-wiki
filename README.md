# AAIF Wiki (`aaif-wiki`)

> **Autonomous Knowledge Graph & Living Wiki Engine for the Agentic AI Foundation (AAIF)**

[![Standard: OKF v0.2](https://img.shields.io/badge/standard-OKF%20v0.2-blue.svg)](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
[![Orchestration: Temporal + ADK](https://img.shields.io/badge/orchestration-Temporal%20%2B%20ADK-purple.svg)](docs/design/ADR-002-orchestration-temporal-adk.md)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-green.svg)](LICENSE)

`aaif-wiki` is an autonomous knowledge engine that ingests, curates, and continuously maintains an interconnected, version-controlled knowledge graph across the 15 repositories of the [Agentic AI Foundation (AAIF)](https://github.com/aaif).

Built on the **Open Knowledge Format (OKF v0.2)** standard, Google's **Agent Development Kit (ADK)**, and **Temporal**, `aaif-wiki` transforms scattered Git commits, PR discussions, and meeting notes into an auditable living wiki for AI agents and human contributors.

---

## 🏛️ Architectural Foundations

`aaif-wiki` is designed around seven core architectural decisions:

1. **[OKF v0.2 Knowledge Representation](docs/design/ADR-001-knowledge-representation-okf.md)**: Standardized Markdown + YAML frontmatter knowledge bundle (`wiki/`) with typed concepts and directional wikilinks.
2. **[Temporal + ADK Durability](docs/design/ADR-002-orchestration-temporal-adk.md)**: Durable state machine orchestration capable of surviving crashes, rate limits, and network transient failures.
3. **[Immutable Event Sourcing](docs/design/ADR-003-event-sourcing-ingestion.md)**: Permanent raw event cache (`raw/events/`) enabling non-destructive replayability from Day 0.
4. **[Resilience & 429 Mitigation](docs/design/ADR-004-resilience-and-rate-limiting.md)**: Exponential backoff with full jitter, iteration budgets, and circuit breakers.
5. **[Horizon-Inspired Harness](docs/design/ADR-005-horizon-agent-harness.md)**: 3-tier prompt assembly (stable, cached, volatile) and context compaction preventing context drift.
6. **[Tiered Context & OpenViking (P2)](docs/design/ADR-006-tiered-context-openviking.md)**: Schema readiness for L0/L1/L2 hierarchical context recall.
7. **[Modular Exporters & Privacy Boundary](docs/design/ADR-007-modular-exporters-and-privacy.md)**: Pluggable exporters for public GitHub Gists and static web visualizers, with strict privacy boundary isolation.

Full architectural specifications are documented in **[`docs/design/`](docs/design/README.md)**.

---

## 📁 Repository Structure

```
aaif-wiki/
├── config.yaml                 # Core configuration & repository manifest
├── pyproject.toml              # UV / Pip project definition
│
├── docs/                       # Project documentation & Architecture Decision Records
│   ├── index.md
│   └── design/                 # ADR-001 through ADR-007
│
├── aaif_wiki/                  # Core Python Package
│   ├── agent.py                # Google ADK Root Agent & Harness
│   ├── config.py               # Pydantic configuration parser
│   ├── connectors/             # Multi-source ingestion connectors (GitHub, PRs, Notes)
│   ├── curator/                # OKF parser, gardener agent, and graph builder
│   ├── workflows/              # Temporal workflow & resilient activities
│   └── exporters/              # Public Gist and Visualizer exporters
│
├── wiki/                       # Canonical OKF v0.2 Knowledge Bundle (Git-versioned)
│   ├── index.md                # Root taxonomy & directory index
│   ├── log.md                  # Cumulative update changelog
│   ├── working-groups/         # 8 Working Group concept pages
│   ├── architectures/          # Reference architecture & RFC concepts
│   ├── taxonomy/               # Official consensus glossary
│   └── graph.json              # Web visualizer graph data
│
└── raw/                        # Immutable Event Store (raw/events/YYYY/MM/DD/*.json)
```

---

## 🚀 Quickstart

### Prerequisites
* Python 3.11+
* [`uv`](https://docs.astral.sh/uv/) (`curl -LsSf https://astral.sh/uv/install.sh | sh`)
* [Temporal CLI / Dev Server](https://docs.temporal.io/cli) (`temporal server start-dev`)
* GitHub CLI (`gh auth status`)

### Setup & Run
```bash
# 1. Clone & install dependencies
cd aaif-wiki
uv sync

# 2. Start local Temporal server (in a separate terminal)
temporal server start-dev

# 3. Run bootstrap ingestion
uv run aaif-wiki ingest --mode=bootstrap

# 4. Generate bi-weekly executive briefing & publish Gist
uv run aaif-wiki digest --publish-gist
```

---

## 🤝 Attribution & Acknowledgements
* Inspired by the [Open Knowledge Format (OKF v0.2)](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) by Google Cloud.
* Concept inspired by [`langchain-ai/openwiki`](https://github.com/langchain-ai/openwiki) and Karpathy's LLM-as-Wiki paradigm.
* Harness patterns adapted from [`google/adk-samples/long-horizon-harness`](https://github.com/google/adk-samples/tree/main/core/python/long-horizon-harness).
