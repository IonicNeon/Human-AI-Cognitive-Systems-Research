#!/usr/bin/env python3
"""Validate the public research registry and study structure.

Requires PyYAML. This validator intentionally checks governance/structure only;
it does not validate empirical claims or private provenance.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "research-registry.yml"
STUDIES = ROOT / "studies"

ID_RE = re.compile(r"^IF-R\d{3}$")
ALLOWED_RELATIONS = {
    "spawned-by",
    "derived-from",
    "extends",
    "tests",
    "replicates",
    "attempts-to-falsify",
    "challenges",
    "operationalizes",
    "uses-method-from",
    "uses-data-from",
    "generalizes",
    "compares-with",
    "supersedes",
    "inspired-by",
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def main() -> int:
    errors: list[str] = []

    data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    objects = data.get("research_objects", [])
    if not objects:
        fail(errors, "research-registry.yml contains no research_objects")

    by_id: dict[str, dict] = {}
    for obj in objects:
        rid = obj.get("id")
        slug = obj.get("slug")
        if not isinstance(rid, str) or not ID_RE.fullmatch(rid):
            fail(errors, f"invalid research id: {rid!r}")
            continue
        if rid in by_id:
            fail(errors, f"duplicate research id: {rid}")
        by_id[rid] = obj
        if not isinstance(slug, str) or not slug.strip():
            fail(errors, f"{rid}: missing slug")

    for rid, obj in by_id.items():
        slug = obj["slug"]
        expected = STUDIES / f"{rid}-{slug}"
        if not expected.is_dir():
            fail(errors, f"{rid}: missing study directory {expected.relative_to(ROOT)}")
            continue

        metadata_path = expected / "study.yml"
        if not metadata_path.is_file():
            fail(errors, f"{rid}: missing {metadata_path.relative_to(ROOT)}")
        else:
            local = yaml.safe_load(metadata_path.read_text(encoding="utf-8")) or {}
            for field in ("id", "slug", "title", "kind", "status", "public_state"):
                if local.get(field) != obj.get(field):
                    fail(
                        errors,
                        f"{rid}: study.yml {field}={local.get(field)!r} "
                        f"!= registry {obj.get(field)!r}",
                    )

        for parent in obj.get("parents", []) or []:
            pid = parent.get("id")
            relation = parent.get("relation")
            if pid not in by_id:
                fail(errors, f"{rid}: unknown parent id {pid!r}")
            if relation not in ALLOWED_RELATIONS:
                fail(errors, f"{rid}: invalid lineage relation {relation!r}")
            if pid == rid:
                fail(errors, f"{rid}: self-parent relationship is not allowed")

    # Public study data must never use an ambiguous raw `data/` directory.
    for path in STUDIES.rglob("data"):
        if path.is_dir():
            fail(errors, f"forbidden public study directory: {path.relative_to(ROOT)}; use data-public/")

    required_root = [
        "README.md",
        "AGENTS.md",
        "GOVERNANCE.md",
        "PUBLICATION-POLICY.md",
        "research-registry.yml",
        "docs/PUBLIC-RELEASE-CHECKLIST.md",
        "lineage/research-lineage.json",
    ]
    for rel in required_root:
        if not (ROOT / rel).exists():
            fail(errors, f"missing required governance artifact: {rel}")

    if errors:
        print("Research-structure validation FAILED:\n")
        for item in errors:
            print(f"- {item}")
        return 1

    print(
        f"Research-structure validation passed: {len(by_id)} research objects, "
        f"{len(ALLOWED_RELATIONS)} controlled lineage relations."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
