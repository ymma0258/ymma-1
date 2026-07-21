# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134397.9 | 0.000% | 7.196921 | 0.000% | 0.221943 | 2.268112 | 0.200436 | 0.872845 | 88.971% |
| 0.25 | 0 | 141770.9 | 5.486% | 4.768315 | 33.745% | 0.136084 | 1.483117 | 0.192522 | 0.856887 | 86.790% |
| 0.5 | 0 | 147226.4 | 9.545% | 3.875505 | 46.151% | 0.111188 | 1.320056 | 0.230390 | 0.840946 | 84.039% |
| 1 | 0 | 154764.1 | 15.154% | 2.401361 | 66.633% | 0.061789 | 0.768544 | 0.236134 | 0.768889 | 74.124% |
| 2 | 0 | 166467.2 | 23.861% | 2.115498 | 70.606% | 0.051202 | 0.685375 | 0.247367 | 0.750634 | 71.028% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
