# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.550486 | 0.000% | 0.216863 | 2.284035 | 0.178850 | 0.864239 | 88.985% |
| 1 | 0 | 155149.8 | 15.786% | 2.691370 | 64.355% | 0.071017 | 0.882867 | 0.254557 | 0.770091 | 75.307% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
