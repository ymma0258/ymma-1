# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 6.316462 | 0.000% | 0.180132 | 1.841064 | 0.170922 | 0.873332 | 88.988% |
| 1 | 0 | 155627.7 | 16.142% | 2.349530 | 62.803% | 0.060587 | 0.870247 | 0.272450 | 0.775795 | 74.347% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
