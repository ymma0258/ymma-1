# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 12.505550 | 0.000% | 0.376147 | 3.393210 | 0.134154 | 0.845374 | 88.155% |
| 1 | 0 | 163321.4 | 21.884% | 5.469933 | 56.260% | 0.149091 | 1.644481 | 0.199403 | 0.769205 | 77.320% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
