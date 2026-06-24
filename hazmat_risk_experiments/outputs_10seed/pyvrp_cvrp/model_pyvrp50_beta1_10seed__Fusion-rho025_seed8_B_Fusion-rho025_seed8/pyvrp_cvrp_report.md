# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.250747 | 0.000% | 0.241284 | 2.719472 | 0.216599 | 0.860724 | 88.652% |
| 1 | 0 | 180758.7 | 23.191% | 3.786623 | 54.106% | 0.081836 | 1.514743 | 0.311722 | 0.797348 | 78.851% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
