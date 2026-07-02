# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 14.149419 | 0.000% | 0.296796 | 3.716978 | 0.133498 | 0.837519 | 87.807% |
| 1 | 0 | 163045.3 | 21.678% | 6.314951 | 55.370% | 0.078143 | 2.063438 | 0.244546 | 0.766710 | 77.022% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
