# IF-R003 — Historically Blind Effectiveness, Replay, and Mechanism Ablation

**Status:** prespecification-in-progress  
**Public state:** methods-only  
**Research class:** retrospective within-case replay/ablation study with separate prospective validation  
**Parents:** IF-R001 (`tests`), IF-R002 (`operationalizes`)

## Core question

Do candidate Idea-Foundry mechanisms appear to improve measurable knowledge-work outcomes when tested against task episodes drawn from the period **after first second-brain concept awareness but before research awareness**?

IF-R003's primary Series-I empirical substrate is the same two-awareness-boundary observation window used by the core series:

- **start — `SB-AWARENESS-01`:** first evidenced awareness of the second-brain concept; timestamp currently unresolved, with the owner's current recollection identifying a Facebook Reel as the first exposure;
- **end — research awareness:** earliest currently recovered candidate 2026-08-20T15:49:33Z, followed twelve seconds later by the first immutable protocol commit.

Eligible tasks, failures, and outcomes inside that concept-aware/research-unaware window are selected under frozen rules, reconstructed to their contemporaneous information state, and tested through replay and mechanism ablation.

Earlier pre-concept episodes may be used as a **separate baseline/comparison class** when source quality and comparability permit. Post-awareness prospective matched tasks may provide stronger causal validation, but they are a separate `RA+` evidence class. Neither baseline nor `RA+` material is silently pooled with the primary observation-window analysis.

Historical growth, persistence, complexity, or owner preference do not count as evidence that the architecture improves outcomes.

No effectiveness result should be claimed before the start/end boundaries, episode-selection rules, reconstruction protocol, scoring rules, exclusions, comparison conditions, and primary outcomes are frozen or defensibly bounded.

## Primary estimand

Within eligible concept-aware/research-unaware episodes, what is the bounded within-case effect of historically instantiated governance mechanisms, relative to prespecified replay or ablation conditions, on task success, critical information-state failure, and recovery burden?

This is a **retrospective within-case counterfactual estimand**. The comparison conditions did not literally occur in the historical timeline, and the investigator may know the original outcome. Those limitations are central to interpretation.

Separate secondary estimands may be defined for:

- pre-concept baseline episodes;
- post-awareness prospective matched tasks (`RA+`).

Those classes must not be pooled silently with the primary analysis.

## Historical episode eligibility

Primary episodes must:

- occur at or after `SB-AWARENESS-01` and before the research-awareness cutoff;
- have sufficient contemporaneous source material to reconstruct the task input and relevant system state;
- represent a recurring task/failure class rather than a demonstration selected for success;
- permit at least one meaningful comparison or mechanism-ablation condition without introducing obviously unrelated breakage;
- have a scorable outcome or recovery endpoint;
- preserve negative, failed, ambiguous, and inconvenient cases when they meet the same eligibility rules.

Until `SB-AWARENESS-01` is source-bound, candidate episodes near the unresolved start must be labeled `PRE-SB?`, `POST-SB?`, or `SB-BOUNDARY-CANDIDATE` rather than forced into the primary corpus.

Episode selection must be frozen before replay outcomes are exposed. Source availability is itself a selection mechanism and must be reported.

## Research questions

1. **RQ3.1 — Task success:** Under historical replay, do the mechanisms available in the contemporaneous full condition improve task success relative to prespecified comparison states?
2. **RQ3.2 — Failure prevention:** Do they reduce classified state, provenance, retrieval, contradiction, and handoff failures?
3. **RQ3.3 — Recovery:** When failure occurs, do they reduce recovery burden or correction work?
4. **RQ3.4 — Mechanism contribution:** Which architecture components materially contribute to observed differences under ablation?
5. **RQ3.5 — Cost:** What maintenance, latency, interaction, or complexity costs accompany any benefit?
6. **RQ3.6 — Pre-concept contrast:** Where comparable earlier episodes exist, do outcomes or mechanism availability differ before second-brain concept exposure?
7. **RQ3.7 — Validation:** When a subset of mechanism-outcome pairs is later tested prospectively, do the `RA+` results agree with the historically blind replay classification?

