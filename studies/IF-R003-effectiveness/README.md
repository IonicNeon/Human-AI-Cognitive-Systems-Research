# IF-R003 — Historically Blind Effectiveness, Replay, and Mechanism Ablation

**Status:** prespecification-in-progress  
**Public state:** methods-only  
**Research class:** retrospective within-case replay/ablation study with separate prospective validation  
**Parents:** IF-R001 (`tests`), IF-R002 (`operationalizes`)

## Core question

Do candidate Idea-Foundry mechanisms appear to improve measurable knowledge-work outcomes when tested against task episodes drawn from the period before the owner knew that this development would become the object of the research program?

IF-R003 no longer treats future prospective work as the primary Series-I corpus. Its primary empirical substrate is the **historically blind period** ending at the recovered research-awareness boundary. Eligible pre-awareness tasks, failures, and outcomes are selected under frozen rules, reconstructed to their contemporaneous information state, and tested through replay and mechanism ablation.

Post-awareness prospective matched tasks may provide stronger causal validation, but they are a separate `RA+` evidence class. They cannot retroactively turn the original development period into prospective or research-blind observation.

Historical growth, persistence, complexity, or owner preference do not count as evidence that the architecture improves outcomes.

No effectiveness result should be claimed before the episode-selection rules, reconstruction protocol, scoring rules, exclusions, comparison conditions, and primary outcomes are frozen.

## Primary estimand

Within eligible pre-awareness episodes, what is the bounded within-case effect of historically instantiated governance mechanisms, relative to prespecified replay or ablation conditions, on task success, critical information-state failure, and recovery burden?

This is a **retrospective within-case counterfactual estimand**. The comparison conditions did not literally occur in the historical timeline, and the investigator may know the original outcome. Those limitations are central to interpretation.

A separate secondary estimand may be defined for post-awareness prospective matched tasks. It must be reported as `RA+` validation and must not be pooled silently with the historically blind primary analysis.

## Historical episode eligibility

Primary episodes must:

- occur before the research-awareness cutoff;
- have sufficient contemporaneous source material to reconstruct the task input and relevant system state;
- represent a recurring task/failure class rather than a demonstration selected for success;
- permit at least one meaningful comparison or mechanism-ablation condition without introducing obviously unrelated breakage;
- have a scorable outcome or recovery endpoint;
- preserve negative, failed, ambiguous, and inconvenient cases when they meet the same eligibility rules.

Episode selection must be frozen before replay outcomes are exposed. Source availability is itself a selection mechanism and must be reported.

## Research questions

1. **RQ3.1 — Task success:** Under historical replay, do the mechanisms available in the contemporaneous full condition improve task success relative to prespecified comparison states?
2. **RQ3.2 — Failure prevention:** Do they reduce classified state, provenance, retrieval, contradiction, and handoff failures?
3. **RQ3.3 — Recovery:** When failure occurs, do they reduce recovery burden or correction work?
4. **RQ3.4 — Mechanism contribution:** Which architecture components materially contribute to observed differences under ablation?
5. **RQ3.5 — Cost:** What maintenance, latency, interaction, or complexity costs accompany any benefit?
6. **RQ3.6 — Validation:** When a subset of mechanism-outcome pairs is later tested prospectively, do the `RA+` results agree with the historically blind replay classification?

## Candidate hypotheses

These remain provisional until a frozen protocol is committed.

- **H3.1:** historically appropriate full-condition replay will produce higher task-success scores than the prespecified comparison condition across eligible episodes.
- **H3.2:** full-condition replay will produce fewer critical information-state failures than comparison conditions.
- **H3.3:** full-condition replay will reduce recovery burden after eligible recoverable failures.
- **H3.4:** ablation of retrieval, provenance/validation, continuity/state, or canonical-state admission controls will degrade at least one prespecified outcome in the subset of episodes where that mechanism was contemporaneously available and relevant.

