# 10seed Consistency Checks

## Answers

- Edge-risk loader consistency: PASS for the sampled 20 edges; exported `R_ij`, OD graph risk, and PyVRP graph risk match.
- Self-evaluation vs common evaluator: self-evaluation is valid for within-model beta/lambda comparisons; cross-model route safety should use the common evaluator.
- beta=0 cost baseline: shared cost baseline = `False`, shared route baseline = `False`. If route hashes differ, compare cross-model cost increases cautiously.
- OD fixed pairs: 150 rows, 150 unique, failures = 0.
- Set A/B fixed instances: Set A hash `28bdcba39d32`, Set B hash `91dec3b14860`; all solver seeds reuse the same depot/customers inside each set.
- Common minus self global-risk mean difference across matched beta=1 rows: `0.114570 +/- 0.514750`.

## Generated Tables

- `edge_risk_consistency_sample_10seed.csv`
- `beta0_baseline_consistency_10seed.csv`
- `beta0_baseline_consistency_summary_10seed.csv`
- `self_vs_common_evaluator_10seed.csv`
- `od_fixed_pair_check_10seed.csv`
- `set_instance_consistency_10seed.csv`

## Paper Wording Notes

- Use common-evaluator results for cross-model PyVRP claims.
- Treat OD results mainly as downstream path-validation evidence, not the sole model ranking criterion.
- Describe concentration-aware cost as a risk-burden concentration penalty plus posterior fairness evaluation, not as a strict fairness-constrained optimizer.
- State that PyVRP optimization uses normalized cost components, while posterior risk metrics use continuous edge risks loaded from the risk matrix.