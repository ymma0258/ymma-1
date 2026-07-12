# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.8 | 0.000% | 11.395055 | 0.000% | 0.357058 | 3.678224 | 0.201738 | 0.869619 | 90.417% |
| 0.25 | 0 | 158356.2 | 7.532% | 9.546363 | 16.224% | 0.266600 | 2.960831 | 0.221411 | 0.868620 | 90.040% |
| 0.5 | 0 | 168842.3 | 14.653% | 7.993451 | 29.852% | 0.220688 | 2.411037 | 0.191882 | 0.868959 | 88.798% |
| 1 | 0 | 183193.4 | 24.398% | 5.648670 | 50.429% | 0.141694 | 1.909546 | 0.266146 | 0.851422 | 84.812% |
| 2 | 0 | 205046.4 | 39.237% | 4.861635 | 57.336% | 0.116613 | 1.611861 | 0.268352 | 0.841351 | 82.235% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
