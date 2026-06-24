# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.420933 | 0.000% | 0.217788 | 2.362199 | 0.193787 | 0.878179 | 89.055% |
| 1 | 0 | 175079.5 | 19.320% | 3.158386 | 57.440% | 0.081404 | 1.260882 | 0.325850 | 0.815500 | 78.509% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
