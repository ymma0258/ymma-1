# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.327009 | 0.000% | 0.258226 | 2.721104 | 0.215418 | 0.861092 | 88.775% |
| 1 | 0 | 176746.0 | 20.456% | 3.996882 | 52.001% | 0.094273 | 1.230597 | 0.251439 | 0.805522 | 80.200% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
