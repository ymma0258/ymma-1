# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.9 | 0.000% | 8.642889 | 0.000% | 0.276117 | 2.429431 | 0.148264 | 0.864188 | 88.934% |
| 0.25 | 0 | 143324.6 | 6.960% | 6.892778 | 20.249% | 0.203192 | 2.124596 | 0.262516 | 0.859497 | 88.281% |
| 0.5 | 0 | 150553.3 | 12.355% | 5.028967 | 41.814% | 0.145801 | 1.830558 | 0.268337 | 0.835982 | 84.647% |
| 1 | 0 | 160683.5 | 19.915% | 3.489641 | 59.624% | 0.079777 | 1.169241 | 0.299979 | 0.785038 | 77.683% |
| 2 | 0 | 176952.7 | 32.056% | 2.773906 | 67.905% | 0.059068 | 1.160938 | 0.333346 | 0.744745 | 71.892% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
