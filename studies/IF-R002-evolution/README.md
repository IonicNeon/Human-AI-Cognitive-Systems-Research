# IF-R002 — Longitudinal Capability Evolution and Selection Pressures

**Status:** corpus-and-adjudication-in-progress  
**Public state:** metadata-and-methods-only  
**Research class:** historically blind longitudinal observational study  
**Parent:** IF-R001 (`extends`)

## Core question

How did the architecture evolve **after the owner first became aware of the second-brain concept but before the owner became aware that this development would become the object of the research program**, and what observable pressures preceded structural adaptation?

IF-R002 extends the historical birth reconstruction in IF-R001. Its primary Series-I observation window is bounded by two awareness events:

- **start — `SB-AWARENESS-01`:** first evidenced second-brain concept awareness; timestamp currently unresolved, with the owner's current recollection identifying a Facebook Reel as the first exposure;
- **end — research awareness:** earliest currently recovered candidate 2026-08-20T15:49:33Z, followed twelve seconds later by the first immutable protocol commit.

The start and end must both be source-bound before final corpus denominators are frozen.

Evidence before `SB-AWARENESS-01` is retained as **pre-concept baseline/context** where relevant. Post-awareness system evolution is coded separately as `RA+` material for validation, reflexivity, later-system history, and future studies rather than silently mixed into the primary Series-I longitudinal dataset.

Its purpose is not to retell the origin story with more events. It asks whether concept-aware/research-unaware structural changes can be described using stable units, pressure classes, and adaptation rules strongly enough to support longitudinal within-case claims about how the system changed under ordinary use rather than research instrumentation.

No candidate pattern is a result until the corpus is frozen for the relevant analysis and adjudication rules have been applied.

## Repository periods and observation-window relationship

Repository-history periods remain useful but are not identical to the observation window:

- **Period A — incubation:** repository creation through first renewed Idea-Foundry Git activity after the January creation sequence; current primary ancestry yields approximately 179.98 days, subject to all-ref verification;
- **Period B — governed-operational birth:** current start candidate 2026-07-27T15:59:48Z through 2026-07-28T23:09:38Z, currently approximately 31.16 hours;
- **blind operational evolution:** governed-operational birth through the research-awareness boundary;
- **RA+:** research-aware period.

`SB-AWARENESS-01` may occur before Period A, inside Period A, at its endpoint, or after it. That ordering is an empirical question.

## Research questions

1. **RQ2.1 — Capability sequence:** Which capability classes appear, persist, merge, split, or disappear inside the concept-aware/research-unaware observation window?
2. **RQ2.2 — Selection pressures:** What observable pressures inside that window precede structural adaptations?
3. **RQ2.3 — Adaptation lag:** How much time and activity separate a supported pressure event from the first implemented response?
4. **RQ2.4 — Persistence:** Which adaptations remain in force long enough to become stable architecture rather than transient fixes?
5. **RQ2.5 — Recurrent mechanisms:** Do similar pressure classes produce similar classes of adaptation across independent observation-window episodes and domains?
6. **RQ2.6 — Pre-concept contrast:** Where source quality permits, how does pre-concept baseline behavior differ from concept-aware development?

## Units of analysis

The study distinguishes five units that must not be silently conflated:

- **artifact change:** a file/code/configuration change at a revision;
- **event:** a meaningfully bounded transition supported by one or more artifacts;
- **pressure episode:** evidence of a problem, constraint, opportunity, failure, correction, or explicit requirement;
- **adaptation:** an implemented structural or procedural response;
- **capability state:** the best-supported state of a named capability during a defined interval.

Commits are evidence carriers, not automatically independent events.

## Core constructs

### Capability class

A stable functional category used to compare changes over time. Candidate classes include authority/decision control, canonical state, provenance, retrieval, validation, observability, coordination, security/privacy, persistence, automation, and recovery/resilience. The final codebook must be frozen before confirmatory counts are produced.

### Selection pressure

Within the primary Series-I corpus, a selection pressure is an observable condition inside the concept-aware/research-unaware observation window that plausibly creates demand for change. Candidate classes include:

- explicit failure or defect;
- contradiction/inconsistency;
- retrieval or continuity failure;
- scaling/coordination burden;
- privacy/security constraint;
- external requirement;
- owner correction or changed preference;
- new opportunity/capability;
- maintenance burden.

Research/audit requirements created after the research-awareness boundary are coded as `RA+`, not as primary blind selection pressures. Pre-concept pressures may be preserved as baseline/context but are not silently pooled with the primary observation-window series.

A pressure label does not itself establish causation.

### Structural adaptation

A change that alters durable system behavior, authority, representation, validation, retrieval, coordination, or maintenance rather than only changing content.

### Adaptation lag