## Candidate hypotheses

These remain provisional until a frozen protocol is committed.

- **H3.1:** historically appropriate full-condition replay will produce higher task-success scores than the prespecified comparison condition across eligible observation-window episodes.
- **H3.2:** full-condition replay will produce fewer critical information-state failures than comparison conditions.
- **H3.3:** full-condition replay will reduce recovery burden after eligible recoverable failures.
- **H3.4:** ablation of retrieval, provenance/validation, continuity/state, or canonical-state admission controls will degrade at least one prespecified outcome in the subset of episodes where that mechanism was contemporaneously available and relevant.

A null result, mixed result, or cost increase must be preserved and reported.

## Experimental/replay conditions

The final protocol should use the smallest condition set that answers the mechanism questions honestly.

### A. Historical full condition

A frozen reconstruction of Idea-Foundry as it existed at the selected observation-window episode. Later mechanisms may not be back-projected into earlier states.

### B. Comparison condition

A prespecified simpler state derived from the same episode inputs, such as conversation/file-based work without one or more governance mechanisms. The comparison must be concretely instantiated rather than described rhetorically.

### C. Mechanism ablations

Candidate ablations include:

- retrieval/indexing unavailable or reduced;
- provenance/validation checks unavailable or reduced;
- explicit continuity/handoff state unavailable or reduced;
- canonical-state admission controls unavailable or reduced.

Only ablations that can be implemented without introducing unrelated failures should be used. Each ablation must document what remains constant.

### D. Pre-concept baseline

Where a comparable episode predating `SB-AWARENESS-01` exists, it may be used to characterize workflow or outcome state before concept exposure. This is a baseline class, not randomized treatment assignment and not automatically a causal estimate of concept exposure.

### E. RA+ prospective validation

A later frozen Idea-Foundry configuration may be tested on novel matched tasks whose answers are not already known to the operator. This is a separate validation layer with separate tables and inference language.

## Task families

Primary tasks are recovered from the concept-aware/research-unaware observation window under frozen eligibility rules rather than invented after seeing what the architecture does well.

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
- relation to `SB-AWARENESS-01` and research-awareness cutoff;
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

1. verify observation-window eligibility or boundary class before replay outcome review;
2. reconstruct only information available at the episode boundary;
3. version the historical full condition and all comparison/ablation conditions;
4. mask the original historical outcome from the executing agent/model where practical;
5. hold model/tool/resource budgets as constant as practical across replay conditions;
6. score with frozen criteria;
7. keep original historical outcome, replay results, pre-concept baseline results, and later prospective validation in separate fields;
8. record reconstruction omissions, contamination, and any knowledge leakage.

Key threats include investigator knowledge of the historical result, source-selection hindsight, incomplete hidden context, model/tool drift, uncertain `SB-AWARENESS-01` timing, and imperfect reconstruction of old software states.

## Start-boundary evidence

The preferred evidence for `SB-AWARENESS-01` is the original Facebook Reel plus a matching Facebook account-export/activity event that supports exposure/view/interaction timing.

Do not substitute the reel publication date, first later save/share, first ChatGPT use of the phrase `second brain`, or first Git implementation unless evidence independently establishes that event as the first concept awareness.

If the start can only be bounded to an interval, replay eligibility and primary results near the boundary should be sensitivity-tested under the earliest and latest plausible start.

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
- sensitivity to episode-selection, reconstruction, and observation-start rules;
- per-episode and per-condition raw outcomes;
- cost/benefit tradeoffs;
- optional separately labeled pre-concept contrasts;
- agreement or disagreement between historical replay classifications and any later `RA+` validation.

Avoid pseudo-replication: repeated tool calls, commits, messages, or generated files are not independent experimental observations.

## Stopping and amendment rules

The protocol should state:

