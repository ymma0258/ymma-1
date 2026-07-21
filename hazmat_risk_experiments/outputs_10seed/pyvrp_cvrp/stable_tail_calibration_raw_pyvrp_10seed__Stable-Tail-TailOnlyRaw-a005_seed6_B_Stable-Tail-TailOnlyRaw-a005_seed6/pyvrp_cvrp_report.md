# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147264.1 | 0.000% | 8.929986 | 0.000% | 0.265228 | 3.172689 | 0.250239 | 0.868861 | 89.203% |
| 0.25 | 0 | 158200.7 | 7.427% | 7.866958 | 11.904% | 0.194036 | 2.706952 | 0.255644 | 0.869433 | 89.338% |
| 0.5 | 0 | 168417.9 | 14.365% | 6.226219 | 30.277% | 0.160543 | 2.027980 | 0.224444 | 0.859921 | 86.853% |
| 1 | 0 | 182178.7 | 23.709% | 4.321394 | 51.608% | 0.108736 | 1.649370 | 0.323213 | 0.831230 | 81.737% |
| 2 | 0 | 202975.9 | 37.831% | 3.785927 | 57.604% | 0.097314 | 1.512123 | 0.360372 | 0.820998 | 79.662% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
