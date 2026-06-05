# OD Path Validation Report

- Year: `data_2021`
- OD pairs: `3`
- k candidate paths: `5`
- lambda RE: `1.0`
- CVaR alpha: `0.8`
- RE threshold: `p75` = `0.024947531521320343`
- risk floor: `0.0`

| Method | Hop | MaxRisk | CVaR80 | CVaR90 | RE | Gini | Hop inc. | Total risk agg. red. | Total risk mean per-OD red. | CVaR90 agg. red. | CVaR90 mean per-OD red. | Path overlap w/ CVaR | Changed rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CVaR+Concentration | 8.667 | 0.041431 | 0.038826 | 0.041431 | 0.004585 | 0.189937 | 5.556% | 35.798% | 15.856% | 61.967% | 27.514% | 66.667% | 33.333% |
| CVaR-risk | 8.333 | 0.041431 | 0.038826 | 0.041431 | 0.004840 | 0.168687 | 0.000% | 36.796% | 17.870% | 61.967% | 27.514% | 100.000% | 0.000% |
| Hop-shortest | 8.333 | 0.176493 | 0.084661 | 0.108935 | 0.015110 | 0.310481 | 0.000% | 0.000% | 0.000% | 0.000% | 0.000% | 66.667% | 33.333% |
| Mean-risk-floor | 8.333 | 0.041431 | 0.039659 | 0.041431 | 0.004725 | 0.168051 | 0.000% | 37.659% | 18.289% | 61.967% | 27.514% | 66.667% | 33.333% |
| Mean-risk-raw | 8.333 | 0.041431 | 0.039659 | 0.041431 | 0.004725 | 0.168051 | 0.000% | 37.659% | 18.289% | 61.967% | 27.514% | 66.667% | 33.333% |

Aggregate reduction is computed from method and baseline means. Mean per-OD reduction first computes a paired reduction for each OD and then averages those reductions.
This is an OD path-validation run on the regional association graph, not a real-road navigation experiment.
Continuous edge risk `R_ij` is used for all downstream metrics.
