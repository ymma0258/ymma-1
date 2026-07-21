# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.1 | 0.000% | 8.030087 | 0.000% | 0.239412 | 2.473949 | 0.220094 | 0.885802 | 90.681% |
| 0.25 | 0 | 141720.0 | 5.763% | 4.705586 | 41.401% | 0.143909 | 1.638594 | 0.256023 | 0.863941 | 86.705% |
| 0.5 | 0 | 147056.8 | 9.745% | 3.874454 | 51.751% | 0.112822 | 1.695790 | 0.328794 | 0.845300 | 84.294% |
| 1 | 0 | 154497.6 | 15.298% | 2.327340 | 71.017% | 0.050421 | 0.907298 | 0.290253 | 0.775166 | 73.798% |
| 2 | 0 | 165796.7 | 23.731% | 1.935144 | 75.901% | 0.036725 | 0.637619 | 0.229444 | 0.747311 | 69.377% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
