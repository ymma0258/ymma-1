# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 7.596085 | 0.000% | 0.241255 | 2.163380 | 0.160101 | 0.870135 | 89.394% |
| 0.25 | 0 | 143105.4 | 6.797% | 4.967658 | 34.602% | 0.141830 | 1.298848 | 0.147346 | 0.853641 | 86.773% |
| 0.5 | 0 | 149626.2 | 11.663% | 3.931378 | 48.245% | 0.099481 | 1.417431 | 0.249853 | 0.829796 | 83.569% |
| 1 | 0 | 158637.4 | 18.388% | 2.649165 | 65.125% | 0.058024 | 0.905300 | 0.240177 | 0.776013 | 76.060% |
| 2 | 0 | 172541.8 | 28.764% | 2.141235 | 71.811% | 0.046433 | 0.636818 | 0.232247 | 0.740106 | 70.896% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
