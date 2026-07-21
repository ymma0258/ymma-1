# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.3 | 0.000% | 7.808220 | 0.000% | 0.240914 | 2.314903 | 0.182263 | 0.870261 | 88.828% |
| 0.25 | 0 | 142281.3 | 6.181% | 5.829109 | 25.347% | 0.165678 | 1.733459 | 0.206988 | 0.863193 | 87.736% |
| 0.5 | 0 | 148363.1 | 10.720% | 4.045798 | 48.185% | 0.113391 | 1.494605 | 0.244715 | 0.828811 | 82.551% |
| 1 | 0 | 157032.7 | 17.190% | 2.898135 | 62.884% | 0.070587 | 0.840586 | 0.186607 | 0.787331 | 76.664% |
| 2 | 0 | 171171.1 | 27.741% | 2.548062 | 67.367% | 0.052776 | 0.790146 | 0.229641 | 0.767398 | 73.376% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
