# IF-R003 analysis

These scripts score and compare **adjudicated run records**. They do not contain the hidden answer key and do not independently judge natural-language responses.

## Score one run

Inputs:

- a frozen battery CSV containing at least `item_id,stratum,status,freeze_version`;
- a run CSV following `../instruments/context-recovery-run-template.csv`;
- the exact frozen version identifier.

Example:

```bash
python score_context_recovery.py \
  --battery ../instruments/context-recovery-battery.csv \
  --run ../data-public/example-scored-run.csv \
  --freeze-version v1 \
  --out generated/context-recovery-score.json
```

The scorer validates completeness and emits item accuracy, exact-evidence rate, unsupported-claim counts, stale-state error rate, unknown detection, authoritative-source discrimination, elapsed time, and tool-call totals.

## Compare repeated runs

```bash
python compare_context_runs.py \
  generated/run-001-score.json \
  generated/run-002-score.json \
  --out generated/context-run-comparison.csv
```

Primary longitudinal comparison requires the same `freeze_version`. Mixed versions require `--allow-mixed` and are labeled non-primary.

## Guardrails

- A single run does not establish improvement.
- Human/independent adjudication remains upstream of these scripts.
- Hidden answer text is not a public input.
- Synthetic/example rows must be labeled non-empirical.
- Confirmatory claims require the frozen protocol, benchmark/key versions, and comparable execution conditions.