A null result, mixed result, or cost increase must be preserved and reported.

## Experimental/replay conditions

The final protocol should use the smallest condition set that answers the mechanism questions honestly.

### A. Historical full condition

A frozen reconstruction of Idea-Foundry as it existed at the selected pre-awareness episode. Later mechanisms may not be back-projected into earlier states.

### B. Comparison condition

A prespecified simpler state derived from the same episode inputs, such as conversation/file-based work without one or more governance mechanisms. The comparison must be concretely instantiated rather than described rhetorically.

### C. Mechanism ablations

Candidate ablations include:

- retrieval/indexing unavailable or reduced;
- provenance/validation checks unavailable or reduced;
- explicit continuity/handoff state unavailable or reduced;
- canonical-state admission controls unavailable or reduced.

Only ablations that can be implemented without introducing unrelated failures should be used. Each ablation must document what remains constant.

### D. RA+ prospective validation

A later frozen Idea-Foundry configuration may be tested on novel matched tasks whose answers are not already known to the operator. This is a separate validation layer with separate tables and inference language.

## Task families

Primary tasks are recovered from the historically blind corpus under frozen eligibility rules rather than invented after seeing what the architecture does well.

Candidate recurring task classes include:

- retrieve and reconcile prior decisions/evidence;
- resume a partially completed multi-step task after interruption;
- update canonical state from mixed new evidence;
- detect a contradiction or invalid data promotion;
- produce a traceable answer with source/provenance recovery;
- hand off a task between sessions/agents without losing state;
- recover from missing/stale/incorrect state.

Each episode needs:

- stable source IDs and timestamp bounds;
- reconstructed input package and contemporaneous state;
- acceptance criteria or outcome rubric;
- comparison/ablation definition;
- critical-failure definition;
- allowed models/tools or a documented approximation;
- contamination/hindsight notes;
- original historical outcome separated from replay outcomes.

## Primary outcomes

### 1. Task success

Binary, ordinal, or task-specific score based on frozen acceptance criteria. Human judgment should be minimized where machine-checkable criteria are possible.

### 2. Critical information-state failure

Candidate failures include:

- wrong canonical fact promoted;
- required provenance unrecoverable;
- contradiction missed;
- stale state treated as current;
- handoff loses required context;
- invalid source treated as authoritative.

The taxonomy must be frozen before confirmatory replay scoring.

### 3. Recovery burden

Time, actions, corrections, or human interventions needed to detect and repair a recoverable failure.

## Secondary outcomes

- completion time or bounded action count;
- corrective actions;
- provenance-recovery success;
- retrieval precision for task-relevant state;
- unnecessary tool/model calls;
- human interventions required;
- maintenance/setup overhead;
- domain-specific quality metrics.

Do not collapse heterogeneous metrics into a single “productivity” score unless the weighting rule is fixed before outcome exposure.

## Replay protocol

Historical replay is the primary Series-I testing mode, but it is not equivalent to a novel randomized prospective task.

For each episode:

1. freeze episode eligibility before replay outcome review;
2. reconstruct only information available at the episode boundary;
3. version the historical full condition and all comparison/ablation conditions;
4. mask the original historical outcome from the executing agent/model where practical;
5. hold model/tool/resource budgets as constant as practical across replay conditions;
6. score with frozen criteria;
7. keep the original historical outcome, replay results, and later prospective validation in separate fields;
8. record reconstruction omissions, contamination, and any knowledge leakage.

Key threats include investigator knowledge of the historical result, source-selection hindsight, incomplete hidden context, model/tool drift, and imperfect reconstruction of old software states.

## RA+ prospective validation

Prospective validation should be used selectively to test whether the historical mechanism classification survives novel tasks. Before any scored validation:

- freeze task IDs and variants;
- define randomization/counterbalancing rules;
- separate practice exposure;
- freeze scoring and failure definitions;
- version the system snapshot;
- record model/tool identifiers and resource budgets;
- prohibit editing primary scoring rules after outcome exposure.

