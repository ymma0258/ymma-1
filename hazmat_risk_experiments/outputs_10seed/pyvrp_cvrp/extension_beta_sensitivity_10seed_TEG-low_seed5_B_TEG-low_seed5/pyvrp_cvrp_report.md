# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.526416 | 0.000% | 0.223916 | 2.417209 | 0.198886 | 0.823515 | 85.201% |
| 0.5 | 0 | 165420.1 | 12.737% | 4.737220 | 37.059% | 0.108203 | 1.286235 | 0.162197 | 0.767613 | 78.326% |
| 1 | 0 | 176436.8 | 20.245% | 3.531081 | 53.084% | 0.076193 | 1.183479 | 0.231821 | 0.704968 | 70.822% |
| 1.5 | 0 | 185797.6 | 26.625% | 3.182407 | 57.717% | 0.069611 | 1.010250 | 0.237677 | 0.683562 | 67.838% |
| 2 | 0 | 194341.0 | 32.447% | 3.039575 | 59.615% | 0.065547 | 0.961450 | 0.239024 | 0.673609 | 66.342% |
| 3 | 0 | 210257.5 | 43.295% | 2.837310 | 62.302% | 0.055479 | 0.838982 | 0.200650 | 0.654054 | 63.808% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