Elapsed time between the earliest supported pressure marker and the first implemented response. Where either boundary is ambiguous, the interval should be represented as bounded/uncertain rather than as a falsely precise point estimate.

### Persistence

The duration or number of subsequent observation windows for which an adaptation remains active without being reverted, superseded, or abandoned. Persistence across the research-awareness boundary may be reported descriptively, but later research-aware behavior cannot retroactively strengthen the historically blind evidence class.

## Source model

Git is one source stream, not the complete case. The longitudinal corpus should reconcile:

- Git commits/diffs and versioned repository artifacts;
- complete private ChatGPT conversation packets;
- Perplexity threads once exported and reproducibly parsed;
- Google Drive files and revision history;
- Facebook activity/account-export evidence for `SB-AWARENESS-01`;
- other contemporaneous records when provenance is sufficient.

The current Period B candidate is short enough to justify near-exhaustive reconstruction. Period A requires special off-repository recovery because sparse Git activity cannot be interpreted as inactivity. The Series-I start cannot be frozen until `SB-AWARENESS-01` is recovered or defensibly bounded.

## Prespecified evidence labels

Each coded relationship should carry one of the repository-wide dependency labels:

- `FIXED`
- `PROVISIONAL`
- `PENDING-CORPUS`
- `PENDING-ADJUDICATION`
- `PENDING-EXPERIMENT`
- `SIMULATED-ONLY`

Longitudinal descriptive findings should not be promoted beyond the weakest unresolved dependency supporting them.

Each event should additionally record:

- `repository_period`: `PRE-REPO` / `PERIOD-A` / `PERIOD-B` / `POST-BIRTH` / `RA+`;
- `sb_awareness_relation`: `PRE-SB` / `SB-BOUNDARY` / `POST-SB` / `UNRESOLVED`;
- `research_awareness_state`: `unaware` / `boundary` / `aware` / `unresolved`.

## Event inclusion rules

A candidate event enters the **primary** adjudication queue when:

- it occurs at or after `SB-AWARENESS-01` and before the research-awareness boundary; and
- at least one contemporaneous artifact supports a change in capability state, an explicit pressure, a corrective action, or a governance/architecture decision.

Pre-concept events may enter a baseline/context ledger under separately frozen rules.

Exclude from the primary event series unless independently meaningful:

- pre-concept events not selected for baseline analysis;
- post-awareness (`RA+`) events;
- generated-only refreshes;
- formatting-only edits;
- mechanical moves without changed authority or behavior;
- repeated automation output;
- duplicate documentation of an already coded event;
- retrospective summaries unsupported by contemporaneous evidence.

Excluded events remain auditable and may be retained in secondary ledgers so that the primary series is not mistaken for the full history.

## Adjudication protocol to freeze before confirmatory analysis

For each candidate event, record:

- repository period;
- relation to `SB-AWARENESS-01`;
- research-awareness state;
- earliest and latest plausible timestamp;
- evidence source(s) and revision/stable-source identifiers;
- pre-state;
- pressure class, if any;
- intervention/adaptation;
- post-state;
- capability class(es);
- implementation maturity;
- causal-language grade;
- confidence;
- contradictory/negative evidence;
- cross-source links where supported;
- whether the event was discovered before or after the coding rules were frozen.

A second coder should independently audit a sample before final manuscript claims are frozen. Disagreements should be preserved with adjudication rationale.

## Planned analyses

### A. Observation-window capability-state timeline

Construct a versioned timeline from `SB-AWARENESS-01` through the research-awareness cutoff showing the first supported appearance, major transformation, and retirement/supersession of capability classes. Report uncertainty where archival coverage is incomplete.

### B. Pressure-to-adaptation analysis

For observation-window episodes with supported pressure markers, summarize:

- pressure class;
- whether an adaptation followed;
- adaptation class;
- lag interval;
- verification maturity;
- persistence.

This analysis is descriptive unless stronger identification is available.

### C. Recurrent mechanism traces

Select repeated observation-window episodes only after the coding frame is frozen. Ask whether the same mechanism appears under different pressures or domains. Negative and failed adaptations are required comparison material, not noise.

### D. Survival/retirement of adaptations

Track whether structural adaptations persist, are revised, are bypassed, or are removed. If the corpus permits, estimate descriptive survival curves or interval summaries. Do not interpret survival as effectiveness without IF-R003 evidence.

### E. Activity-composition control

Separate substantive changes from automation, generated state, maintenance, documentation, and merges before using repository activity as a denominator or growth measure.

### F. Start/end-boundary sensitivity

If either `SB-AWARENESS-01` or the research-awareness cutoff is only bounded rather than point-identified, repeat key counts/classifications under the earliest and latest plausible boundary positions. Report whether substantive conclusions depend on boundary-adjacent events.

### G. Pre-concept baseline comparison

