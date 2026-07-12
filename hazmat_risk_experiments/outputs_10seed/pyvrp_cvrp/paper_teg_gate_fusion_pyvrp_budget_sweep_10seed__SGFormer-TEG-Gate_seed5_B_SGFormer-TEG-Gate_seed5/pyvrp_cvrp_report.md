# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.2 | 0.000% | 8.537998 | 0.000% | 0.254341 | 2.797377 | 0.217599 | 0.864390 | 88.807% |
| 0.25 | 0 | 156455.5 | 6.434% | 7.039840 | 17.547% | 0.180388 | 2.398022 | 0.232968 | 0.859975 | 87.849% |
| 0.5 | 0 | 164971.0 | 12.227% | 5.633606 | 34.017% | 0.145196 | 1.877407 | 0.221496 | 0.849449 | 85.366% |
| 1 | 0 | 175863.2 | 19.637% | 3.165605 | 62.923% | 0.075706 | 1.161278 | 0.275075 | 0.779133 | 74.893% |
| 2 | 0 | 190111.7 | 29.330% | 2.913433 | 65.877% | 0.068459 | 1.160595 | 0.276565 | 0.773025 | 73.707% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
