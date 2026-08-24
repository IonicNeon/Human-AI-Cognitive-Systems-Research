#!/usr/bin/env python3
"""Score a frozen IF-R003 context-recovery run.

This script never contains or reads hidden answer text. Human/independent
adjudication supplies item-level correctness fields in a run CSV. The script
validates the run against the frozen battery and computes prespecified metrics.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path

ALLOWED_SCORES = {0.0, 0.5, 1.0}
TRUE = {"1", "true", "yes", "y"}
FALSE = {"0", "false", "no", "n"}


def parse_bool(value: str, field: str, item_id: str, allow_blank: bool = False):
    v = (value or "").strip().lower()
    if allow_blank and not v:
        return None
    if v in TRUE:
        return True
    if v in FALSE:
        return False
    raise SystemExit(f"{item_id}: invalid boolean for {field}: {value!r}")


def wilson_interval(successes: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return (math.nan, math.nan)
    phat = successes / n
    denom = 1 + z * z / n
    center = (phat + z * z / (2 * n)) / denom
    margin = z * math.sqrt((phat * (1 - phat) + z * z / (4 * n)) / n) / denom
    return max(0.0, center - margin), min(1.0, center + margin)


def load_battery(path: Path) -> dict[str, dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    required = {"item_id", "stratum", "status", "freeze_version"}
    if not rows or not required.issubset(rows[0]):
        raise SystemExit(f"Battery missing columns: {sorted(required - set(rows[0] if rows else []))}")
    out = {}
    for row in rows:
        item_id = row["item_id"].strip()
        if item_id in out:
            raise SystemExit(f"Duplicate battery item: {item_id}")
        out[item_id] = row
    return out


def load_run(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    required = {
        "item_id", "accuracy_score", "evidence_exact", "unsupported_claim_count",
        "unknown_correct", "authoritative_source_correct", "stale_state_error",
        "elapsed_seconds", "tool_calls", "invalid_reason",
    }
    if not rows or not required.issubset(rows[0]):
        raise SystemExit(f"Run missing columns: {sorted(required - set(rows[0] if rows else []))}")
    return rows


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--battery", required=True)
    p.add_argument("--run", required=True)
    p.add_argument("--freeze-version", required=True)
    p.add_argument("--out", default="analysis/generated/context-recovery-score.json")
    args = p.parse_args()

    battery = load_battery(Path(args.battery))
    run = load_run(Path(args.run))

    frozen_ids = {
        item_id for item_id, row in battery.items()
        if row["status"].strip().lower() == "frozen"
        and row["freeze_version"].strip() == args.freeze_version
    }
    if not frozen_ids:
        raise SystemExit("No frozen battery items match the requested freeze version.")

    seen = set()
    valid_items = []
    invalid_items = []
    for row in run:
        item_id = row["item_id"].strip()
        if item_id in seen:
            raise SystemExit(f"Duplicate run item: {item_id}")
        seen.add(item_id)
        if item_id not in frozen_ids:
            raise SystemExit(f"Run item {item_id} is not in frozen battery {args.freeze_version}")
        if row["invalid_reason"].strip():
            invalid_items.append({"item_id": item_id, "reason": row["invalid_reason"].strip()})
            continue

        try:
            score = float(row["accuracy_score"])
        except ValueError:
            raise SystemExit(f"{item_id}: invalid accuracy_score {row['accuracy_score']!r}")
        if score not in ALLOWED_SCORES:
            raise SystemExit(f"{item_id}: accuracy_score must be one of {sorted(ALLOWED_SCORES)}")
        try:
            unsupported = int(row["unsupported_claim_count"])
            elapsed = float(row["elapsed_seconds"])
            tool_calls = int(row["tool_calls"])
        except ValueError as exc:
            raise SystemExit(f"{item_id}: numeric parse error: {exc}")
        if unsupported < 0 or elapsed < 0 or tool_calls < 0:
            raise SystemExit(f"{item_id}: counts/times cannot be negative")

        valid_items.append({
            "item_id": item_id,
            "stratum": battery[item_id]["stratum"],
            "accuracy_score": score,
            "evidence_exact": parse_bool(row["evidence_exact"], "evidence_exact", item_id),
            "unsupported_claim_count": unsupported,
            "unknown_correct": parse_bool(row["unknown_correct"], "unknown_correct", item_id, True),
            "authoritative_source_correct": parse_bool(
                row["authoritative_source_correct"], "authoritative_source_correct", item_id, True
            ),
            "stale_state_error": parse_bool(row["stale_state_error"], "stale_state_error", item_id),
            "elapsed_seconds": elapsed,
            "tool_calls": tool_calls,
        })

    missing = frozen_ids - seen
    if missing:
        raise SystemExit(f"Run is incomplete; missing frozen items: {sorted(missing)}")

    n = len(valid_items)
    if n == 0:
        raise SystemExit("No valid scored items remain after invalid-item filtering.")

    exact = sum(x["evidence_exact"] for x in valid_items)
    stale = sum(x["stale_state_error"] for x in valid_items)
    unknown_eligible = [x for x in valid_items if x["unknown_correct"] is not None]
    auth_eligible = [x for x in valid_items if x["authoritative_source_correct"] is not None]
    exact_ci = wilson_interval(exact, n)

    result = {
        "freeze_version": args.freeze_version,
        "n_frozen_items": len(frozen_ids),
        "n_valid_items": n,
        "n_invalid_items": len(invalid_items),
        "invalid_items": invalid_items,
        "mean_item_accuracy": sum(x["accuracy_score"] for x in valid_items) / n,
        "item_accuracy_distribution": {
            "0": sum(x["accuracy_score"] == 0 for x in valid_items),
            "0.5": sum(x["accuracy_score"] == 0.5 for x in valid_items),
            "1": sum(x["accuracy_score"] == 1 for x in valid_items),
        },
        "exact_evidence_rate": exact / n,
        "exact_evidence_rate_wilson_95": [exact_ci[0], exact_ci[1]],
        "unsupported_claims_total": sum(x["unsupported_claim_count"] for x in valid_items),
        "items_with_unsupported_claims": sum(x["unsupported_claim_count"] > 0 for x in valid_items),
        "stale_state_error_rate": stale / n,
        "unknown_detection": {
            "eligible_n": len(unknown_eligible),
            "correct_n": sum(bool(x["unknown_correct"]) for x in unknown_eligible),
        },
        "authoritative_source_discrimination": {
            "eligible_n": len(auth_eligible),
            "correct_n": sum(bool(x["authoritative_source_correct"]) for x in auth_eligible),
        },
        "elapsed_seconds_total": sum(x["elapsed_seconds"] for x in valid_items),
        "tool_calls_total": sum(x["tool_calls"] for x in valid_items),
        "item_results": valid_items,
        "interpretation_guardrail": (
            "This file scores one run only. Longitudinal effectiveness requires repeated comparable runs; "
            "a single run or readiness observation is not evidence of improvement."
        ),
    }

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
