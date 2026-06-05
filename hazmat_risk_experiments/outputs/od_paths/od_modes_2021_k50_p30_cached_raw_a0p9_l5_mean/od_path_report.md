# OD Path Validation Report

- Year: `data_2021`
- OD pairs: `90`
- k candidate paths: `50`
- lambda RE: `5.0`
- CVaR alpha: `0.9`
- RE threshold: `mean` = `0.020521744250827055`
- risk floor: `0.0001`

| Method | Hop | MaxRisk | CVaR80 | CVaR90 | RE | Gini | Hop inc. | Total risk agg. red. | Total risk mean per-OD red. | CVaR90 agg. red. | CVaR90 mean per-OD red. | Path overlap w/ CVaR | Changed rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CVaR+Concentration | 9.267 | 0.018640 | 0.003888 | 0.009611 | 0.001929 | 0.079281 | 6.479% | 91.566% | 47.767% | 94.110% | 48.411% | 96.667% | 3.333% |
| CVaR-risk | 9.200 | 0.018640 | 0.006879 | 0.009611 | 0.002749 | 0.076042 | 5.383% | 90.205% | 47.165% | 94.110% | 48.411% | 100.000% | 0.000% |
| Hop-shortest | 8.756 | 0.187776 | 0.078489 | 0.163159 | 0.029324 | 0.434754 | 0.000% | 0.000% | 0.000% | 0.000% | 0.000% | 50.000% | 50.000% |
| Mean-risk-floor | 9.311 | 0.003278 | 0.000546 | 0.003278 | 0.000508 | 0.009259 | 6.750% | 98.675% | 51.111% | 97.991% | 51.111% | 76.667% | 23.333% |
| Mean-risk-raw | 9.411 | 0.003278 | 0.000546 | 0.003278 | 0.000508 | 0.009259 | 8.058% | 98.675% | 51.111% | 97.991% | 51.111% | 68.889% | 31.111% |

Aggregate reduction is computed from method and baseline means. Mean per-OD reduction first computes a paired reduction for each OD and then averages those reductions.
This is an OD path-validation run on the regional association graph, not a real-road navigation experiment.
Continuous edge risk `R_ij` is used for all downstream metrics.
