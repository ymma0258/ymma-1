# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 10.500343 | 0.000% | 0.217532 | 3.111577 | 0.152760 | 0.876131 | 90.060% |
| 1 | 0 | 160479.2 | 19.763% | 4.089257 | 61.056% | 0.064793 | 1.534783 | 0.334978 | 0.813071 | 78.943% |
| 2 | 0 | 175211.0 | 30.757% | 3.166973 | 69.839% | 0.048511 | 1.281548 | 0.348049 | 0.769655 | 72.828% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
