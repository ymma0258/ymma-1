# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.921122 | 0.000% | 0.230336 | 2.781520 | 0.187972 | 0.836034 | 86.972% |
| 1 | 0 | 177702.0 | 21.107% | 3.599174 | 59.656% | 0.080974 | 1.169411 | 0.230311 | 0.700024 | 69.527% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
