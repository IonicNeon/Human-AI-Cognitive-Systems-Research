# IF-R003 — Prospective Effectiveness, Replay, and Mechanism Ablation

**Status:** prespecification-in-progress  
**Public state:** methods-only  
**Research class:** prospective experimental study  
**Parents:** IF-R001 (`tests`), IF-R002 (`operationalizes`)

## Core question

Does maturation of the architecture improve measurable knowledge-work performance and reduce classified failures?

IF-R003 is the first study in the program intended to test effectiveness prospectively rather than infer it from repository history. Historical growth, persistence, complexity, or owner preference do not count as evidence that the architecture improves outcomes.

No effectiveness result should be claimed before the protocol, task battery, scoring rules, exclusions, and primary outcomes are frozen.

## Primary estimand

Within the defined study environment, what is the effect of the full governed architecture, relative to prespecified comparison conditions, on successful completion of standardized knowledge-work tasks under a fixed resource/time budget?

This is initially a **within-case** estimand. It does not establish population-level human benefit.

## Research questions

1. **RQ3.1 — Task success:** Does the full architecture increase the proportion of tasks completed to prespecified acceptance criteria?
2. **RQ3.2 — Failure prevention:** Does it reduce classified state, provenance, retrieval, contradiction, and handoff failures?
3. **RQ3.3 — Recovery:** When failure occurs, does it reduce recovery time or correction work?
4. **RQ3.4 — Mechanism contribution:** Which architecture components materially contribute to observed effects?
5. **RQ3.5 — Cost:** What maintenance, latency, interaction, or complexity costs accompany any benefit?

## Candidate confirmatory hypotheses

These remain provisional until a preregistration/frozen protocol is committed.

- **H3.1:** the full architecture will produce a higher standardized task-success rate than the baseline condition.
- **H3.2:** the full architecture will produce fewer critical information-state failures per task than baseline.
- **H3.3:** the full architecture will reduce median time-to-recovery after seeded or naturally occurring recoverable failures.
- **H3.4:** ablation of retrieval, provenance/validation, or continuity/state mechanisms will degrade at least one prespecified primary or secondary outcome relative to the full condition.

A null result, mixed result, or cost increase must be preserved and reported.

## Experimental conditions

The final protocol should use the smallest set of conditions that can answer the mechanism questions without creating an unmanageable experiment.

### A. Baseline

A minimally governed AI-assisted workflow approximating conversation/file-based work without the full canonical-state, provenance, validation, and continuity machinery. The exact baseline must be instantiated and versioned rather than described abstractly.

### B. Full architecture

The frozen Idea-Foundry configuration selected for the experiment, including the mechanisms explicitly named in the protocol.

### C. Mechanism ablations

Candidate ablations include:

- retrieval/indexing unavailable or reduced;
- provenance/validation checks unavailable or reduced;
- explicit continuity/handoff state unavailable or reduced;
- canonical-state admission controls unavailable or reduced.

Only ablations that can be implemented without introducing unrelated breakage should be used. Each ablation must document what remains constant.

## Task battery

Tasks should represent recurring classes of knowledge work rather than bespoke demonstrations chosen because the system already performs them well.

Candidate task classes:

- retrieve and reconcile prior decisions/evidence;
- resume a partially completed multi-step task after interruption;
- update canonical state from mixed new evidence;
- detect a contradiction or invalid data promotion;
- produce a traceable answer with source/provenance recovery;
- hand off a task between sessions/agents without losing state;
- recover from a seeded missing/stale/incorrect state condition.

Each task needs:

- fixed prompt/input package;
- acceptance criteria;
- maximum time or action budget;
- scoring rubric;
- critical-failure definition;
- allowed tools/models;
- contamination/learning notes.

## Primary outcomes

### 1. Standardized task success

Binary or ordinal score based on prespecified acceptance criteria. Human judgment should be minimized where machine-checkable criteria are possible.

### 2. Critical information-state failure rate

Number or proportion of tasks containing prespecified failures such as:

- wrong canonical fact promoted;
- required provenance unrecoverable;
- contradiction missed;
- stale state treated as current;
- handoff loses required context;
- invalid source treated as authoritative.

The taxonomy must be frozen before confirmatory scoring.

## Secondary outcomes

- completion time;
- number of corrective actions;
- recovery time after failure;
- provenance-recovery success;
- retrieval precision for task-relevant state;
- number of unnecessary tool/model calls;
- human interventions required;
- maintenance/setup overhead;
- subjective workload, if collected with a prespecified instrument.

Do not collapse heterogeneous metrics into a single “productivity” score unless the weighting rule is fixed before data exposure.

