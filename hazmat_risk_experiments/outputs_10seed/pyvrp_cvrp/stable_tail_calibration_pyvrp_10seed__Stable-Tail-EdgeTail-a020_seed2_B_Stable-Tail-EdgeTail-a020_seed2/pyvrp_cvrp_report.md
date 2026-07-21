# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.2 | 0.000% | 9.240166 | 0.000% | 0.288248 | 3.513797 | 0.315674 | 0.878572 | 90.025% |
| 0.25 | 0 | 156298.4 | 6.327% | 7.842863 | 15.122% | 0.244584 | 3.435694 | 0.350013 | 0.875184 | 89.411% |
| 0.5 | 0 | 164601.2 | 11.976% | 6.376456 | 30.992% | 0.180564 | 2.341297 | 0.279089 | 0.863394 | 87.247% |
| 1 | 0 | 176807.6 | 20.280% | 4.346156 | 52.965% | 0.115923 | 1.895133 | 0.347984 | 0.842846 | 82.961% |
| 2 | 0 | 195367.5 | 32.906% | 3.745693 | 59.463% | 0.095360 | 1.581382 | 0.348064 | 0.831437 | 80.721% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
