# Human–AI Cognitive Systems Research

Open research on evolving human–AI cognitive, knowledge, and operational systems: methods, studies, reproducibility artifacts, research lineage, and publications.

## Purpose

This repository is the public research surface for a broader private, provenance-rich research environment. It is intentionally **not** a mirror of that private environment. Only deliberately reviewed public derivatives belong here.

The research program studies how human–AI knowledge and operational systems emerge, evolve, retain provenance, recover context, coordinate work, generalize across domains, actualize goals, and develop descendants over time.

## Permanent research identity

Every materially distinct research object receives a stable `IF-R###` identifier.

Canonical public home:

```text
studies/IF-R###-slug/
```

Publication is an output of research; publication numbering does not define research identity. An IF-R object may produce one paper, several papers, a dataset, a method, a null result, an abandoned branch, or new research without changing identity.

Each study also carries a local `study.yml` so the research object remains machine-readable independently of the top-level registry.

## Research spawning research

Research lineage is first-class data. Typed parent/child and related relationships are recorded in `research-registry.yml` and rendered under `lineage/`.

## Public-release boundary

This repository may contain public protocols, preregistrations, sanitized/derived datasets, data dictionaries, analysis code, figures, approved manuscripts/preprints, release manifests, and public provenance metadata.

It must not contain raw private corpora, private communications, credentials, unnecessary personal records, hidden experimental keys, or material with unresolved rights, privacy, security, or ethics status.

Public study data belongs only under `data-public/`.

## Lifecycle

```text
spawn → triage → prespecify → collect → adjudicate → analyze → write
      → adversarial review → public-safe derivation → release → spawn
```

The manuscript is a view over governed research state, not the source of truth.

## Public methods now available

The repository includes more than metadata scaffolding. Current public method artifacts include:

- governed research-production / “Paper Factory” workflow under `methods/common-protocols/`;
- IF-R002 longitudinal event-adjudication and anti-hindsight rules;
- IF-R003 experiment-freeze, historical replay, future Replay Bundle, hidden-key schema, run/battery templates, scoring code, and longitudinal run-comparison code;
- IF-R004 prospective cross-domain generalization threshold, public matrix schema, and deterministic threshold evaluator;
- IF-R005 project-outcome and goal-actualization coding design;
- IF-R006 comparative inception/path-dependence and lineage-drift program design;
- IF-R009 conceptual-lineage evidence coding and anti-hindsight method.

These are methods and research infrastructure, not positive empirical results.

## AI and automation

`AGENTS.md` defines the operating rules for AI/code agents working in this public research repository. It inherits the same public/private firewall, stable research identity, evidence-state, amendment, and lineage requirements used by human contributors.

## Current state

The public registry defines `IF-R001` through `IF-R011`. Their presence here does not imply completed data collection, validated results, peer review, or publication.