If sufficient source material exists before `SB-AWARENESS-01`, compare selected pre-concept workflow/repository characteristics to the concept-aware observation window without treating this as randomized causal identification.

## Relationship to IF-R003 and IF-R004

IF-R002 is intentionally finalized last. IF-R003 evaluates candidate mechanisms against task traces inside the concept-aware/research-unaware observation window through replay/ablation and may use pre-concept baseline episodes plus separate `RA+` prospective validation. IF-R004 classifies the degree of cross-domain support using application environments inside the same observation window, again with baseline and later validation separated.

IF-R004 may determine which mechanism histories receive primary explanatory emphasis in the final IF-R002 manuscript. It may not determine which historical events are allowed to exist. The complete archival record, including pre-concept, primary-window, failed, local, contradictory, inconvenient, and later `RA+` material, remains preserved independently of IF-R004 results.

## Candidate propositions — exploratory until frozen

These are hypotheses to test against the completed primary observation-window corpus, not findings.

- **P2.1:** major structural adaptations are more often preceded by observable failure/coordination pressures than by unprompted feature accumulation.
- **P2.2:** adaptations that create explicit authority, validation, or provenance mechanisms persist longer than local one-off fixes.
- **P2.3:** repeated pressure classes will produce partially recurrent adaptation patterns, but not deterministic one-to-one mappings.
- **P2.4:** apparent growth rates will materially change after automated/generated activity is separated from substantive transitions.
- **P2.5:** where a usable pre-concept baseline exists, concept-aware development will show a measurable shift in the rate or type of second-brain-relevant architectural changes; this is exploratory and not a causal claim.

Any revision after exposure to the completed coded corpus must be labeled exploratory or amended.

## Falsification and disconfirmation targets

The strongest interpretation would be weakened if:

- `SB-AWARENESS-01` cannot be bounded well enough to define the primary observation window;
- most structural changes cannot be linked even weakly to contemporaneous pressures;
- the apparent pressure/adaptation relationship disappears when documentation backfill is excluded;
- adaptations coded as stable are frequently abandoned or bypassed soon after implementation;
- capability classes cannot be applied reliably by an independent coder;
- archival gaps are large enough that sequence and lag estimates are not trustworthy;
- automation/documentation activity explains the apparent evolutionary pattern better than substantive architecture changes;
- key conclusions depend strongly on a few events whose classification changes under plausible start/end-boundary movement.

## Major confounds

- retrospective coding of the historically blind period;
- hindsight in source selection and interpretation;
- AI-generated documentation that may make causality appear cleaner than it was;
- missing private-source evidence;
- uncertain concept-awareness timing;
- simultaneous interventions that make single-cause attribution impossible;
- cloud-model/tool changes over time;
- branch/default-branch sampling bias;
- survivorship bias toward mechanisms that remain visible in the current architecture;
- uneven source coverage across pre-concept, incubation, birth, and post-birth intervals.

The historically blind end cutoff reduces research-reactivity within the primary corpus; the concept-awareness start boundary aligns the corpus with the actual conceptual exposure of interest. Neither removes the other confounds.

## Manuscript architecture

A future paper derived from IF-R002 should be organized around the governed evidence state rather than chronology alone:

1. problem, two-awareness-boundary scope, and contribution;
2. relationship to IF-R001;
3. source streams, repository periods, observation window, and event-construction method;
4. `SB-AWARENESS-01` evidence and boundary uncertainty;
5. frozen capability/pressure codebook;
6. capability-state evolution;
7. pressure/adaptation timing and recurrence;
8. optional pre-concept baseline comparison;
9. failed, reverted, contradictory, and local cases;
10. start/end-boundary sensitivity and threats to validity;
11. IF-R004-informed mechanism emphasis without hindsight deletion;
12. design propositions and limits.

## Publication gate

Do not claim an evolutionary law, adaptation mechanism, or stable pressure-response relationship until:

- `SB-AWARENESS-01` is source-bound or defensibly bounded;
- the research-awareness end boundary is source-bound and sensitivity checked;
- the primary observation-window corpus bounds are documented;
- Period A's true Git endpoint has been checked across all refs;
- the current Period B candidate has received dense multi-source reconstruction;
- major incubation/off-repository gaps have been actively investigated;
- the adjudication codebook is frozen;
- a manual/independent audit is complete;
- generated/automated activity is separated from substantive events;
- negative/reverted cases are included;
- all quantitative outputs are generated from versioned data;
- claims are limited to within-case longitudinal evidence unless later studies justify broader generalization.

## Current public position

IF-R002 is a methods-and-corpus study in progress. Its primary dataset is the **concept-aware/research-unaware observation window**, with earlier material retained as pre-concept baseline/context and later research-aware material retained separately. Candidate events and propositions remain provisional until corpus completion and frozen adjudication.