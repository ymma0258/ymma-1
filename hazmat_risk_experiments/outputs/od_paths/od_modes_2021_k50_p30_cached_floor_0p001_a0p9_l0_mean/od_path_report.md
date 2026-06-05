# OD Path Validation Report

- Year: `data_2021`
- OD pairs: `90`
- k candidate paths: `50`
- lambda RE: `0.0`
- CVaR alpha: `0.9`
- RE threshold: `mean` = `0.020969236826882696`
- risk floor: `0.0`

| Method | Hop | MaxRisk | CVaR80 | CVaR90 | RE | Gini | Hop inc. | Total risk agg. red. | Total risk mean per-OD red. | CVaR90 agg. red. | CVaR90 mean per-OD red. | Path overlap w/ CVaR | Changed rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CVaR+Concentration | 9.667 | 0.019367 | 0.010885 | 0.013285 | 0.002756 | 0.157644 | 11.708% | 88.437% | 43.863% | 92.248% | 50.000% | 100.000% | 0.000% |
| CVaR-risk | 9.667 | 0.019367 | 0.010885 | 0.013285 | 0.002756 | 0.157644 | 11.708% | 88.437% | 43.863% | 92.248% | 50.000% | 100.000% | 0.000% |
| Hop-shortest | 8.756 | 0.188173 | 0.110161 | 0.171365 | 0.029298 | 0.475596 | 0.000% | 0.000% | 0.000% | 0.000% | 0.000% | 30.000% | 70.000% |
| Mean-risk-floor | 9.811 | 0.003884 | 0.002226 | 0.003882 | 0.000508 | 0.119798 | 12.351% | 96.903% | 52.164% | 97.734% | 54.141% | 36.667% | 63.333% |
| Mean-risk-raw | 9.811 | 0.003884 | 0.002226 | 0.003882 | 0.000508 | 0.119798 | 12.351% | 96.903% | 52.164% | 97.734% | 54.141% | 36.667% | 63.333% |

Aggregate reduction is computed from method and baseline means. Mean per-OD reduction first computes a paired reduction for each OD and then averages those reductions.
This is an OD path-validation run on the regional association graph, not a real-road navigation experiment.
Continuous edge risk `R_ij` is used for all downstream metrics.
