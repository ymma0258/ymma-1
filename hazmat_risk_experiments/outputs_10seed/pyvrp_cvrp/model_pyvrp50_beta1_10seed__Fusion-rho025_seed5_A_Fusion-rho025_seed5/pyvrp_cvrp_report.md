# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 6.876013 | 0.000% | 0.195714 | 2.106191 | 0.182723 | 0.856831 | 87.974% |
| 1 | 0 | 156678.6 | 16.926% | 2.584534 | 62.412% | 0.065651 | 0.907773 | 0.262170 | 0.746404 | 73.196% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
