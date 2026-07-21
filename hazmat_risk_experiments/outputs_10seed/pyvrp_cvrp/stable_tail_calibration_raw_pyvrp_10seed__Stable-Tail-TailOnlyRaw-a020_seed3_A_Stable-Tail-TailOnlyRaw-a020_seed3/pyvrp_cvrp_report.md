# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.8 | 0.000% | 7.679488 | 0.000% | 0.240358 | 2.621145 | 0.216126 | 0.878256 | 89.528% |
| 0.25 | 0 | 142051.8 | 5.800% | 5.195323 | 32.348% | 0.150807 | 1.532641 | 0.174039 | 0.864356 | 87.742% |
| 0.5 | 0 | 147713.7 | 10.017% | 3.998248 | 47.936% | 0.115083 | 1.463631 | 0.265977 | 0.842730 | 84.402% |
| 1 | 0 | 155146.5 | 15.553% | 2.492270 | 67.546% | 0.065347 | 0.810387 | 0.249477 | 0.779791 | 75.647% |
| 2 | 0 | 167474.6 | 24.735% | 2.267759 | 70.470% | 0.056443 | 0.798591 | 0.275027 | 0.761396 | 72.752% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
