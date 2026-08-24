# IF-R004 analysis

`evaluate_generalization.py` evaluates the **descriptive structural threshold** defined in `../protocol/STUDY-DESIGN.md`. It does not infer outcome generalization from reuse or maturity counts.

## Input

Start from the public schema:

`../data-public/mechanism-environment-matrix-template.csv`

Populate a reviewed matrix as:

`../data-public/mechanism-environment-matrix.csv`

Primary analysis uses rows whose `reviewer_disposition` is `included`.

## Run

From the IF-R004 study directory:

```bash
python analysis/evaluate_generalization.py \
  --input data-public/mechanism-environment-matrix.csv \
  --out analysis/generated/generalization-summary.json
```

For exploratory diagnostics that include candidate/disputed/deferred rows:

```bash
python analysis/evaluate_generalization.py \
  --input data-public/mechanism-environment-matrix.csv \
  --include-candidates \
  --out analysis/generated/generalization-summary-exploratory.json
```

## Qualification logic

A mechanism must show actual use in at least three non-core application environments, verification beyond proposal in at least two, independent source identifiers for actual-use rows, and a defined invariant core.

The standalone-positive-paper flag requires at least two qualifying mechanisms.

## Guardrail

Structural qualification establishes descriptive cross-domain reuse only. Outcome generalization requires comparable functional measures and the stronger conditions in `../protocol/STUDY-DESIGN.md`.
