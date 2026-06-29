# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 6.878324 | 0.000% | 0.198600 | 2.291333 | 0.216493 | 0.878165 | 89.534% |
| 2 | 1 | 173490.4 | 29.473% | 1.475036 | 78.555% | 0.023248 | 0.469550 | 0.235373 | 0.667932 | 59.131% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
