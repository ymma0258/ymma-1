# OD Path Validation Report

- Year: `data_2021`
- OD pairs: `90`
- k candidate paths: `50`
- lambda RE: `1.0`
- CVaR alpha: `0.8`
- RE threshold: `mean` = `0.04289633211285255`
- risk floor: `0.0`

| Method | Hop | MaxRisk | CVaR80 | CVaR90 | RE | Gini | Hop inc. | Total risk agg. red. | Total risk mean per-OD red. | CVaR90 agg. red. | CVaR90 mean per-OD red. | Path overlap w/ CVaR | Changed rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CVaR+Concentration | 9.833 | 0.048467 | 0.037855 | 0.043543 | 0.001833 | 0.122365 | 14.814% | 43.720% | 24.250% | 77.284% | 43.432% | 97.778% | 2.222% |
| CVaR-risk | 9.789 | 0.048467 | 0.037855 | 0.043543 | 0.002033 | 0.123109 | 14.100% | 43.941% | 24.472% | 77.284% | 43.432% | 100.000% | 0.000% |
| Hop-shortest | 8.756 | 0.207668 | 0.135119 | 0.191688 | 0.028046 | 0.324286 | 0.000% | 0.000% | 0.000% | 0.000% | 0.000% | 22.222% | 77.778% |
| Mean-risk-floor | 9.789 | 0.033384 | 0.030787 | 0.033293 | 0.000494 | 0.114835 | 12.157% | 50.249% | 32.423% | 82.632% | 48.048% | 37.778% | 62.222% |
| Mean-risk-raw | 9.789 | 0.033384 | 0.030787 | 0.033293 | 0.000494 | 0.114835 | 12.157% | 50.249% | 32.423% | 82.632% | 48.048% | 37.778% | 62.222% |

Aggregate reduction is computed from method and baseline means. Mean per-OD reduction first computes a paired reduction for each OD and then averages those reductions.
This is an OD path-validation run on the regional association graph, not a real-road navigation experiment.
Continuous edge risk `R_ij` is used for all downstream metrics.
