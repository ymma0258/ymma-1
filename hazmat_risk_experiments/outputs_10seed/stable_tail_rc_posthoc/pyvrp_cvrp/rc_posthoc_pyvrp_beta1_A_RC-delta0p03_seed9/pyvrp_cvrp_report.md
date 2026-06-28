# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.6 | 0.000% | 7.600460 | 0.000% | 0.230824 | 2.242797 | 0.180960 | 0.879159 | 89.919% |
| 1 | 0 | 154341.3 | 15.125% | 2.162164 | 71.552% | 0.043613 | 0.798249 | 0.273137 | 0.756016 | 71.643% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
