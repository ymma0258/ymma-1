# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.918001 | 0.000% | 0.244567 | 2.611301 | 0.231434 | 0.858147 | 88.643% |
| 1 | 0 | 179617.7 | 22.413% | 3.648664 | 53.919% | 0.090659 | 1.253223 | 0.297190 | 0.810492 | 80.492% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
