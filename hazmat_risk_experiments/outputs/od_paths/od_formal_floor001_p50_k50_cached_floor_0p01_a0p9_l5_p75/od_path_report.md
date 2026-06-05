# OD Path Validation Report

- Year: `data_2021`
- OD pairs: `150`
- k candidate paths: `50`
- lambda RE: `5.0`
- CVaR alpha: `0.9`
- RE threshold: `p75` = `0.0049895052798092365`
- risk floor: `0.0`

| Method | Hop | MaxRisk | CVaR80 | CVaR90 | RE | Gini | Hop inc. | Total risk agg. red. | Total risk mean per-OD red. | CVaR90 agg. red. | CVaR90 mean per-OD red. | Path overlap w/ CVaR | Changed rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CVaR+Concentration | 10.667 | 0.023658 | 0.013491 | 0.021161 | 0.002044 | 0.140904 | 19.404% | 80.240% | 45.261% | 89.397% | 58.331% | 50.667% | 49.333% |
| CVaR-risk | 9.920 | 0.024262 | 0.014544 | 0.020990 | 0.002689 | 0.140537 | 10.191% | 80.317% | 49.058% | 89.483% | 58.379% | 100.000% | 0.000% |
| Hop-shortest | 9.093 | 0.232666 | 0.131668 | 0.199583 | 0.034558 | 0.496441 | 0.000% | 0.000% | 0.000% | 0.000% | 0.000% | 26.000% | 74.000% |
| Mean-risk-floor | 10.020 | 0.013722 | 0.009688 | 0.013699 | 0.001234 | 0.121191 | 10.900% | 84.468% | 53.488% | 93.136% | 61.118% | 48.667% | 51.333% |
| Mean-risk-raw | 10.020 | 0.013722 | 0.009688 | 0.013699 | 0.001234 | 0.121191 | 10.900% | 84.468% | 53.488% | 93.136% | 61.118% | 48.667% | 51.333% |

Aggregate reduction is computed from method and baseline means. Mean per-OD reduction first computes a paired reduction for each OD and then averages those reductions.
This is an OD path-validation run on the regional association graph, not a real-road navigation experiment.
Continuous edge risk `R_ij` is used for all downstream metrics.
