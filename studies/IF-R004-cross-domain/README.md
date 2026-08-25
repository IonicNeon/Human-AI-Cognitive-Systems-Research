# IF-R004 — Cross-Domain Generalization

**Status:** conditional  
**Public state:** metadata-and-methods-only  
**Research class:** conditional comparative study  
**Parent:** IF-R003 (`extends`)

## Core question

Do core mechanisms generalize across materially different application environments?

IF-R004 asks whether mechanisms that appear useful in one class of work retain value when the work product, evidence structure, error costs, temporal horizon, and success criteria change. It does **not** treat multiple examples from one person or one repository as population-level generalization.

The earliest defensible target is within-case **cross-domain transfer**. Broader human or organizational generalization belongs to later external-validation work.

## Entry condition

IF-R004 should not move into confirmatory analysis until IF-R003 has identified at least one mechanism and outcome pair worth testing under a frozen protocol.

A mechanism should not enter this study merely because it is prominent in the architecture. It should enter because prior evidence provides a specific reason to expect an effect.

## Research questions

1. **RQ4.1 — Transfer:** Does a mechanism associated with improved outcomes in one domain preserve the direction of effect in other materially different domains?
2. **RQ4.2 — Boundary conditions:** Which domain properties weaken, reverse, or eliminate the effect?
3. **RQ4.3 — Adaptation:** Which implementation details must change for the same abstract mechanism to function in different domains?
4. **RQ4.4 — Cost:** Do maintenance and interaction costs vary enough by domain to change whether a mechanism is worthwhile?
5. **RQ4.5 — Failure modes:** Does transfer introduce new domain-specific failure modes even when common metrics improve?

## Domain selection

Domains must be selected before confirmatory outcome review and must differ on prespecified dimensions rather than by folder name alone.

Candidate domain dimensions include:

- **primary output:** physical artifact, software artifact, business/operational state, research/knowledge artifact;
- **evidence type:** measurements, code/tests, transactions/records, literature/provenance;
- **error cost:** reversible nuisance, financial/operational loss, physical rework, research-validity harm;
- **time horizon:** minutes/hours, days, weeks/months;
- **state volatility:** mostly static versus frequently changing;
- **verification style:** machine test, physical inspection, ledger reconciliation, source audit;
- **coordination demand:** single-session versus multi-session/multi-agent;
- **privacy/security burden:** low, moderate, high.

A final comparison should include at least three domains that are materially separated on multiple dimensions.

## Candidate initial domains

These are design candidates, not a frozen sample:

1. **Engineering/build work** — physical design/build tasks with measurements, part state, and test/inspection evidence.
2. **Software/automation work** — executable artifacts with tests, versioning, and reproducible build behavior.
3. **Business/operations work** — inventory, commitments, financial/operational records, and correction costs.
4. **Research/knowledge work** — source-backed synthesis, claim state, provenance, and methodological controls.

A domain may be removed before freeze if it cannot support matched tasks or comparable outcomes.

## Mechanism selection

Candidate cross-domain mechanisms should be defined abstractly enough to survive implementation differences. Examples include:

- canonical-state admission rules;
- provenance linkage;
- explicit validation before promotion;
- persistent task/decision state;
- structured retrieval;
- handoff/continuity records;
- generated-view separation from canonical state;
- correction/audit trails.

The study should compare the **mechanism**, not require identical file structures or software implementations across domains.

## Common outcome family

To support cross-domain comparison, each task should map domain-specific scoring to a small common outcome family.

### Primary common outcomes

- **task success:** acceptance criteria satisfied within the fixed budget;
- **critical state error:** incorrect, stale, contradictory, or unverifiable state reaches an authoritative output;
- **recovery burden:** time/actions needed to detect and correct a recoverable failure.

### Secondary common outcomes

- provenance recovery;
- continuity/handoff success;
- unnecessary rework;
- maintenance overhead;
- number of human interventions;
- domain-specific quality metrics.

Domain-specific outcomes should not be discarded merely to create superficial comparability.

