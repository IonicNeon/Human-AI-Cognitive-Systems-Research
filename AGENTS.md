# AGENTS.md — Public Research Repository Operating Rules

This repository is the public, sanitized research distribution for the Human–AI Cognitive Systems research program. It is **not** a mirror of private Idea-Foundry state.

## Before making changes

Read, in order:

1. `GOVERNANCE.md`
2. `PUBLICATION-POLICY.md`
3. `docs/RESEARCH-LIFECYCLE.md`
4. `docs/EVIDENCE-TAXONOMY.md`
5. `docs/PUBLIC-RELEASE-CHECKLIST.md`
6. `research-registry.yml`

## Non-negotiable rules

- Every materially distinct research object has a stable `IF-R###` identity.
- Publication numbering never replaces or renumbers an IF-R identity.
- `studies/IF-R###-slug/` is the permanent home of that research object.
- Manuscripts and papers are outputs/views over governed research state, not the source of truth.
- Do not silently promote provisional, simulated, pending, or exploratory material into confirmed findings.
- Never stage raw private data in this repository, even temporarily.
- Public study data belongs only in `data-public/` after release review.
- Do not expose credentials, private contacts, private chats/email/SMS, hidden answer keys, private second-brain material, or identifiable third-party material without explicit approval and an appropriate release class.
- Preserve negative, null, rejected, abandoned, and contradictory evidence where methodologically relevant.
- Changes after confirmatory data exposure must be versioned and labeled as amendments or exploratory work.
- Research lineage must use the controlled relation vocabulary in `docs/LINEAGE-RELATIONS.md`.

## Contribution behavior

Prefer a branch and pull request for substantive changes. Keep each PR focused enough to review the research consequences. Update registry/lineage when research identity or descent changes.

When adding analysis code:

- keep inputs/outputs explicit;
- record or expose version/hash fields where practical;
- avoid hand-edited generated results;
- distinguish synthetic/example data from empirical data;
- never embed secrets or hidden experimental keys.

When adding a method or protocol, state whether it is proposed, frozen, amended, exploratory, or superseded.

## AI contribution rule

AI agents may research, draft, transform, code, test, and review within delegated scope, but must not infer owner approval for privacy-sensitive public release, human-participant manipulation, authorship decisions, or claims exceeding the evidence state.

When uncertain whether material is safe for public release, keep it out and document the dependency rather than guessing.
