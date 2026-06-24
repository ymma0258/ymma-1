# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 7.736093 | 0.000% | 0.233101 | 2.305522 | 0.160077 | 0.879734 | 89.716% |
| 0.25 | 0 | 143350.5 | 6.980% | 5.094041 | 34.152% | 0.135813 | 1.881158 | 0.319873 | 0.866253 | 86.624% |
| 0.5 | 0 | 149614.5 | 11.655% | 4.047717 | 47.678% | 0.112820 | 1.427905 | 0.263684 | 0.842823 | 83.340% |
| 1 | 0 | 158998.3 | 18.658% | 2.898866 | 62.528% | 0.077334 | 0.951183 | 0.275062 | 0.808054 | 77.941% |
| 2 | 0 | 173007.4 | 29.112% | 2.280632 | 70.520% | 0.045605 | 0.895112 | 0.310494 | 0.768364 | 72.142% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
