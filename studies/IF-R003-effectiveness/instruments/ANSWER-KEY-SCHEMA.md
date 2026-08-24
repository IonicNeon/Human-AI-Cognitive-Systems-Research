# IF-R003 — Hidden Answer/Evidence Key Schema

**Purpose:** define ground truth before a controlled run without placing private answer text in public-safe measurement artifacts.

The key is researcher/reviewer-controlled and must not be exposed to the tested process.

## Required fields per item

| Field | Meaning |
|---|---|
| `item_id` | Stable battery item ID |
| `freeze_version` | Exact frozen battery version |
| `key_version` | Key revision; immutable after first valid run except documented correction |
| `answer_class` | `known`, `unknown`, `partially-known`, or `invalid-item` |
| `minimum_required_facts` | Atomic facts required for full credit |
| `partial_credit_rule` | Exact partial-credit conditions |
| `disqualifying_errors` | Errors that force zero credit |
| `authoritative_sources` | Canonical source pointers accepted for evidence credit |
| `acceptable_secondary_sources` | Optional corroborating sources |
| `stale_or_rejected_sources` | Sources that should not receive current-state credit |
| `required_uncertainty` | Unresolved issue the answer must preserve |
| `unknown_detection_expected` | yes/no |
| `authority_discrimination_expected` | yes/no |
| `privacy_boundary` | What may appear in the public scored derivative |
| `reviewer_1` | Key author/reviewer |
| `reviewer_2` | Independent checker where required |
| `freeze_timestamp_utc` | When the item/key became immutable for the run |

## Scoring

### 1.0

All minimum required facts are correct; no disqualifying error is present; required uncertainty is preserved; evidence requirements are satisfied.

### 0.5

The response is not materially wrong but meets the prespecified partial-credit rule. Partial credit is not a generic “close enough” category.

### 0.0

Any material contradiction, unsupported promotion, wrong authoritative state, or disqualifying error specified in the key.

## Exact-evidence field

`evidence_exact=true` only when the response supplies the evidence pointer required by the key. Content accuracy and exact-evidence credit are separate dimensions.

## Unknown items

If `answer_class=unknown`, correctness requires explicit recognition that evidence is insufficient. Inventing closure receives zero content credit and increments unsupported-claim counts.

## Key correction after a run

If a key is discovered to be wrong or ambiguous after a controlled run:

1. preserve the original key and run unchanged;
2. mark the affected item invalid or perform a separately labeled corrected rescoring;
3. create a new key version;
4. state why the key changed and whether prior conclusions change;
5. never silently overwrite the key to match a tested response.

## Privacy

Private keys may contain restricted source pointers. Public derivatives expose only the minimum evidence description needed to audit published scoring and never expose the hidden key before relevant experiments are complete.
