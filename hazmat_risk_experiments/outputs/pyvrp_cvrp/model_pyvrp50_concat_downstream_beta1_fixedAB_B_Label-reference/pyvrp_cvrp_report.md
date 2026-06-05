# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146531.2 | 0.000% | 7.440737 | 0.000% | 0.192672 | 2.788685 | 0.284119 | 0.832535 | 85.112% |
| 1 | 0 | 175104.2 | 19.500% | 4.413919 | 40.679% | 0.067923 | 1.691635 | 0.278588 | 0.772557 | 76.179% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