These results may strengthen or weaken a mechanism claim but do not become evidence that the original development period was prospectively observed.

## Blinding and scoring

Full operator blinding is generally impossible. Preferred safeguards include:

- mask original historical outcomes from the replay executor where practical;
- machine-check primary criteria where possible;
- blinded or masked secondary review of output artifacts;
- independent audit of a sample of failure classifications;
- preserve raw scoring decisions and adjudication disagreements.

## Analysis plan

The frozen protocol should name one primary historical comparison and a small primary outcome family.

Initial analysis should emphasize:

- paired within-episode condition differences;
- effect sizes or bounded uncertainty appropriate to the sample structure;
- failure-type distributions;
- sensitivity to episode-selection and reconstruction rules;
- per-episode and per-condition raw outcomes;
- cost/benefit tradeoffs;
- agreement or disagreement between historical replay classifications and any later `RA+` validation.

Avoid pseudo-replication: repeated tool calls, commits, messages, or generated files are not independent experimental observations.

## Stopping and amendment rules

The protocol should state:

- planned number or minimum coverage of eligible historical episodes;
- what makes an episode unreconstructable;
- when a broken replay condition is replaced versus retained as a failure;
- privacy/safety stop conditions;
- how post-freeze changes are versioned;
- the trigger for moving a mechanism-outcome pair into IF-R004.

Any post-exposure change to hypotheses, primary outcomes, episode eligibility, exclusion rules, or scoring thresholds must be labeled as an amendment; newly introduced analyses are exploratory unless otherwise justified.

## Disconfirmation targets

The architecture should not be described as effective if any of the following dominate the result:

- no meaningful task-success improvement under historical replay;
- failure reduction is offset by equal or greater new failure modes;
- results disappear when negative or inconvenient episodes are included;
- apparent benefit depends on back-projecting mechanisms unavailable at the historical timestamp;
- improvements are explained primarily by greater time/tool/model resources;
- ablations show that supposedly central mechanisms contribute little;
- maintenance and coordination costs outweigh measured benefit;
- scoring or episode reconstruction is unreliable;
- later prospective validation systematically contradicts the replay classification.

## Major confounds

- retrospective episode selection;
- investigator knowledge of historical outcomes;
- incomplete reconstruction of contemporaneous state;
- model/vendor drift;
- unequal tool access across conditions;
- contamination through retained memory/files;
- survivorship in preserved source material;
- subjective scoring;
- small within-case sample size.

## Manuscript architecture

A future IF-R003 paper should contain:

1. historically blind scope and awareness cutoff;
2. episode eligibility and source-reconstruction method;
3. versioned historical full/comparison/ablation conditions;
4. primary replay outcomes;
5. failure-type and recovery results;
6. mechanism-ablation results;
7. cost/overhead results;
8. reconstruction sensitivity and negative/null findings;
9. separately labeled `RA+` prospective validation, if run;
10. limitations and scope of the within-case counterfactual claim.

## Publication gate

No effectiveness claim should be promoted until:

- the awareness boundary and historical episode window are documented;
- episode-selection rules are frozen before replay outcome exposure;
- source reconstruction is auditable;
- comparison/ablation conditions are versioned and historically appropriate;
- task acceptance criteria and failure taxonomy are frozen;
- primary outcomes and analysis plan are named before scored replay;
- resource budgets are comparable or explicitly modeled;
- scoring reliability is audited;
- deviations/amendments are preserved;
- historical replay is not conflated with prospective validation;
- costs and adverse/failure outcomes are reported alongside benefits.

## Current public position

IF-R003 tests mechanisms motivated by IF-R001/IF-R002 using the historically blind task corpus as its primary evidence base. At present it contains a developing replay/ablation method, not evidence that Idea-Foundry improves knowledge-work outcomes. Any later prospective study is a separate validation layer.