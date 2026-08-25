# IF-R002 — Longitudinal Capability Evolution and Selection Pressures

**Status:** corpus-and-adjudication-in-progress  
**Public state:** metadata-and-methods-only  
**Research class:** historically blind longitudinal observational study  
**Parent:** IF-R001 (`extends`)

## Core question

How did the architecture evolve during the period before its owner knew that this development would become the object of the research program, and what observable pressures preceded structural adaptation?

IF-R002 extends the historical birth reconstruction in IF-R001. Its primary corpus is the **historically blind development interval**, ending at the first recovered explicit research-awareness turn on 2026-08-20T15:49:33Z. The first immutable protocol commit follows twelve seconds later and provides a corroborating upper bound. The exact semantic timestamp remains subject to re-verification from the source conversation packet.

Post-awareness system evolution is not deleted. It is coded separately as `RA+` material for validation, reflexivity, later-system history, and future studies rather than silently mixed into the primary Series-I longitudinal dataset.

Its purpose is not to retell the origin story with more events. It asks whether pre-awareness structural changes can be described using stable units, pressure classes, and adaptation rules strongly enough to support longitudinal within-case claims about how the system changed under ordinary use rather than research instrumentation.

No candidate pattern is a result until the corpus is frozen for the relevant analysis and adjudication rules have been applied.

## Historical strata

The primary corpus is divided into four source-recovery strata:

- **HB-0 — pre-repository precursor:** earlier evidence admitted only when directly relevant to a later Foundry mechanism or pressure;
- **HB-1 — conceptual incubation:** repository genesis on 2026-01-28 through the structural transition on 2026-07-27, approximately 179.98 days;
- **HB-2 — governed-operational birth:** 2026-07-27T15:59:48Z through 2026-07-28T23:09:38Z, approximately 31.16 hours;
- **HB-3 — blind operational evolution:** operational birth through the 2026-08-20 research-awareness boundary.

`RA+` begins at research awareness and is a separate evidence class.

## Research questions

1. **RQ2.1 — Capability sequence:** Which capability classes appear, persist, merge, split, or disappear during HB-0 through HB-3?
2. **RQ2.2 — Selection pressures:** What observable pre-awareness pressures precede structural adaptations?
3. **RQ2.3 — Adaptation lag:** How much time and activity separate a supported pressure event from the first implemented response?
4. **RQ2.4 — Persistence:** Which adaptations remain in force long enough to become stable architecture rather than transient fixes?
5. **RQ2.5 — Recurrent mechanisms:** Do similar pressure classes produce similar classes of adaptation across independent pre-awareness episodes and domains?

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

Within the primary Series-I corpus, a selection pressure is an observable **pre-awareness** condition that plausibly creates demand for change. Candidate classes include:

- explicit failure or defect;
- contradiction/inconsistency;
- retrieval or continuity failure;
- scaling/coordination burden;
- privacy/security constraint;
- external requirement;
- owner correction or changed preference;
- new opportunity/capability;
- maintenance burden.

Research/audit requirements created after the awareness boundary are coded as `RA+`, not as primary blind selection pressures.

A pressure label does not itself establish causation.

### Structural adaptation

A change that alters durable system behavior, authority, representation, validation, retrieval, coordination, or maintenance rather than only changing content.

### Adaptation lag

Elapsed time between the earliest supported pressure marker and the first implemented response. Where either boundary is ambiguous, the interval should be represented as bounded/uncertain rather than as a falsely precise point estimate.

### Persistence

The duration or number of subsequent observation windows for which an adaptation remains active without being reverted, superseded, or abandoned. Persistence across the research-awareness boundary may be reported descriptively, but later research-aware behavior cannot retroactively strengthen the naturalistic pre-awareness evidence class.

## Source model

Git is one source stream, not the complete case. The longitudinal corpus should reconcile:

- Git commits/diffs and versioned repository artifacts;
- complete private ChatGPT conversation packets;
- Perplexity threads once exported and reproducibly parsed;
- Google Drive files and revision history;
- other contemporaneous records when provenance is sufficient.

The 31.16-hour HB-2 interval is short enough to justify near-exhaustive reconstruction. HB-1 requires special off-repository recovery because sparse Git activity cannot be interpreted as inactivity.

## Prespecified evidence labels

Each coded relationship should carry one of the repository-wide dependency labels:

- `FIXED`
- `PROVISIONAL`
- `PENDING-CORPUS`
- `PENDING-ADJUDICATION`
- `PENDING-EXPERIMENT`
- `SIMULATED-ONLY`

Longitudinal descriptive findings should not be promoted beyond the weakest unresolved dependency supporting them.

Each event should additionally record `historical_stratum` (`HB-0`/`HB-1`/`HB-2`/`HB-3`/`RA+`) and `owner_awareness_state` (`unaware`/`boundary`/`aware`/`unresolved`).

## Event inclusion rules

A candidate event enters the primary adjudication queue when at least one contemporaneous **pre-awareness** artifact supports a change in capability state, an explicit pressure, a corrective action, or a governance/architecture decision.

Exclude from the primary event series unless independently meaningful:

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

- historical stratum and owner-awareness state;
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