## Experimental design

A blocked within-case repeated-measures design is preferred for the initial study because the same principal operator can encounter matched tasks under multiple conditions.

Where feasible:

- randomize or counterbalance condition order;
- use matched task variants;
- separate training/practice tasks from scored tasks;
- freeze the system snapshot used by each condition;
- record model/tool identifiers and configuration;
- repeat enough tasks to expose variance rather than rely on demonstrations.

If cloud AI models cannot be frozen, model drift must be treated as an experimental nuisance variable and logged explicitly.

## Replay design

Historical episodes may be replayed only when the input state can be reconstructed without leaking the known answer into the tested condition.

Replay is useful for mechanism testing, but it is not equivalent to a genuinely prospective task because:

- the researcher may know the historical outcome;
- source selection can encode hindsight;
- reconstructed state may omit hidden context.

Replay results should therefore be labeled separately from prospective novel-task results.

## Randomization and contamination controls

Before confirmatory testing:

- freeze task IDs and variants;
- define randomization/counterbalancing rules;
- define practice exposure;
- prohibit editing scoring rules after seeing condition outcomes;
- record any task where prior familiarity may bias performance;
- distinguish investigator-authored from externally authored tasks;
- record AI assistance used to construct the experiment itself.

## Blinding and scoring

Full operator blinding is generally impossible because architecture conditions are visible. Scoring can still be partially blinded.

Preferred safeguards:

- machine-check primary criteria where possible;
- blinded or masked secondary review of output artifacts;
- independent audit of a sample of failure classifications;
- preserve raw scoring decisions and adjudication disagreements.

## Analysis plan

The frozen protocol should name one primary comparison and one primary outcome family.

Initial analysis should emphasize:

- paired/within-task condition differences;
- effect sizes and uncertainty intervals;
- failure-type distributions;
- sensitivity to exclusion rules;
- per-task and per-condition raw outcomes;
- cost/benefit tradeoffs rather than success-only reporting.

Statistical tests should be chosen only after the final unit structure and sample size are known. Avoid pseudo-replication: repeated tool calls or commits are not independent experimental observations.

## Stopping and amendment rules

The confirmatory protocol should state:

- planned number of scored tasks/blocks;
- conditions under which a broken task is replaced;
- safety/privacy stop conditions;
- what constitutes an implementation failure versus an outcome failure;
- how protocol changes are versioned after data exposure.

Any post-exposure change to hypotheses, primary outcomes, exclusion rules, or scoring thresholds must be labeled as an amendment; newly introduced analyses are exploratory unless otherwise justified.

## Disconfirmation targets

The architecture should not be described as effective if any of the following dominate the result:

- no meaningful task-success improvement;
- failure reduction is offset by equal or greater new failure modes;
- benefits disappear under matched tasks rather than historical demonstrations;
- improvements are explained primarily by greater time/tool/model resources;
- ablations show that supposedly central mechanisms contribute little;
- maintenance and coordination costs outweigh the measured benefit for the target tasks;
- scoring reliability is poor.

## Major confounds

- operator learning and fatigue;
- knowledge of system internals;
- task familiarity;
- model/vendor drift;
- unequal tool access across conditions;
- condition contamination through retained memory/files;
- experimenter-created tasks that favor the architecture;
- temporal improvements unrelated to the tested mechanisms;
- subjective scoring;
- small within-case sample size.

## Manuscript architecture

A future IF-R003 paper should contain:

1. explicit distinction from historical IF-R001/IF-R002 evidence;
2. preregistered/frozen hypotheses and primary outcomes;
3. versioned conditions and task battery;
4. randomization/counterbalancing and contamination controls;
5. primary effectiveness results;
6. failure-type and recovery results;
7. mechanism-ablation results;
8. cost/overhead results;
9. negative/null findings and protocol deviations;
10. limitations and scope of the within-case estimand.

## Publication gate

No effectiveness claim should be promoted until:

- a frozen prospective protocol exists;
- comparison conditions are versioned and reproducible;
- task acceptance criteria and failure taxonomy are frozen;
- primary outcome(s) and analysis plan are named before scored data exposure;
- condition resource budgets are comparable or explicitly modeled;
- scoring reliability is audited;
- deviations/amendments are preserved;
- results distinguish novel prospective tasks from historical replay;
- costs and adverse/failure outcomes are reported alongside benefits.

## Current public position

IF-R003 tests mechanisms motivated by IF-R001 and operationalized by IF-R002. At present it contains a developing experimental method, not evidence that Idea-Foundry improves knowledge-work outcomes.
