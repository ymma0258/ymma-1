# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.9 | 0.000% | 8.816417 | 0.000% | 0.294242 | 2.693494 | 0.184016 | 0.882199 | 89.686% |
| 0.25 | 0 | 142959.0 | 6.475% | 5.712982 | 35.201% | 0.182077 | 1.702958 | 0.196623 | 0.872885 | 86.618% |
| 0.5 | 0 | 149066.1 | 11.024% | 4.112502 | 53.354% | 0.115369 | 1.434584 | 0.262001 | 0.841817 | 81.828% |
| 1 | 0 | 156323.6 | 16.429% | 2.570978 | 70.839% | 0.064635 | 0.943052 | 0.281991 | 0.786573 | 73.075% |
| 2 | 0 | 167535.9 | 24.780% | 2.037923 | 76.885% | 0.041142 | 0.625115 | 0.223572 | 0.747574 | 66.882% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
