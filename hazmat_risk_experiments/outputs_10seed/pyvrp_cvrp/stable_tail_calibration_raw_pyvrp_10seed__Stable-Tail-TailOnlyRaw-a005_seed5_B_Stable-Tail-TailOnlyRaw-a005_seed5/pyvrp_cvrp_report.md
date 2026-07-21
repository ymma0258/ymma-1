# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147064.3 | 0.000% | 7.762130 | 0.000% | 0.228995 | 2.629125 | 0.229050 | 0.874697 | 89.107% |
| 0.25 | 0 | 157059.7 | 6.797% | 6.752129 | 13.012% | 0.174951 | 2.200078 | 0.246197 | 0.868847 | 88.195% |
| 0.5 | 0 | 165728.9 | 12.691% | 5.051782 | 34.918% | 0.120511 | 1.674051 | 0.245316 | 0.848952 | 84.982% |
| 1 | 0 | 175840.5 | 19.567% | 3.629793 | 53.237% | 0.086789 | 1.258908 | 0.271523 | 0.818511 | 79.899% |
| 2 | 0 | 191704.8 | 30.354% | 2.826207 | 63.590% | 0.067796 | 0.893229 | 0.277175 | 0.793733 | 75.281% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
