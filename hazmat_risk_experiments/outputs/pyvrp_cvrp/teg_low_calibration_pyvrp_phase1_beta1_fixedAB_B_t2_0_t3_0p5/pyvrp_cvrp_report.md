# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146531.2 | 0.000% | 8.432592 | 0.000% | 0.257797 | 2.726327 | 0.214925 | 0.835211 | 86.681% |
| 1 | 0 | 179685.6 | 22.626% | 3.699089 | 56.133% | 0.086306 | 1.145434 | 0.213532 | 0.708380 | 70.150% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
