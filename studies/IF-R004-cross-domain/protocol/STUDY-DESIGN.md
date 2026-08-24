# IF-R004 — Cross-Domain Generalization Study Design

**Version:** 0.1  
**Status:** prospective conditional design  
**Public class:** `NONEMPIRICAL-METHOD`

## Purpose

IF-R004 asks whether core mechanisms are genuinely reusable across distinct application environments rather than merely copied into multiple folders.

The study is conditional. It should be abandoned or reframed as a negative/design-limit result if the prespecified threshold is not met.

## Research questions

- Which core mechanisms are independently instantiated in at least three distinct application environments?
- Which parts remain invariant and which require domain-specific adaptation?
- Does reuse preserve intended governance properties such as provenance, authority, privacy, and correction behavior?
- Where comparable outcome measures exist, is reuse associated with similar functional behavior across domains?

## Mechanism definition

A mechanism is a reusable procedure, data structure, governance rule, retrieval pattern, state-management pattern, validation gate, or source-to-output workflow with a stable definition independent of any one project.

Eligible mechanism classes may include:

- canonical state management;
- provenance/source-chain preservation;
- private-to-public derivation;
- correction and contradiction handling;
- agent handoff/context recovery;
- evidence admission gates;
- project/entity classification;
- generated-view regeneration from canonical state;
- authority/approval boundaries;
- failure/adaptation recording.

A shared filename, template, or terminology alone does not establish a mechanism.

## Application environments

Current domain strata:

- Business
- Engineering
- AI & Software
- Education
- Personal
- Creative
- Cross-domain
- Foundry-core / infrastructure

`Foundry-core / infrastructure` is the mechanism source and does not count toward the three application environments required for generalization.

## Descriptive-generalization threshold

A mechanism qualifies only if all are supported:

1. stable definition before final comparison inspection;
2. evidenced in at least three distinct application environments;
3. each environment has an independent source trail showing actual use;
4. at least two environments show verification beyond proposal/documentation;
5. no environment is counted solely because a generated/derived view mentions the mechanism;
6. material domain-specific deviations are recorded.

This threshold establishes reuse only, not outcome generalization.

## Stronger outcome-generalization threshold

Outcome generalization additionally requires:

1. descriptive threshold met;
2. same or explicitly harmonized functional outcome measured in at least three environments;
3. comparable opportunity denominator or explicit modeling of denominator differences;
4. effect direction not produced only by one environment;
5. system/model/access changes do not make environments incomparable;
6. released evidence remains sufficient to validate the claim.

## Unit of analysis

One row in the mechanism-by-environment matrix:

`mechanism × application_environment`

Required fields include mechanism ID/version, environment, first supported use, source pointers, implementation/verification state, invariant core, adaptation, failure/correction evidence, privacy class, comparable functional metric where applicable, and reviewer disposition.

## Analysis

### Mechanism-environment matrix

Code proposed, implemented, tested, demonstrated, deployed, sustained, degraded, or retired state.

### Invariant-versus-adapted decomposition

For qualifying mechanisms identify invariant core, domain-specific inputs/outputs, authority differences, privacy differences, and verification differences.

### Negative cases

Actively include attempted reuse that failed, was abandoned, or became too domain-specific to count as the same mechanism.

### Outcome comparison

Only attempt outcome comparison when IF-R003 supplies stable functional metrics. Until then, IF-R004 remains primarily structural/process-oriented.

## Anti-selection-bias rule

Freeze the eligible core-mechanism population before evaluating which mechanisms qualify. Do not choose only mechanisms already known to recur. Rejected mechanisms remain in the matrix.

## Stop / abandon rules

Do not publish a positive standalone cross-domain-generalization claim if fewer than two mechanisms meet the descriptive threshold. Preserve zero/one-qualifier analyses as negative or design-limit results rather than forcing a positive paper.

Do not publish an outcome-generalization claim unless the stronger threshold is independently satisfied.

## Threats to validity

- subjective project/domain boundaries;
- correlated design choices under shared ownership;
- later templates making domains appear more similar retrospectively;
- hidden common causes from shared model/agent stacks;
- easy-domain overrepresentation;
- asymmetric privacy restrictions;
- administrative standardization mistaken for functional generality.

## Required outputs before results

- frozen mechanism population;
- mechanism-by-environment matrix;
- evidence matrix;
- negative-case register;
- invariant/adaptation table;
- sensitivity analysis under alternate domain grouping;
- independent adjudication of every claimed qualifying mechanism.
