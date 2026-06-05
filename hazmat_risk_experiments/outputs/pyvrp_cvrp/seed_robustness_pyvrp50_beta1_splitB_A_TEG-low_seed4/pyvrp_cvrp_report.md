# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.4 | 0.000% | 8.513734 | 0.000% | 0.263242 | 2.531204 | 0.131034 | 0.841208 | 87.294% |
| 1 | 0 | 161712.0 | 20.683% | 3.767400 | 55.749% | 0.081446 | 1.243509 | 0.281713 | 0.750050 | 74.423% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
