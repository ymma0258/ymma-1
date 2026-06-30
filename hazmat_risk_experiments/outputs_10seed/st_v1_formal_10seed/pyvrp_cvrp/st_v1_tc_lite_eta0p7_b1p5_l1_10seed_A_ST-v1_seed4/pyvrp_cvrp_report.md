# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.651668 | 0.000% | 0.269117 | 2.477326 | 0.142433 | 0.874600 | 89.967% |
| 1.5 | 1 | 181698.3 | 35.598% | 2.347338 | 72.868% | 0.042966 | 1.144850 | 0.372241 | 0.734738 | 68.171% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
