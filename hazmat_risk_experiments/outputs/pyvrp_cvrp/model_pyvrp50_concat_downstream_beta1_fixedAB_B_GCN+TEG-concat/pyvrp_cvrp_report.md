# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146531.2 | 0.000% | 7.782682 | 0.000% | 0.244204 | 2.694265 | 0.248715 | 0.882545 | 90.603% |
| 1 | 0 | 176686.4 | 20.579% | 2.983237 | 61.668% | 0.062350 | 1.036451 | 0.276663 | 0.818129 | 78.827% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
