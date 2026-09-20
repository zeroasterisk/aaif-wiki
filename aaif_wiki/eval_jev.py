"""Build a deterministic Jev evaluation report from committed review records."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any


def evaluate_review_records(directory: Path) -> dict[str, Any]:
    """Summarize labelled outcomes without calling Jev or any other network."""
    totals: Counter[str] = Counter()
    kinds: Counter[str] = Counter()
    confidences: list[float] = []
    for path in sorted(directory.glob("*.json")):
        record = json.loads(path.read_text())
        status = str(record.get("review_status", "pending"))
        for mutation in record.get("mutations", []):
            assessment = mutation.get("jev_assessment")
            if not assessment:
                continue
            totals["assessed"] += 1
            totals[f"review_status:{status}"] += 1
            totals[f"decision:{assessment.get('decision', 'unknown')}"] += 1
            kinds[str(assessment.get("mutation_kind", "unknown"))] += 1
            confidences.append(float(assessment.get("confidence", 0.0)))
            # A reviewer may add this when closing the record. Keeping the label
            # in the committed JSON makes the eval reproducible in CI.
            label = mutation.get("human_label")
            if label:
                totals["labelled"] += 1
                totals["agreed"] += label.get("mutation_kind") == assessment.get("mutation_kind")
    labelled = totals["labelled"]
    return {
        "assessed": totals["assessed"],
        "labelled": labelled,
        "agreement": (totals["agreed"] / labelled) if labelled else None,
        "average_confidence": sum(confidences) / len(confidences) if confidences else None,
        "mutation_kinds": dict(sorted(kinds.items())),
        "counts": dict(sorted(totals.items())),
    }
