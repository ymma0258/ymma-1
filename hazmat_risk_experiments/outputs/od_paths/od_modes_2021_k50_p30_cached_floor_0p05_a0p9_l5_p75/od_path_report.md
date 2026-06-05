# OD Path Validation Report

- Year: `data_2021`
- OD pairs: `90`
- k candidate paths: `50`
- lambda RE: `5.0`
- CVaR alpha: `0.9`
- RE threshold: `p75` = `0.024947531521320343`
- risk floor: `0.0`

| Method | Hop | MaxRisk | CVaR80 | CVaR90 | RE | Gini | Hop inc. | Total risk agg. red. | Total risk mean per-OD red. | CVaR90 agg. red. | CVaR90 mean per-OD red. | Path overlap w/ CVaR | Changed rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CVaR+Concentration | 10.344 | 0.048669 | 0.038236 | 0.043202 | 0.003564 | 0.122091 | 20.802% | 41.629% | 21.220% | 77.462% | 43.760% | 53.333% | 46.667% |
| CVaR-risk | 9.678 | 0.048636 | 0.040267 | 0.043170 | 0.004901 | 0.122333 | 11.867% | 43.230% | 24.786% | 77.479% | 43.774% | 100.000% | 0.000% |
| Hop-shortest | 8.756 | 0.207668 | 0.135119 | 0.191688 | 0.032163 | 0.324286 | 0.000% | 0.000% | 0.000% | 0.000% | 0.000% | 30.000% | 70.000% |
| Mean-risk-floor | 9.789 | 0.033384 | 0.030787 | 0.033293 | 0.001978 | 0.114835 | 12.157% | 50.249% | 32.423% | 82.632% | 48.048% | 37.778% | 62.222% |
| Mean-risk-raw | 9.789 | 0.033384 | 0.030787 | 0.033293 | 0.001978 | 0.114835 | 12.157% | 50.249% | 32.423% | 82.632% | 48.048% | 37.778% | 62.222% |

Aggregate reduction is computed from method and baseline means. Mean per-OD reduction first computes a paired reduction for each OD and then averages those reductions.
This is an OD path-validation run on the regional association graph, not a real-road navigation experiment.
Continuous edge risk `R_ij` is used for all downstream metrics.
