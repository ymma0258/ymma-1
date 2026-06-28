# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.904276 | 0.000% | 0.277100 | 2.521856 | 0.146460 | 0.873996 | 89.696% |
| 1 | 0 | 158389.7 | 18.203% | 3.234524 | 63.674% | 0.069830 | 1.238613 | 0.322645 | 0.800094 | 76.942% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
