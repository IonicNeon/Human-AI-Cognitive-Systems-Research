# IF-R006 — Comparative Inception and Drift Program

**Status:** prospective program design; no cross-owner result claimed  
**Public class:** `NONEMPIRICAL-METHOD`

## Core question

How does the initial architecture and onboarding pathway of an AI-augmented personal knowledge/operations system influence its later structure, behavior, knowledge organization, recoverability, maintenance burden, and owner-specific adaptation?

This is distinct from within-system cross-domain generalization and requires different units of analysis, consent/privacy rules, and eventually a larger participant sample.

## Research sequence

### Exploratory path-dependence comparison

Compare an organically emergent/co-evolved system with one or more deliberately seeded descendant or sibling systems. The purpose is hypothesis generation, not population inference or causal estimation.

Measure whether inherited mechanisms are retained, removed, mutated, or independently rediscovered while separating seed effects from owner/project/environment differences.

### IF-R007 — Seeded onboarding experiment

Candidate seed conditions, to be frozen before recruitment, may include:

1. **Minimal seed** — tool/repository shell with little prescribed information architecture.
2. **Template-first seed** — conventional capture/project/resource structure.
3. **Governed-lite seed** — canonical state, provenance, authority, correction history, stable IDs, and handoff rules without full mature architecture.
4. **Mature lineage seed** — sanitized owner-neutral structural descendant of a mature governed system.

Equivalent support/time budgets are needed so assistance intensity is not confounded with architecture.

Candidate outcomes:

- time to first stable operating structure;
- owner-driven structural change count;
- inherited-mechanism retention/removal/modification;
- structural churn;
- ontology growth/collapse;
- provenance coverage;
- canonical-state accuracy;
- retrieval/context-recovery performance;
- correction recurrence;
- maintenance burden;
- repository complexity;
- emergence of new governance mechanisms;
- owner-reported fit/usefulness.

### IF-R008 — Longitudinal lineage and drift

Track systems after onboarding and quantify divergence from seed and sibling systems.

Key questions include:

- how quickly sibling systems diverge;
- whether divergence plateaus;
- which mechanisms are stable, repeatedly removed, or independently re-emerge;
- whether knowledge/content divergence outpaces structural/behavioral divergence;
- whether different seeds converge under similar pressures;
- whether similar seeds diverge under owner-specific pressures.

## Two information classes

### Structural / behavioral information

Information that changes how the system behaves, including ontology, authority, governance, instructions, roles, workflows, validation gates, retrieval/context assembly, evidence admission, contradiction/correction behavior, automation, schemas, privacy/publication boundaries, and agent-coordination mechanisms.

### Knowledge / content information

Information the system stores about work, world state, owner-provided context, evidence, decisions, projects, references, and outcomes.

### Mixed artifacts

Many artifacts contain both; coding should be field/section-aware where feasible rather than forcing every file into one class.

## Structural-drift measurements

Candidate measures:

- normalized tree-edit distance;
- feature-vector Jaccard distance;
- schema/ontology edit count;
- governance-rule edit count;
- mechanism retention/mutation/deletion rates;
- newly evolved mechanism count;
- cumulative structural divergence.

## Knowledge-drift measurements

Measure separately:

- source/evidence inventory growth;
- project/domain content turnover;
- semantic-topic distribution change;
- entity growth;
- state-update velocity;
- archive/hot-memory distribution;
- consolidation/retirement;
- provenance-linked versus unlinked knowledge.

More stored knowledge is not automatically better performance.

## Authorship and agency attribution

Where provenance supports it, distinguish:

- human explicitly requested;
- AI proposed, human accepted;
- AI implemented a human requirement;
- AI proposed within delegated scope;
- inherited from seed;
- automated/generated;
- unknown/mixed.

Commit author identity alone does not prove intellectual origin.

## Snapshot cadence

Prospective systems should preserve explicit research snapshots at meaningful intervals such as onboarding, 24 hours, 7 days, 30 days, 90 days, 180 days, and one year where retention permits. Functional comparisons should also preserve runtime/access metadata using IF-R003 replay-bundle methods.

## Human-participant boundary

Once participants are recruited, assigned seed/onboarding conditions, asked to perform study tasks, or identifiable private repository data are analyzed, obtain the appropriate ethics/IRB determination before experimental manipulation or private-data analysis.

Do not use covert repository access, undisclosed semantic/personality analysis, or hidden manipulation as substitutes for clean study design. Consent scope must specify which repository data and semantic content may be used.

## Guardrails

- Two-case comparison does not establish seed causation.
- Commit/file counts are not success measures.
- Do not infer human cognitive change solely from repository change.
- Preserve null, abandoned, and failed systems.
- Predefine exclusion/attrition handling.
- Report differential model/tool access.
- Keep owner outcome/fit measures separate from repository elegance.
