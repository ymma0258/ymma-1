# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.072629 | 0.000% | 0.224033 | 2.220910 | 0.199043 | 0.877152 | 89.589% |
| 1 | 0 | 154376.7 | 15.209% | 2.271279 | 67.886% | 0.046362 | 0.709523 | 0.180468 | 0.758245 | 72.274% |
| 1 | 1 | 162153.3 | 21.012% | 1.903973 | 73.080% | 0.035465 | 0.548873 | 0.193629 | 0.738016 | 68.823% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
