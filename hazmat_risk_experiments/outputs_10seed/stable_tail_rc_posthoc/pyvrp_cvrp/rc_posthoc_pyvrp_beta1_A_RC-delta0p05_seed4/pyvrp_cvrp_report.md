# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.769274 | 0.000% | 0.272700 | 2.508497 | 0.141885 | 0.874226 | 89.944% |
| 1 | 0 | 160157.7 | 19.523% | 3.446276 | 60.701% | 0.075424 | 1.281529 | 0.346315 | 0.810615 | 78.895% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
