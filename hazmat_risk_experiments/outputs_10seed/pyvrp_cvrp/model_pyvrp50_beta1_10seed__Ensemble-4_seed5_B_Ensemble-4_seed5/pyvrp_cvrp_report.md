# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.417313 | 0.000% | 0.224273 | 2.445766 | 0.210033 | 0.842823 | 86.944% |
| 1 | 0 | 176540.8 | 20.316% | 3.492589 | 52.913% | 0.082496 | 1.141024 | 0.262015 | 0.756607 | 75.752% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
