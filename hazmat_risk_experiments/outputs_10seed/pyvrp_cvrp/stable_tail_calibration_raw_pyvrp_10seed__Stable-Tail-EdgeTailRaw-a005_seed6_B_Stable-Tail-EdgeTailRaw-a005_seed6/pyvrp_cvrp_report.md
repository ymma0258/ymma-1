# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.3 | 0.000% | 8.822580 | 0.000% | 0.261984 | 3.069834 | 0.241940 | 0.868805 | 89.195% |
| 0.25 | 0 | 158156.1 | 7.445% | 7.728912 | 12.396% | 0.190822 | 2.660005 | 0.255094 | 0.869492 | 89.257% |
| 0.5 | 0 | 168665.5 | 14.585% | 6.089257 | 30.981% | 0.153156 | 2.268149 | 0.290133 | 0.855168 | 86.498% |
| 1 | 0 | 181848.0 | 23.540% | 4.165866 | 52.782% | 0.104526 | 1.545032 | 0.314681 | 0.825087 | 80.872% |
| 2 | 0 | 202470.9 | 37.551% | 3.723697 | 57.794% | 0.095313 | 1.538331 | 0.362906 | 0.816793 | 79.133% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
