# OD Path Validation Report

- Year: `data_2021`
- OD pairs: `3`
- k candidate paths: `5`
- lambda RE: `0.0`
- CVaR alpha: `0.8`
- RE threshold: `p75` = `0.0`
- risk floor: `0.0001`

| Method | Hop | MaxRisk | CVaR80 | CVaR90 | RE | Gini | Hop inc. | Total risk agg. red. | Total risk mean per-OD red. | CVaR90 agg. red. | CVaR90 mean per-OD red. | Path overlap w/ CVaR | Changed rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CVaR+Concentration | 8.333 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000% | 100.000% | 33.333% | 100.000% | 33.333% | 100.000% | 0.000% |
| CVaR-risk | 8.333 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000% | 100.000% | 33.333% | 100.000% | 33.333% | 100.000% | 0.000% |
| Hop-shortest | 8.333 | 0.142228 | 0.010941 | 0.010941 | 0.010941 | 0.307692 | 0.000% | 0.000% | 0.000% | 0.000% | 0.000% | 66.667% | 33.333% |
| Mean-risk-floor | 8.333 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000% | 100.000% | 33.333% | 100.000% | 33.333% | 66.667% | 33.333% |
| Mean-risk-raw | 8.333 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000% | 100.000% | 33.333% | 100.000% | 33.333% | 66.667% | 33.333% |

Aggregate reduction is computed from method and baseline means. Mean per-OD reduction first computes a paired reduction for each OD and then averages those reductions.
This is an OD path-validation run on the regional association graph, not a real-road navigation experiment.
Continuous edge risk `R_ij` is used for all downstream metrics.
