# Series I — Functional Capability and Public-Benchmark Comparison Protocol

**Status:** proposed research-method amendment; exploratory and **not frozen**.  
**Scope:** IF-R001 through IF-R004; retains the existing historical observation-window, public-release, and stable-identity rules.  
**Date:** 2026-10-18.  
**Evidence class:** `NONEMPIRICAL-METHOD` / `PENDING-CORPUS` / `PENDING-EXPERIMENT`.  
**Release boundary:** public methods and published external references only; no private operational history, transcripts, or held-out test items.

## Central change in explanatory priority

Instead of treating the existence, size, or sophistication of Idea-Foundry as an outcome, make **demonstrated functionality at a historical timestamp** the primary descriptive object. Structural development and selection pressures become candidate explanations for capability changes. Evidence from current architecture is never projected backward.

Series-I umbrella question: **Which memory, continuity, knowledge-management, governance, retrieval, and task-execution capabilities were demonstrably present in the concept-aware/research-unaware window; how did they change; how did they perform against simple baselines; and which comparisons with published AI memory/agent systems are actually commensurable?**

The term **"AI second brain" is an evaluable proposition, not a given classification**. An implemented knowledge store or working repository alone is insufficient evidence for reliable retrieval, decision support, contradiction correction, recovery, or measurable human benefit. No paper should infer human-equivalent cognition, agency, intelligence amplification, autonomy, or benchmark superiority from naming, repository size, owner satisfaction, or passing structural CI.

## Historical design invariants

- Primary window: `SB-AWARENESS-01` (unresolved start) through first research awareness (earliest candidate 2026-08-20T15:49:33Z). Preserve source uncertainty and the separate pre-concept and `RA+` evidence classes.
- Distinguish four timestamps: **function first proposed**, **artifact first implemented**, **first independently verified**, and **first observed in a real task**. They need not coincide.
- Each comparison must use an as-of system snapshot and identify what a contemporaneous user/agent could actually operate. A mechanism added in `RA+` cannot prove Series-I ability.
- All claims require stable public-safe evidence pointers, or must remain `PENDING-CORPUS`. Private sources can be examined in the protected workspace; this public methods document contains none.

## Function inventory and testable outcomes

| Function | Minimal observable evidence | Outcome family |
|---|---|---|
| Durable capture/canonicalization | Time-bounded source -> durable record with authority rule | coverage; admissible write accuracy |
| Retrieval/context recovery | Time-appropriate answer with source trace | recall@k, precision@k, answer correctness, citations, latency |
| Cross-session continuity | Task halted and resumed from bounded saved state | resumability, lost requirements, interventions |
| Temporal update/contradiction handling | Earlier fact superseded with auditable authority and date | update accuracy, false promotion, contradiction detection |
| Provenance and calibrated uncertainty | Claim points to recoverable evidence or explicitly abstains | source attribution, unsupported assertion, abstention |
| Planning/task follow-through | Requested artifact satisfies predeclared acceptance criteria | completed tasks, correctness, recovery burden, cost |
| Governed coordination | Distinct actors share state while preserving writers/permissions | handoff success, contamination, unauthorized writes |
| Portability/resilience | System restored/rebuilt independently of one chat/model | rebuild and restart success, dependency/failure cost |
| Privacy/revocation | Scoped access and deletion/revocation checks actually executed | leakage, lingering derived data, unauthorized retrieval |

Treat these as candidate families; freeze the codebook before confirmatory analysis. A capability may be absent, designed only, implemented but untested, fixture-verified, independently validated, or demonstrated in use. Preserve all negative cases.

## Capability-state ledger (required fields)

For each `mechanism × function × timestamp interval` row, capture:

`capability_id, function, historical_period, sb_awareness_relation, research_awareness_state, start/end_bounds, first_proposed_at, implemented_at, fixture_verified_at, real_use_verified_at, source_ids, git_ref, runnable_entrypoint, observed_input, observed_output, acceptance_oracle, test_context, baseline_id, model_version, tool_versions, token/time_budget, human_interventions, success/failure, resource_cost, privacy_class, coding_confidence, disconfirming_evidence`.

**Evidence ladder (not a numerical performance scale):**
- **C0 — Proposed:** design or plan only.
- **C1 — Artifact:** versioned implementation/configuration exists but has not been executed.
- **C2 — Fixture exercised:** documented executable test on representative/synthetic fixture.
- **C3 — Operationally exercised:** reproducible test on actual historical or real-size data under controlled constraints.
- **C4 — Task-demonstrated:** independently scorable user-relevant outcome, with input/output/evidence linkage.
- **C5 — Comparatively validated:** benchmarked against matched simpler and peer conditions, with negative tests, uncertainty, cost, and contamination controls.

Assign the highest **supported** category *per function and timestamp*, not globally to a project. C0–C5 describe an evidence chain, not a claim that every system must implement every function.

## Comparator ladder and external benchmarks

**B0:** contemporaneous no-memory conversation or manual notes; **B1:** original files + literal keyword search; **B2:** full-context/raw-history retrieval where feasible; **B3:** simple RAG or SQLite FTS; **B4:** versioned memory implementations such as MemGPT/Letta or Mem0 under identical task and tool budgets; **B5:** Idea-Foundry as-of snapshot with only historically available components.

