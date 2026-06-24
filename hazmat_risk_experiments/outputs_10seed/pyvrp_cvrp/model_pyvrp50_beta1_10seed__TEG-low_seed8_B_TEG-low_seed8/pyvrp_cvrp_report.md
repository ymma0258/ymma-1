# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.519431 | 0.000% | 0.251641 | 2.779042 | 0.217431 | 0.841806 | 87.151% |
| 1 | 0 | 177414.7 | 20.912% | 4.195370 | 50.755% | 0.104044 | 1.694735 | 0.345037 | 0.758719 | 75.865% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
