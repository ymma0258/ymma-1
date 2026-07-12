# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147264.1 | 0.000% | 6.673592 | 0.000% | 0.195632 | 2.076434 | 0.196650 | 0.866585 | 89.540% |
| 0.25 | 0 | 156210.8 | 6.075% | 5.247909 | 21.363% | 0.139397 | 1.620594 | 0.204314 | 0.864081 | 88.405% |
| 0.5 | 0 | 164573.4 | 11.754% | 4.728935 | 29.140% | 0.126467 | 1.406757 | 0.176616 | 0.859674 | 87.138% |
| 1 | 0 | 175846.9 | 19.409% | 3.157556 | 52.686% | 0.081027 | 0.939551 | 0.223765 | 0.828532 | 81.435% |
| 2 | 0 | 193742.8 | 31.561% | 2.382969 | 64.293% | 0.051201 | 0.716493 | 0.216600 | 0.792856 | 75.277% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
