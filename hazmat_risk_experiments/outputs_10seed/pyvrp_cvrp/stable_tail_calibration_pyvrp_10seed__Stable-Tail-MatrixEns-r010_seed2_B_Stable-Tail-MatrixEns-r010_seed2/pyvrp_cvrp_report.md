# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 7.860031 | 0.000% | 0.243775 | 2.964301 | 0.304080 | 0.873571 | 89.437% |
| 0.25 | 0 | 156559.4 | 6.505% | 6.710833 | 14.621% | 0.204964 | 2.508056 | 0.313395 | 0.872052 | 88.883% |
| 0.5 | 0 | 164999.3 | 12.246% | 5.347364 | 31.968% | 0.155450 | 1.864891 | 0.254561 | 0.858199 | 86.540% |
| 1 | 0 | 177951.8 | 21.058% | 3.938580 | 49.891% | 0.104951 | 1.447585 | 0.265761 | 0.843733 | 83.233% |
| 2 | 0 | 196472.8 | 33.657% | 3.230453 | 58.900% | 0.079800 | 1.443623 | 0.347844 | 0.825078 | 79.785% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
