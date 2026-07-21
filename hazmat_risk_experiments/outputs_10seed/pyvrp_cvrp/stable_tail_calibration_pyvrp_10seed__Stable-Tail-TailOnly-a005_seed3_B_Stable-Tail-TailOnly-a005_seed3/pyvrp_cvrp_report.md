# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147131.0 | 0.000% | 6.816754 | 0.000% | 0.197056 | 2.444567 | 0.260956 | 0.868282 | 88.924% |
| 0.25 | 0 | 155804.7 | 5.895% | 5.889296 | 13.606% | 0.141467 | 2.281311 | 0.277061 | 0.864843 | 87.963% |
| 0.5 | 0 | 163445.8 | 11.089% | 4.921818 | 27.798% | 0.127762 | 2.015841 | 0.296262 | 0.859008 | 86.415% |
| 1 | 0 | 175310.3 | 19.153% | 3.553507 | 47.871% | 0.091789 | 1.503978 | 0.317127 | 0.834039 | 82.000% |
| 2 | 0 | 191974.1 | 30.478% | 2.754274 | 59.596% | 0.068750 | 1.155511 | 0.299015 | 0.808268 | 77.526% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
