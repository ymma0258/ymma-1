# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134531.2 | 0.000% | 8.979171 | 0.000% | 0.275456 | 2.450998 | 0.143534 | 0.873012 | 89.512% |
| 0.25 | 0 | 143355.0 | 6.559% | 5.774452 | 35.691% | 0.168137 | 1.874725 | 0.256463 | 0.857683 | 86.917% |
| 0.5 | 0 | 149872.2 | 11.403% | 4.164568 | 53.620% | 0.123646 | 1.394148 | 0.251798 | 0.827077 | 82.457% |
| 1 | 0 | 158793.2 | 18.034% | 3.085079 | 65.642% | 0.084225 | 1.125750 | 0.313081 | 0.789726 | 77.127% |
| 2 | 0 | 173255.0 | 28.784% | 2.493143 | 72.234% | 0.060462 | 0.911207 | 0.299578 | 0.751185 | 71.847% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