### A. Capability-state timeline

Construct a versioned HB-0 through HB-3 timeline showing the first supported appearance, major transformation, and retirement/supersession of capability classes. Report uncertainty where archival coverage is incomplete.

### B. Pressure-to-adaptation analysis

For pre-awareness episodes with supported pressure markers, summarize:

- pressure class;
- whether an adaptation followed;
- adaptation class;
- lag interval;
- verification maturity;
- persistence.

This analysis is descriptive unless stronger identification is available.

### C. Recurrent mechanism traces

Select repeated pre-awareness episodes only after the coding frame is frozen. Ask whether the same mechanism appears under different pressures or domains. Negative and failed adaptations are required comparison material, not noise.

### D. Survival/retirement of adaptations

Track whether structural adaptations persist, are revised, are bypassed, or are removed. If the corpus permits, estimate descriptive survival curves or interval summaries. Do not interpret survival as effectiveness without IF-R003 evidence.

### E. Activity-composition control

Separate substantive changes from automation, generated state, maintenance, documentation, and merges before using repository activity as a denominator or growth measure.

### F. Awareness-boundary sensitivity

Repeat key counts or classifications under plausible nearby awareness-boundary timestamps if source recovery changes the exact semantic cutoff. Report whether substantive conclusions depend on a few boundary-adjacent events.

## Relationship to IF-R003 and IF-R004

IF-R002 is intentionally finalized last. IF-R003 evaluates candidate mechanisms against historically blind task traces through replay/ablation and may use separate `RA+` prospective validation. IF-R004 classifies the degree of cross-domain support using the historically blind application environments, again with later validation separated.

IF-R004 may determine which mechanism histories receive primary explanatory emphasis in the final IF-R002 manuscript. It may not determine which historical events are allowed to exist. The complete HB-0 through HB-3 ledger, including failed, local, contradictory, and inconvenient cases, remains preserved independently of IF-R004 results.

## Candidate propositions — exploratory until frozen

These are hypotheses to test against the completed historically blind corpus, not findings.

- **P2.1:** major structural adaptations are more often preceded by observable failure/coordination pressures than by unprompted feature accumulation.
- **P2.2:** adaptations that create explicit authority, validation, or provenance mechanisms persist longer than local one-off fixes.
- **P2.3:** repeated pressure classes will produce partially recurrent adaptation patterns, but not deterministic one-to-one mappings.
- **P2.4:** apparent growth rates will materially change after automated/generated activity is separated from substantive transitions.

These propositions may be revised before confirmatory adjudication. Any revision after exposure to the completed coded corpus must be labeled exploratory or amended.

## Falsification and disconfirmation targets

The strongest interpretation would be weakened if:

- most structural changes cannot be linked even weakly to contemporaneous pressures;
- the apparent pressure/adaptation relationship disappears when documentation backfill is excluded;
- adaptations coded as stable are frequently abandoned or bypassed soon after implementation;
- capability classes cannot be applied reliably by an independent coder;
- archival gaps are large enough that sequence and lag estimates are not trustworthy;
- automation/documentation activity explains the apparent evolutionary pattern better than substantive architecture changes;
- key conclusions depend strongly on a few events whose classification changes under plausible awareness-boundary movement.

## Major confounds

- retrospective coding of the historically blind period;
- hindsight in source selection and interpretation;
- AI-generated documentation that may make causality appear cleaner than it was;
- missing private-source evidence;
- simultaneous interventions that make single-cause attribution impossible;
- cloud-model/tool changes over time;
- branch/default-branch sampling bias;
- survivorship bias toward mechanisms that remain visible in the current architecture;
- uneven source coverage across HB-0/HB-1/HB-2/HB-3.

The historically blind cutoff reduces research-reactivity within the primary development corpus, but does not remove these other threats.

## Manuscript architecture

A future paper derived from IF-R002 should be organized around the governed evidence state rather than chronology alone:

1. problem, historically blind scope, and contribution;
2. relationship to IF-R001;
3. corpus, source streams, interval strata, and event-construction method;
4. frozen capability/pressure codebook;
5. capability-state evolution;
6. pressure/adaptation timing and recurrence;
7. failed, reverted, contradictory, and local cases;
8. awareness-boundary sensitivity and threats to validity;
9. IF-R004-informed mechanism emphasis without hindsight deletion;
10. design propositions and limits.

## Publication gate

Do not claim an evolutionary law, adaptation mechanism, or stable pressure-response relationship until:

- the awareness boundary is source-bound and sensitivity checked;
- HB-0 through HB-3 corpus bounds are documented;
- the 31.16-hour birth interval has received dense multi-source reconstruction;
- major HB-1 off-repository gaps have been actively investigated;
- the adjudication codebook is frozen;
- a manual/independent audit is complete;
- generated/automated activity is separated from substantive events;
- negative/reverted cases are included;
- all quantitative outputs are generated from versioned data;
- claims are limited to within-case longitudinal evidence unless later studies justify broader generalization.

## Current public position

IF-R002 is a methods-and-corpus study in progress. Its primary dataset is the pre-awareness development history, not the later research-instrumented system. Candidate events and propositions remain provisional until corpus completion and frozen adjudication.