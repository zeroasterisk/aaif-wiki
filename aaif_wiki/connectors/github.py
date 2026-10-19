"""GitHub ingestion (ADR-003 / D7).

Rate limiting drives the whole shape of this module. Unauthenticated GitHub REST
allows 60 requests/hour, which is nowhere near enough to walk 15 repositories. So:

* **File content comes from git**, not the API. ``git clone --depth`` against a
  public repo has no REST rate limit, gives us real blob SHAs for free, and doubles
  as the offline cache that makes replay work without network.
* **The REST API is reserved for what git cannot see**: pull requests, issues and
  discussions. These are also precisely the sources that are editable and deletable
  upstream, which is why they are the ones stored inline rather than as pointers.
* ``GITHUB_TOKEN``/``GH_TOKEN`` raises the ceiling to 5000/hour and is used when set.

Every response is cached on disk, so a re-run inside the same window costs nothing.
"""

from __future__ import annotations

import hashlib
import json
import logging
import subprocess
import time
from datetime import UTC, datetime
from pathlib import Path

import httpx

from ..config import ExternalSourceCfg, GitHubCfg
from ..models import FilePointer, Lifecycle, RawEvent, SourceType

log = logging.getLogger("aaif_wiki.connectors.github")

API = "https://api.github.com"
USER_AGENT = "aaif-wiki/0.1 (+https://github.com/zeroasterisk/aaif-wiki)"


def _slug(text: str) -> str:
    return "".join(c if c.isalnum() else "-" for c in text.lower()).strip("-")[:60]


def _digest(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:12]


class RateLimited(RuntimeError):
    """Raised when GitHub refuses further requests; the caller degrades gracefully."""


def is_external(repo: str) -> bool:
    """Syntactic check: AAIF repos are bare names; external sources are ``owner/name``.

    Being ``owner/name`` is not enough to be ingested: ``GitHubConnector.resolve``
    rejects anything not on the ``sources.github.external`` allowlist (ADR-013).
    """
    return "/" in repo


class UnlistedRepo(ValueError):
    """An ``owner/name`` that is not on the external allowlist."""


