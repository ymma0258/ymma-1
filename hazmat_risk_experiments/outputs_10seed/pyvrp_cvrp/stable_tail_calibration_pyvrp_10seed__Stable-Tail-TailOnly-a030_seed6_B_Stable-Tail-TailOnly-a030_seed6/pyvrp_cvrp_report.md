# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 9.527138 | 0.000% | 0.288461 | 3.221590 | 0.236406 | 0.874374 | 89.863% |
| 0.25 | 0 | 157377.2 | 7.110% | 8.398829 | 11.843% | 0.203703 | 2.504008 | 0.220363 | 0.873436 | 90.020% |
| 0.5 | 0 | 167567.7 | 14.045% | 6.255238 | 34.343% | 0.163502 | 1.933279 | 0.216717 | 0.861871 | 87.119% |
| 1 | 0 | 180337.1 | 22.736% | 4.392160 | 53.898% | 0.111265 | 1.663482 | 0.336967 | 0.835808 | 82.159% |
| 2 | 0 | 200131.5 | 36.208% | 3.839855 | 59.696% | 0.099972 | 1.485444 | 0.353964 | 0.822794 | 80.052% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
