# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.9 | 0.000% | 8.095694 | 0.000% | 0.236614 | 2.480978 | 0.187814 | 0.833900 | 85.897% |
| 0.25 | 0 | 157771.6 | 7.135% | 6.667619 | 17.640% | 0.172005 | 2.117246 | 0.192403 | 0.819941 | 84.086% |
| 0.5 | 0 | 166873.0 | 13.316% | 4.925231 | 39.162% | 0.111867 | 1.630402 | 0.230956 | 0.775736 | 78.734% |
| 1 | 0 | 177410.4 | 20.471% | 3.572062 | 55.877% | 0.076676 | 1.171009 | 0.224901 | 0.715843 | 71.282% |
| 2 | 0 | 194799.6 | 32.279% | 2.934081 | 63.758% | 0.060308 | 0.854179 | 0.195325 | 0.667729 | 65.074% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
