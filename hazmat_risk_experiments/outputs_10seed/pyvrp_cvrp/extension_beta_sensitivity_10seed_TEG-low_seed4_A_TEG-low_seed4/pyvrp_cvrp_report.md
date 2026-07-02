# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.529046 | 0.000% | 0.258772 | 2.457982 | 0.131836 | 0.845500 | 87.460% |
| 0.5 | 0 | 151005.7 | 12.693% | 5.302035 | 37.836% | 0.153036 | 2.024362 | 0.285326 | 0.809084 | 82.175% |
| 1 | 0 | 161521.2 | 20.540% | 3.658152 | 57.109% | 0.086245 | 1.299867 | 0.306020 | 0.746411 | 73.782% |
| 1.5 | 0 | 170471.7 | 27.220% | 3.375522 | 60.423% | 0.071136 | 1.175422 | 0.274373 | 0.728593 | 71.412% |
| 2 | 0 | 178015.5 | 32.850% | 3.062396 | 64.095% | 0.060353 | 1.236170 | 0.287303 | 0.709134 | 68.843% |
| 3 | 0 | 191968.1 | 43.262% | 2.835480 | 66.755% | 0.052995 | 1.151009 | 0.321691 | 0.688635 | 66.342% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
