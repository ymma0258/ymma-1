# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.701649 | 0.000% | 0.270892 | 2.469651 | 0.147285 | 0.874652 | 89.737% |
| 3 | 1 | 197481.1 | 47.377% | 2.186730 | 74.870% | 0.040941 | 0.970343 | 0.351097 | 0.721128 | 65.023% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
