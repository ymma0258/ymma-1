# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.038404 | 0.000% | 0.222652 | 2.831697 | 0.276223 | 0.864026 | 88.897% |
| 1 | 0 | 173507.9 | 18.249% | 3.558515 | 55.731% | 0.086047 | 1.193681 | 0.255553 | 0.797653 | 77.461% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
