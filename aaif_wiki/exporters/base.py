"""Exporter interface and the outbound trust boundary.

Every exporter must pass the leak guard before publishing. This is the outbound
half of ADR-007; the inbound half lives in the curator's prompt fencing and the
structured-mutation write path.
"""

from __future__ import annotations

import re
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urlparse

from ..config import Config
from ..models import Concept

URL_RE = re.compile(r"https?://[^\s<>()\[\]\"']+")


@dataclass
class ExportResult:
    ok: bool
    artifacts: list[Path] = field(default_factory=list)
    blocked: list[str] = field(default_factory=list)
    message: str = ""


class PrivacyViolation(RuntimeError):
    pass


class BaseExporter(ABC):
    name = "base"

    def __init__(self, cfg: Config):
        self.cfg = cfg

    # -- guards ---------------------------------------------------------
    def validate_privacy(self, text: str, origin: str = "") -> list[str]:
        """Deterministic regex audit. Returns a list of violations."""
        violations = []
        for pattern in self.cfg.trust.forbidden_patterns:
            for match in re.finditer(pattern, text):
                violations.append(f"{origin}: forbidden pattern {pattern!r} -> {match.group(0)!r}")
        for url in URL_RE.findall(text):
            host = (urlparse(url).hostname or "").lower()
            allow = self.cfg.trust.link_allowlist
            if host and not any(host == a or host.endswith("." + a) for a in allow):
                violations.append(f"{origin}: non-allowlisted host {host!r}")
        return violations

    def sanitize(self, text: str) -> str:
        """Strip local file URIs and normalize to public URLs."""
        text = re.sub(r"file://\S+", "[local-path-removed]", text)
        text = text.replace(str(self.cfg.root), "")
        return text

    def guard(self, concepts: list[Concept]) -> list[str]:
        blocked = []
        for c in concepts:
            blocked.extend(self.validate_privacy(c.body, origin=c.relative_path()))
        return blocked

    # -- contract -------------------------------------------------------
    @abstractmethod
    def export(self) -> ExportResult: ...
