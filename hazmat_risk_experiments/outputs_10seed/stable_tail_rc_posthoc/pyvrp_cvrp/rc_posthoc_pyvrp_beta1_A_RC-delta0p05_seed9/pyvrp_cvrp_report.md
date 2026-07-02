# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.169804 | 0.000% | 0.227026 | 2.246691 | 0.198289 | 0.876664 | 89.551% |
| 1 | 0 | 154245.2 | 15.110% | 2.307798 | 67.812% | 0.046474 | 0.771894 | 0.222853 | 0.761135 | 72.640% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
