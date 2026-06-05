# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.2 | 0.000% | 8.452250 | 0.000% | 0.247524 | 2.775063 | 0.210980 | 0.847142 | 87.737% |
| 1 | 0 | 159880.0 | 19.316% | 3.292546 | 61.045% | 0.081298 | 1.144897 | 0.252542 | 0.726400 | 71.886% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
