# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 10.952550 | 0.000% | 0.195260 | 3.657211 | 0.238342 | 0.881017 | 90.367% |
| 1 | 0 | 171902.9 | 17.155% | 3.510315 | 67.950% | 0.051545 | 1.236386 | 0.294784 | 0.794627 | 74.776% |
| 2 | 0 | 183025.8 | 24.736% | 2.935944 | 73.194% | 0.040202 | 1.018599 | 0.241762 | 0.756293 | 69.470% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