## Comparative design

The preferred initial design is a replicated within-case comparative experiment using matched task families across domains.

For each selected mechanism:

1. define the full mechanism condition and comparison/ablation condition;
2. build matched task variants within each domain;
3. hold model/tool/resource budgets as constant as practical;
4. randomize or counterbalance condition order within domain;
5. score with common and domain-specific criteria;
6. estimate effect direction and magnitude separately by domain before pooling anything.

A pooled summary is secondary. Domain-level results remain primary because heterogeneity is itself the research question.

## Generalization criteria

The manuscript must distinguish three levels of claim.

### Level 1 — demonstrated in one domain

A mechanism shows a supported effect under IF-R003 conditions in one domain.

### Level 2 — within-case cross-domain transfer

The effect direction is preserved in multiple materially different domains under comparable tests, with no unresolved domain-specific failure that makes the mechanism net harmful.

A candidate operational threshold for exploratory planning is preservation across at least three selected domains, but the final threshold must be frozen before confirmatory analysis.

### Level 3 — external generalization

The mechanism retains value across other people, organizations, or independently instantiated systems. IF-R004 cannot establish this alone.

## Heterogeneity and boundary-condition analysis

A failed transfer is not automatically a failed study. It may identify a useful boundary condition.

For every domain, record:

- effect direction;
- effect magnitude/uncertainty;
- implementation changes needed;
- new failure modes;
- overhead/cost;
- domain characteristics that may explain heterogeneity.

Candidate moderators include state volatility, verification cost, task duration, privacy burden, and whether outputs are physical, executable, transactional, or epistemic.

## Disconfirmation targets

Claims of cross-domain transfer should be weakened or rejected if:

- effects are confined to one domain;
- matched tasks show opposite effect directions across domains;
- the mechanism must be changed so extensively that the “same mechanism” label is no longer meaningful;
- benefits depend mainly on one domain's native infrastructure rather than the tested architecture;
- maintenance/interaction costs erase outcome gains in several domains;
- domain-specific harms or critical failures emerge;
- common outcomes cannot be scored reliably across domains.

## Major confounds

- the same operator participates in all domains;
- domain expertise differs substantially;
- task difficulty may not be truly matched;
- different verification methods create measurement asymmetry;
- model/tool ecosystems differ by domain;
- historical familiarity with some projects can create advantage;
- architecture components may have been originally optimized for particular domains;
- carryover learning between conditions and domains;
- small domain count.

## Analysis plan

The final protocol should prioritize:

1. domain-specific paired condition effects;
2. direction-of-effect replication across domains;
3. heterogeneity rather than a single pooled score;
4. cost/failure tradeoffs;
5. sensitivity to task matching and exclusion rules;
6. explicit boundary-condition cases.

Do not claim cross-domain generalization from a collection of anecdotes or repository examples that were not prospectively sampled and scored.

## Manuscript architecture

A future IF-R004 paper should contain:

1. mechanism(s) inherited from IF-R003 and why they were selected;
2. prespecified domain-selection dimensions;
3. matched task construction;
4. common and domain-specific outcomes;
5. domain-level results;
6. heterogeneity/boundary conditions;
7. transfer costs and new failure modes;
8. negative or reversed domains;
9. limits of within-case generalization;
10. handoff to external validation studies.

## Publication gate

Do not make a cross-domain transfer claim until:

- the tested mechanism has prior support under IF-R003;
- domain inclusion criteria are frozen;
- selected domains differ on prespecified dimensions;
- matched task and scoring rules are frozen before outcome review;
- each domain has sufficient repeated observations to expose variance;
- failures and costs are reported alongside benefits;
- domain-level effects are shown before any pooled summary;
- the claim is explicitly labeled within-case unless external participants/systems are studied.

## Current public position

IF-R004 is conditional on IF-R003. Individual examples from engineering, software, business, research, or other domains are motivating cases only. They do not establish prevalence, transfer, or generalization until prospectively selected and scored under a frozen comparative protocol.
