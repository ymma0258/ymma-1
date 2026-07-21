# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 8.674325 | 0.000% | 0.276348 | 2.473552 | 0.163720 | 0.872171 | 89.683% |
| 0.25 | 0 | 142716.9 | 6.507% | 5.723798 | 34.014% | 0.162288 | 1.806848 | 0.224044 | 0.858574 | 87.481% |
| 0.5 | 0 | 148830.8 | 11.069% | 4.398616 | 49.292% | 0.109888 | 1.787501 | 0.283432 | 0.831892 | 83.937% |
| 1 | 0 | 157787.3 | 17.753% | 2.917639 | 66.365% | 0.061273 | 1.052124 | 0.275331 | 0.773724 | 75.932% |
| 2 | 0 | 171435.0 | 27.938% | 2.414490 | 72.165% | 0.053056 | 0.741741 | 0.220460 | 0.745600 | 71.589% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
