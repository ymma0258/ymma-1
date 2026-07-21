# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.3 | 0.000% | 6.994552 | 0.000% | 0.206506 | 2.353163 | 0.223948 | 0.868782 | 89.128% |
| 0.25 | 0 | 157914.3 | 7.281% | 6.253824 | 10.590% | 0.152407 | 2.082539 | 0.238424 | 0.868603 | 89.238% |
| 0.5 | 0 | 168151.3 | 14.235% | 4.799605 | 31.381% | 0.121731 | 1.739616 | 0.263131 | 0.855373 | 86.419% |
| 1 | 0 | 181601.1 | 23.373% | 3.580393 | 48.812% | 0.088142 | 1.258751 | 0.305922 | 0.831362 | 82.019% |
| 2 | 0 | 202925.0 | 37.859% | 3.022267 | 56.791% | 0.076812 | 1.177747 | 0.363892 | 0.817782 | 79.281% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
