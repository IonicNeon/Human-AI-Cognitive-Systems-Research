# IF-R004 — Historically Blind Cross-Domain Generalization and Mechanism Selection

**Status:** conditional  
**Public state:** metadata-and-methods-only  
**Research class:** historically blind within-case comparative study with separate prospective validation  
**Parent:** IF-R003 (`extends`)

## Core question

Which Idea-Foundry mechanisms show supported reuse or outcome consistency across materially different application environments **before the owner knew this development would become the research object**, and what boundary conditions limit those claims?

IF-R004 is the decision gate of the core four-paper sequence. Its primary corpus is the same historically blind development period used by IF-R001–IF-R003. It asks whether mechanisms visible in eligible pre-awareness task traces recur across materially different domains and whether Paper 3 replay/ablation evidence supports a common useful role, a boundary-conditioned role, a local adaptation, or a negative/maladaptive interpretation.

Post-awareness prospective cross-domain testing may provide stronger validation, but it is a separate `RA+` evidence class. It cannot count as blind replication of the original development period.

The earliest defensible primary claim is **within-case historically observed cross-domain transfer/reuse**. Broader human or organizational generalization belongs to later external-validation work.

## Entry condition

A mechanism should not enter the primary comparison merely because it is prominent in the current architecture.

It should enter when:

1. its abstract identity is supported in the pre-awareness corpus;
2. it appears in at least one eligible pre-awareness task/outcome trace;
3. IF-R003 has a supported replay/ablation result, a justified null/negative result, or a documented reason why the mechanism can be evaluated historically without that result;
4. at least two materially different pre-awareness application environments contain comparable evidence, with the final confirmatory historical threshold frozen before outcome classification;
5. later architecture is not back-projected into earlier domain states.

Any later `RA+` prospective transfer study has its own entry conditions and protocol.

## Research questions

1. **RQ4.1 — Historical transfer/reuse:** Does a mechanism associated with improved or failure-reducing outcomes in one pre-awareness domain show the same direction or functional role in other materially different pre-awareness domains?
2. **RQ4.2 — Boundary conditions:** Which domain properties weaken, reverse, or eliminate the supported role?
3. **RQ4.3 — Mechanism identity:** Which implementation details may change while the same abstract mechanism remains identifiable?
4. **RQ4.4 — Cost:** Do maintenance and interaction costs vary enough by domain to change whether a mechanism is worthwhile?
5. **RQ4.5 — Failure modes:** Does reuse introduce domain-specific failure modes even when some common outcomes improve?
6. **RQ4.6 — Validation:** Do later `RA+` matched cross-domain tests agree with or overturn the historically blind classification?

## Domain selection

Primary domains are selected from the pre-awareness corpus under frozen inclusion rules. They must differ on prespecified dimensions rather than by folder name alone.

Candidate dimensions include:

- **primary output:** physical artifact, software artifact, business/operational state, research/knowledge artifact, educational work product, creative artifact;
- **evidence type:** measurements, code/tests, transactions/records, literature/provenance, course requirements, design/inspection evidence;
- **error cost:** reversible nuisance, operational loss, physical rework, research-validity loss, missed academic requirement;
- **time horizon:** minutes/hours, days, weeks/months;
- **state volatility:** mostly static versus frequently changing;
- **verification style:** machine test, physical inspection, ledger reconciliation, source audit, rubric/assignment check;
- **coordination demand:** single-session versus multi-session/multi-agent;
- **privacy/security burden:** low, moderate, high;
- **reversibility:** easy correction versus costly or path-dependent correction.

The primary historical comparison should contain at least three materially separated pre-awareness domains if the source corpus supports honest reconstruction. A domain should be removed if evidence density, task comparability, or mechanism identity is too weak.

## Candidate historical domains

These are source-recovery candidates, not a frozen sample:

1. **Engineering/build work** — physical design/build tasks with measurements, part state, and test/inspection evidence.
2. **Software/automation work** — executable artifacts with tests, versioning, and reproducible behavior.
3. **Business/operations work** — inventory, commitments, operational records, and correction costs.
4. **Research/knowledge work** — source-backed synthesis, claim state, provenance, and methodological controls.
5. **Education** — coursework, deadlines, rubrics, submission state, and learning constraints where pre-awareness traces support them.
6. **Creative work** — design/artifact workflows where the same state, provenance, validation, or continuity mechanisms are genuinely instantiated.

