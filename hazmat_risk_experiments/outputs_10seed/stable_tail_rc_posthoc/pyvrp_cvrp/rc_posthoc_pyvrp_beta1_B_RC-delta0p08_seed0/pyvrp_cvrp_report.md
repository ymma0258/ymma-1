# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.216549 | 0.000% | 0.260692 | 2.689588 | 0.222431 | 0.881330 | 90.541% |
| 1 | 0 | 176669.5 | 20.404% | 3.217001 | 60.847% | 0.070437 | 1.295356 | 0.314747 | 0.826487 | 79.895% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
