# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 8.183975 | 0.000% | 0.208181 | 2.467975 | 0.175825 | 0.875455 | 88.969% |
| 1 | 0 | 155397.1 | 15.970% | 2.844891 | 65.238% | 0.065819 | 1.037186 | 0.277315 | 0.773567 | 73.390% |
| 2 | 0 | 166066.1 | 23.932% | 2.112072 | 74.193% | 0.042496 | 0.697169 | 0.254921 | 0.708482 | 64.226% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
