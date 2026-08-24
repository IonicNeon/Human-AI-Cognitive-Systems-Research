# Studies

Each directory is the permanent public home of one stable research identity.

```text
IF-R###-slug/
  README.md
  study.yml
  protocol/
  claims/
  literature/
  data-public/
  analysis/
  figures/
  outputs/
  provenance/
```

Folders do not move when publication plans change. Subdirectories are created when releasable material exists rather than as empty placeholders.

## Current public research objects

| ID | Study | Public surface |
|---|---|---|
| IF-R001 | Birth and emergence | metadata; historical result remains review-gated |
| IF-R002 | Evolution and selection pressures | metadata + event-adjudication method |
| IF-R003 | Effectiveness / replay / ablation | freeze/replay protocols, instruments, scoring and comparison code |
| IF-R004 | Cross-domain generalization | prospective design, public matrix schema, threshold evaluator |
| IF-R005 | Goal actualization | project/outcome coding method |
| IF-R006 | Inception and path dependence | comparative inception/drift program design |
| IF-R007 | Seeded onboarding | metadata; ethics-gated human-participant design |
| IF-R008 | Lineage drift | metadata; longitudinal comparative program |
| IF-R009 | Intellectual antecedents | conceptual-lineage coding method |
| IF-R010 | Self-model emergence | metadata/hypothesis only |
| IF-R011 | High-benefit validation | metadata/prospective program only |

Every study has a local `study.yml` that must agree with `../research-registry.yml`. CI checks this correspondence on pull requests and pushes to `main`.

## Data boundary

Public study data belongs only in `data-public/`. A raw `data/` directory under a study is prohibited by the repository validator because raw/private evidence must never be staged here.
