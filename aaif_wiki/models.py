"""Shared data contracts for aaif-wiki.

Every type here is a plain Pydantic model with JSON-serializable fields. This is a
hard requirement, not a style preference: activities are passed across the
``Orchestrator`` boundary (ADR-002) and must round-trip through JSON unchanged so
the same activity code runs under ``LocalOrchestrator`` and Temporal alike.
"""

from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field

# --------------------------------------------------------------------------
# Ingestion
# --------------------------------------------------------------------------


class SourceType(str, Enum):
    """Where an event came from.

    ``repo_file`` is git-reproducible and therefore stored as a pointer.
    Everything else is editable or deletable upstream and is stored inline,
    because git cannot reproduce it later (ADR-003 / D5).
    """

    REPO_FILE = "repo_file"
    PULL_REQUEST = "pull_request"
    ISSUE = "issue"
    DISCUSSION = "discussion"
    DELETION = "deletion"


class Lifecycle(str, Enum):
    """How settled the source material is.

    This is the load-bearing distinction for the whole project: a merged charter
    and an open draft PR must never be presented to a reader as equally
    authoritative (ADR-003 / D7).
    """

    MERGED = "merged"
    OPEN = "open"
    DRAFT = "draft"
    CLOSED = "closed"

    @property
    def is_authoritative(self) -> bool:
        return self is Lifecycle.MERGED


class FilePointer(BaseModel):
    """A reference to git-reproducible content.

    We deliberately do not inline the bytes. Git already stores this content,
    content-addressed, with better diffs than a JSON-escaped string blob.
    """

    repo: str
    commit_sha: str
    path: str
    blob_sha: str
    status: str = "modified"  # added | modified | removed


class RawEvent(BaseModel):
    """One immutable observation about the upstream world.

    The event store is append-only. The wiki is a projection over it.
    """

    event_id: str
    source_type: SourceType
    lifecycle: Lifecycle
    repository: str
    reference_id: str
    title: str
    timestamp: datetime
    author: str | None = None
    url: str | None = None

    summary: str = ""

    # Exactly one of these is populated, decided by reproducibility (D5).
    pointers: list[FilePointer] = Field(default_factory=list)
    inline_text: str | None = None

    labels: list[str] = Field(default_factory=list)

    @property
    def is_pointer_backed(self) -> bool:
        return bool(self.pointers)

    def cache_key(self) -> str:
        return f"{self.repository}:{self.reference_id}"


# --------------------------------------------------------------------------
# OKF v0.2
# --------------------------------------------------------------------------


class ConceptStatus(str, Enum):
    """OKF v0.2 lifecycle. Absent means stable, per spec; we are explicit."""

    DRAFT = "draft"
    STABLE = "stable"
    DEPRECATED = "deprecated"


class Actor(BaseModel):
    """OKF v0.2 actor convention for ``generated.by`` / ``verified[].by``.

    Machine actors are ``agent:<id>``; humans are ``human:<id>``. The consumer
    derives a trust tier from this; the spec deliberately stores no score.
    """

    by: str
    at: datetime


class ConceptSource(BaseModel):
    """OKF v0.2 ``sources[]`` entry, including credibility signals."""

    id: str
    resource: str
    author: str | None = None
    last_modified: datetime | None = None
    usage_count: int | None = None


class Concept(BaseModel):
    """One OKF v0.2 concept document.

    Note the profile boundary: OKF requires only ``type``. Everything else this
    project mandates is an aaif-wiki profile decision, not a spec requirement.
    """

    # Required by OKF.
    type: str

    # Recommended by OKF; required by the aaif-wiki profile.
    title: str
    description: str
    resource: str | None = None
    tags: list[str] = Field(default_factory=list)

    # v0.2 trust / provenance / lifecycle.
    generated: Actor | None = None
    verified: list[Actor] = Field(default_factory=list)
    status: ConceptStatus = ConceptStatus.DRAFT
    stale_after: date | None = None
    sources: list[ConceptSource] = Field(default_factory=list)

    # Not frontmatter.
    slug: str = ""
    body: str = ""

    @property
    def trust_tier(self) -> str:
        """Derived, never stored -- consumers compute this from ``verified``."""
        if not self.verified:
            return "unverified"
        if any(a.by.startswith("human:") for a in self.verified):
            return "human-reviewed"
        return "machine-confirmed"

    def relative_path(self) -> str:
        return f"{self.slug}.md"


class Mutation(BaseModel):
    """A structured, schema-validated change request from the curator.

    The curator never writes files directly. It returns mutations, which are
    validated before being applied. This is the inbound half of the trust
    boundary (ADR-007): ingested text cannot become a filesystem write.
    """

    action: str  # create | update | deprecate
    slug: str
    concept: Concept | None = None
    rationale: str = ""
    source_event_ids: list[str] = Field(default_factory=list)


# --------------------------------------------------------------------------
# Orchestration
# --------------------------------------------------------------------------


class RunMode(str, Enum):
    BOOTSTRAP = "bootstrap"
    INCREMENTAL = "incremental"
    REPLAY = "replay"


class ScanRequest(BaseModel):
    mode: RunMode = RunMode.INCREMENTAL
    repos: list[str] = Field(default_factory=list)
    max_events: int = 0  # 0 = unbounded


class ScanResult(BaseModel):
    events: list[RawEvent] = Field(default_factory=list)
    repos_scanned: list[str] = Field(default_factory=list)
    skipped: dict[str, str] = Field(default_factory=dict)


class CurateRequest(BaseModel):
    event_ids: list[str] = Field(default_factory=list)
    dry_run: bool = False


class CurateResult(BaseModel):
    mutations: list[Mutation] = Field(default_factory=list)
    tokens_in: int = 0
    tokens_out: int = 0
    usd: float = 0.0
    model: str = ""
    halted_reason: str | None = None


class ValidationIssue(BaseModel):
    severity: str  # error | warning
    check: str
    path: str
    message: str


class ValidateResult(BaseModel):
    issues: list[ValidationIssue] = Field(default_factory=list)
    checked: int = 0

    @property
    def errors(self) -> list[ValidationIssue]:
        return [i for i in self.issues if i.severity == "error"]

    @property
    def ok(self) -> bool:
        return not self.errors


class BudgetState(BaseModel):
    """Enforced ceilings (ADR-004 / D6). Breach aborts with partial progress."""

    usd_spent: float = 0.0
    tokens_used: int = 0
    concepts_written: int = 0

    def would_breach(self, limits: Any) -> str | None:
        if self.usd_spent >= limits.max_usd_per_run:
            return f"USD ceiling reached ({self.usd_spent:.2f} >= {limits.max_usd_per_run})"
        if self.tokens_used >= limits.max_tokens_per_run:
            return f"token ceiling reached ({self.tokens_used} >= {limits.max_tokens_per_run})"
        if self.concepts_written >= limits.max_concepts_per_run:
            return f"concept ceiling reached ({self.concepts_written})"
        return None
