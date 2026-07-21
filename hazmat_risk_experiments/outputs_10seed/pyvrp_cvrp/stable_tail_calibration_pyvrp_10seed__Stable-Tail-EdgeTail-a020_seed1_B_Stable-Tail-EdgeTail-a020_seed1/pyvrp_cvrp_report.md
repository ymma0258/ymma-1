# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 9.870126 | 0.000% | 0.312270 | 3.444827 | 0.256586 | 0.873866 | 90.006% |
| 0.25 | 0 | 155751.2 | 5.955% | 7.971410 | 19.237% | 0.228166 | 2.599372 | 0.242187 | 0.868911 | 88.546% |
| 0.5 | 0 | 164022.5 | 11.582% | 7.018463 | 28.892% | 0.191400 | 2.254068 | 0.232875 | 0.865275 | 87.490% |
| 1 | 0 | 173534.4 | 18.053% | 4.060598 | 58.860% | 0.095089 | 1.316152 | 0.213597 | 0.818140 | 79.909% |
| 2 | 0 | 187465.8 | 27.530% | 3.305202 | 66.513% | 0.066971 | 1.162667 | 0.250276 | 0.797585 | 76.022% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
