# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.033840 | 0.000% | 0.244086 | 2.316733 | 0.136974 | 0.845207 | 86.834% |
| 1 | 0 | 160133.0 | 19.504% | 3.251072 | 59.533% | 0.063925 | 1.004495 | 0.246543 | 0.739278 | 72.175% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
