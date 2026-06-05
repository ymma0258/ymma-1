# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.4 | 0.000% | 8.429541 | 0.000% | 0.234511 | 2.716354 | 0.213907 | 0.842542 | 87.221% |
| 1 | 0 | 159880.0 | 19.316% | 3.428133 | 59.332% | 0.084646 | 1.192044 | 0.252542 | 0.726400 | 71.885% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
