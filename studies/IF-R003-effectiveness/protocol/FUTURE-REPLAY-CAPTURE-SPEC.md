# IF-R003 — Future Replay Capture Specification

**Status:** prospective capture specification  
**Public class:** `NONEMPIRICAL-METHOD`

## Objective

Future research checkpoints should preserve enough state to support substantially higher-fidelity replay than Git history alone. The goal is not perfect platform emulation when providers do not expose immutable internals; the goal is to make missing runtime state explicit and preserve everything under researcher control that can reasonably be frozen.

## Replay Bundle levels

### RB-1 — repository reproducibility

Required:

- `snapshot_id`
- UTC capture timestamp
- repository commit SHA
- branch/tag
- canonical-state manifest hash
- generated-view manifest hash
- public/private classification

### RB-2 — information-state reproducibility

RB-1 plus:

- source inventory and hashes/pointers;
- source revision IDs when available;
- relevant export/manifest versions;
- retrieval corpus cutoff;
- index/database schema version;
- index checksum or deterministic rebuild manifest;
- known uncommitted/external evidence omissions.

### RB-3 — evaluator/runtime reproducibility

RB-2 plus:

- provider/product/model label;
- exact model/version/build identifier where exposed;
- releasable prompt-stack versions;
- benchmark prompt version;
- tool list and tool-policy version;
- connector list and access scope;
- relevant source-access profile;
- persistent-memory configuration/version;
- retrieval/reranking settings;
- context/token limits if exposed;
- environment/dependency lockfile or container digest for local components;
- analysis code SHA;
- benchmark and hidden-key versions;
- run timeout/retry rules;
- timezone/locale where relevant;
- known provider-side state that cannot be frozen.

### RB-4 — execution trace

RB-3 plus:

- evaluator transcript/output;
- tool-call trace where available;
- retrieved source IDs;
- latency/timing data;
- usage data where available;
- human interventions;
- errors/retries;
- invalidation/contamination notes;
- final scored run artifact.

## Suggested manifest

```yaml
snapshot_id: IF-P3-RB-YYYYMMDD-NN
captured_at_utc: ...
git_commit_sha: ...
repo_tree_hash: ...
canonical_state_manifest_sha: ...
generated_view_manifest_sha: ...
source_inventory_version: ...
retrieval_corpus_cutoff: ...
retrieval_index_manifest_sha: ...
model_provider: ...
model_product_label: ...
model_version_exposed: ...
prompt_stack_versions: []
tool_access_profile: ...
connector_access_profile: ...
persistent_memory_profile: ...
benchmark_version: ...
answer_key_version: ...
analysis_code_sha: ...
environment_digest: ...
known_unfrozen_platform_state: []
privacy_class: ...
validity_notes: ...
```

## Snapshot triggers

Create Replay Bundles at least for:

- controlled IF-R003 batteries;
- major architecture changes;
- major retrieval/index changes;
- model family/product changes;
- connector/access-profile changes;
- major governance/canonical-state changes;
- immediately before/after planned ablation;
- publication evidence freeze.

Routine Git commits remain useful historical snapshots but do not all require RB-3/RB-4 capture.

## Preservation policy

- preserve manifests immutably after a run;
- corrections create new versions rather than overwrite old bundles;
- private connector/source details may stay restricted while released derivatives expose safe hashes/categories;
- hidden answer keys never enter a public pre-run bundle;
- provider secrets/tokens are never captured;
- external state that cannot be archived is represented by timestamped identifiers and explicit missing-state fields.

## Scientific value

Replay Bundles help distinguish changes caused by stored structure/content, retrieval/index configuration, model/runtime changes, access/tool changes, benchmark changes, and unexplained residual platform variation.
