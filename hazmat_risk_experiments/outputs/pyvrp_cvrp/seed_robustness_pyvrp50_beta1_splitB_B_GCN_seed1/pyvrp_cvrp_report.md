# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146531.2 | 0.000% | 8.123781 | 0.000% | 0.250195 | 2.788871 | 0.235738 | 0.869809 | 89.599% |
| 1 | 0 | 176885.2 | 20.715% | 3.837640 | 52.760% | 0.092251 | 1.243389 | 0.278448 | 0.817836 | 80.411% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
