# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 133997.4 | 0.000% | 9.632765 | 0.000% | 0.225424 | 3.094975 | 0.217939 | 0.842991 | 87.161% |
| 1 | 158937.6 | 18.612% | 3.966297 | 58.825% | 0.073242 | 1.422173 | 0.235743 | 0.729475 | 72.132% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
