# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 7.192151 | 0.000% | 0.213115 | 2.211158 | 0.181073 | 0.875628 | 89.250% |
| 0.25 | 0 | 141562.4 | 5.645% | 5.160050 | 28.254% | 0.146824 | 1.644144 | 0.239349 | 0.862408 | 87.439% |
| 0.5 | 0 | 146949.9 | 9.666% | 3.769627 | 47.587% | 0.107898 | 1.376261 | 0.258249 | 0.838262 | 83.580% |
| 1 | 0 | 154481.8 | 15.287% | 2.390375 | 66.764% | 0.061160 | 0.799034 | 0.254096 | 0.769855 | 74.323% |
| 2 | 0 | 166033.9 | 23.908% | 2.142548 | 70.210% | 0.051524 | 0.741852 | 0.277255 | 0.751165 | 71.537% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