Benchmark families, not assumed results:

1. **LoCoMo** (Maharana et al., ACL 2024): very long conversational recall, summarization, temporal/causal questions. Appropriate for conversational memory, not governance or real-world goal attainment. https://aclanthology.org/2024.acl-long.747/
2. **LongMemEval** (Wu et al., ICLR 2025): extraction, multi-session reasoning, temporal reasoning, knowledge updates, abstention. Its 500 questions are a public comparison instrument, not proof that a system performs well. https://proceedings.iclr.cc/paper_files/paper/2025/hash/d813d324dbf0598bbdc9c8e79740ed01-Abstract-Conference.html
3. **LongMemEval-V2** (Wu et al., 2026): memory for experienced web/enterprise agents, including static/dynamic environment state, workflows, gotchas and premise awareness. Score only if the system genuinely supports its data/agent setting. https://arxiv.org/abs/2605.12493
4. **MemGPT** (Packer et al., 2023) and **Mem0** (Chhikara et al., ECAI 2025): architecture and potential peer baselines, not independent universal second-brain standards. Reproduce compatible conditions; avoid copying vendor/author-reported performance as Foundry scores. https://arxiv.org/abs/2310.08560 ; https://arxiv.org/abs/2504.19413
5. **Generative Agents** (Park et al., UIST 2023): observation/reflection/planning ablations; conceptual and design comparators, not a direct productivity benchmark. https://doi.org/10.1145/3586183.3606763
6. **GAIA** (Mialon et al., ICLR 2024): mixed reasoning/tool-use assistant tasks; optional boundary comparator for task execution, not a test of long-term personal memory. https://proceedings.iclr.cc/paper_files/paper/2024/hash/25ae35b5b1738d80f1f03a8713e405ec-Abstract-Conference.html

**Temporal eligibility:** distinguish what literature and software existed during a historical episode from what was published by the later analysis date. Modern benchmarks may evaluate *reconstructed historical snapshots*, but must never be described as having influenced a historical architecture without source evidence. Compare results only when data, scoring, model/tool versions, hardware/budget, access and retrieval corpus are matched. An indirect conceptual comparison is labeled **qualitative only**.

## A falsifiable "AI second brain" classification

Report a **multidimensional profile** rather than a binary marketing verdict:

- **External knowledge base:** durable data with recoverable identifiers and owner-governed writes.
- **Retrieval-augmented workspace:** can retrieve relevant prior context and cite its origin under blind test.
- **Persistent cognitive assistant:** can accurately reconcile updates and resume meaningful work across time.
- **Governed agentic operations:** can execute, checkpoint, recover, and audit multi-step tasks with explicit authority.
- **Validated second-brain function:** shows reproducible improvement over B0–B3 on preregistered, user-relevant task sets without unacceptable cost, privacy, or error regressions.

A system can qualify for a lower tier without reaching the next. Absence of evidence means **unverified**, not automatic evidence of failure; a negative controlled result should be reported as a genuine failure. Use "AI second brain" only as a qualified informal description until an operational definition and success criteria are frozen.

## Mapping the core four studies

- **IF-R001 (What existed?)** Historical first-appearance and birth of each verified functional capability. Specify proposed/implemented/tested/used milestones and disputed start/end chronology. Do not infer effectiveness.
- **IF-R003 (Did it work?)** Replay eligible episodes with B0–B3, mechanism ablations, scorer agreement, and a limited separately marked B4 peer comparison when executable. Include memory and real-work outcomes; avoid back-projecting later software.
- **IF-R004 (Where did it work?)** Compare identical functional constructs across distinct domains; retain heterogeneity, costs, mismatches, and failures. A mechanism shared by folders is not demonstrated cross-domain functionality.
- **IF-R002 (Why/how did it change?)** Write the complete temporal capability-state and pressure/adaptation history; finalize interpretation after IF-R003/004. Record false starts and nonfunctional feature growth, not just successes.

Publication order and existing study identities remain unchanged.

## Immediate implementation and analysis gates

1. Recover and bound `SB-AWARENESS-01`; reconcile off-repository source coverage; preserve uncertainty.
2. Freeze a **function taxonomy** and as-of snapshot extraction process; generate the initial complete ledger, including unavailable outcomes.
3. Audit oldest artifact/test evidence for each candidate function without using present-day implementations as historical proof.
4. Create a small public-safe, consent/rights-cleared task suite and frozen answer keys kept outside the public repository; include negative and temporal-update items.
5. Implement B0/B1/B2/B3 as genuinely runnable controls, then test selected B4 peers only if fair and reproducible.
6. Record paired results, human correction burden, source accuracy, tool/token costs, false-positive authority promotions, and leakage/revocation failures.
7. Maintain separate tables for primary Series I, pre-concept baseline, and later `RA+` prospective testing. Independently audit a sample.

**Current assertion limit:** this document sets a direction and method. It does not report new retrospective findings, benchmark scores, causal effects, proof of human-like cognition, or a completed second brain. Do not change historical results or publication claims on the strength of this amendment alone.
