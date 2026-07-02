# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.593196 | 0.000% | 0.239314 | 2.265632 | 0.172750 | 0.878710 | 89.538% |
| 2 | 2 | 180981.6 | 35.063% | 1.686551 | 77.789% | 0.028364 | 0.652411 | 0.262472 | 0.695812 | 61.186% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
