# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 9.128826 | 0.000% | 0.216614 | 2.990002 | 0.226089 | 0.884019 | 90.308% |
| 1 | 0 | 156194.9 | 16.566% | 2.847335 | 68.809% | 0.055889 | 1.153759 | 0.298272 | 0.790738 | 75.069% |
| 2 | 0 | 167222.7 | 24.795% | 2.111590 | 76.869% | 0.036166 | 0.619853 | 0.193152 | 0.724954 | 65.349% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
