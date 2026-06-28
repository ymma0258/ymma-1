# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 11.181315 | 0.000% | 0.207140 | 3.582292 | 0.214692 | 0.883260 | 90.664% |
| 1 | 0 | 176625.5 | 20.374% | 4.387384 | 60.761% | 0.073121 | 1.913277 | 0.347405 | 0.826299 | 79.685% |
| 2 | 0 | 191582.7 | 30.567% | 3.345740 | 70.077% | 0.051243 | 1.525216 | 0.339590 | 0.790509 | 73.539% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