class GitHubConnector:
    def __init__(self, cfg: GitHubCfg, cache_dir: Path):
        self.cfg = cfg
        self.cache_dir = cache_dir
        self.api_cache = cache_dir / "api"
        self.repo_cache = cache_dir / "repos"
        self.api_cache.mkdir(parents=True, exist_ok=True)
        self.repo_cache.mkdir(parents=True, exist_ok=True)
        self._budget_exhausted = False

    # -- HTTP -----------------------------------------------------------
    def _headers(self, *, authenticated: bool = True) -> dict:
        headers = {"Accept": "application/vnd.github+json", "User-Agent": USER_AGENT}
        # The AAIF token is scoped to the aaif org; never send it elsewhere (ADR-013 §4).
        token = self.cfg.token() if authenticated else None
        if token:
            headers["Authorization"] = f"Bearer {token}"
        return headers

    def _get(
        self, url: str, *, ttl_seconds: int = 3600, authenticated: bool = True
    ) -> list | dict | None:
        """Cached GET. Returns None when the request cannot be served."""
        key = self.api_cache / f"{_digest(url)}.json"
        if key.exists() and (time.time() - key.stat().st_mtime) < ttl_seconds:
            try:
                return json.loads(key.read_text())
            except json.JSONDecodeError:
                pass
        if self._budget_exhausted:
            return None
        try:
            resp = httpx.get(url, headers=self._headers(authenticated=authenticated), timeout=30.0)
        except httpx.HTTPError:
            return None

        if resp.status_code == 403 and "rate limit" in resp.text.lower():
            self._budget_exhausted = True
            return None
        if resp.status_code == 404:
            return None
        if resp.status_code >= 400:
            return None

        data = resp.json()
        key.write_text(json.dumps(data))
        return data

    def rate_limit(self) -> dict:
        data = self._get(f"{API}/rate_limit", ttl_seconds=0) or {}
        core = (data.get("resources") or {}).get("core") or {}
        return {"limit": core.get("limit", 0), "remaining": core.get("remaining", 0)}

    # -- repo discovery -------------------------------------------------
    def discover_repos(self) -> list[str]:
        """Discover repos from the org API, falling back to the configured list.

        Hardcoding the repo list means silently missing a new working group, which
        would be a direct failure of the project's purpose.

        External (non-AAIF) sources are appended as ``owner/name``. They are an
        explicit allowlist, never discovered: adjacent orgs are not ours to crawl.
        """
        return self._discover_aaif() + [e.repo for e in self.cfg.external]

    def _discover_aaif(self) -> list[str]:
        if not self.cfg.discover_repos:
            return list(self.cfg.repositories)
        data = self._get(f"{API}/orgs/{self.cfg.org}/repos?per_page=100", ttl_seconds=86400)
        if not isinstance(data, list) or not data:
            return list(self.cfg.repositories)
        names = [
            r["name"]
            for r in data
            if isinstance(r, dict)
            and not r.get("archived")
            and r.get("name") not in set(self.cfg.exclude_repos)
        ]
        return sorted(names) or list(self.cfg.repositories)

    # -- coordinates ----------------------------------------------------
    def resolve(self, repo: str) -> str:
        """Canonical repo key. Bare names (and ``aaif/name``) are AAIF; any other
        ``owner/name`` must be allowlisted and is returned in its configured case,
        so ``Coinbase/X402`` and ``coinbase/x402`` produce the same coordinates."""
        repo = repo.strip().strip("/")
        owner, _, name = repo.partition("/")
        if name and owner.lower() == self.cfg.org.lower():
            return name
        if not name:
            return repo
        ext = self.cfg.external_for(repo)
        if ext is None:
            raise UnlistedRepo(f"{repo} is not in sources.github.external (ADR-013)")
        return ext.repo

    def _full_name(self, repo: str) -> str:
        return repo if is_external(repo) else f"{self.cfg.org}/{repo}"

    def _external(self, repo: str) -> ExternalSourceCfg | None:
        return self.cfg.external_for(repo) if is_external(repo) else None

    def _event_prefix(self, repo: str) -> str:
        """Event ids become filenames, so ``owner/name`` cannot appear verbatim.

        The slug is lossy (``a-b/c`` and ``a/b-c`` both slug to ``a-b-c``), so a
        short hash of the exact lower-cased name keeps ids collision-free.
        """
        if not is_external(repo):
            return repo
        return f"ext-{_slug(repo)}-{_digest(repo.lower())[:6]}"

    # -- git mirror -----------------------------------------------------
    def sync_repo(self, repo: str) -> Path | None:
        """Maintain a shallow local mirror. This is the offline replay cache."""
        import os

        dest = self.repo_cache / repo
        dest.parent.mkdir(parents=True, exist_ok=True)
        token = self.cfg.token()
        # External sources are public and outside the AAIF token's scope: clone anonymously.
        if token and not is_external(repo):
            url = f"https://x-access-token:{token}@github.com/{self.cfg.org}/{repo}.git"
        else:
            url = f"https://github.com/{self._full_name(repo)}.git"
        env = {**os.environ, "GIT_TERMINAL_PROMPT": "0"}
        try:
            if dest.exists():
                subprocess.run(
                    ["git", "-C", str(dest), "fetch", "--depth", "50", "--quiet", "origin"],
                    check=True, capture_output=True, timeout=120, env=env,
                )
                head = subprocess.run(
                    ["git", "-C", str(dest), "rev-parse", "FETCH_HEAD"],
                    check=True, capture_output=True, text=True, timeout=30, env=env,
                ).stdout.strip()
                subprocess.run(
                    ["git", "-C", str(dest), "reset", "--hard", head, "--quiet"],
                    check=True, capture_output=True, timeout=60, env=env,
                )
            else:
                subprocess.run(
                    ["git", "clone", "--depth", "50", "--quiet", url, str(dest)],
                    check=True, capture_output=True, timeout=60, env=env,
                )
            return dest
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
            return dest if dest.exists() else None

    def _git(self, repo_dir: Path, *args: str) -> str:
        try:
            return subprocess.run(
                ["git", "-C", str(repo_dir), *args],
                check=True, capture_output=True, text=True, timeout=60,
            ).stdout
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
            return ""

    def read_pointer(self, ptr: FilePointer) -> str | None:
        """Rehydrate pointer-backed content from the local mirror."""
        repo_dir = self.repo_cache / ptr.repo
        if not repo_dir.exists():
            return None
        out = self._git(repo_dir, "cat-file", "-p", ptr.blob_sha)
        return out or None

    # -- events: repository files ---------------------------------------
    def scan_files(self, repo: str, limit: int = 200) -> list[RawEvent]:
        """One event per tracked document, pointer-backed (git reproduces content)."""
        repo_dir = self.sync_repo(repo)
        if not repo_dir:
            return []

        head = self._git(repo_dir, "rev-parse", "HEAD").strip()
        if not head:
            return []

        listing = self._git(repo_dir, "ls-tree", "-r", "HEAD")
        ext = self._external(repo)
        full = self._full_name(repo)
        prefix = self._event_prefix(repo)
        events: list[RawEvent] = []
        lines = listing.splitlines()
        if ext is not None:
            limit = min(limit, ext.file_limit)
            candidates = self._select_external(lines, ext)
            if len(candidates) > limit:
                log.warning(
                    "%s: file_limit %d keeps %d of %d matching files; dropped e.g. %s",
                    repo, limit, limit, len(candidates), candidates[limit][1],
                )
        else:
            candidates = [
                c for c in map(self._blob, lines[: limit * 4])
                if c and any(c[1].endswith(x) for x in self.cfg.doc_extensions)
            ]
        for blob_sha, path in candidates:
            when = self._git(repo_dir, "log", "-1", "--format=%cI", "--", path).strip()
            author = self._git(repo_dir, "log", "-1", "--format=%an", "--", path).strip()
            subject = self._git(repo_dir, "log", "-1", "--format=%s", "--", path).strip()
            try:
                ts = datetime.fromisoformat(when) if when else datetime.now(UTC)
            except ValueError:
                ts = datetime.now(UTC)

            events.append(
                RawEvent(
                    event_id=f"evt-{prefix}-file-{_digest(path)}-{blob_sha[:8]}",
                    source_type=SourceType.REPO_FILE,
                    lifecycle=Lifecycle.MERGED,
                    repository=full,
                    reference_id=path,
                    title=path.rsplit("/", 1)[-1],
                    timestamp=ts,
                    author=author or None,
                    url=f"https://github.com/{full}/blob/{head}/{path}",
                    summary=subject,
                    labels=self._labels(ext),
                    pointers=[
                        FilePointer(
                            repo=repo, commit_sha=head, path=path, blob_sha=blob_sha, status="present"
                        )
                    ],
                )
            )
            if len(events) >= limit:
                break
        return events

    @staticmethod
    def _blob(line: str) -> tuple[str, str] | None:
        """``<mode> <type> <sha>\\t<path>`` -> (sha, path) for blobs."""
        try:
            meta, path = line.split("\t", 1)
            _mode, obj_type, blob_sha = meta.split()
        except ValueError:
            return None
        return (blob_sha, path) if obj_type == "blob" else None

    @staticmethod
    def _select_external(lines: list[str], ext: ExternalSourceCfg) -> list[tuple[str, str]]:
        """Matching files ranked by ``include_paths`` order, then by path.

        ``ls-tree`` order is alphabetical, so cutting at ``file_limit`` kept
        ``docs/examples/*`` and dropped the actual specs. Listing order in the
        config is now the priority: put the normative paths first.
        """
        def rank(path: str) -> int | None:
            for i, p in enumerate(ext.include_paths or [""]):
                if not p or path == p or path.startswith(p.rstrip("/") + "/"):
                    return i
            return None

        ranked = []
        for blob in map(GitHubConnector._blob, lines):
            if not blob or not any(blob[1].endswith(x) for x in ext.doc_extensions):
                continue
            r = rank(blob[1])
            if r is not None:
                ranked.append((r, blob[1].count("/"), blob[1], blob[0]))
        return [(sha, path) for _r, _d, path, sha in sorted(ranked)]

    # -- events: pull requests, issues, discussions ----------------------
    def scan_pull_requests(self, repo: str) -> list[RawEvent]:
        ext = self._external(repo)
        if not (ext.include_prs if ext is not None else self.cfg.include_open_prs):
            return []
        data = self._get(
            f"{API}/repos/{self._full_name(repo)}/pulls"
            f"?state=all&sort=updated&direction=desc&per_page={self.cfg.max_items_per_repo}",
            authenticated=ext is None,
        )
        if not isinstance(data, list):
            return []
        events = []
        for pr in data:
            if not isinstance(pr, dict):
                continue
            if pr.get("merged_at"):
                lifecycle = Lifecycle.MERGED
            elif pr.get("state") == "closed":
                lifecycle = Lifecycle.CLOSED
            elif pr.get("draft"):
                lifecycle = Lifecycle.DRAFT
            else:
                lifecycle = Lifecycle.OPEN
            events.append(
                self._issue_like_event(repo, pr, SourceType.PULL_REQUEST, lifecycle, "PR")
            )
        return [e for e in events if e]

    def scan_issues(self, repo: str) -> list[RawEvent]:
        ext = self._external(repo)
        if not (ext.include_issues if ext is not None else self.cfg.include_issues):
            return []
        data = self._get(
            f"{API}/repos/{self._full_name(repo)}/issues"
            f"?state=open&sort=updated&direction=desc&per_page={self.cfg.max_items_per_repo}",
            authenticated=ext is None,
        )
        if not isinstance(data, list):
            return []
        events = []
        for issue in data:
            if not isinstance(issue, dict) or issue.get("pull_request"):
                continue  # the issues endpoint also returns PRs
            events.append(
                self._issue_like_event(repo, issue, SourceType.ISSUE, Lifecycle.OPEN, "ISSUE")
            )
        return [e for e in events if e]

    def _issue_like_event(
        self, repo: str, payload: dict, source_type: SourceType, lifecycle: Lifecycle, prefix: str
    ) -> RawEvent | None:
        number = payload.get("number")
        if number is None:
            return None
        when = payload.get("updated_at") or payload.get("created_at")
        try:
            ts = datetime.fromisoformat(when.replace("Z", "+00:00")) if when else datetime.now(UTC)
        except (ValueError, AttributeError):
            ts = datetime.now(UTC)

        # Inline, because git cannot reproduce this and it can be edited or deleted.
        body = (payload.get("body") or "").strip()
        return RawEvent(
            event_id=f"evt-{self._event_prefix(repo)}-{prefix.lower()}-{number}",
            source_type=source_type,
            lifecycle=lifecycle,
            repository=self._full_name(repo),
            reference_id=f"{prefix}#{number}",
            title=payload.get("title") or f"{prefix} #{number}",
            timestamp=ts,
            author=(payload.get("user") or {}).get("login"),
            url=payload.get("html_url"),
            summary=(body[:280] + "...") if len(body) > 280 else body,
            inline_text=body or None,
            labels=[
                lbl.get("name", "")
                for lbl in (payload.get("labels") or [])
                if isinstance(lbl, dict)
            ]
            + self._labels(self._external(repo)),
        )

    @staticmethod
    def _labels(ext: ExternalSourceCfg | None) -> list[str]:
        """Provenance labels the curator and validators key off (ADR-013)."""
        if ext is None:
            return []
        return ["external", f"steward:{ext.steward}", *(f"topic:{t}" for t in ext.topics)]

    # -- orchestration entry point ---------------------------------------
    def scan_repo(self, repo: str, file_limit: int = 200) -> list[RawEvent]:
        repo = self.resolve(repo)  # raises UnlistedRepo for non-allowlisted owner/name
        events: list[RawEvent] = []
        events.extend(self.scan_files(repo, limit=file_limit))
        events.extend(self.scan_pull_requests(repo))
        events.extend(self.scan_issues(repo))
        return events
