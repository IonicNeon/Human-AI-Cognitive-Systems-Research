# IF-R005 — Project Outcome and Goal-Actualization Coding

**Status:** prospective coding design; no success/generalization result claimed  
**Public class:** `NONEMPIRICAL-METHOD`

## Core distinction

A project's inception window does not have to equal its outcome-observation window. Projects in a frozen inception population may reach success, failure, abandonment, transformation, or goal revision later. Those outcomes are eligible follow-up evidence under a declared cutoff.

This prevents a young project from being coded as merely “unfinished” because of an arbitrary snapshot date.

## Primary questions

For projects in the frozen population:

1. Which project/representation formats were used?
2. Which core mechanisms were applied?
3. How far did each project progress?
4. What verified outcomes occurred?
5. Which projects stalled, failed, were abandoned, or changed goals?
6. Which structural formats were associated with continuity or development?
7. Where did human and AI labor divide, overlap, or hand off?
8. Which patterns plausibly reflect system structure versus project difficulty, resources, expertise, motivation, or model/tool changes?

## Population rule

Freeze projects by **inception date**, not by later success. Include successful, partial, dormant, abandoned, goal-revised, merged/split, and poorly documented projects. Do not select only impressive outcomes.

## Outcome maturity scale

0. `idea_only`
1. `captured`
2. `scoped`
3. `planned`
4. `work_started`
5. `prototype_or_first_artifact`
6. `tested_or_real_world_attempt`
7. `verified_functional_or_completed`
8. `deployed_used_sold_submitted_or_other_domain_success`
9. `sustained_or_repeated_outcome`

The ladder supplements rather than replaces domain-specific verification criteria.

## Goal-state coding

Preserve:

- original stated goal;
- subsequent goal revisions;
- success criteria and when they were introduced;
- current/final outcome;
- evidence supporting outcome;
- unresolved ambiguity.

Do not rewrite the original goal after seeing the outcome.

## Candidate structural features

- explicit authority/owner boundary;
- canonical state record;
- stable identifier;
- manifest/entity record;
- explicit next action;
- decision records;
- open questions;
- evidence/provenance links;
- milestone/checklist structure;
- agent handoff/runbook;
- automation;
- validation/test criteria;
- scheduled follow-up;
- public/private boundary;
- decomposition into subprojects/worksets;
- goal/desired-state clarity;
- explicit abandonment/stop rule.

Code these features from the project state available at the relevant time, not from later backfilled templates.

## Goal-actualization measures

Candidate measures include:

- goal-to-first-action latency;
- action-to-first-artifact latency;
- proportion reaching a verified outcome;
- proportion stalled/abandoned;
- goal-revision count;
- reconstruction interventions after gaps;
- continuity across fresh agents/sessions;
- feedback/correction loops;
- feedback-to-correction latency;
- fraction of outcomes with independent/physical/external verification;
- maintenance burden;
- human intervention burden;
- project resurrection after dormancy;
- fidelity between original desired state and final outcome.

Repository activity is not goal attainment.

## Division of labor

Where provenance supports it, code work episodes as:

- `human_intent_or_goal_setting`
- `human_domain_judgment`
- `human_physical_execution`
- `human_authority_or_approval`
- `AI_research_or_retrieval`
- `AI_synthesis_or_planning`
- `AI_documentation_or_state_management`
- `AI_code_or_artifact_generation`
- `AI_quality_control`
- `joint_iterative_reasoning`
- `automated_system_process`
- `external_person_or_service`
- `mixed_or_unknown`

Git commit author alone is insufficient to establish intellectual authorship or division of labor.

## Efficiency versus effectiveness

Separate:

- **effectiveness:** goal attainment, quality/fidelity, error rates;
- **efficiency:** time, steps, reconstruction burden, human effort.

Faster advancement with a worse verified outcome is not unambiguously improved.

## Follow-up cutoff

Freeze before final analysis:

- `project_inception_window_start`
- `project_inception_window_end`
- `outcome_followup_cutoff`

All projects receive the same follow-up rule or an explicitly modeled censoring rule.

## Suggested schema

```text
project_id
inception_date
domain
original_goal
goal_revision_count
format_features_at_inception
core_mechanisms_used
first_action_date
first_artifact_date
max_maturity
verified_outcome_class
verified_outcome_date
success_criteria_defined_at_inception
success_criteria_met
stalled
abandoned
merged_or_split
feedback_loop_count
human_interventions
AI_work_classes
human_work_classes
external_work_classes
maintenance_burden
continuity_failures
provenance_coverage
limitations
reviewer_disposition
```

## Scientific boundary

Causal interpretation must consider project difficulty, domain familiarity, motivation/interest where defensibly measured, resource availability, physical-world constraints, project age, collaborators, model/tool capability, selective documentation, and survival bias.

The purpose is to make goal actualization measurable without turning successful projects into automatic evidence that the system caused the success.
