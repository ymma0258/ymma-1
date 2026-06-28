# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 10.666306 | 0.000% | 0.196435 | 3.663406 | 0.259014 | 0.884999 | 90.211% |
| 1 | 0 | 173753.5 | 18.416% | 3.745068 | 64.889% | 0.054946 | 1.345587 | 0.276626 | 0.811228 | 75.956% |
| 2 | 0 | 187351.7 | 27.684% | 3.316233 | 68.909% | 0.048537 | 1.254908 | 0.300687 | 0.795795 | 73.509% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
