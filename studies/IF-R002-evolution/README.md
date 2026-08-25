# IF-R002 — Longitudinal Capability Evolution and Selection Pressures

**Status:** corpus-and-adjudication-in-progress  
**Public state:** metadata-and-methods-only  
**Research class:** longitudinal observational study  
**Parent:** IF-R001 (`extends`)

## Core question

How does the architecture evolve, and what pressures precede structural adaptation?

IF-R002 extends the historical birth reconstruction in IF-R001. Its purpose is not to retell the origin story with more events. It asks whether subsequent structural changes can be described using stable units, pressure classes, and adaptation rules strongly enough to support longitudinal claims about how the system changes.

No candidate pattern is a result until the corpus is frozen for the relevant analysis and adjudication rules have been applied.

## Research questions

1. **RQ2.1 — Capability sequence:** Which capability classes appear, persist, merge, split, or disappear over time?
2. **RQ2.2 — Selection pressures:** What observable pressures precede structural adaptations?
3. **RQ2.3 — Adaptation lag:** How much time and activity separate a supported pressure event from the first implemented response?
4. **RQ2.4 — Persistence:** Which adaptations remain in force long enough to become stable architecture rather than transient fixes?
5. **RQ2.5 — Recurrent mechanisms:** Do similar pressure classes produce similar classes of adaptation across independent episodes?

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

An observable condition that plausibly creates demand for change. Candidate classes include:

- explicit failure or defect;
- contradiction/inconsistency;
- retrieval or continuity failure;
- scaling/coordination burden;
- privacy/security constraint;
- external requirement;
- owner correction or changed preference;
- new opportunity/capability;
- maintenance burden;
- research/audit requirement.

A pressure label does not itself establish causation.

### Structural adaptation

A change that alters durable system behavior, authority, representation, validation, retrieval, coordination, or maintenance rather than only changing content.

### Adaptation lag

Elapsed time between the earliest supported pressure marker and the first implemented response. Where either boundary is ambiguous, the interval should be represented as bounded/uncertain rather than as a falsely precise point estimate.

### Persistence

The duration or number of subsequent observation windows for which an adaptation remains active without being reverted, superseded, or abandoned.

## Prespecified evidence labels

Each coded relationship should carry one of the repository-wide dependency labels:

- `FIXED`
- `PROVISIONAL`
- `PENDING-CORPUS`
- `PENDING-ADJUDICATION`
- `PENDING-EXPERIMENT`
- `SIMULATED-ONLY`

Longitudinal descriptive findings should not be promoted beyond the weakest unresolved dependency supporting them.

## Event inclusion rules

A candidate event enters the adjudication queue when at least one contemporaneous artifact supports a change in capability state, an explicit pressure, a corrective action, or a governance/architecture decision.

Exclude from the primary event series unless independently meaningful:

- generated-only refreshes;
- formatting-only edits;
- mechanical moves without changed authority or behavior;
- repeated automation output;
- duplicate documentation of an already coded event;
- retrospective summaries unsupported by contemporaneous evidence.

Excluded events remain auditable and may be retained in a secondary ledger so that the primary series is not mistaken for the full history.

## Adjudication protocol to freeze before confirmatory analysis

For each candidate event, record:

- earliest and latest plausible timestamp;
- evidence source(s) and revision identifiers;
- pre-state;
- pressure class, if any;
- intervention/adaptation;
- post-state;
- capability class(es);
- implementation maturity;
- causal-language grade;
- confidence;
- contradictory/negative evidence;
- whether the event was discovered before or after the coding rules were frozen.

A second coder should independently audit a sample before final manuscript claims are frozen. Disagreements should be preserved with adjudication rationale.

## Planned analyses

### A. Capability-state timeline

Construct a versioned timeline showing the first supported appearance, major transformation, and retirement/supersession of capability classes. Report uncertainty where archival coverage is incomplete.

### B. Pressure-to-adaptation analysis

For episodes with supported pressure markers, summarize:

- pressure class;
- whether an adaptation followed;
- adaptation class;
- lag interval;
- verification maturity;
- persistence.

This analysis is descriptive unless stronger identification is available.

### C. Recurrent mechanism traces

Select repeated episodes only after the coding frame is frozen. Ask whether the same mechanism appears under different pressures or domains. Negative and failed adaptations are required comparison material, not noise.

### D. Survival/retirement of adaptations

Track whether structural adaptations persist, are revised, are bypassed, or are removed. If the corpus permits, estimate descriptive survival curves or interval summaries. Do not interpret survival as effectiveness without IF-R003 evidence.

### E. Activity-composition control

Separate substantive changes from automation, generated state, maintenance, documentation, and merges before using repository activity as a denominator or growth measure.

## Candidate propositions — exploratory until frozen

These are hypotheses to test against the completed corpus, not findings.

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
- automation/documentation activity explains the apparent evolutionary pattern better than substantive architecture changes.

## Major confounds

- retrospective coding of pre-protocol history;
- owner/researcher reactivity after formal observation begins;
- AI-generated documentation that may make causality appear cleaner than it was;
- missing private-source evidence;
- simultaneous interventions that make single-cause attribution impossible;
- cloud-model/tool changes over time;
- branch/default-branch sampling bias;
- survivorship bias toward mechanisms that remain visible in the current architecture.

## Manuscript architecture

A future paper derived from IF-R002 should be organized around the governed evidence state rather than chronology alone:

1. problem and contribution;
2. relationship to IF-R001;
3. corpus and event-construction method;
4. frozen capability/pressure codebook;
5. capability-state evolution;
6. pressure/adaptation timing and recurrence;
7. failed, reverted, and contradictory cases;
8. threats to validity;
9. design propositions and handoff to IF-R003.

## Publication gate

Do not claim an evolutionary law, adaptation mechanism, or stable pressure-response relationship until:

- corpus bounds are documented;
- the adjudication codebook is frozen;
- a manual/independent audit is complete;
- generated/automated activity is separated from substantive events;
- negative/reverted cases are included;
- all quantitative outputs are generated from versioned data;
- claims are limited to within-case longitudinal evidence unless later studies justify broader generalization.

## Current public position

IF-R002 is a methods-and-corpus study in progress. It extends IF-R001 but does not inherit IF-R001 conclusions as proof of later evolutionary mechanisms. Candidate events and propositions remain provisional until corpus completion and frozen adjudication.
