# IF-R003 — Historical Replay and Snapshot Design

**Status:** methodological extension; retrospective replay is secondary to prospective controlled measurement  
**Public class:** `NONEMPIRICAL-METHOD`

## Core distinction

The study separates two questions:

1. **Prospective longitudinal effectiveness:** does the live system improve over repeated controlled runs?
2. **Historical-state replay:** given a reconstructed earlier system state, how does a standardized evaluator perform against that state?

Git preserves repository snapshots, but it does not by itself preserve the complete historical AI runtime: model build, system prompt, hidden memory, product configuration, connector permissions, external-service state, retrieval backend state, local files not committed, or platform-side behavior.

Therefore retrospective replay may support claims about **repository-state-conditioned recoverability**, but must not be presented as an exact recreation of historical agent behavior unless runtime state was independently preserved.

## Replay tiers

### R1 — Repository-state replay

Freeze:

- target commit SHA;
- benchmark version;
- evaluator model/access profile;
- prompt and time limits;
- permitted repository interfaces;
- answer/evidence key appropriate to that historical state.

Valid claim form:

> Under a fixed evaluator, this historical repository state supported a measured level of context recovery, provenance reconstruction, or state discrimination.

Invalid claim form:

> This is how the historical AI would have behaved at that date.

### R2 — Information-state replay

Supplement the repository snapshot with contemporaneous source-state evidence where available, such as archived canonical-state files, source revision identifiers, preserved indexes, source manifests, or decision/incident records.

This can reconstruct what information was available more faithfully while still not recreating the historical model/tool runtime.

### R3 — Runtime replay

Requires enough metadata to recreate or closely emulate:

- model/provider/version or immutable model artifact;
- releasable prompt stack;
- tool list and versions;
- connector permissions and accessible source set;
- retrieval/index configuration;
- environment/dependency versions;
- persistent-memory/configuration state;
- external-service snapshots or bounded mocks;
- benchmark and answer key.

Unavailable state is recorded rather than silently approximated.

## Experimental families

### P3-A — Prospective live longitudinal series

Primary evidence: run the frozen battery prospectively at controlled intervals.

### P3-B — Historical repository replay

Prespecify historical commits representing supported developmental states and run the same evaluator and harmonized benchmark logic against each reconstructed state.

Primary interpretation: how much of context-recovery performance is associated with differences in the stored information architecture and governed state available to the evaluator?

### P3-C — Mechanism ablation

Where feasible, begin from one replayable state and remove/disable one mechanism while holding other conditions fixed, such as canonical-state indexing, provenance pointers, generated views, handoff files, contradiction records, or authority labels.

Ablation can provide stronger evidence about mechanism contribution than chronological comparison, provided the intervention does not create an unrealistic broken state.

## Historical applicability coding

Each benchmark item is marked as one of:

- `historically_applicable`
- `not_yet_applicable`
- `answer_is_unknown`
- `incomparable`

Early snapshots are not penalized for facts or mechanisms that did not yet exist.

## Major confounds

Report at least:

- evaluator-model advantage from using a later model on earlier state;
- incomplete off-Git historical evidence;
- changed repository interfaces/file volume;
- differing benchmark applicability;
- retrospective construction of historical answer keys;
- organization/retrieval improvements that make facts easier to locate without changing underlying factual content.

## Interpretation boundary

If performance differs across replayed states under a fixed evaluator, that can support a limited claim that the information architecture changed recoverability/governability. Stronger behavioral or causal claims require stronger replay fidelity or controlled intervention.
