#!/usr/bin/env python3
"""Compare scored IF-R003 context-recovery runs.

Primary comparisons require the same freeze_version. Mixed-version summaries need
an explicit --allow-mixed flag and are labeled non-primary.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

METRICS = [
    "mean_item_accuracy",
    "exact_evidence_rate",
    "stale_state_error_rate",
    "unsupported_claims_total",
    "items_with_unsupported_claims",
    "elapsed_seconds_total",
    "tool_calls_total",
]


def load_score(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    required = {"freeze_version", "n_valid_items", *METRICS}
    missing = required - set(data)
    if missing:
        raise SystemExit(f"{path}: missing fields {sorted(missing)}")
    data["_path"] = str(path)
    return data


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("scores", nargs="+", help="Score JSON files in chronological order")
    p.add_argument("--allow-mixed", action="store_true")
    p.add_argument("--out", default="analysis/generated/context-run-comparison.csv")
    args = p.parse_args()

    runs = [load_score(Path(x)) for x in args.scores]
    versions = {r["freeze_version"] for r in runs}
    if len(versions) > 1 and not args.allow_mixed:
        raise SystemExit(
            "Primary longitudinal comparison requires one freeze_version. "
            "Use --allow-mixed only for explicitly non-primary diagnostics."
        )

    rows = []
    first = runs[0]
    prev = None
    for i, run in enumerate(runs, start=1):
        row = {
            "run_order": i,
            "source_file": run["_path"],
            "freeze_version": run["freeze_version"],
            "comparison_class": "PRIMARY-COMPARABLE" if len(versions) == 1 else "MIXED-VERSION-NONPRIMARY",
            "n_valid_items": run["n_valid_items"],
        }
        for metric in METRICS:
            value = run[metric]
            row[metric] = value
            row[f"delta_from_first__{metric}"] = value - first[metric]
            row[f"delta_from_previous__{metric}"] = "" if prev is None else value - prev[metric]
        rows.append(row)
        prev = run

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    print(f"Wrote {len(rows)} runs to {out}")
    if len(versions) > 1:
        print("WARNING: mixed freeze versions; output is non-primary and must not support a longitudinal effectiveness claim.")


if __name__ == "__main__":
    main()
