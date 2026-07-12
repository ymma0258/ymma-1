# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.9 | 0.000% | 6.931043 | 0.000% | 0.207141 | 2.282394 | 0.237144 | 0.869241 | 88.906% |
| 0.25 | 0 | 155808.1 | 5.802% | 5.780805 | 16.595% | 0.145917 | 2.217460 | 0.270096 | 0.863041 | 87.720% |
| 0.5 | 0 | 163641.8 | 11.121% | 4.712089 | 32.015% | 0.119457 | 1.872227 | 0.288817 | 0.851497 | 85.614% |
| 1 | 0 | 175576.5 | 19.226% | 3.730668 | 46.175% | 0.094688 | 1.393167 | 0.281102 | 0.837668 | 82.714% |
| 2 | 0 | 193635.1 | 31.489% | 2.759229 | 60.190% | 0.066996 | 1.154743 | 0.303408 | 0.806630 | 77.331% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
