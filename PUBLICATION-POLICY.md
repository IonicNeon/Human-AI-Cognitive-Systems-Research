# Publication and Public-Release Policy

The private research environment is a provenance-rich source. This public repository is a **sanitized derivative and release target**, not a mirror.

## Release classes

- `PUBLIC-APPROVED` — cleared for release as-is.
- `PUBLIC-SANITIZE` — releasable only after transformation/redaction/aggregation.
- `PRIVATE-ONLY` — must not be released here.
- `RIGHTS-REVIEW` — copyright/licensing unresolved.
- `SECURITY-REVIEW` — may expose secrets, infrastructure, location, or attack surface.
- `ETHICS-REVIEW` — may expose or affect human participants/third parties.
- `UNKNOWN` — not evaluated; treated as private.

## Generally suitable after review

Research questions, hypotheses, protocols, rubrics, preregistrations, public-safe event metadata, aggregate counts, sanitized datasets, data dictionaries, analysis code, figures, approved manuscripts/preprints, release manifests, and public provenance.

## Excluded by default

Raw private chats/SMS/email, credentials/tokens, private contacts, unnecessary personal records, private collaborator material without authorization, hidden answer keys/held-out material, rights-unclear copyrighted media, and private second-brain material unnecessary to audit a public claim.

## Data rule

Public study folders use `data-public/`. Raw private data should never be staged in this repository, even temporarily.

## Pre-result release

Methods, hypotheses, definitions, instruments, schemas, synthetic examples, and reproducibility code may be released before results when transparency benefits outweigh experiment-contamination risks.

## Venue compatibility

Before releasing a manuscript intended for a specific venue, check that venue's current preprint/prior-publication policy.
