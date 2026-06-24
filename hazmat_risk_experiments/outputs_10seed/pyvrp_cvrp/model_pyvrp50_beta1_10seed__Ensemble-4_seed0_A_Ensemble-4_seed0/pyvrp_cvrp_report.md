# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 7.671549 | 0.000% | 0.238328 | 2.483005 | 0.202621 | 0.854736 | 88.156% |
| 1 | 0 | 158080.3 | 17.973% | 2.790066 | 63.631% | 0.065151 | 0.997304 | 0.262489 | 0.728513 | 72.236% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