Domain inclusion is evidence-driven. A domain may be absent from the final analysis even if Idea-Foundry contains a folder with that label.

## Mechanism selection

Candidate mechanisms should be defined abstractly enough to survive implementation differences while remaining falsifiable. Examples include:

- canonical-state admission rules;
- provenance linkage;
- explicit validation before promotion;
- persistent task/decision state;
- structured retrieval;
- handoff/continuity records;
- generated-view separation from canonical state;
- correction/audit trails;
- explicit authority boundaries.

The study compares the **mechanism**, not identical file structures or software implementations.

Mechanism identity must be frozen before comparative classification. If implementation changes are so extensive that only the label remains, the transfer claim fails.

## Historical evidence unit

A domain-mechanism observation should include:

- historical stratum and timestamp bounds;
- stable source identifiers;
- contemporaneous mechanism state;
- task/failure class;
- evidence and verification style;
- original historical outcome;
- IF-R003 replay/ablation result when available;
- costs/overhead visible in the source record;
- contradictory or negative evidence;
- reconstruction confidence.

Repeated references to a mechanism do not create independent observations.

## Common outcome family

To support cross-domain comparison, historical task traces should map domain-specific evidence to a small common outcome family without erasing domain-specific quality.

### Primary common outcomes

- **task success:** acceptance criteria or durable goal state satisfied;
- **critical state error:** incorrect, stale, contradictory, or unverifiable state reaches an authoritative output or decision;
- **recovery burden:** actions/time/rework required to detect and correct a recoverable failure.

### Secondary common outcomes

- provenance recovery;
- continuity/handoff success;
- unnecessary rework;
- maintenance overhead;
- human interventions;
- domain-specific quality metrics.

Where the historical record cannot support a common outcome honestly, mark it missing rather than manufacturing comparability.

## Primary comparative design

The primary Series-I analysis is a **historically blind cross-domain comparison**, not a future replicated experiment.

For each selected mechanism:

1. freeze mechanism identity and domain-inclusion rules;
2. identify eligible pre-awareness episodes in each domain;
3. reconstruct contemporaneous mechanism state without using later architecture;
4. link IF-R003 replay/ablation results where available;
5. code common and domain-specific outcomes, costs, and failures;
6. report domain-level evidence before any cross-domain classification;
7. preserve null, negative, reversed, and missing cases;
8. perform sensitivity checks for episode selection and reconstruction confidence.

A later `RA+` confirmatory layer may use matched task families, full-mechanism and ablation conditions, fixed resource budgets, and randomized/counterbalanced order. Those results are reported separately.

## Mechanism classification

The paper produces a classification used to control the explanatory emphasis of IF-R002.

### Class A — provisional transferable core

Supported pre-awareness evidence preserves a useful functional role or effect direction across the frozen minimum number of materially different domains, with mechanism identity intact and no unresolved cost/failure pattern that reverses the interpretation.

Because the primary data are retrospective and nonrandomized, this is a bounded **historical within-case** classification. Later `RA+` validation may strengthen, weaken, or overturn it.

### Class B — boundary-conditioned

The mechanism appears useful only under identifiable domain properties such as state volatility, verification cost, task duration, coordination demand, privacy burden, or reversibility.

### Class C — local adaptation

The mechanism solves a real problem in one environment but the available pre-awareness evidence does not support transfer beyond that setting.

### Class D — negative/maladaptive

The mechanism creates recurring cost, new failure modes, or reversed outcomes that outweigh its intended benefit in the relevant historical environments.

### Class U — unresolved

Source coverage, reconstruction quality, mechanism identity, or outcome comparability is insufficient for a defensible classification. Unresolved is a valid result.

## Relationship to IF-R002

IF-R004 determines **analytical emphasis**, not historical existence.

IF-R002 preserves the complete HB-0 through HB-3 event corpus independently of IF-R004. After IF-R004 classification:

