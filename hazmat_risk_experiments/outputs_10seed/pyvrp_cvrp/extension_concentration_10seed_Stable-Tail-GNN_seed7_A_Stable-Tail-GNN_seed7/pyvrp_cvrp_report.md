# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 8.860071 | 0.000% | 0.280270 | 2.612395 | 0.153796 | 0.875752 | 89.901% |
| 1 | 0 | 158498.5 | 18.285% | 3.260477 | 63.200% | 0.072756 | 1.191802 | 0.291764 | 0.805873 | 77.756% |
| 1 | 0.5 | 163316.4 | 21.880% | 2.650282 | 70.087% | 0.052053 | 0.756550 | 0.228131 | 0.782628 | 73.628% |
| 1 | 1 | 167925.1 | 25.320% | 2.455267 | 72.288% | 0.047519 | 0.827664 | 0.273661 | 0.756087 | 70.062% |
| 1 | 2 | 175326.9 | 30.843% | 2.322282 | 73.789% | 0.044278 | 0.870533 | 0.296764 | 0.738324 | 67.665% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
