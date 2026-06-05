# OD Path Validation Report

- Year: `data_2021`
- OD pairs: `90`
- k candidate paths: `50`
- lambda RE: `1.0`
- CVaR alpha: `0.8`
- RE threshold: `mean` = `0.024996661302295893`
- risk floor: `0.0`

| Method | Hop | MaxRisk | CVaR80 | CVaR90 | RE | Gini | Hop inc. | Total risk agg. red. | Total risk mean per-OD red. | CVaR90 agg. red. | CVaR90 mean per-OD red. | Path overlap w/ CVaR | Changed rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CVaR+Concentration | 9.822 | 0.024636 | 0.014308 | 0.019138 | 0.001909 | 0.145970 | 14.656% | 76.371% | 38.181% | 89.074% | 48.392% | 97.778% | 2.222% |
| CVaR-risk | 9.778 | 0.024636 | 0.014308 | 0.019138 | 0.002115 | 0.145770 | 13.941% | 76.441% | 38.239% | 89.074% | 48.392% | 100.000% | 0.000% |
| Hop-shortest | 8.756 | 0.191754 | 0.114710 | 0.175161 | 0.029068 | 0.431728 | 0.000% | 0.000% | 0.000% | 0.000% | 0.000% | 22.222% | 77.778% |
| Mean-risk-floor | 9.811 | 0.009341 | 0.007512 | 0.009322 | 0.000506 | 0.119163 | 12.351% | 83.284% | 46.484% | 94.678% | 52.838% | 36.667% | 63.333% |
| Mean-risk-raw | 9.811 | 0.009341 | 0.007512 | 0.009322 | 0.000506 | 0.119163 | 12.351% | 83.284% | 46.484% | 94.678% | 52.838% | 36.667% | 63.333% |

Aggregate reduction is computed from method and baseline means. Mean per-OD reduction first computes a paired reduction for each OD and then averages those reductions.
This is an OD path-validation run on the regional association graph, not a real-road navigation experiment.
Continuous edge risk `R_ij` is used for all downstream metrics.
