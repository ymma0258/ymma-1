# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.829986 | 0.000% | 0.274821 | 2.920423 | 0.217895 | 0.862456 | 89.296% |
| 1 | 0 | 180217.6 | 22.822% | 4.267423 | 51.671% | 0.106990 | 1.419274 | 0.249227 | 0.821270 | 81.562% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
