# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 10.580708 | 0.000% | 0.200090 | 3.459715 | 0.224831 | 0.884468 | 90.706% |
| 1 | 0 | 176383.1 | 20.209% | 3.881656 | 63.314% | 0.066106 | 1.498871 | 0.302490 | 0.821510 | 78.837% |
| 2 | 0 | 191008.2 | 30.176% | 3.236924 | 69.407% | 0.054136 | 1.385365 | 0.340641 | 0.795358 | 74.497% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
