# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.2 | 0.000% | 7.161000 | 0.000% | 0.219232 | 2.374442 | 0.242012 | 0.872019 | 89.248% |
| 0.25 | 0 | 154958.3 | 5.416% | 5.796581 | 19.053% | 0.146150 | 2.387935 | 0.293701 | 0.864891 | 87.783% |
| 0.5 | 0 | 162385.0 | 10.468% | 5.004183 | 30.119% | 0.127265 | 2.196729 | 0.306996 | 0.859180 | 86.532% |
| 1 | 0 | 173798.9 | 18.233% | 3.366368 | 52.990% | 0.088410 | 1.401366 | 0.322449 | 0.834091 | 81.774% |
| 2 | 0 | 189738.8 | 29.076% | 2.740237 | 61.734% | 0.068766 | 1.106802 | 0.282409 | 0.807202 | 77.322% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