- transferable mechanisms receive primary evolutionary tracing;
- boundary-conditioned mechanisms are traced with the domain properties that shaped them;
- local adaptations remain in the data without being presented as general architecture;
- maladaptive mechanisms are traced as failures of selection or stabilization;
- unresolved mechanisms remain unresolved rather than being forced into a narrative.

IF-R002 must not recycle the same historical traces as independent confirmation of IF-R004.

## Heterogeneity and boundary-condition analysis

A failed transfer is not a failed study. It may identify a useful boundary condition.

For every domain, record:

- supported effect/functional direction;
- reconstruction confidence and uncertainty;
- implementation differences;
- new failure modes;
- overhead/cost;
- domain characteristics that may explain heterogeneity.

Candidate moderators include state volatility, verification cost, task duration, privacy burden, coordination demand, reversibility, and whether outputs are physical, executable, transactional, educational, creative, or epistemic.

## RA+ prospective validation

Later cross-domain experiments may be run when a historically classified mechanism is important enough to justify stronger causal testing.

A validation protocol should:

- freeze mechanism identity and domain-selection dimensions;
- use matched task families;
- freeze common and domain-specific scoring;
- hold tool/model/resource budgets as constant as practical;
- randomize or counterbalance where feasible;
- report domain-level results before pooling;
- explicitly compare prospective classification with the historically blind classification.

Prospective validation is scientifically valuable precisely because it is **not** the same evidence class as the historical corpus.

## Disconfirmation targets

Claims of historically supported cross-domain transfer should be weakened or rejected if:

- evidence is confined to one domain;
- IF-R003 replay shows opposite effects across domains;
- mechanism identity collapses under implementation differences;
- source coverage systematically omits negative domains or episodes;
- apparent transfer is just repeated terminology rather than the same abstract function;
- maintenance/interaction costs erase outcome gains;
- domain-specific failure modes reverse the interpretation;
- common outcomes cannot be reconstructed reliably;
- later `RA+` validation systematically contradicts the historical classification.

## Major confounds

- same owner/operator across domains;
- unequal domain expertise;
- retrospective episode selection;
- historical familiarity and hindsight;
- unequal source survival across domains;
- model/tool drift over time;
- architecture originally optimized for some domains;
- nonindependence of episodes that share the same underlying project or correction;
- small domain count;
- mechanism definitions created after seeing the mature architecture.

The historically blind scope reduces one form of research reactivity in the primary corpus, but does not remove these confounds.

## Analysis plan

The final historical protocol should prioritize:

1. domain-specific episode and replay evidence;
2. direction/functional-role consistency across domains;
3. heterogeneity and boundary conditions;
4. cost/failure tradeoffs;
5. sensitivity to mechanism definition, episode selection, and reconstruction quality;
6. explicit unresolved cases;
7. separate comparison with any later `RA+` validation.

Do not claim cross-domain support from folder counts, anecdotes, or repeated mentions alone.

## Manuscript architecture

A future IF-R004 paper should contain:

1. historically blind scope and awareness boundary;
2. mechanisms inherited from IF-R003 and selection rules;
3. pre-awareness domain-selection dimensions and source coverage;
4. mechanism-identity definitions;
5. domain-level historical/replay evidence;
6. heterogeneity and boundary conditions;
7. transfer costs and new failure modes;
8. negative, reversed, missing, and unresolved domains;
9. mechanism classification and effect on IF-R002 emphasis;
10. separately labeled `RA+` prospective validation, if available;
11. limits of within-case generalization and handoff to external validation.

## Publication gate

Do not make a primary historically supported cross-domain claim until:

- the research-awareness boundary is source-bound;
- mechanism identity is frozen;
- domain inclusion rules are frozen before final classification;
- the selected pre-awareness domains are materially different on prespecified dimensions;
- eligible historical episodes are auditable;
- IF-R003 replay/ablation evidence is incorporated where applicable;
- source coverage and missingness are reported;
- failures and costs are shown alongside benefits;
- domain-level evidence precedes any cross-domain summary;
- the claim is explicitly labeled within-case and historical;
- `RA+` validation, if run, is reported separately rather than pooled.

## Current public position

IF-R004 is the mechanism-selection gate for the core series. Its primary evidence base is the historically blind pre-awareness application record, not newer research-aware projects or future experiments. At present it contains a developing comparative method, not evidence that any mechanism generalizes.