# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.4 | 0.000% | 8.549538 | 0.000% | 0.281811 | 2.363396 | 0.164651 | 0.873801 | 89.618% |
| 0.25 | 0 | 143059.2 | 6.656% | 5.584955 | 34.675% | 0.167913 | 2.023431 | 0.247148 | 0.856977 | 86.374% |
| 0.5 | 0 | 149259.1 | 11.278% | 4.466905 | 47.753% | 0.130104 | 1.856341 | 0.286637 | 0.840299 | 83.981% |
| 1 | 0 | 158685.4 | 18.306% | 3.103966 | 63.694% | 0.083542 | 1.213882 | 0.302223 | 0.797861 | 77.103% |
| 2 | 0 | 171780.2 | 28.069% | 2.435949 | 71.508% | 0.058320 | 0.810906 | 0.270485 | 0.764903 | 71.851% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
