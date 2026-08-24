# IF-R002 — Event Adjudication Rubric

**Status:** method candidate; freeze before final candidate adjudication  
**Public class:** `NONEMPIRICAL-METHOD`

## Unit

A candidate event is a proposed meaningful transition in the system's architecture, capability, governance, information flow, failure response, or operating behavior. A conversation, commit, file, or incident is a source record, not automatically an event.

## Decision sequence

### 1. Identity

Ask whether the candidate is distinct from already coded events, whether its time interval can be bounded, and whether relevant source records resolve to stable provenance identifiers.

If not, use `DEFER-IDENTITY` or `REJECT-DUPLICATE`.

### 2. System relevance

The candidate must concern a core mechanism, or an application-domain event that exercises or changes a core mechanism. A project accomplishment alone is not an evolutionary event.

If not, use `CONTEXT-ONLY` or `REJECT-NONCORE`.

### 3. Observable transition

Supported evidence should show at least one of:

- state-before versus state-after change;
- new or removed capability;
- governance change;
- new reusable workflow;
- failure followed by documented adaptation;
- change in information flow, persistence, retrieval, provenance, coordination, authority, privacy, validation, or publication machinery.

Intent, proposal, wish, or discussion alone is `PROPOSED-ONLY` and must not be promoted to implemented transition.

### 4. Evidence sufficiency

Minimum inclusion requires:

- at least one traceable contemporaneous primary source; and
- enough context to distinguish what happened from what was merely claimed.

Historical AI assertions are not independent verification. Retrospective testimony can support interpretation but cannot alone establish implementation.

### 5. Causal coding

Assign only the strongest supported level:

- `C0` — temporal sequence only
- `C1` — plausible influence
- `C2` — explicit contemporaneous response
- `C3` — measured intervention effect
- `C4` — sustained/repeated measured effect

Never infer `C2+` merely because a later change is sensible in light of an earlier failure.

### 6. Maturity coding

Record evidence maturity separately from causal strength:

1. Proposed
2. Implemented
3. Simulated/mocked
4. Tested
5. Demonstrated
6. Deployed
7. Sustained

### 7. Selection-pressure coding

When applicable, code primary and secondary pressures from a controlled vocabulary such as:

- retrieval failure
- stale/incorrect state
- provenance loss
- duplicate/conflicting records
- coordination collision
- authority ambiguity/violation
- privacy/security concern
- excessive manual maintenance
- integration/synchronization failure
- validation/test failure
- user correction
- scale/complexity pressure
- publication/evidence pressure
- external opportunity/requirement
- unknown/other

## Dispositions

Every adjudication ends in exactly one primary disposition:

- `INCLUDE`
- `INCLUDE-CONTEXTUAL`
- `PROPOSED-ONLY`
- `CONTEXT-ONLY`
- `DEFER-IDENTITY`
- `DEFER-EVIDENCE`
- `DEFER-INDEPENDENT-REVIEW`
- `REJECT-DUPLICATE`
- `REJECT-NONCORE`
- `REJECT-UNSUPPORTED`

Null and rejected candidates remain in the audit trail.

## Independent review

High-salience, privacy-sensitive, causally strong (`C2+`), or chronology-altering candidates should receive independent adjudication before final inclusion. Reviewer disagreement is data: preserve both decisions, reasons, and the resolution method.

## Anti-hindsight rule

Apply the rubric to evidence available for the candidate, not to whether the event fits the eventual narrative. Inclusion is decided before aggregate conclusions about dominant evolutionary patterns are written where feasible.

## Freeze rule

Once formally frozen, changes require a dated protocol amendment. Newly discovered evidence may change candidate dispositions but must not silently change the decision rules.
