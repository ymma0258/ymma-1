# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 14.257603 | 0.000% | 0.372467 | 4.444715 | 0.189360 | 0.860755 | 89.850% |
| 1 | 0 | 182677.7 | 24.498% | 6.979003 | 51.051% | 0.152864 | 2.410058 | 0.245158 | 0.826274 | 83.376% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
