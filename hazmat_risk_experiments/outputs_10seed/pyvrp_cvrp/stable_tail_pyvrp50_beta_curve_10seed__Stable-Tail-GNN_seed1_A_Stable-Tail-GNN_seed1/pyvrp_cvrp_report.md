# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.593196 | 0.000% | 0.239314 | 2.265632 | 0.172750 | 0.878710 | 89.538% |
| 0.25 | 0 | 141942.1 | 5.929% | 5.815237 | 23.415% | 0.188457 | 1.790334 | 0.221711 | 0.874722 | 88.100% |
| 0.5 | 0 | 147516.3 | 10.089% | 3.967101 | 47.755% | 0.104920 | 1.463858 | 0.267683 | 0.845559 | 83.389% |
| 1 | 0 | 155007.6 | 15.679% | 2.614960 | 65.562% | 0.061735 | 0.899936 | 0.243726 | 0.792743 | 75.546% |
| 2 | 0 | 165869.5 | 23.785% | 2.080456 | 72.601% | 0.047786 | 0.608937 | 0.226811 | 0.755680 | 69.824% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
