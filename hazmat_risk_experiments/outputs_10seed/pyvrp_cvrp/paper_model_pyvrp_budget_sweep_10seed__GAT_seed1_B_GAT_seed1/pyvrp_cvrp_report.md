# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147463.7 | 0.000% | 7.127241 | 0.000% | 0.205481 | 2.433686 | 0.291898 | 0.858195 | 88.115% |
| 0.25 | 0 | 155575.3 | 5.501% | 5.979145 | 16.109% | 0.169794 | 2.022848 | 0.254313 | 0.852291 | 86.970% |
| 0.5 | 0 | 163070.9 | 10.584% | 4.514758 | 36.655% | 0.126253 | 1.277282 | 0.201058 | 0.827840 | 83.061% |
| 1 | 0 | 173923.5 | 17.943% | 3.747389 | 47.422% | 0.099717 | 1.076111 | 0.192681 | 0.814118 | 80.658% |
| 2 | 0 | 189685.8 | 28.632% | 2.852679 | 59.975% | 0.063728 | 0.937097 | 0.257205 | 0.785868 | 76.074% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
