# OD Path Validation Report

- Year: `data_2021`
- OD pairs: `30`
- k candidate paths: `20`
- lambda RE: `1.0`

| Method | Hop | MaxRisk | CVaR80 | CVaR90 | RE | Gini | Hop inc. | Risk red. | CVaR90 red. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CVaR+Concentration | 8.967 | 0.006513 | 0.000592 | 0.000592 | 0.000530 | 0.030303 | 5.315% | 55.353% | 56.470% |
| CVaR-risk | 8.967 | 0.006513 | 0.000592 | 0.000592 | 0.000530 | 0.030303 | 5.315% | 55.353% | 56.470% |
| Hop-shortest | 8.567 | 0.188538 | 0.076331 | 0.148955 | 0.026203 | 0.479297 | 0.000% | 0.000% | 0.000% |
| Mean-risk | 9.167 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 7.730% | 56.667% | 56.667% |

This is an OD path-validation run on the regional association graph, not a real-road navigation experiment.
Continuous edge risk `R_ij` is used for all downstream metrics.
