# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146531.2 | 0.000% | 8.816814 | 0.000% | 0.264521 | 2.848011 | 0.205297 | 0.839757 | 87.081% |
| 1 | 0 | 181168.4 | 23.638% | 4.316387 | 51.044% | 0.086429 | 1.481230 | 0.257557 | 0.747713 | 74.730% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
