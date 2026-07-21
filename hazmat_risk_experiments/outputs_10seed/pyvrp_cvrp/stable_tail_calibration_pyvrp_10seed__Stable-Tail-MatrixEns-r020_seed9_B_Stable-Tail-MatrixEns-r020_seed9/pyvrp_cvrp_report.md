# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 7.197170 | 0.000% | 0.227390 | 2.281486 | 0.211172 | 0.871250 | 89.981% |
| 0.25 | 0 | 157833.4 | 7.420% | 6.233044 | 13.396% | 0.168950 | 2.002816 | 0.221401 | 0.870630 | 89.680% |
| 0.5 | 0 | 167974.5 | 14.322% | 3.916722 | 45.580% | 0.105268 | 1.360929 | 0.256274 | 0.839048 | 84.276% |
| 1 | 0 | 179192.6 | 21.957% | 2.798456 | 61.117% | 0.064797 | 1.001951 | 0.281766 | 0.811909 | 79.150% |
| 2 | 0 | 196073.8 | 33.447% | 2.419072 | 66.389% | 0.048159 | 0.736035 | 0.228110 | 0.791213 | 76.132% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
