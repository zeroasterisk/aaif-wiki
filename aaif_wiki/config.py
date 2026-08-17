"""Typed configuration, loaded from ``config.yaml``.

``config.yaml`` is the single source of truth for tunables. ADRs reference these
values rather than restating literals, because restated literals drift (this
already happened once: ADR-004 said 6 retries while the config said 5).
"""

from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path

import yaml
from pydantic import BaseModel, Field


def repo_root() -> Path:
    """Locate the project root by walking up to the directory holding config.yaml."""
    here = Path(__file__).resolve()
    for parent in [here.parent, *here.parents]:
        if (parent / "config.yaml").exists():
            return parent
    return Path.cwd()


class ProjectCfg(BaseModel):
    name: str = "AAIF Knowledge Wiki"
    organization: str = "aaif"
    bundle_root: str = "wiki"
    event_store: str = "raw/events"
    cache_dir: str = "raw/cache"
    index_db: str = "raw/index.db"
    dist_dir: str = "dist"


class VertexCfg(BaseModel):
    project: str | None = None
    location: str = "global"

    def resolved_project(self) -> str | None:
        return self.project or os.environ.get("GOOGLE_CLOUD_PROJECT")


class CuratorCfg(BaseModel):
    model: str = "gemini-3.7-flash"
    fallback_model: str = "gemini-flash-latest"
    vertex: VertexCfg = Field(default_factory=VertexCfg)
    iteration_budget: int = 15
    compaction_threshold: int = 10
    temperature: float = 0.2
    # Introductory pricing for gemini-3.7-flash, USD per 1M tokens. Used for the
    # budget ceiling; approximate by design, and cheap to correct.
    usd_per_1m_input: float = 0.75
    usd_per_1m_output: float = 3.75

    def model_post_init(self, __context: object) -> None:
        if self.compaction_threshold >= self.iteration_budget:
            raise ValueError(
                f"compaction_threshold ({self.compaction_threshold}) must be below "
                f"iteration_budget ({self.iteration_budget}) or the compactor can never fire"
            )


class BudgetCfg(BaseModel):
    max_usd_per_run: float = 25.0
    max_tokens_per_run: int = 20_000_000
    max_concepts_per_run: int = 100
    # Absolute guard rail; no run may be configured above this.
    hard_usd_ceiling: float = 200.0

    def model_post_init(self, __context: object) -> None:
        if self.max_usd_per_run > self.hard_usd_ceiling:
            raise ValueError(
                f"max_usd_per_run ({self.max_usd_per_run}) exceeds the hard ceiling "
                f"({self.hard_usd_ceiling})"
            )


class RetryCfg(BaseModel):
    initial_interval_seconds: float = 2.0
    backoff_coefficient: float = 2.0
    maximum_interval_seconds: float = 60.0
    maximum_attempts: int = 5


class OrchestratorCfg(BaseModel):
    """ADR-002. ``local`` by default; ``temporal`` is a config swap, not a rewrite."""

    backend: str = "local"
    checkpoint_path: str = "raw/.checkpoint.json"
    retry_policy: RetryCfg = Field(default_factory=RetryCfg)
    # Only read when backend == "temporal".
    host: str = "localhost:7233"
    namespace: str = "default"
    task_queue: str = "aaif-wiki-queue"


class GitHubCfg(BaseModel):
    org: str = "aaif"
    discover_repos: bool = True
    exclude_repos: list[str] = Field(default_factory=lambda: [".github"])
    repositories: list[str] = Field(default_factory=list)
    doc_extensions: list[str] = Field(default_factory=lambda: [".md", ".markdown", ".yaml", ".yml"])
    include_open_prs: bool = True
    include_issues: bool = True
    include_discussions: bool = True
    max_items_per_repo: int = 25

    def token(self) -> str | None:
        return os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")


class SourcesCfg(BaseModel):
    github: GitHubCfg = Field(default_factory=GitHubCfg)


class PublishCfg(BaseModel):
    """ADR-009. The curator never writes to main."""

    enabled: bool = True
    branch_prefix: str = "wiki/update"
    auto_merge: bool = False
    base_branch: str = "main"
    review_records: str = "raw/reviews"


class GistCfg(BaseModel):
    enabled: bool = False
    public: bool = True


class VisualizerCfg(BaseModel):
    enabled: bool = True
    output_dir: str = "dist"


class ExportersCfg(BaseModel):
    gist: GistCfg = Field(default_factory=GistCfg)
    visualizer: VisualizerCfg = Field(default_factory=VisualizerCfg)
    openviking_enabled: bool = False


class TrustCfg(BaseModel):
    """ADR-007 outbound half: only these hosts survive sanitization."""

    link_allowlist: list[str] = Field(
        default_factory=lambda: [
            "github.com",
            "raw.githubusercontent.com",
            "aaif.io",
            "www.aaif.io",
            "linuxfoundation.org",
            "www.linuxfoundation.org",
        ]
    )
    forbidden_patterns: list[str] = Field(
        default_factory=lambda: [
            r"/google/(bin|src)/",
            r"\bgoogle3\b",
            r"file:///",
            r"\b[A-Za-z0-9._%+-]+@google\.com\b",
        ]
    )


class Config(BaseModel):
    project: ProjectCfg = Field(default_factory=ProjectCfg)
    curator: CuratorCfg = Field(default_factory=CuratorCfg)
    budget: BudgetCfg = Field(default_factory=BudgetCfg)
    orchestrator: OrchestratorCfg = Field(default_factory=OrchestratorCfg)
    sources: SourcesCfg = Field(default_factory=SourcesCfg)
    exporters: ExportersCfg = Field(default_factory=ExportersCfg)
    publish: PublishCfg = Field(default_factory=PublishCfg)
    trust: TrustCfg = Field(default_factory=TrustCfg)

    root: Path = Field(default_factory=repo_root)

    # -- resolved paths -------------------------------------------------
    @property
    def bundle_dir(self) -> Path:
        return self.root / self.project.bundle_root

    @property
    def events_dir(self) -> Path:
        return self.root / self.project.event_store

    @property
    def cache_dir(self) -> Path:
        return self.root / self.project.cache_dir

    @property
    def index_db_path(self) -> Path:
        return self.root / self.project.index_db

    @property
    def dist_dir(self) -> Path:
        return self.root / self.project.dist_dir

    @property
    def reviews_dir(self) -> Path:
        return self.root / self.publish.review_records


def load_config(path: Path | None = None) -> Config:
    root = repo_root()
    path = path or (root / "config.yaml")
    data: dict = {}
    if path.exists():
        data = yaml.safe_load(path.read_text()) or {}

    # config.yaml keeps a flat `temporal:` block for backward compatibility with
    # the original ADR-002 design; fold it into the orchestrator config.
    legacy = data.pop("temporal", None)
    orch = data.get("orchestrator") or {}
    if legacy:
        orch.setdefault("host", legacy.get("host", "localhost:7233"))
        orch.setdefault("namespace", legacy.get("namespace", "default"))
        orch.setdefault("task_queue", legacy.get("task_queue", "aaif-wiki-queue"))
        if "retry_policy" in legacy:
            orch.setdefault("retry_policy", legacy["retry_policy"])
    if orch:
        data["orchestrator"] = orch

    data["root"] = root
    return Config.model_validate(data)


@lru_cache(maxsize=1)
def get_config() -> Config:
    return load_config()
