# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 7.736093 | 0.000% | 0.233101 | 2.305522 | 0.160077 | 0.879734 | 89.716% |
| 1 | 0 | 158998.3 | 18.658% | 2.898866 | 62.528% | 0.077334 | 0.951183 | 0.275062 | 0.808054 | 77.941% |
| 1 | 0.5 | 164241.7 | 22.571% | 2.340634 | 69.744% | 0.043956 | 0.903476 | 0.304059 | 0.771475 | 72.594% |
| 1 | 1 | 169065.5 | 26.171% | 2.287156 | 70.435% | 0.045082 | 0.913329 | 0.307608 | 0.765978 | 71.860% |
| 1 | 2 | 177531.7 | 32.489% | 2.073593 | 73.196% | 0.041589 | 0.962511 | 0.334644 | 0.748437 | 68.974% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
