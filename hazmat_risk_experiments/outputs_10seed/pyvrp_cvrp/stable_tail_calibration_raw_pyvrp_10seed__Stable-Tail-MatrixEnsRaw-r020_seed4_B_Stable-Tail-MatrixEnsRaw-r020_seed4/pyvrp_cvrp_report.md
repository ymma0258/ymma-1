# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.4 | 0.000% | 6.815911 | 0.000% | 0.203819 | 2.297560 | 0.229253 | 0.873911 | 89.313% |
| 0.25 | 0 | 156454.6 | 6.289% | 5.857006 | 14.069% | 0.154916 | 1.951619 | 0.245149 | 0.870135 | 88.172% |
| 0.5 | 0 | 165074.0 | 12.145% | 4.456696 | 34.613% | 0.116317 | 1.466851 | 0.269237 | 0.853254 | 85.194% |
| 1 | 0 | 175707.4 | 19.369% | 3.194836 | 53.127% | 0.081448 | 1.206409 | 0.296634 | 0.822210 | 80.361% |
| 2 | 0 | 191928.0 | 30.388% | 2.473604 | 63.708% | 0.050628 | 0.961285 | 0.311916 | 0.794264 | 75.944% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
