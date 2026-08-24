#!/usr/bin/env python3
"""Evaluate IF-R004 descriptive-generalization thresholds.

This script evaluates structural qualification only. It does not infer outcome
generalization from reuse or maturity counts.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path

TRUE = {"1", "true", "yes", "y"}
FALSE = {"0", "false", "no", "n"}
ALLOWED_DISPOSITIONS = {"candidate", "included", "excluded", "disputed", "deferred", "superseded"}


def parse_bool(value: str, item: str, field: str) -> bool:
    v = (value or "").strip().lower()
    if v in TRUE:
        return True
    if v in FALSE:
        return False
    raise SystemExit(f"{item}: {field} must be yes/no, got {value!r}")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--input", default="data-public/mechanism-environment-matrix.csv")
    p.add_argument("--out", default="analysis/generated/generalization-summary.json")
    p.add_argument("--include-candidates", action="store_true", help="Exploratory only; primary output uses included rows.")
    args = p.parse_args()

    path = Path(args.input)
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        raise SystemExit(f"No matrix rows in {path}")

    required = {
        "mechanism_id", "mechanism_version", "mechanism_name", "application_environment",
        "source_ids", "maturity", "actual_use", "verified_beyond_proposal",
        "invariant_core", "reviewer_disposition",
    }
    missing = required - set(rows[0])
    if missing:
        raise SystemExit(f"Missing columns: {sorted(missing)}")

    selected = []
    seen = set()
    for row in rows:
        key = (row["mechanism_id"].strip(), row["application_environment"].strip())
        if not all(key):
            raise SystemExit(f"Missing mechanism/environment key: {key}")
        if key in seen:
            raise SystemExit(f"Duplicate mechanism/environment row: {key}")
        seen.add(key)
        disp = row["reviewer_disposition"].strip().lower()
        if disp not in ALLOWED_DISPOSITIONS:
            raise SystemExit(f"{key}: invalid reviewer_disposition {disp!r}")
        row["_actual_use"] = parse_bool(row["actual_use"], str(key), "actual_use")
        row["_verified"] = parse_bool(row["verified_beyond_proposal"], str(key), "verified_beyond_proposal")
        if disp == "included" or (args.include_candidates and disp in {"candidate", "disputed", "deferred"}):
            selected.append(row)

    by_mechanism = defaultdict(list)
    for row in selected:
        by_mechanism[row["mechanism_id"]].append(row)

    evaluations = []
    qualifying = []
    for mechanism_id, mrows in sorted(by_mechanism.items()):
        actual = [r for r in mrows if r["_actual_use"]]
        domains = sorted({r["application_environment"] for r in actual if r["application_environment"] != "Foundry-core / infrastructure"})
        verified_domains = sorted({
            r["application_environment"] for r in actual
            if r["_verified"] and r["application_environment"] != "Foundry-core / infrastructure"
        })
        independent_sources = all(bool(r["source_ids"].strip()) for r in actual)
        invariant_defined = all(bool(r["invariant_core"].strip()) for r in actual)
        qualifies = (
            len(domains) >= 3
            and len(verified_domains) >= 2
            and independent_sources
            and invariant_defined
        )
        record = {
            "mechanism_id": mechanism_id,
            "mechanism_name": mrows[0]["mechanism_name"],
            "mechanism_version": mrows[0]["mechanism_version"],
            "actual_use_domains": domains,
            "verified_domains": verified_domains,
            "independent_sources_present": independent_sources,
            "invariant_core_defined": invariant_defined,
            "descriptive_generalization_qualifies": qualifies,
        }
        evaluations.append(record)
        if qualifies:
            qualifying.append(mechanism_id)

    result = {
        "analysis_class": "EXPLORATORY" if args.include_candidates else "INCLUDED-ROWS-ONLY",
        "n_selected_matrix_rows": len(selected),
        "n_mechanisms_evaluated": len(evaluations),
        "qualifying_mechanism_ids": qualifying,
        "n_qualifying_mechanisms": len(qualifying),
        "standalone_positive_paper_threshold_met": len(qualifying) >= 2,
        "mechanisms": evaluations,
        "guardrail": (
            "Qualification establishes descriptive cross-domain reuse only. "
            "Outcome generalization requires separate comparable functional measures under protocol/STUDY-DESIGN.md."
        ),
    }

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
