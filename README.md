# AAIF Wiki (`aaif-wiki`)

> **Autonomous OKF v0.2 knowledge engine for the Agentic AI Foundation**

[![Standard: OKF v0.2](https://img.shields.io/badge/standard-OKF%20v0.2-blue.svg)](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-green.svg)](LICENSE)

> [!IMPORTANT]
> **Unofficial.** This is a personal open-source project. It is **not** endorsed by,
> affiliated with, or an official communication of the [Agentic AI Foundation](https://github.com/aaif)
> or the Linux Foundation. All content is machine-derived from public sources; every
> concept links to its canonical upstream material. See [ADR-010](docs/design/ADR-010-project-positioning-and-attribution.md).

`aaif-wiki` ingests the AAIF GitHub organisation — repository documents, open pull
requests, and issues — and curates them into a version-controlled
[Open Knowledge Format (OKF) v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
knowledge bundle that both humans and agents can read.

**Status: working prototype.** The pipeline runs end-to-end against real AAIF repos
and real Vertex AI. It has not yet been run at full scale, and several ADRs are
still `Proposed` pending a full bootstrap. See [the architecture review](docs/design/ARCHITECTURE-REVIEW-2026-08.md).

---

## What it actually does

```
GitHub (files · open PRs · issues)
          │
          ▼  scan_sources          git clone for content · REST for PRs/issues
   raw/events/**.json              append-only, pointers not blobs
          │
          ▼  curate_concepts       Vertex · gemini-3.7-flash · 3-tier prompts
   structured Mutations            schema-validated; no direct file writes
          │
          ▼  apply_mutations
   wiki/**.md                      OKF v0.2, status: draft, unverified
          │
          ▼  validate_bundle       deterministic · no LLM · CI-gating
          │
          ▼  publish (optional)
   branch → Pull Request → human review → status: stable + verified[]
```

Four ideas do most of the work:

- **The event log is the source of truth; the wiki is a projection.** Change the
  prompt, re-derive. Nothing is lost because nothing is overwritten in place.
- **Nothing is published without a human.** Every generated concept is
  `status: draft` and unverified. Only a human review promotes it to `stable`.
  Machine claims about a Linux Foundation body do not get to publish themselves.
- **Ingested text is untrusted.** Anyone can open a PR on a public repo. Third-party
  content is fenced as data, never followed as instructions, and cannot reach the
  filesystem except through a validated, typed mutation.
- **Orchestration is swappable.** Runs in-process by default; Temporal is a config
  change, not a rewrite, because activities are Temporal-compatible by construction.

---

## Quickstart

Requires Python 3.11+, [`uv`](https://docs.astral.sh/uv/), `git`, and Google Cloud
ADC (`gcloud auth application-default login`).

```bash
uv sync --extra dev
uv run aaif-wiki doctor            # verify git / GitHub / Vertex / optional extras
```

```bash
# Ingest one repo without touching an LLM (free, fast)
uv run aaif-wiki ingest --repo wg-security-and-privacy --no-curate

# Curate a small batch through Vertex
uv run aaif-wiki ingest --repo wg-security-and-privacy --max-events 6

# Deterministic gate — no LLM, no network, no credentials
uv run aaif-wiki validate

# Projections
uv run aaif-wiki export graph      # -> dist/graph.json
uv run aaif-wiki export digest     # -> dist/digest-<date>.md (reviewed content only)
```

A first curation batch of 6 events costs roughly **$0.014** and takes about 22s.

### Commands

| Command | Purpose |
| :-- | :-- |
| `doctor` | Check git, GitHub rate limit, Vertex, and optional extras |
| `ingest` | Scan → curate → apply → validate. `--publish` opens a PR |
| `validate` | Deterministic OKF conformance gate; exits non-zero on error |
| `export graph\|digest` | Build `dist/` artifacts |
| `events` / `index` / `cursor` | Inspect the event store and its derived state |
| `mcp` | Serve **any** OKF bundle over MCP |
| `worker` / `activities` | Temporal worker; list registered activities |

### Serving the bundle to agents

The MCP server is deliberately **bundle-agnostic** — point it at any OKF v0.2
bundle, not just this one:

```bash
uv sync --extra mcp
uv run aaif-wiki mcp --bundle wiki
```

It exposes tiered reads so an agent can triage cheaply and only pay for what it
needs: `okf_search`, `okf_abstract` (L0), `okf_overview` (L1), `okf_read` (L2),
plus `okf_provenance` for trust signals.

### Using Temporal instead

```bash
uv sync --extra temporal
temporal server start-dev
# config.yaml -> orchestrator.backend: temporal
uv run aaif-wiki worker      # in another terminal
uv run aaif-wiki ingest
```

No activity code changes. That is the whole point of [ADR-002](docs/design/ADR-002-orchestration-temporal-adk.md).

---

## Repository layout

```
aaif_wiki/
  models.py          # shared contracts (JSON-serializable by requirement)
  okf.py             # OKF v0.2 read/write/conformance — knows nothing about AAIF
  config.py          # typed config; config.yaml is the single source of truth
  pipeline.py        # activity definitions + run sequence
  orchestration/     # Orchestrator protocol · local (checkpointed) · temporal
  connectors/        # GitHub: git for content, REST for PRs/issues
  store/             # append-only events + derived SQLite index
  curator/           # 3-tier prompt assembly + Vertex client
  validate/          # deterministic, LLM-free checks
  exporters/         # graph · digest · generic OKF MCP server
  publish.py         # branch → commit → PR → eval record

wiki/                # canonical OKF v0.2 bundle          (committed)
raw/events/          # immutable event log                (committed)
raw/reviews/         # PR review records → eval corpus    (committed)
raw/cache/           # git mirrors + HTTP cache           (disposable)
dist/                # build artifacts                    (disposable)
docs/design/         # ADR-001 … ADR-010 + architecture review
```

---

## Architecture decisions

Ten ADRs in [`docs/design/`](docs/design/README.md). The ones that shape everything else:

| ADR | Decision |
| :-- | :-- |
| [001](docs/design/ADR-001-knowledge-representation-okf.md) | OKF v0.2 as the canonical format — and where this bundle's *profile* is stricter than the spec |
| [002](docs/design/ADR-002-orchestration-temporal-adk.md) | Swappable orchestration; local by default, Temporal one config line away |
| [003](docs/design/ADR-003-event-sourcing-ingestion.md) | Pointers for git-reproducible content, inline for what git cannot reproduce |
| [007](docs/design/ADR-007-modular-exporters-and-privacy.md) | Trust boundary — inbound untrusted input *and* outbound leak guard |
| [009](docs/design/ADR-009-human-in-the-loop-publication.md) | No publication without human review; review records become eval data |
| [010](docs/design/ADR-010-project-positioning-and-attribution.md) | Unofficial status, attribution, and the path to donate this to AAIF |

A [critical review](docs/design/ARCHITECTURE-REVIEW-2026-08.md) of the original design
records what was wrong and why it changed — including one finding the review itself
got wrong, kept visible rather than quietly deleted.

---

## Attribution

- [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) (OKF v0.2) by Google Cloud.
- Concept inspired by [`langchain-ai/openwiki`](https://github.com/langchain-ai/openwiki) and Karpathy's LLM-as-Wiki idea.
- Harness patterns from [`google/adk-samples`](https://github.com/google/adk-samples) long-horizon-harness.
- Tiered L0/L1/L2 context model from [`volcengine/OpenViking`](https://github.com/volcengine/OpenViking).

Content in `wiki/` is derived from public AAIF repositories; each concept records its
sources and links upstream. Licensed Apache-2.0.
