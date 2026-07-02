# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 12.004003 | 0.000% | 0.293538 | 3.340024 | 0.137755 | 0.845145 | 88.237% |
| 1.5 | 1 | 185678.1 | 38.568% | 3.440813 | 71.336% | 0.058680 | 1.628443 | 0.370688 | 0.663259 | 64.861% |
| 2 | 1 | 193707.2 | 44.560% | 3.523276 | 70.649% | 0.061590 | 1.596209 | 0.357605 | 0.672574 | 65.663% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
