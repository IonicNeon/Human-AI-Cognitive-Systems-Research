# IF-R009 — Intellectual Antecedents and Conceptual Lineage Design

**Status:** method design; no causal intellectual-history result claimed  
**Public class:** `NONEMPIRICAL-METHOD`

## Research opportunity

Repository history alone does not exhaust the origin of a complex human–AI system. Earlier reading, notes, philosophical commitments, abstractions, metaphors, design sketches, and recurring conceptual models may supply intellectual material later operationalized as system mechanisms.

Potential source classes include:

- dated notebooks and book notes;
- reading-history records as evidence of exposure;
- annotations/highlights where rights permit;
- older essays, messages, project notes, and design sketches;
- contemporaneous statements connecting a concept to a later design choice;
- later retrospective testimony, explicitly labeled as such.

Exposure evidence supports an **exposure claim**, not a claim that a particular idea was remembered, adopted, or causally responsible for a later mechanism.

## Three histories

Separate:

1. **Intellectual history** — what concepts, philosophies, authors, metaphors, and abstractions were available over time.
2. **Problem history** — what failures, needs, constraints, and recurring pressures were encountered.
3. **Implementation history** — what structures/mechanisms were implemented and when.

A strong lineage trace connects all three without collapsing them.

## Conceptual-lineage evidence levels

### A0 — exposure only

Evidence shows a work/concept was encountered before the later mechanism.

### A1 — antecedent resemblance

A pre-existing source contains a specific idea resembling a later mechanism. Generic similarity is insufficient.

### A2 — distinctive continuity

Rare terminology, distinctive formulation, repeated conceptual structure, or a source sequence strongly links antecedent and descendant concept. This is still not automatically causal.

### A3 — explicit lineage

Contemporaneous evidence explicitly connects the antecedent concept to a design choice or requirement.

### A4 — traced operationalization

Evidence supports a sequence such as:

`antecedent concept → explicit application to current problem → design decision → implemented mechanism → later use/verification`

This is the strongest conceptual-lineage claim and remains distinct from measured intervention effects under C0–C4 causal coding.

## Anti-hindsight protections

- antecedent evidence must predate the claimed descendant feature;
- generic ideas receive low weight;
- rare/distinctive formulations receive more weight;
- contradictory antecedent ideas remain in the corpus;
- rejected/abandoned lineages remain visible;
- later interpretation cannot rewrite an old source's original text;
- similarity alone cannot be labeled causation;
- coding should precede aggregate narrative construction where practical;
- independent review should sample high-salience lineage claims.

## Candidate conceptual families

Candidate families may include, when supported by source evidence:

- skepticism / epistemic humility;
- provenance and source criticism;
- external/extended cognition;
- human-computer symbiosis;
- evolutionary/selection metaphors;
- inheritance / lineage / selective reproduction;
- identity continuity;
- distributed cognition;
- learning from failure;
- sovereignty / local control;
- canonical versus provisional knowledge;
- recursive self-improvement / bootstrapping;
- goal actualization / intention-to-action bridging.

These are candidate coding families, not findings.

## Dataset schema

One row per antecedent candidate:

```text
antecedent_id
source_type
source_id
author_or_work
source_date_start
source_date_end
concept_label
verbatim_or_precise_summary
exposure_status
first_later_system_appearance
candidate_descendant_mechanism
lineage_level_A0_A4
bridge_source_ids
contradictory_sources
alternative_explanations
privacy_class
reviewer_disposition
limitations
```

## Relationship to other research

- **IF-R001:** distinguishes conceptual ancestry from design gestation and operational birth.
- **IF-R002:** studies which antecedents survive, mutate, disappear, re-emerge, or become operational mechanisms.
- **IF-R006–IF-R008:** can test whether inherited structural rules retain meaning when transferred across system lineages.

## Publication boundary

IF-R009 may become a supporting dataset/method appendix, a standalone lineage study if evidence warrants it, a public-safe conceptual-lineage dataset, or a methods contribution. Publication form is assigned only after the corpus demonstrates a standalone contribution.