- planned number or minimum coverage of eligible observation-window episodes;
- what makes an episode unreconstructable;
- how unresolved start-boundary episodes are handled;
- when a broken replay condition is replaced versus retained as a failure;
- privacy/safety stop conditions;
- how post-freeze changes are versioned;
- the trigger for moving a mechanism-outcome pair into IF-R004.

Any post-exposure change to hypotheses, primary outcomes, episode eligibility, exclusion rules, or scoring thresholds must be labeled as an amendment; newly introduced analyses are exploratory unless otherwise justified.

## Disconfirmation targets

The architecture should not be described as effective if any of the following dominate the result:

- `SB-AWARENESS-01` cannot be bounded well enough to identify the intended primary corpus;
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
- uncertain second-brain awareness timing;
- model/vendor drift;
- unequal tool access across conditions;
- contamination through retained memory/files;
- survivorship in preserved source material;
- subjective scoring;
- small within-case sample size.

## Manuscript architecture

A future IF-R003 paper should contain:

1. two-awareness-boundary scope;
2. `SB-AWARENESS-01` evidence and uncertainty;
3. episode eligibility and source-reconstruction method;
4. versioned historical full/comparison/ablation conditions;
5. primary replay outcomes;
6. failure-type and recovery results;
7. mechanism-ablation results;
8. optional pre-concept baseline comparison;
9. cost/overhead results;
10. start/end-boundary and reconstruction sensitivity;
11. separately labeled `RA+` prospective validation, if run;
12. limitations and scope of the within-case counterfactual claim.

## Publication gate

No effectiveness claim should be promoted until:

- `SB-AWARENESS-01` is source-bound or defensibly bounded;
- the research-awareness end boundary is source-bound;
- the historical episode window is documented;
- episode-selection rules are frozen before replay outcome exposure;
- source reconstruction is auditable;
- comparison/ablation conditions are versioned and historically appropriate;
- task acceptance criteria and failure taxonomy are frozen;
- primary outcomes and analysis plan are named before scored replay;
- resource budgets are comparable or explicitly modeled;
- scoring reliability is audited;
- deviations/amendments are preserved;
- historical replay is not conflated with pre-concept baseline or prospective validation;
- costs and adverse/failure outcomes are reported alongside benefits.

## Current public position

IF-R003 tests mechanisms motivated by IF-R001/IF-R002 using the **concept-aware/research-unaware task corpus** as its primary evidence base. Earlier material may support a separately labeled pre-concept baseline; later prospective work is a separate validation layer. At present IF-R003 contains a developing replay/ablation method, not evidence that Idea-Foundry improves knowledge-work outcomes.

## RA+ candidate experiment — collective-memory topology

**Evidence state:** `NONEMPIRICAL-METHOD` / `PENDING-EXPERIMENT`  
**Status:** proposed only; not part of the frozen IF-R003 primary protocol unless admitted by a versioned amendment.

A 2026-08-26 methods intake added a candidate controlled topology experiment for multi-agent memory. The proposed comparison holds model, roles, task suite, tools, source corpus, budgets, rubric, agent count, and retry policy constant while varying only the memory topology:

- **T0 — canonical/raw-search baseline:** no cross-agent durable derived-memory write;
- **T1 — shared disposable blackboard:** shared task state without persistent collective learning;
- **T2 — fully shared derived read/write memory:** exposes upside together with contamination and stale-write risk;
- **T3 — hybrid crystallized governed memory:** private scratch plus validated shared facts/rules/evidence pointers;
- **T4 — scoped-write/shared-read namespaces:** optional variant in which writers retain scoped authority while approved team retrieval spans namespaces.

Candidate evaluation families include retrieval accuracy, cross-source synthesis, superseded-state handling, contradiction handling, abstention, duplicate-work avoidance, handoff/restart recovery, writer attribution, deletion/revocation behavior, permission isolation, poisoning resistance, provenance preservation, and context-budget efficiency.

The raw-history/search condition is mandatory: more structure must beat the simpler evidence-preserving baseline rather than merely appear more sophisticated. No effectiveness result exists yet, and no topology is presumed to win.
