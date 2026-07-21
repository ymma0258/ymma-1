# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.5 | 0.000% | 5.554464 | 0.000% | 0.173666 | 1.626687 | 0.164089 | 0.882361 | 90.486% |
| 0.25 | 0 | 143084.4 | 6.675% | 4.133128 | 25.589% | 0.131708 | 1.289468 | 0.231049 | 0.875704 | 89.127% |
| 0.5 | 0 | 149943.7 | 11.789% | 3.118567 | 43.855% | 0.094324 | 1.097942 | 0.291656 | 0.856871 | 86.124% |
| 1 | 0 | 159294.3 | 18.760% | 2.228981 | 59.870% | 0.059188 | 0.884409 | 0.371951 | 0.825247 | 81.281% |
| 2 | 0 | 173826.0 | 29.594% | 1.761373 | 68.289% | 0.043346 | 0.657740 | 0.349358 | 0.795788 | 76.659% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
