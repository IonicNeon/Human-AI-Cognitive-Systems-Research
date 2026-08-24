# IF-R003 — Experiment Freeze Checklist

**Status:** pre-data-collection gate  
**Public class:** `NONEMPIRICAL-METHOD`

No controlled effectiveness run should enter the confirmatory dataset until every required item below is frozen or explicitly waived in a dated amendment.

## Research question and hypotheses

- [ ] Primary effectiveness question is testable.
- [ ] Primary hypotheses are written before controlled outcome collection.
- [ ] Secondary/exploratory analyses are labeled separately.
- [ ] Unit of analysis is defined.
- [ ] Comparison condition(s) are defined.

## Benchmark battery

- [ ] Benchmark strata are defined and justified.
- [ ] Inclusion/exclusion rules are fixed.
- [ ] Item count per stratum is fixed or governed by a predeclared sampling rule.
- [ ] Difficulty/breadth balancing is documented.
- [ ] Items that depend on unstable current state are version-pinned.
- [ ] Private material is classified and publication handling is defined.

## Ground truth and answer key

- [ ] Correct-answer/evidence key exists independently of the tested response.
- [ ] Key is hidden from the tested process.
- [ ] Each item identifies acceptable evidence sources.
- [ ] Ambiguous or partially correct answers have explicit scoring rules.
- [ ] Unresolvable items are removable only under predeclared invalid-item criteria.

## Scoring

- [ ] Required facts recovered is defined.
- [ ] Incorrect claims is defined.
- [ ] Unsupported claims is defined.
- [ ] Provenance quality uses a fixed rule.
- [ ] Contradiction handling is scored where applicable.
- [ ] Completion/abstention behavior is explicit.
- [ ] Composite formulas, if any, are fixed.
- [ ] Human judgment fields have adjudication guidance.

## Conditions and execution

- [ ] Model/tool identity recording rule is fixed.
- [ ] System/prompt/context package is versioned.
- [ ] Allowed tools/connectors are fixed per condition.
- [ ] Time/step/token limits, if used, are fixed.
- [ ] Ordering/randomization/counterbalancing is fixed.
- [ ] Retry policy is fixed.
- [ ] Fresh-session requirement is defined.
- [ ] Contamination/leakage rule is defined.

## Invalid-run and stopping rules

- [ ] Infrastructure failure criteria are defined.
- [ ] Tool outage/connector failure treatment is defined.
- [ ] Human-intervention invalidation criteria are defined.
- [ ] Duplicate/accidental rerun handling is defined.
- [ ] Planned sample size or stopping rule is fixed.
- [ ] Favorable-result early stopping is prohibited unless preregistered.

## Data capture

- [ ] Observation schema is versioned.
- [ ] Raw response preservation rule is defined.
- [ ] Provenance and timestamps are mandatory.
- [ ] Environment/version metadata are mandatory.
- [ ] Manual scorer identity/adjudication fields exist where needed.
- [ ] Private/raw and public-safe derivative fields are separated.

## Analysis plan

- [ ] Primary metrics are named before outcome review.
- [ ] Aggregation procedure is fixed.
- [ ] Missing-data treatment is fixed.
- [ ] Outlier treatment is fixed.
- [ ] Uncertainty reporting method is fixed.
- [ ] Statistical tests, if used, are selected before confirmatory analysis.
- [ ] Multiple-comparison handling is specified where relevant.
- [ ] Exploratory analyses are visibly separated.

## Reproducibility

- [ ] Analysis scripts run on mock/simulated data.
- [ ] Mock data are unmistakably labeled non-empirical.
- [ ] Generated tables/figures come from inputs/code rather than hand-edited values.
- [ ] Environment/dependency specification exists.
- [ ] Random seeds are recorded where applicable.
- [ ] Versioned artifact paths are fixed.

## Publication and ethics/privacy

- [ ] Raw private corpus material is excluded from public release by default.
- [ ] Public-safe derivation rules are documented.
- [ ] AI-use disclosure language is prepared.
- [ ] Authorship/contribution decision process is documented.
- [ ] First-person study limitations are predeclared where relevant.

## Freeze declaration

Create a dated freeze record containing:

- protocol version;
- benchmark version/hash;
- answer-key version/hash;
- scoring-rubric version/hash;
- analysis-plan version/hash;
- execution-environment specification;
- exact commit SHA containing the frozen package.

Any later change that could alter outcomes, scoring, inclusion, or interpretation requires an amendment stating whether existing observations remain comparable.
