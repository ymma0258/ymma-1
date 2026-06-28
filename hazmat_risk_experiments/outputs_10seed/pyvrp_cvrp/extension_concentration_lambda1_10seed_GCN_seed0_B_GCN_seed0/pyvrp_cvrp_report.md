# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.918001 | 0.000% | 0.244567 | 2.611301 | 0.231434 | 0.858147 | 88.643% |
| 1 | 0 | 179529.1 | 22.353% | 3.519247 | 55.554% | 0.086281 | 1.232476 | 0.308070 | 0.805851 | 79.896% |
| 1 | 1 | 193991.8 | 32.209% | 2.818454 | 64.404% | 0.064719 | 0.851339 | 0.243977 | 0.770965 | 74.531% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
