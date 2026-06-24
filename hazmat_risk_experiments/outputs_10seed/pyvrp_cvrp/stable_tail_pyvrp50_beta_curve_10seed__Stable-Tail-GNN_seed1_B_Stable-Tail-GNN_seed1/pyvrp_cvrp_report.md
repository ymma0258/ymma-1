# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.357164 | 0.000% | 0.239110 | 2.944828 | 0.274723 | 0.883600 | 90.215% |
| 0.25 | 0 | 155611.0 | 6.052% | 6.741563 | 19.332% | 0.210365 | 2.473367 | 0.268763 | 0.880043 | 88.480% |
| 0.5 | 0 | 163770.4 | 11.613% | 5.315485 | 36.396% | 0.153070 | 1.574794 | 0.214485 | 0.861342 | 85.234% |
| 1 | 0 | 173258.1 | 18.079% | 3.125534 | 62.601% | 0.066100 | 1.082979 | 0.274297 | 0.813934 | 77.109% |
| 2 | 0 | 186571.4 | 27.152% | 2.710151 | 67.571% | 0.053091 | 1.014961 | 0.292356 | 0.798433 | 74.529% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
