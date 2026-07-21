# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.3 | 0.000% | 8.940790 | 0.000% | 0.284826 | 2.582367 | 0.175254 | 0.876309 | 89.843% |
| 0.25 | 0 | 143227.2 | 6.622% | 6.383165 | 28.606% | 0.199216 | 2.051214 | 0.237099 | 0.870578 | 88.416% |
| 0.5 | 0 | 150218.1 | 11.827% | 4.890300 | 45.303% | 0.139313 | 1.588030 | 0.243757 | 0.850480 | 85.308% |
| 1 | 0 | 159677.1 | 18.868% | 3.609586 | 59.628% | 0.086035 | 1.134740 | 0.245667 | 0.819306 | 80.504% |
| 2 | 0 | 175102.1 | 30.351% | 2.847927 | 68.147% | 0.059747 | 1.063430 | 0.338842 | 0.790587 | 76.014% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
