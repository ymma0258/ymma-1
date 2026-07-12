# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134397.9 | 0.000% | 7.477371 | 0.000% | 0.234468 | 2.293046 | 0.181460 | 0.871453 | 88.511% |
| 0.25 | 0 | 141447.2 | 5.245% | 5.391661 | 27.894% | 0.167845 | 1.730972 | 0.217741 | 0.859626 | 87.169% |
| 0.5 | 0 | 147027.6 | 9.397% | 3.890940 | 47.964% | 0.118037 | 1.446386 | 0.248301 | 0.832217 | 83.059% |
| 1 | 0 | 154863.6 | 15.228% | 2.769038 | 62.968% | 0.074257 | 0.856023 | 0.196622 | 0.784948 | 76.447% |
| 2 | 0 | 166547.7 | 23.921% | 2.502060 | 66.538% | 0.062995 | 0.754725 | 0.191256 | 0.769125 | 73.836% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
