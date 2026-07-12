# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.5 | 0.000% | 7.668056 | 0.000% | 0.244963 | 2.414086 | 0.193303 | 0.883662 | 90.531% |
| 0.25 | 0 | 143296.6 | 6.674% | 5.048472 | 34.162% | 0.154987 | 1.642028 | 0.217950 | 0.879241 | 88.766% |
| 0.5 | 0 | 149591.2 | 11.360% | 4.068490 | 46.942% | 0.108386 | 1.493837 | 0.244965 | 0.863898 | 86.557% |
| 1 | 0 | 158934.1 | 18.315% | 2.809425 | 63.362% | 0.064803 | 0.820659 | 0.203473 | 0.826651 | 80.231% |
| 2 | 0 | 173484.8 | 29.147% | 2.058464 | 73.155% | 0.044453 | 0.752312 | 0.277973 | 0.782975 | 73.022% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
