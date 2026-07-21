# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.6 | 0.000% | 7.026202 | 0.000% | 0.208616 | 2.145362 | 0.210595 | 0.884660 | 90.520% |
| 0.25 | 0 | 142411.1 | 6.226% | 4.069826 | 42.076% | 0.123590 | 1.432724 | 0.255417 | 0.859957 | 86.186% |
| 0.5 | 0 | 148154.5 | 10.510% | 3.372082 | 52.007% | 0.097083 | 1.298958 | 0.286943 | 0.838339 | 83.343% |
| 1 | 0 | 155880.0 | 16.272% | 2.208012 | 68.575% | 0.050335 | 0.804162 | 0.260149 | 0.783822 | 75.218% |
| 2 | 0 | 167792.5 | 25.158% | 1.631596 | 76.778% | 0.029152 | 0.558529 | 0.259051 | 0.733131 | 67.290% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
