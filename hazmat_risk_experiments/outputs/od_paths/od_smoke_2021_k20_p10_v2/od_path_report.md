# OD Path Validation Report

- Year: `data_2021`
- OD pairs: `30`
- k candidate paths: `20`
- lambda RE: `1.0`
- risk floor: `0.0001`

| Method | Hop | MaxRisk | CVaR80 | CVaR90 | RE | Gini | Hop inc. | Total risk agg. red. | Total risk mean per-OD red. | CVaR90 agg. red. | CVaR90 mean per-OD red. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CVaR+Concentration | 8.967 | 0.006513 | 0.000592 | 0.000592 | 0.000530 | 0.030303 | 5.315% | 97.084% | 55.353% | 99.603% | 56.470% |
| CVaR-risk | 8.967 | 0.006513 | 0.000592 | 0.000592 | 0.000530 | 0.030303 | 5.315% | 97.084% | 55.353% | 99.603% | 56.470% |
| Hop-shortest | 8.567 | 0.188538 | 0.076331 | 0.148955 | 0.026203 | 0.479297 | 0.000% | 0.000% | 0.000% | 0.000% | 0.000% |
| Mean-risk-floor | 9.000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 5.648% | 100.000% | 56.667% | 100.000% | 56.667% |
| Mean-risk-raw | 9.167 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 7.730% | 100.000% | 56.667% | 100.000% | 56.667% |

Aggregate reduction is computed from method and baseline means. Mean per-OD reduction first computes a paired reduction for each OD and then averages those reductions.
This is an OD path-validation run on the regional association graph, not a real-road navigation experiment.
Continuous edge risk `R_ij` is used for all downstream metrics.
