# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.440314 | 0.000% | 0.263800 | 2.286327 | 0.134511 | 0.873717 | 90.233% |
| 1 | 0 | 159710.0 | 19.189% | 3.776579 | 55.255% | 0.105621 | 1.131933 | 0.214604 | 0.836215 | 81.900% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
